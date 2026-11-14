"""Rakip (@emirreddit) tarzı görseller: YouTube kartı, kapak, abone animasyonu, TikTok paylaş oku.

Kart: turkuaz çerçeveli büyük beyaz kutu, sol üstte yuvarlak logo, kanal adı + onay rozeti, altında dev büyük harf başlık.
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BURA = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(BURA, "fonts", "Montserrat-ExtraBold.otf")
TURKUAZ = (46, 224, 221)
KIRMIZI = (230, 33, 23)
KANAL = "Reddit Günlüğü"


def tr_buyuk(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


def _font(boyut):
    return ImageFont.truetype(FONT, boyut)


def _sar(metin, font, genislik, d):
    """Kelimeleri genişliğe göre satırlara böler."""
    satirlar, simdiki = [], ""
    for k in metin.split():
        deneme = (simdiki + " " + k).strip()
        if d.textlength(deneme, font=font) <= genislik:
            simdiki = deneme
        else:
            if simdiki:
                satirlar.append(simdiki)
            simdiki = k
    if simdiki:
        satirlar.append(simdiki)
    return satirlar


def _sigdir(metin, d, genislik, yukseklik, en_buyuk, en_kucuk=40, satir_aralik=1.08):
    for boyut in range(en_buyuk, en_kucuk - 1, -2):
        f = _font(boyut)
        satirlar = _sar(metin, f, genislik, d)
        h = len(satirlar) * boyut * satir_aralik
        if h <= yukseklik:
            return f, satirlar, boyut
    f = _font(en_kucuk)
    return f, _sar(metin, f, genislik, d), en_kucuk


def _rozet(d, x, y, r):
    """Mavi onay rozeti."""
    d.ellipse([x - r, y - r, x + r, y + r], fill=(29, 155, 240))
    w = max(3, r // 4)
    d.line([(x - r * 0.45, y + r * 0.02), (x - r * 0.1, y + r * 0.38), (x + r * 0.5, y - r * 0.35)],
           fill="white", width=w, joint="curve")


def _avatar(logo, cap):
    lg = Image.open(logo).convert("RGBA").resize((cap, cap), Image.LANCZOS)
    maske = Image.new("L", (cap, cap), 0)
    ImageDraw.Draw(maske).ellipse([0, 0, cap - 1, cap - 1], fill=255)
    out = Image.new("RGBA", (cap, cap), (0, 0, 0, 0))
    out.paste(lg, (0, 0), maske)
    return out


def kart_ciz(baslik, logo, W, H, kenar=(90, 50), alt_bosluk=0, baslik_max=118):
    """Şeffaf zemin üstünde kart (RGBA). alt_bosluk: kartın altında altyazı için bırakılan yükseklik."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    mx, my = kenar
    x0, y0, x1, y1 = mx, my, W - mx, H - my
    s = W / 1280
    cerceve = round(14 * s)
    d.rounded_rectangle([x0, y0, x1, y1], radius=round(40 * s), fill=TURKUAZ)
    d.rounded_rectangle([x0 + cerceve, y0 + cerceve, x1 - cerceve, y1 - cerceve],
                        radius=round(30 * s), fill="white")
    # başlık satırı: avatar + kanal adı + rozet
    cap = round(150 * s)
    ax, ay = x0 + round(170 * s), y0 + round(28 * s)
    d.ellipse([ax - 6, ay - 6, ax + cap + 6, ay + cap + 6], fill=TURKUAZ)
    img.alpha_composite(_avatar(logo, cap), (ax, ay))
    fad = _font(round(62 * s))
    tx = ax + cap + round(45 * s)
    ty = ay + round(18 * s)
    d.text((tx, ty), KANAL, font=fad, fill="black")
    rw = d.textlength(KANAL, font=fad)
    _rozet(d, tx + rw + round(32 * s), ty + round(38 * s), round(20 * s))
    falt = _font(round(30 * s))
    d.text((tx + 4, ty + round(80 * s)), "r/reddit · hikaye", font=falt, fill=(120, 120, 120))
    # dev başlık
    bx0, bx1 = x0 + round(50 * s), x1 - round(50 * s)
    by0 = ay + cap + round(18 * s)
    by1 = y1 - round(30 * s) - alt_bosluk
    f, satirlar, boyut = _sigdir(tr_buyuk(baslik), d, bx1 - bx0, by1 - by0, round(baslik_max * s))
    toplam = len(satirlar) * boyut * 1.08
    y = by0 + (by1 - by0 - toplam) / 2
    for st in satirlar:
        w = d.textlength(st, font=f)
        d.text(((W - w) / 2, y), st, font=f, fill="black")
        y += boyut * 1.08
    return img, (x0, y0, x1, y1)


