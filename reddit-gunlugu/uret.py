#!/usr/bin/env python3
"""Reddit Günlüğü video üretim hattı (Python + FFmpeg).

Girdiler (çalışma klasöründe):
    hikaye.txt     uzun Reddit hikayesi (YouTube için)
    tiktok.txt     kısaltılmış + hook'lu metin (TikTok için, onaylı)
    logo.png       yuvarlak kanal logosu (şeffaf arka plan)
    minecraft.png  YouTube arka planı

Komutlar:
    python3 uret.py youtube            -> youtube.mp4  (1920x1080, hikayenin tamamı)
    python3 uret.py tiktok             -> tiktok.mp4   (1080x1920)
    python3 uret.py test               -> test-youtube.mp4 + test-tiktok.mp4 (30 sn)
    python3 uret.py klipler            -> Pexels'ten dikey klipleri indirir
    python3 uret.py teslim             -> youtube-gonder.mp4 / tiktok-gonder.mp4 (<380 MiB)

logo.png ve minecraft.png bölüm klasöründe yoksa girdi/ klasöründekiler kullanılır.

Seçenekler: --klasor DIR (girdi/çıktı klasörü), --sure SN (sadece ilk N saniye)

Pexels anahtarı PEXELS_API_KEY ortam değişkeninden okunur (isteğe bağlı).
Sıra: Pexels -> klipler/ klasöründeki hazır dikey videolar -> Mixkit'in
ücretsiz dikey slime klipleri (anahtar gerekmez). Kırpma yapılmaz;
sadece doğal 9:16 dikey (en az 1080x1920) klipler kullanılır.
"""
import argparse
import asyncio
import glob
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

BURA = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BURA, "fonts")
FONT = "Montserrat ExtraBold"
SES = "tr-TR-AhmetNeural"
HIZ = "+10%"
TURKUAZ = "&H00F5E03E&"          # #3EE0F5, ASS renk sırası BGR
KAPANIS = "Hikayenin devamı ve finali YouTube'da! Daha fazlası için profildeki linke tıklayın ya da YouTube'da Reddit Günlüğü diye aratın."
PEXELS_ARAMALAR = ["satisfying slime", "soap cutting", "kinetic sand"]
FPS = 30


def calistir(komut):
    subprocess.run(komut, check=True)


def sure_olc(yol):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", yol]).decode())


# ---------------------------------------------------------------- SES ----
def parcala(metin, sinir=1500):
    """Uzun metni paragraf sınırlarından ~1500 karakterlik parçalara böler."""
    parcalar, simdiki = [], ""
    for p in [x.strip() for x in metin.split("\n") if x.strip()]:
        if simdiki and len(simdiki) + len(p) > sinir:
            parcalar.append(simdiki)
            simdiki = ""
        simdiki = (simdiki + "\n" + p).strip()
    if simdiki:
        parcalar.append(simdiki)
    return parcalar


async def _tts_parca(metin, mp3):
    import edge_tts
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    com = edge_tts.Communicate(metin, SES, rate=HIZ, boundary="WordBoundary", proxy=proxy)
    kelimeler = []
    with open(mp3, "wb") as f:
        async for c in com.stream():
            if c["type"] == "audio":
                f.write(c["data"])
            elif c["type"] == "WordBoundary":
                b = c["offset"] / 1e7
                kelimeler.append([b, b + c["duration"] / 1e7, c["text"]])
    return kelimeler


def whisper_zamanlari(mp3):
    """WordBoundary gelmezse yedek: faster-whisper ile Türkçe kelime zamanları."""
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(mp3, language="tr", word_timestamps=True)
    return [[w.start, w.end, w.word.strip()] for s in segs for w in s.words]


