# Video Kurgu

Hikaye videoları (dikey 9:16, Reels/Shorts/TikTok) için araç seti.

| Araç | Ne işe yarar |
|---|---|
| **FFmpeg** | Video/ses kesme, birleştirme, format dönüştürme |
| **yt-dlp** | İnternetten video/ses indirme |
| **Whisper** | Seslendirmeyi yazıya döker → altyazı (`.srt`) |
| **edge-tts** | Metni Türkçe seslendirir (Emel/Ahmet), karakter sınırı yok |
| **HyperFrames** | HTML ile video sahneleri yapıp MP4'e render eder |

## Kurulum

```bash
./kurulum.sh   # araçları kurar
./kontrol.sh   # hepsinin çalıştığını kontrol eder
```

## Örnek proje: `test-hikaye/`

1080×1920 dikey, 3 saniyelik başlık animasyonu.

```bash
cd test-hikaye
npm install
npx hyperframes render -o renders/hikaye.mp4
```

## Telifsiz arka plan: `arka-plan-slime/`

Kendi ürettiğimiz akışkan slime animasyonu (1080×1920, 15 sn kusursuz döngü).

```bash
cd arka-plan-slime && npx hyperframes render -o renders/slime.mp4
ffmpeg -stream_loop 3 -i renders/slime.mp4 -c copy slime-60sn.mp4   # 60 sn yap
```

## Telifsiz arka plan: `arka-plan-sabun/`

Renkli katmanlı sabunun bıçakla dilimlendiği animasyon (1080×1920, 15 sn döngü).

## Hikayeden tek komutla video: `hikaye-video.py`

Hikaye dosyasının ilk satırı anlatıcıyı seçer: `anlatici: kadin` (Emel sesi) veya `anlatici: erkek` (Ahmet sesi).
Script seslendirir, TikTok tarzı tek kelimelik altyazı ekler ve arka planı döngüye alır.

```bash
python3 hikaye-video.py hikayeler/001-evlenme-abla.txt arka-plan.mp4 cikti.mp4 --hiz +10%
```

## Sık kullanılan komutlar

```bash
# Hikayeyi seslendir + altyazı üret (kadin/erkek, hız)
./seslendir.sh hikaye.txt kadin +10%

# Seslendirmeden Türkçe altyazı çıkar
whisper seslendirme.mp3 --language tr --model small --output_format srt

# Altyazıyı videoya göm
ffmpeg -i video.mp4 -vf subtitles=seslendirme.srt -c:a copy altyazili.mp4

# Videodan sadece ses al
ffmpeg -i video.mp4 -vn -c:a mp3 ses.mp3

# Video indir
yt-dlp -f mp4 "VIDEO_LINKI"
```
