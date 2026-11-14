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

### Kanalın stratejisi (önemli)
TikTok'un amacı **kitle toplayıp izleyiciyi YouTube'a göndermek**. Bu yüzden TikTok videosu hikayenin
**özeti değildir** ve **finali asla vermez**: hikayenin **başıdır (~5:00-5:10)** ve en heyecanlı yerde,
bir uçurum anında (cliffhanger) kesilir. Hikayenin devamı ve finali sadece YouTube'dadır.

### `hikaye.txt` (YouTube, tamamı)
- **4.300-4.800 kelime** (Ahmet sesi +%10 hızda dakikada ~110 kelime okur → 39-44 dk; en az 30 dk şart).
- İlk iki cümle güçlü bir merak kancası olsun.
- Hikayeyi öyle kur ki **yaklaşık 520-560. kelime civarında büyük bir dönüm noktası / sır / şok** olsun, **800-850. kelime civarında da ikinci bir uçurum** olsun
  (TikTok tam orada kesilecek). Kancayı ve ilk 6 dakikayı en güçlü şekilde yaz; ilk 6 dakikada izleyici
  kötü karakteri tanısın, haksızlığı hissetsin ve "şimdi ne olacak?" diye sorsun.

### Rakip analizi (11 Kasım 2026): @sultan.reddit ve @emirreddit
En çok izlenen Türkçe Reddit TikTok hesapları (video başına ort. 366 bin ve 436 bin izlenme, zirve 2,5 milyon
ve 1,7 milyon). Analiz edilen en iyi videoların ortak kalıpları; bunları uygula:
- **Hook = hikayenin tek paragraflık "özeti + intikam hamlesi"** (ilk 10-20 sn, 2-4 cümle). Kahramanın
  uğradığı haksızlığı ve **kendi yaptığı karşı hamleyi** söyler, ama sonucun nasıl biteceğini söylemez. Sonra
  hikaye o sahneden detaylıca baştan anlatılmaya başlar. Örnekler:
  - "Babam 'bu yıl hediye yok' dedi. Kız kardeşim ise bir iPhone ve elmas takılar açıyordu. 'Peki ya ben?'
    diye sorduğumda annem bana tokat attı. Ben de onların yaşam tarzını finanse eden bütün hesapları iptal ettim."
  - "Düğünden dakikalar önce nişanlımdan bir mesaj geldi: 'Bunu yapamam.' Nikâh memuruna dönüp 'planlarda
    ufak bir değişiklik var' dedim. Sonra onun en yakın arkadaşıyla evlendim. 72 saat sonra eski nişanlım
    bir şans daha için yalvarıyordu."
  - "Babamın vasiyetinde bana maddi değeri olan hiçbir şey bırakılmadığı söylendiğinde herkes güldü. Ta ki bana
    kalan şeye ihtiyaçları olana kadar."
- **Kesim yeri:** Olaylar hızlanırken, bir sahnenin ortasında, hatta bir cümlenin ortasında aniden keserler
  (ör. "Akşam altıda kapıya tebligatçı geldi." / "Açıldığında beş profili gördüm. Benimki, anneminki…").
  Ayrı bir "her şey değişecekti" cümlesine gerek yok; kesinti kendisi merak yaratır.
- **Kapanış (sabit, script ekler):** "İkinci bölümü beklemek istemiyorsan…" kalıbıyla YouTube'a yönlendirirler.
- **TikTok açıklaması:** Hikayenin ilk cümlesi **BÜYÜK HARFLE** ve "..." ile kesik + 🛑 + "Hikâyenin 2. bölümü
  profilimdeki bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ” kanalını arayın" + 2-3 hashtag.
- Hikayeler genelde aile içi haksızlık (miras/vasiyet, hediye ayrımcılığı, düğün/nişan iptali, aldatma,
  ailenin "işe yaramaz" dediği kişinin aslında herkesi finanse etmesi) ve **kahramanın sakin ama ezici
  karşı hamlesi** üzerine.

