# Günlük bölüm üretimi (zamanlanmış görev talimatı)

Bu dosya, her gün çalışan zamanlanmış görevin adım adım talimatıdır. Kanal: **Reddit Günlüğü**.
Kullanıcı Türkçe konuşur; ona yazdığın her mesaj Türkçe, sade ve telefonda okunacak kadar kısa olsun.
Görev her gece/sabaha karşı çalışır; kullanıcı sabah bildirimi görüp videoları gün içinde kendisi yükler.
Tercih ettiği yayın saatleri: **YouTube 19:30, TikTok 21:00** (Türkiye saati); yükleme saatini kendisi seçebilir.

## 0. Kurulum (her çalıştırmada)
```bash
cd reddit-gunlugu
pip install -q edge-tts pillow
which ffmpeg ffprobe   # yoksa: apt-get install -y ffmpeg
```
Font repoda: `fonts/Montserrat-ExtraBold.otf`. Logo ve Minecraft görseli: `girdi/logo.png`, `girdi/minecraft.png`.

## 1. Araştır: ne izleniyor?
Amaç: bugünün hikayesini, şu an en çok izlenen tema ve kanca kalıplarına göre seçmek. 10-15 dakikayı geçirme.

```bash
# Türkçe Reddit hikaye kanallarının son videoları ve izlenmeleri (YouTube)
yt-dlp --flat-playlist --playlist-end 30 --print "%(view_count)s	%(title)s" "https://www.youtube.com/@sultanreddit/videos"
# YouTube araması: güncel Türkçe Reddit hikayeleri
yt-dlp --flat-playlist --print "%(view_count)s	%(channel)s	%(title)s" "ytsearch30:reddit hikayeleri türkçe"
yt-dlp --flat-playlist --print "%(view_count)s	%(channel)s	%(title)s" "ytsearch20:reddit hikaye aile intikam"
```
- YouTube tek tek video sayfalarını bot engeline takabilir; liste ve arama çalışır. Bir komut başarısız olursa
  diğerleriyle devam et.
- Varsa web aramasıyla (WebSearch) son haftalarda Türkiye'de TikTok/YouTube'da konuşulan Reddit hikaye
  temalarına bak (ör. "reddit hikayeleri tiktok trend", "AITA en çok konuşulan").
- **Videoları indirme, başkasının hikayesini kopyalama.** Sadece hangi temaların, başlık kalıplarının ve
  kancaların izlendiğine bak; hikayeyi kendin özgün yaz.
- Bulduklarını bugünün klasöründe `arastirma.md`'ye kısaca yaz: en çok izlenen 5 başlık (izlenme sayısıyla),
  öne çıkan temalar, seçtiğin tema ve neden, kullandığın kanca kalıbı.

## 2. Yeni hikaye yaz
- Önce `bolumler/ARSIV.md`'yi oku. **Konu, olay örgüsü, final ve karakter isimleri önceki bölümlerle aynı olmasın.**
- Araştırmada en çok izlenen temalardan birini, arşivde olmayan bir açıyla kullan.
- Bugünün tarihiyle klasör aç: `bolumler/YYYY-AA-GG-kisa-konu/`.
- Tamamen **özgün** bir hikaye yaz; gerçek kişi, marka veya başka bir yazarın hikayesi olmasın.
- Tarz: Türkçe, birinci tekil şahıs, Reddit gönderisi gibi ("Bu hesabı sadece bunu anlatmak için açtım…"),
  sonunda 2-3 "GÜNCELLEME" bölümü. Anlatıcı **erkek** (ses: Ahmet). Aile dramı, ihanet, haksızlık ve
  tatmin edici bir adalet/intikam finali en çok izlenen türler; her gün farklı bir ana tema seç
  (miras, düğün, iş yeri, komşu, ev arkadaşı, kayınvalide, okul, sahte arkadaş vb.).
- Sahne sahne, diyaloglu yaz. Kötü karakterlerin bile anlaşılır sebepleri olsun. Şiddet, cinsellik, nefret
  söylemi yok; TikTok ve YouTube topluluk kurallarına uygun olsun.