def seslendir(metin, hedef):
    """metin -> hedef.mp3 + hedef.json (kelime zamanları). Varsa yeniden üretmez."""
    mp3, js = hedef + ".mp3", hedef + ".json"
    if os.path.exists(mp3) and os.path.exists(js):
        return mp3, json.load(open(js, encoding="utf-8"))
    os.makedirs(hedef + "_parca", exist_ok=True)
    tum, ofset, liste = [], 0.0, []
    parcalar = parcala(metin)
    for i, p in enumerate(parcalar):
        pm = os.path.join(hedef + "_parca", f"{i:03d}.mp3")
        print(f"  seslendirme {i + 1}/{len(parcalar)}", flush=True)
        beklenen = len(p.split())
        son_kelime = re.sub(r"\W", "", p.split()[-1]).lower()
        for deneme in range(4):
            k = asyncio.run(_tts_parca(p, pm))
            # edge-tts bazen akışı erken keser: son kelime metnin sonuna ulaşmadıysa tekrar dene
            son_ok = bool(k) and re.sub(r"\W", "", k[-1][2]).lower() == son_kelime
            if son_ok and len(k) >= 0.9 * beklenen:
                break
            print(f"    eksik seslendirme ({len(k)}/{beklenen} kelime), tekrar deneniyor", flush=True)
        else:
            sys.exit(f"Parça {i + 1} seslendirilemedi.")
        if not k:
            k = whisper_zamanlari(pm)
        tum += [[b + ofset, s + ofset, t] for b, s, t in k]
        ofset += sure_olc(pm)
        liste.append(pm)
    lst = hedef + "_parca/liste.txt"
    with open(lst, "w") as f:
        f.writelines(f"file '{os.path.abspath(x)}'\n" for x in liste)
    calistir(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
              "-c:a", "libmp3lame", "-b:a", "128k", mp3])
    json.dump(tum, open(js, "w", encoding="utf-8"), ensure_ascii=False)
    return mp3, tum


# ----------------------------------------------------------- ALTYAZI ----
def tr_buyuk(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


def gruplar(kelimeler, en_fazla=3):
    """2-3 kelimelik gruplar: noktalama ya da uzun duraklamada grup kapanır."""
    out, g = [], []
    for i, w in enumerate(kelimeler):
        g.append(w)
        son = w[2].rstrip()[-1:] in ".!?,;:…\""
        bosluk = i + 1 < len(kelimeler) and kelimeler[i + 1][0] - w[1] > 0.45
        if len(g) >= en_fazla or son or bosluk:
            out.append(g)
            g = []
    if g:
        out.append(g)
    # tek kelimelik grupları bir öncekine ekle (3'ü geçmeyecekse)
    birlesik = []
    for g in out:
        if birlesik and len(g) == 1 and len(birlesik[-1]) < en_fazla \
                and g[0][0] - birlesik[-1][-1][1] < 0.3:
            birlesik[-1] += g
        else:
            birlesik.append(g)
    return birlesik


def ts(s):
    s = max(0.0, s)
    return f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}"