### Emir Reddit kalıbı (13 Kasım 2026 güncellemesi, kullanıcı isteği: "Emir Reddit'in hook'larını kullan")
Kullanıcı "şu an izlenmiyor" dedi; @emirreddit (TikTok, video başı 200 B-1,8 M) ile karşılaştırınca bulunan farklar ve
artık uygulanan kurallar (ayrıntı: `ANALIZ-TIKTOK.md`, 13 Kasım bölümü):
- **Duraklama yok:** Emir'de 0,25 sn üstü sessizlik yok; bizde her cümle sonunda ~1,2 sn vardı (sürenin %30'u).
  `uret.py` artık TikTok sesinde tüm sessizlikleri 0,1 sn'ye kısaltıyor ve +%20 hızla okutuyor (YouTube değişmedi).
- **Süre 5:00-5:10** (Emir'in bütün videoları 300-310 sn). TikTok metni bu yüzden **~830-850 kelime** (hook dahil).
- **Altyazı:** ekranda tek kelime, kırmızı, ince siyah kenar; logo ortada değil, sağ altta küçük. (`uret.py` otomatik.)
- **Hook = tek, somut, ilk cümle**; açıklama bu cümlenin ilk ~10 kelimesi + "...". Emir'in en çok izlenen kalıpları:
  - Sır/kulak misafiri: "BABAM BUNU BİLMİYOR AMA BİR ADAMA…" (777 B), "KOCAM, ANNESİNE KORECE OLARAK…SÖYLEMİŞTİ" (722 B)
  - Haksızlık + somut eşya karşıtlığı: "BABAM 'BU YIL HEDİYE YOK' DEDİ, KIZ KARDEŞİM İSE BİR İPHONE, 5.000 DOLARLIK…" (926 B)
  - Hakaret alıntısı: "KARDEŞİM DEDİ Kİ: 'AİLENİN İŞE YARAMAZ İNSANLARINI ATALIM. SEN ÖNCE GİDERSİN'" (798 B),
    "YEĞENİM 7 YAŞINDAKİ OĞLUMA BAKIP 'SADECE BÜYÜKANNENİN GERÇEK TORUNLARI ÖNCE YER'" (724 B)
  - İroni/paradoks: "BABAMIN VASİYETİNDE BANA MADDİ DEĞERİ OLAN HİÇBİR ŞEY BIRAKILMADIĞI…" (1,8 M),
    "ANNEMİN DÜĞÜNÜNDEYDİM. ORADA OLDUĞUMDAN HABERİ BİLE YOKTU" (493 B)
  - Talep + beklenmedik karşılık: "KİRACILARIM KİRAYI DÜŞÜRMEMİ İSTEDİ. BEN DE…" (902 B)
  - Kaza ile ortaya çıkan gerçek: "NİŞANLIM INSTAGRAM'A BİR VİDEO YÜKLEDİ VE SESİNİ KAPATMAYI UNUTTU" (418 B)
  İki TikTok'tan birinde mutlaka bu kalıplardan birini **kelimesi kelimesine yapı olarak** kullan (içerik özgün kalsın).
- **Açıklama formatı (Emir'in birebir yapısı):** `İLK CÜMLENİN İLK ~10 KELİMESİ... 🛑 Hikâyenin 2. Bölümü profilimdeki
  bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ” kanalını aratarak bulabilirsiniz. 🛑 #redditturkiye` (tek hashtag).
- **Yeniden yükleme:** Emir aynı videoyu 2-3 kez yüklüyor (aynı video 36 B / 65 B / 148 B; 259 B / 493 B aldı).
  Son mesajda kullanıcıya hatırlat: ilk yükleme düşük kalırsa ertesi gün aynısını tekrar yüklesin.

### Konu seçimi ve 3 versiyon (13 Kasım 2026, kullanıcı kararı)
Kullanıcı: "Videoda hiçbir şey dikkatimi çekmiyor; Emir Reddit'in hook'larını al, aynı hikayeyi farklı editlerle tekrar paylaşıyorlar."
- **Konu:** Her gün @emirreddit'in (ve Sultan Reddit'in) en çok izlenen hikayelerinden, arşivde olmayan birinin
  **konusunu ve hook yapısını** al; olayları, karakterleri ve finali **kendin yaz** (metni/videoyu kopyalama).
  Liste: `yt-dlp --flat-playlist --print "%(view_count)s|||%(description)s" "https://www.tiktok.com/@emirreddit" | sort -rn`.
  Henüz kullanılmayanlar (13 Kasım): kiracılar kira indirimi (902 B), "babam bunu bilmiyor ama" (777 B),
  yeğen "gerçek torunlar önce yer" (724 B), kocanın yabancı dilde sırrı (722 B), annemin düğünü (493 B),
  kocamın günlüğü (423 B), nişanlının sesi açık video (418 B), Disney biletleri (201 B), tatil masrafı yeğenler (148 B).
- **3 TikTok:** `tiktok.txt`, `tiktok2.txt`, `tiktok3.txt`; gövde aynı, hook'lar farklı (1: Emir'in yapısı birebir,
  2: gizli gerçek/şok, 3: hakaret alıntısı). `uret.py` her versiyona farklı arka plan sırası ve kesit verir.
  metadata.md'de üç açıklama ve paylaşım saatleri olsun.