def kapak(baslik, logo, arka, cikti, W=1280, H=720):
    """YouTube kapağı: bulanık arka plan + kart."""
    bg = Image.open(arka).convert("RGB")
    oran = max(W / bg.width, H / bg.height)
    bg = bg.resize((round(bg.width * oran), round(bg.height * oran)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(14)).convert("RGBA")
    k, _ = kart_ciz(baslik, logo, W, H, kenar=(60, 40), baslik_max=96)
    bg.alpha_composite(k)
    bg.convert("RGB").save(cikti, quality=95)
    return cikti


def abone_animasyonu(cikti, W=1920, H=1080, sure=4.0, fps=30):
    """Ortada beliren 'ABONE OL' butonu; imleç tıklar, 'ABONE OLUNDU ✓' olur. Alfa kanallı .mov."""
    if os.path.exists(cikti):
        return cikti
    kare_dir = cikti + "_kareler"
    os.makedirs(kare_dir, exist_ok=True)
    bh = 160
    d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bw = d0.textlength("ABONE OLUNDU", font=_font(70)) + 46 + 24 + 130
    cx, cy = W // 2, H // 2
    f = _font(66)
    n = int(sure * fps)
    for i in range(n):
        t = i / fps
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        # giriş/çıkış ölçeği
        if t < 0.35:
            sc = 0.6 + 0.4 * (t / 0.35)
            a = int(255 * t / 0.35)
        elif t > sure - 0.4:
            sc = 1.0
            a = int(255 * max(0, (sure - t) / 0.4))
        else:
            sc = 1.0
            a = 255
        tiklandi = t >= 1.6
        if 1.5 <= t < 1.75:
            sc *= 0.94
        w, h = bw * sc, bh * sc
        renk = (210, 210, 210) if tiklandi else (230, 0, 0)
        yazi = "ABONE OLUNDU" if tiklandi else "ABONE OL"
        yazi_renk = (60, 60, 60) if tiklandi else (255, 255, 255)
        katman = Image.new("RGBA", (W, H), (0, 0, 0, 110))   # arka planı hafif karart
        dk = ImageDraw.Draw(katman)
        dk.rounded_rectangle([cx - w / 2 + 8, cy - h / 2 + 10, cx + w / 2 + 8, cy + h / 2 + 10],
                             radius=h / 2, fill=(0, 0, 0, 90))
        dk.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=h / 2, fill=renk)
        fs = _font(max(20, int(70 * sc)))
        tw = dk.textlength(yazi, font=fs)
        ikon = int(46 * sc)
        toplam = tw + (ikon + 24 if tiklandi else 0)
        tx = cx - toplam / 2
        if tiklandi:   # onay işareti
            dk.line([(tx, cy), (tx + ikon * 0.35, cy + ikon * 0.35), (tx + ikon, cy - ikon * 0.4)],
                    fill=yazi_renk, width=max(4, int(10 * sc)))
            tx += ikon + 24
        dk.text((tx, cy - int(70 * sc) * 0.62), yazi, font=fs, fill=yazi_renk)
        # zil
        if tiklandi:
            zx, zy, zr = cx + w / 2 + 80, cy, 52
            dk.ellipse([zx - zr, zy - zr, zx + zr, zy + zr], fill=(255, 255, 255))
            dk.polygon([(zx - 20, zy + 14), (zx + 20, zy + 14), (zx + 14, zy - 4), (zx + 12, zy - 18),
                        (zx, zy - 26), (zx - 12, zy - 18), (zx - 14, zy - 4)], fill=(30, 30, 30))
            dk.ellipse([zx - 6, zy + 14, zx + 6, zy + 24], fill=(30, 30, 30))
        # imleç (el yerine ok): sağ alttan butona gelir, tıklar, geri çekilir
        if 0.5 <= t < 2.4:
            p = min(1.0, (t - 0.5) / 0.9)
            ix = cx + 420 - 300 * p
            iy = cy + 260 - 230 * p
            if t >= 1.9:
                q = (t - 1.9) / 0.5
                ix += 120 * q
                iy += 120 * q
            ok = [(0, 0), (0, 64), (16, 50), (28, 76), (40, 70), (28, 46), (50, 46)]
            dk.polygon([(ix + x * 1.4, iy + y * 1.4) for x, y in ok], fill="white", outline="black")
            if 1.5 <= t < 1.9:   # tıklama halkası
                r = 20 + 90 * (t - 1.5) / 0.4
                dk.ellipse([ix - r, iy - r, ix + r, iy + r], outline=(255, 255, 255, int(200 * (1 - (t - 1.5) / 0.4))),
                           width=6)
        if a < 255:
            katman.putalpha(katman.getchannel("A").point(lambda v: v * a // 255))
        img.alpha_composite(katman)
        img.save(os.path.join(kare_dir, f"{i:04d}.png"))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i",
                    os.path.join(kare_dir, "%04d.png"), "-c:v", "qtrle", "-pix_fmt", "argb", cikti], check=True)
    for x in os.listdir(kare_dir):
        os.remove(os.path.join(kare_dir, x))
    os.rmdir(kare_dir)
    return cikti


def paylas_oku(cikti, W=1080, H=1920):
    """TikTok kapanışı için: sağdaki paylaş butonunu gösteren ok + 'PAYLAŞ' yazısı (şeffaf PNG)."""
    img = Image.new("RGBA", (420, 200), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = _font(64)
    d.text((10, 60), "PAYLAŞ", font=f, fill=(255, 255, 255), stroke_width=6, stroke_fill=(0, 0, 0))
    ok = [(280, 70), (350, 70), (350, 40), (410, 100), (350, 160), (350, 130), (280, 130)]
    d.polygon(ok, fill=(230, 33, 23), outline=(0, 0, 0), width=5)
    img.save(cikti)
    return cikti