def ass_yaz(kelimeler, yol, W, H, boyut, metin_y, sinir=None):
    """Grup ekranda dururken o an okunan kelime turkuaz yanar."""
    sat = [f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Ana,{FONT},{boyut},&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,{max(4, boyut // 11)},2,5,{W // 12},{W // 12},0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"""]
    gs = gruplar(kelimeler)
    for gi, g in enumerate(gs):
        g_son = gs[gi + 1][0][0] if gi + 1 < len(gs) else g[-1][1] + 0.4
        g_son = min(g_son, g[-1][1] + 0.6)
        for wi, w in enumerate(g):
            bas = w[0]
            bit = g[wi + 1][0] if wi + 1 < len(g) else g_son
            if sinir and bas >= sinir:
                continue
            parcalar = []
            for wj, w2 in enumerate(g):
                t = tr_buyuk(w2[2].strip())
                parcalar.append(f"{{\\c{TURKUAZ}}}{t}{{\\c&H00FFFFFF&}}" if wj == wi else t)
            sat.append(f"Dialogue: 0,{ts(bas)},{ts(bit)},Ana,,0,0,0,,{{\\pos({W // 2},{metin_y})}}" + " ".join(parcalar))
    open(yol, "w", encoding="utf-8").write("\n".join(sat) + "\n")


# -------------------------------------------------------- ARKA PLAN ----
def youtube_arka_plan(resim, cikti, W=1920, H=1080):
    """minecraft.png'den 40 sn'lik ileri-geri yavaş zoom döngüsü (sonra döngülenir)."""
    if os.path.exists(cikti):
        return cikti
    n = 20 * FPS
    # 1.00 -> 1.08 -> 1.00 yumuşak zoom (kosinüs), kenar titremesini önlemek için 2x ölçekten
    z = f"1+0.04*(1-cos(2*PI*on/{2 * n}))"
    calistir(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", resim, "-vf",
              f"scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},format=yuv420p",
              "-frames:v", str(2 * n), "-c:v", "libx264", "-preset", "medium", "-crf", "18", cikti])
    return cikti


def pexels_indir(klasor, adet=8):
    """Pexels'ten SADECE doğal dikey (≥1080x1920, 9:16) klipleri indirir."""
    anahtar = os.environ.get("PEXELS_API_KEY")
    if not anahtar:
        print("PEXELS_API_KEY yok: Pexels atlandı.")
        return []
    os.makedirs(klasor, exist_ok=True)
    alinan = []
    for q in PEXELS_ARAMALAR:
        url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
            {"query": q, "orientation": "portrait", "size": "large", "per_page": 30})
        req = urllib.request.Request(url, headers={"Authorization": anahtar, "User-Agent": "reddit-gunlugu/1.0"})
        veri = json.load(urllib.request.urlopen(req, timeout=60))
        say = 0
        for v in veri.get("videos", []):
            if v["height"] <= v["width"] or v["width"] < 1080 or v["height"] < 1920:
                continue
            dosyalar = [f for f in v["video_files"] if f.get("width") and f.get("height")
                        and f["height"] > f["width"] and f["width"] >= 1080 and f["height"] >= 1920
                        and abs(f["width"] / f["height"] - 9 / 16) < 0.01]
            if not dosyalar:
                continue
            f = min(dosyalar, key=lambda x: x["width"])        # en küçük uygun çözünürlük
            yol = os.path.join(klasor, f"pexels-{v['id']}.mp4")
            if not os.path.exists(yol):
                print(f"  indiriliyor: {q} -> {v['id']} ({f['width']}x{f['height']})")
                urllib.request.urlretrieve(f["link"], yol)
            alinan.append(yol)
            say += 1
            if say >= adet // len(PEXELS_ARAMALAR) + 1:
                break
    return alinan


# Mixkit ücretsiz lisanslı, doğal dikey (1080x1920) slime klipleri. Anahtar gerekmez.
MIXKIT_DIKEY = [47343, 47351, 47342, 47346, 47340, 47348, 47349, 47337, 47347, 47350, 47341, 47345]


def mixkit_indir(klasor):
    """Pexels anahtarı yoksa: Mixkit'in dikey slime kliplerini indirir."""
    os.makedirs(klasor, exist_ok=True)
    alinan = []
    for i in MIXKIT_DIKEY:
        yol = os.path.join(klasor, f"mixkit-{i}.mp4")
        if not os.path.exists(yol):
            print(f"  indiriliyor: Mixkit {i}")
            try:
                urllib.request.urlretrieve(f"https://assets.mixkit.co/videos/{i}/{i}-1080.mp4", yol)
            except Exception as e:
                print(f"  atlandı ({e})")
                continue
        alinan.append(yol)
    return alinan


def dikey_mi(yol):
    w, h = map(int, subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
         "-of", "csv=p=0", yol]).decode().strip().split(",")[:2])
    return h > w and w >= 1080 and h >= 1920 and abs(w / h - 9 / 16) < 0.01