### `tiktok.txt`, `tiktok2.txt`, `tiktok3.txt` (üç TikTok, hikayenin başı, **~5:00-5:10**)
- Aynı hikayeden **iki ayrı TikTok** yaz: gövde aynı, **hook'lar farklı** (biri hikayenin başındaki
  haksızlığı, öbürü ilerideki büyük şoku/karşı hamleyi öne çıkarsın). Örnek: `bolumler/2026-11-11-ambulans/`.
- Başa **Emir kalıbında tek güçlü ilk cümle** + en fazla 2-3 kısa cümle (haksızlık/sır + kahramanın hamlesi) yaz;
  sonucu ve finali söyleme. İlk cümle tek başına açıklamaya yazılacak; somut, alıntılı, şaşırtıcı olsun.
- Hook'tan sonra `hikaye.txt`'nin **başını aynen** kullan (Reddit başlık cümlesi yerine hook gelir),
  **özetleme, kısaltma yapma**. Toplam **~830-850 kelime** (duraklamasız +%20 seste dakikada ~165 kelime; kapanışla ~5:00-5:10) olacak şekilde kes.
- Olaylar hızlanırken, bir sahnenin ortasında kes (gerekirse cümle ortasında). Ayrı bir uçurum cümlesi şart
  değil; kesinti noktası merak yaratmalı.
- Kapanış cümlesini **yazma**; script otomatik ekler ("İkinci bölümü beklemek istemiyorsan…").
- Örnek: `bolumler/2026-11-11-ambulans/tiktok.txt` ve `tiktok2.txt`.

