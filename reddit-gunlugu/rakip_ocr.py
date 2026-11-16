"""Rakip TikTok videosunun kırmızı tek kelime altyazısını OCR ile okur (sadece analiz için; depoya koyma).
Kullanım: python3 rakip_ocr.py <tiktok_video_url> <çıktı.txt>
Gerekli: apt-get install -y tesseract-ocr tesseract-ocr-tur
"""
import os, re, subprocess, sys, tempfile
import numpy as np
from PIL import Image

url, cikti = sys.argv[1], sys.argv[2]
with tempfile.TemporaryDirectory() as d:
    mp4 = os.path.join(d, "v.mp4")
    subprocess.run(["yt-dlp", "-q", "-f", "b", "-o", mp4, url], check=True)
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", mp4, "-vf", "fps=6,scale=576:1024,crop=576:200:0:380",
                                   "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
    fh = 200
    n = len(raw) // (576 * fh * 3)
    a = np.frombuffer(raw, np.uint8)[:n * 576 * fh * 3].reshape(n, fh, 576, 3).astype(int)
    kel, onceki = [], None
    for i in range(n):
        r, g, b = a[i, ..., 0], a[i, ..., 1], a[i, ..., 2]
        m = (r > 170) & (g < 90) & (b < 90)
        if m.sum() < 150:
            continue
        p = os.path.join(d, "k.png")
        Image.fromarray(np.where(m, 0, 255).astype(np.uint8)).resize((1152, 400)).save(p)
        t = subprocess.run(["tesseract", p, "-", "-l", "tur", "--psm", "7"], capture_output=True, text=True).stdout.strip()
        t = re.sub(r"[^\wÇĞİÖŞÜçğıöşü'’\".,!?-]", "", t)
        if t and t != onceki:
            kel.append(t)
            onceki = t
open(cikti, "w").write(" ".join(kel))
print(len(kel), "kelime")