### `hikaye.txt` (YouTube, tamamı)
- **4.300-4.800 kelime** (Ahmet sesi +%10 hızda dakikada ~110 kelime okur → 39-44 dk; en az 30 dk şart).
- İlk iki cümle güçlü bir merak kancası olsun.

### `tiktok.txt` (TikTok, ~10 dk)
- `hikaye.txt`'nin kısaltması: **1.050-1.100 kelime** (~10 dk).
- Tekrarları, gereksiz detayları, uzun girişleri çıkar; olay örgüsü ve final bozulmasın.
- **Başa 1-2 cümlelik etkileyici hook** yaz: en çarpıcı anı ya da soruyu öne çek.
- Kapanış cümlesini **yazma**; script otomatik ekler.

### `metadata.md`
- YouTube başlığı (en fazla 100 karakter, merak uyandıran, sonunda `| Reddit Hikayeleri`)
- YouTube açıklaması (3-4 cümle özet, spoiler vermeden; sonunda `#reddit #reddithikayeleri #redditgunlugu`)
- YouTube etiketleri (10-15 tane, virgülle)
- TikTok açıklaması (en fazla 150 karakter, emoji + `#redditturkiye #hikaye #reddit #keşfet`)
- Hatırlatma: "İki platformda da 'yapay zekâ ile oluşturulan içerik' seçeneğini aç. YouTube 19:30, TikTok 21:00."

## 3. Videoları üret
```bash
cd reddit-gunlugu
K=bolumler/<bugünün klasörü>
python3 uret.py tiktok  --klasor $K
python3 uret.py youtube --klasor $K
python3 uret.py teslim  --klasor $K     # tiktok-gonder.mp4, youtube-gonder.mp4 (<380 MiB)
```
Uzun süren komutları arka planda çalıştır (YouTube render ~12 dk). Seslendirme kesilirse script kendisi tekrar dener.

## 4. Kontrol et
- `ffprobe` ile süreler: YouTube **≥ 30 dk**, TikTok **9-11 dk**. Dışındaysa metni uzat/kısalt,
  `$K/_*ses*` dosyalarını sil ve tekrar üret.
- Her videonun başından, ortasından ve sonundan birer kare al ve bak: altyazı okunuyor mu, logo yerinde mi,
  Türkçe harfler (İ, Ş, Ğ) doğru mu, TikTok'un son karesinde kapanış cümlesi var mı.

## 5. Teslim et
1. `SendUserFile` ile `tiktok-gonder.mp4`, `youtube-gonder.mp4`, `metadata.md` ve `hikaye.txt`'yi gönder
   (`status: "proactive"`, `display: "attach"`). Bir dosya sınırı aşarsa `teslim`'i daha düşük `sinir_mb` ile çalıştır.
2. Google Drive'daki **"Reddit Günlüğü"** klasörüne (id `1sI2YL12nqI-Wj9PToB66bBJUsZYAwqJf`) o günün adıyla
   `metadata.md`'yi metin dosyası olarak yükle. Drive 10 MB üstünü kabul etmez; videoları Drive'a yükleme.
   Drive bağlantısı yoksa veya izin hatası verirse bu adımı atla ve son mesajda söyle.
3. `bolumler/ARSIV.md`'ye yeni satır ekle. Metin dosyalarını (`hikaye.txt`, `tiktok.txt`, `metadata.md`, `arastirma.md`) ve
   arşivi commit edip `main`'e push et. Video ve ara dosyalar `.gitignore`'da; onları ekleme.

## 6. Son mesaj (kullanıcıya, Türkçe, kısa)
- "Günaydın" ile başla; bugünün hikayesinin adı ve tek cümlelik özeti
- Araştırmadan tek cümle: bu temayı neden seçtin (ör. hangi başlık kaç izlenme almış)
- Video süreleri
- Yükleme hatırlatması (tercih: YouTube 19:30, TikTok 21:00), başlık ve açıklamaların metadata.md'de olduğu
- Bir adım başarısız olduysa ne olduğu, dürüstçe
