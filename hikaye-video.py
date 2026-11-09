#!/usr/bin/env python3
"""Hikaye metninden TikTok videosu üretir.

Kullanım:
    python3 hikaye-video.py hikayeler/001.txt arka-plan.mp4 cikti.mp4 [--hiz +10%]

Hikaye dosyasının ilk satırı anlatıcıyı belirtir:
    anlatici: kadin   -> Emel sesi
    anlatici: erkek   -> Ahmet sesi

Adımlar: seslendirme (edge-tts, kelime zamanlarıyla) -> tek kelimelik
altyazı (ASS) -> arka planı döngüye al, sesi ve altyazıyı ekle (FFmpeg).
"""
import argparse
import asyncio
import os
import subprocess
import sys
import tempfile

import edge_tts

SESLER = {"kadin": "tr-TR-EmelNeural", "erkek": "tr-TR-AhmetNeural"}


def oku(yol):
    satirlar = open(yol, encoding="utf-8").read().strip().splitlines()
    ilk = satirlar[0].lower().replace("ı", "i")
    if not ilk.startswith("anlatici:"):
        sys.exit("İlk satır 'anlatici: kadin' veya 'anlatici: erkek' olmalı.")
    anlatici = ilk.split(":", 1)[1].strip()
    if anlatici not in SESLER:
        sys.exit(f"Bilinmeyen anlatıcı: {anlatici}")
    return anlatici, "\n".join(satirlar[1:]).strip()


async def seslendir(metin, ses, hiz, mp3):
    kelimeler = []
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    com = edge_tts.Communicate(metin, ses, rate=hiz, boundary="WordBoundary", proxy=proxy)
    with open(mp3, "wb") as f:
        async for parca in com.stream():
            if parca["type"] == "audio":
                f.write(parca["data"])
            elif parca["type"] == "WordBoundary":
                bas = parca["offset"] / 1e7
                kelimeler.append([bas, bas + parca["duration"] / 1e7, parca["text"]])
    return kelimeler


def zaman(s):
    s = max(0, s)
    return f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}"


def ass_yaz(kelimeler, yol):
    # Bir sonraki kelimeye kadar ekranda kalsın (boşlukta titreme olmasın)
    for i in range(len(kelimeler) - 1):
        kelimeler[i][1] = min(max(kelimeler[i][1], kelimeler[i + 1][0]), kelimeler[i][0] + 1.2)
    bas = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Kelime,Inter ExtraBold,108,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,-1,0,0,100,100,0,0,1,7,4,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(yol, "w", encoding="utf-8") as f:
        f.write(bas)
        for b, s, k in kelimeler:
            # Türkçe büyük harf: i -> İ, ı -> I
            k = k.strip().replace("i", "İ").replace("ı", "I").upper()
            # Ekranın üst-orta bandı (TikTok arayüzünden uzak), hafif büyüme efekti
            f.write(f"Dialogue: 0,{zaman(b)},{zaman(s)},Kelime,,0,0,0,,"
                    f"{{\\pos(540,820)\\fscx85\\fscy85\\t(0,90,\\fscx100\\fscy100)}}{k}\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("hikaye"); p.add_argument("arka_plan"); p.add_argument("cikti")
    p.add_argument("--hiz", default="+10%")
    a = p.parse_args()

    anlatici, metin = oku(a.hikaye)
    ses = SESLER[anlatici]
    print(f"Anlatıcı: {anlatici} -> {ses}")
    tmp = tempfile.mkdtemp()
    mp3, ass = os.path.join(tmp, "ses.mp3"), os.path.join(tmp, "altyazi.ass")
    kelimeler = asyncio.run(seslendir(metin, ses, a.hiz, mp3))
    ass_yaz(kelimeler, ass)
    sure = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", mp3]).decode())
    print(f"Ses süresi: {sure:.1f} sn, {len(kelimeler)} kelime")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-stream_loop", "-1", "-i", a.arka_plan, "-i", mp3,
                    "-t", f"{sure + 0.5:.2f}", "-map", "0:v", "-map", "1:a",
                    "-vf", f"scale=1080:1920,setsar=1,ass={ass}",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "26", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", a.cikti], check=True)
    print(f"Hazır: {a.cikti}")


if __name__ == "__main__":
    main()