### `metadata.md`
- YouTube başlığı (en fazla 100 karakter, merak uyandıran, sonunda `| Reddit Hikayeleri`)
- YouTube açıklaması (3-4 cümle özet, spoiler vermeden; sonunda `#reddit #reddithikayeleri #redditgunlugu`)
- YouTube etiketleri (10-15 tane, virgülle)
- İki TikTok açıklaması (Emir formatı, her biri kendi hook'unun ilk cümlesiyle): ilk cümlenin ilk ~10 kelimesi BÜYÜK HARFLE ve "..." ile kesik + ` 🛑 Hikâyenin 2. Bölümü profilimdeki bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ” kanalını aratarak bulabilirsiniz. 🛑 #redditturkiye`. İki TikTok'u farklı saatlerde paylaşmasını öner (ör. 13:00 ve 21:00).
- Hatırlatma: "İki platformda da 'yapay zekâ ile oluşturulan içerik' seçeneğini aç. YouTube 19:30, TikTok 21:00."

### YouTube görünümü ve abone hatırlatmaları (14 Kasım 2026, kullanıcı isteği)
Kullanıcı: "TikTok'ta ilk video 14 B izlendi; YouTube'da abone az, kapak yok."
- `uret.py youtube` artık Emir tarzı üretir (`kart.py`): Minecraft arka planının üstünde ekranın çoğunu kaplayan
  turkuaz çerçeveli beyaz kart; kartta logo, "Reddit Günlüğü" + onay rozeti ve dev büyük harf başlık; altyazı kartın
  alt kısmında siyah, okunan kelime kırmızı; sol altta logo.
- Başlık: bölüm klasöründe `kart.txt` varsa o (en iyi hook cümlesi, ~15-25 kelime, sonu "..."), yoksa
  `hikaye.txt`'nin ilk paragrafının ilk 22 kelimesi. **TikTok'ta en çok tutan hook'u `kart.txt`'ye yaz.**
- Ses: ilk paragraftan sonra "Başlamadan önce küçük bir rica… abone olmayı ve zil butonuna basmayı unutma",
  sonda abone/beğen/yorum çağrısı (`YT_GIRIS`, `YT_KAPANIS`). Ekranda: girişte, sonra her 5 dakikada bir ve kapanışta
  ortada "ABONE OL → ✓ ABONE OLUNDU" animasyonu.
- Kapak: `kapak.jpg` (1280x720, aynı kart, bulanık arka plan) otomatik üretilir; teslimde gönder ve
  "YouTube'da özel küçük resim olarak yükle" de.
- Maskotlu logo gelirse `girdi/logo.png` yerine koy (kare, şeffaf PNG); kart, kapak ve köşe logosu onu kullanır.

### TikTok kapanışı (14 Kasım 2026)
Emir kapanışta izleyiciye "paylaş seçeneğine" bastırıyor (paylaşım TikTok'ta en güçlü sinyal). Bizim kapanış
(`KAPANIS`): YouTube yönlendirmesi + "Önce sağdaki paylaş butonuna bas ve bu hikayeyi bir arkadaşına gönder" +
abone hatırlatması; kapanış boyunca sağda paylaş butonunu gösteren sallanan "PAYLAŞ ➜" oku.

## 3. Videoları üret
```bash
cd reddit-gunlugu
K=bolumler/<bugünün klasörü>
python3 uret.py tiktok  --klasor $K
python3 uret.py youtube --klasor $K
python3 uret.py teslim  --klasor $K     # tiktok-gonder.mp4, tiktok2-gonder.mp4, youtube-gonder.mp4 (<380 MiB)
```
Uzun süren komutları arka planda çalıştır (YouTube render ~12 dk). Seslendirme kesilirse script kendisi tekrar dener.

## 4. Kontrol et
- `ffprobe` ile süreler: YouTube **≥ 30 dk**, her TikTok **4:55-5:15**. Dışındaysa metni uzat/kısalt,
  `$K/_*ses*` dosyalarını sil ve tekrar üret.
- Her videonun başından, ortasından ve sonundan birer kare al ve bak: altyazı okunuyor mu, logo yerinde mi,
  Türkçe harfler (İ, Ş, Ğ) doğru mu, TikTok'un son karesinde kapanış cümlesi var mı.

## 5. Teslim et
1. `SendUserFile` ile üç TikTok, YouTube, `kapak.jpg`, `metadata.md` ve `hikaye.txt`'yi gönder. Her TikTok'u ayrı gönder, açıklamasını dosya notuna yaz (kullanıcı böyle istiyor).
   Kullanıcı telefonda 368 MB'lık YouTube dosyasını indiremedi: önce 720p küçük kopyayı gönder
   (`ffmpeg -i youtube.mp4 -vf scale=1280:720 -c:v libx264 -preset veryfast -b:v 420k -maxrate 600k -bufsize 1200k -c:a aac -b:a 96k -movflags +faststart youtube-kucuk.mp4`, ~155 MB),
   sonra ayrıca `youtube-gonder.mp4`'ü
   (`status: "proactive"`, `display: "attach"`). Bir dosya sınırı aşarsa `teslim`'i daha düşük `sinir_mb` ile çalıştır.
2. Google Drive'daki **"Reddit Günlüğü"** klasörüne (id `1sI2YL12nqI-Wj9PToB66bBJUsZYAwqJf`) o günün adıyla
   `metadata.md`'yi metin dosyası olarak yükle. Drive 10 MB üstünü kabul etmez; videoları Drive'a yükleme.
   Drive bağlantısı yoksa veya izin hatası verirse bu adımı atla ve son mesajda söyle.
3. `bolumler/ARSIV.md`'ye yeni satır ekle. Metin dosyalarını (`hikaye.txt`, `tiktok.txt`, `tiktok2.txt`, `metadata.md`, `arastirma.md`) ve
   arşivi commit edip `main`'e push et. Video ve ara dosyalar `.gitignore`'da; onları ekleme.

## 6. Son mesaj (kullanıcıya, Türkçe, kısa)
- "Günaydın" ile başla; bugünün hikayesinin adı ve tek cümlelik özeti
- Araştırmadan tek cümle: bu temayı neden seçtin (ör. hangi başlık kaç izlenme almış)
- Video süreleri
- Yükleme hatırlatması (tercih: YouTube 19:30; TikTok 1 ve 2 farklı saatlerde, ör. 13:00 ve 21:00), başlık ve açıklamaların metadata.md'de olduğu
- Bir adım başarısız olduysa ne olduğu, dürüstçe