def tiktok_arka_plan(klasor, cikti):
    """Dikey klipleri 1080x1920'ye ölçekleyip (kırpmadan) art arda ekler, sesi atar."""
    if os.path.exists(cikti):
        return cikti
    kdir = os.path.join(klasor, "klipler")
    hazir = pexels_indir(kdir) + glob.glob(os.path.join(kdir, "*.mp4"))
    if not hazir:
        hazir = mixkit_indir(kdir)
    klipler = sorted(set(hazir))
    klipler = [k for k in klipler if dikey_mi(k)]
    if not klipler:
        sys.exit("Dikey klip yok: PEXELS_API_KEY ayarlayın ya da klipler/ klasörüne dikey video koyun.")
    print(f"  {len(klipler)} dikey klip birleştiriliyor")
    gecici = []
    for i, k in enumerate(klipler):
        g = os.path.join(klasor, f"_klip{i:02d}.mp4")
        calistir(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", k, "-an", "-vf",
                  f"scale=1080:1920,fps={FPS},setsar=1,format=yuv420p",
                  "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", g])
        gecici.append(g)
    lst = os.path.join(klasor, "_klipler.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{os.path.abspath(x)}'\n" for x in gecici)
    calistir(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", cikti])
    for g in gecici:
        os.remove(g)
    return cikti


# ------------------------------------------------------------ VİDEO ----
def video_yap(arka, mp3, ass, logo, cikti, W, H, logo_y, sure=None):
    """Arka planı döngüler; logo ve ASS altyazıyı gömer; sesi ekler."""
    toplam = sure if sure else sure_olc(mp3) + 0.6
    logo_w = round(W * 0.18)
    fc = (f"[0:v]scale={W}:{H},setsar=1[bg];"
          f"[2:v]scale={logo_w}:-1[lg];"
          f"[bg][lg]overlay=x=(W-w)/2:y={logo_y}-h/2[v1];"
          f"[v1]ass='{ass}':fontsdir='{FONT_DIR}'[v]")
    calistir(["ffmpeg", "-nostdin", "-v", "error", "-stats", "-y", "-stream_loop", "-1", "-i", arka,
              "-i", mp3, "-i", logo, "-filter_complex", fc, "-map", "[v]", "-map", "1:a",
              "-t", f"{toplam:.2f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
              "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", cikti])
    print(f"Hazır: {cikti}")


ORTAK = os.path.join(BURA, "girdi")   # paylaşılan logo.png ve minecraft.png


def varlik(klasor, ad):
    """Bölüm klasöründe yoksa ortak girdi/ klasöründekini kullanır."""
    yol = os.path.join(klasor, ad)
    return yol if os.path.exists(yol) else os.path.join(ORTAK, ad)


def teslim(klasor, sinir_mb=380):
    """Gönderilebilir küçük kopyalar: *-gonder.mp4 (her biri sinir_mb altında)."""
    for tur in ("tiktok", "youtube"):
        kaynak = os.path.join(klasor, f"{tur}.mp4")
        if not os.path.exists(kaynak):
            continue
        hedef = os.path.join(klasor, f"{tur}-gonder.mp4")
        sure = sure_olc(kaynak)
        kbps = int(sinir_mb * 8 * 1024 * 1024 / sure / 1000) - 140   # ses + kap payı
        kbps = max(400, min(kbps, 1500 if tur == "tiktok" else 2500))
        ek = ["-tune", "stillimage"] if tur == "youtube" else []
        calistir(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", kaynak, "-c:v", "libx264", "-preset", "medium",
                  *ek, "-b:v", f"{kbps}k", "-maxrate", f"{kbps * 2}k", "-bufsize", f"{kbps * 4}k",
                  "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", hedef])
        mb = os.path.getsize(hedef) / 1024 / 1024
        print(f"Teslim: {hedef} ({mb:.0f} MiB, {sure / 60:.1f} dk)")
        if mb > 395:
            sys.exit(f"{hedef} 395 MiB üstünde, daha düşük sinir_mb ile tekrar çalıştırın.")


def uret(tur, klasor, sure=None, onek=""):
    if tur == "youtube":
        W, H, metin = 1920, 1080, open(os.path.join(klasor, "hikaye.txt"), encoding="utf-8").read()
        boyut, metin_y = 100, 650
    else:
        W, H = 1080, 1920
        yol = os.path.join(klasor, "tiktok.txt")
        if not os.path.exists(yol):
            sys.exit("tiktok.txt yok: önce kısaltılmış metni hazırlayıp onaylayın.")
        metin = open(yol, encoding="utf-8").read().strip()
        if KAPANIS not in metin:
            metin += "\n" + KAPANIS
        boyut, metin_y = 122, 1010
    if sure:   # test: yaklaşık süreye yetecek kadar metin (≈2.6 kelime/sn)
        kel = metin.split()
        metin = " ".join(kel[:int(sure * 2.8) + 10])
    print(f"[{tur}] seslendiriliyor…")
    mp3, kelimeler = seslendir(metin, os.path.join(klasor, f"_{onek}{tur}_ses"))
    # logo: altyazı bloğunun hemen üstünde, ortalı
    logo_h = round(W * 0.18)
    logo_y = metin_y - boyut * 1.15 - logo_h / 2 - 12
    ass = os.path.join(klasor, f"_{onek}{tur}.ass")
    ass_yaz(kelimeler, ass, W, H, boyut, metin_y, sinir=sure)
    if tur == "youtube":
        arka = youtube_arka_plan(varlik(klasor, "minecraft.png"), os.path.join(ORTAK, "_youtube_bg.mp4"))
    else:
        arka = tiktok_arka_plan(ORTAK, os.path.join(ORTAK, "_tiktok_bg.mp4"))
    video_yap(arka, mp3, ass, varlik(klasor, "logo.png"),
              os.path.join(klasor, f"{onek}{tur}.mp4"), W, H, round(logo_y), sure)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("komut", choices=["youtube", "tiktok", "test", "klipler", "teslim"])
    p.add_argument("--klasor", default=".")
    p.add_argument("--sure", type=float)
    a = p.parse_args()
    k = os.path.abspath(a.klasor)
    if a.komut == "klipler":
        print(pexels_indir(os.path.join(k, "klipler")))
    elif a.komut == "teslim":
        teslim(k)
    elif a.komut == "test":
        for t in ("youtube", "tiktok"):
            uret(t, k, sure=a.sure or 30, onek="test-")
    else:
        uret(a.komut, k, sure=a.sure)


if __name__ == "__main__":
    main()
