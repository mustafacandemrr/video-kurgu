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
  profilimdeki bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ PLUS” kanalını arayın" + 2-3 hashtag.
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
  Her hikayenin hook'unda bu kalıplardan birini **yapı olarak** kullan (içerik özgün kalsın).
- **Açıklama formatı (Emir'in birebir yapısı):** `İLK CÜMLENİN İLK ~10 KELİMESİ... 🛑 Hikâyenin 2. Bölümü profilimdeki
  bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ PLUS” kanalını aratarak bulabilirsiniz. 🛑 #redditturkiye` (tek hashtag).
- **Yeniden yükleme:** Emir aynı videoyu 2-3 kez yüklüyor (aynı video 36 B / 65 B / 148 B; 259 B / 493 B aldı).
  Son mesajda kullanıcıya hatırlat: ilk yükleme düşük kalırsa ertesi gün aynısını tekrar yüklesin.

### TİKTOK OPTİMİZASYON SİSTEMİ (21 Kasım 2026, kullanıcı brifingi — bu bölüm aşağıdaki eski TikTok kurallarının önüne geçer)
Kullanıcının verisi: TikTok 1 → 108,6 B izlenme, ort. 51 sn, %17 izlenme, %2,52 tamamlama; TikTok 2 → 26,5 B, 37,9 sn,
%13, %3,41. İkisinde de ilk saniyelerde büyük kayıp. **Öncelik daha çok video değil, tutma oranı.** Önerileri garanti
gibi değil, test edilecek hipotez olarak sun.

**Her hikaye için `tiktok_plan.md` (teslimde gönder) şunları içerir:**
1. Üç farklı hook (H1, H2, H3). Kurallar: ilk 1-2 sn'de olay/cümle; 10-15 sn'de güçlü merak; selamlama yok;
   sonu söyleme; yapay/abartılı cümle yok; hook'tan sonra hikaye doğal devam eder, aynı olay ikinci kez anlatılmaz.
2. En güçlü hook'un seçimi ve gerekçesi.
3. ~4-5 dk TikTok anlatım metni (YouTube'un ilk 5 dk'sının kopyası DEĞİL, TikTok'a özel kurgu):
   0-15 sn hook · 15-45 sn temel çatışma · 45-90 sn yeni gelişme/merak · 90-180 sn ilerleme, gerilim ·
   180-270 sn dönüm noktası · son 10-15 sn doğal merak noktası + YouTube yönlendirmesi (katı değil, akışa göre).
   "Bu hesabı sadece bunu anlatmak için açtım…" gibi dolgu cümleleri TikTok'ta YOK; geçmiş bilgisi kısa ve çatışmanın
   içine serpiştirilir. ~680-760 kelime (+ kapanış) ≈ 4:00-4:30 (hızlı tempoda ~2,8 kelime/sn; 22.11'de 590 kelime 3:40 tuttu).
   **Son cümle(ler) `hikaye.txt`'deki bir cümleyle kelimesi kelimesine aynı olmalı** (en az son 8 kelime): YouTube'daki
   "2. bölüm buradan başlıyor" zamanı bu eşleşmeyle bulunur.
4. Zaman kodlarına göre arka plan önerisi (hangi kategori hangi bölümde).
5. Altyazı vurguları: metinde `*kelime*` (en fazla ~8-10 kelime, hikayenin kilit nesneleri/isimleri). Script bunları
   sarı gösterir, seslendirmeye yıldız gitmez.
6. TikTok başlığı ve açıklaması (ilk ~10 kelime BÜYÜK HARF + "..." + 🛑 REDDIT GÜNLÜĞÜ PLUS kalıbı + #redditturkiye).
7. YouTube'a yönlendiren kapanış: sabit `KAPANIS` (uret.py): "Hikâyenin devamı ve tamamı YouTube'da, Reddit Günlüğü Plus
   kanalında. Devamı için profilime göz atabilirsin. Beğendiysen sağdaki paylaş butonuyla bu hikâyeyi bir arkadaşına
   gönder." Sahte merak noktası yok: kesilen yer hikayede gerçekten olan bir an.

**Dosyalar:** `tiktok.txt` = H1 + TikTok gövdesi; `tiktok2.txt` = günün testine göre (aşağı bak). Her TikTok'un yanına
isteğe bağlı `tiktok.json` / `tiktok2.json`: `{"altyazi": "tek"|"grup", "tempo": "hizli"|"dogal", "arka": "karisik"|
["sac","pasta",...], "varyant": 0}`. Varsayılan (kontrol): tek kelime kırmızı altyazı, hızlı tempo (+%20, duraklama ≤0,1 sn),
karışık kategori sahneleri.

**Arka plan (uret.py `KATEGORI`, Mixkit ücretsiz lisans):** sac, pasta, slime (slime + oyun hamuru), sabun (el yapımı sabun),
el_sanati (boyama, çömlek, oje), ahsap, metal (kaynak, taşlama, demirci), temizlik (oto cila, koltuk/halı), yemek, bakim
(spa, dövme). Her sahne tek kategoriden 30-60 sn; klipler bütün oynar. Kinetik kum için lisanslı klip bulunamadı.
Lisanssız (rakip/başka üreticilerin) görüntüsü kullanma.

**Test sistemi (bir testte tek değişken):** Her gün A/B/C'nin iki TikTok'u farklı bir değişkeni test eder; diğer her şey
(metin gövdesi, arka plan sırası `varyant`, tempo, altyazı) aynı tutulur:
- Hook testi: tiktok.txt = H1, tiktok2.txt = H2 + aynı gövde; ikisinde `"varyant": 0`.
- Arka plan testi: aynı hook; tiktok.json `"arka": "karisik"`, tiktok2.json `"arka": [tek ya da iki kategori]`.
- Altyazı testi: aynı hook ve arka plan; tiktok2.json `"altyazi": "grup"`.
- Tempo testi: aynı hook; tiktok2.json `"tempo": "dogal"`.
Sırayla döndür. Not: iki TikTok farklı saatlerde paylaşıldığı için saat de karışan bir etken; mümkünse aynı saatte
farklı günlerde karşılaştır. Sonuçları `bolumler/TIKTOK_TEST.md` tablosuna kullanıcı doldurur (ilk 3 sn tutma, ort.
izleme, %izlenme, tamamlama, profil ziyareti, yeni takipçi, YouTube'a giden). Kazanan ayar bir sonraki haftanın kontrolü olur.

### ⚠️ GÜNCEL GÜNLÜK PLAN (24 Kasım 2026, kullanıcı kararı — aşağıdaki "günde 3 hikaye" planının ve günlük test rotasyonunun yerine geçer)
Kullanıcı: "Günlük video sayımızı 1'e indiriyoruz. YouTube'da izlenmesi için 3 çok video. TikTok için 3 tane aynı video
farklı arka plan olsun."
- Her çalıştırmada **tek hikaye**: `bolumler/<YARININ TARİHİ>-konu/` (harf eki yok). **1 YouTube** (yayın 08:00) + **3 TikTok**.
- Üç TikTok **aynı metin, aynı hook, aynı tempo ve altyazı**; yalnızca **arka plan** farklı:
  `tiktok.txt`, `tiktok2.txt`, `tiktok3.txt` birebir aynı (H1 + gövde). JSON'lar:
  tiktok.json `{"arka": "karisik", "varyant": N}`, tiktok2.json `{"arka": [hikayeye uygun 1-2 kategori], "varyant": N}`,
  tiktok3.json `{"arka": [başka 1-2 kategori], "varyant": N}` (altyazı "tek", tempo "hizli"). `uret.py tiktok` tüm
  `tiktok*.txt`'leri üretir; kuyrukta sıkıştırma döngüsü `tiktok tiktok2 tiktok3`.
- TikTok saatleri (24.11 rakip analizi): üç TikTok aynı oturumda, YouTube yayına girdikten sonra 08:15-08:17, 1-2 dk arayla (bkz. ANALIZ-TIKTOK.md). metadata.md'de üç TikTok açıklaması (aynı başlık) + sabitlenmiş yorum.
- `tiktok_plan.md` yine 7 maddeyi içerir (3 hook, seçim, metin, arka plan, vurgu, başlık, kapanış); test = arka plan
  (üç ayar). TIKTOK_TEST.md'ye 3 satır.
- Hikaye ≥3.000 kelime (YouTube 30+ dk), TikTok ~700-760 kelime. Rakip listesinden her gün bir konu.
- **Geçiş (24 Kasım):** 25 Kasım için üretilmiş üç hikaye yayına bölünüyor: `2026-11-25-a-kaza` → 25 Kasım,
  `2026-11-25-b-sofor` → 26 Kasım, `2026-11-25-c-istasyon` → 27 Kasım (her biri 08:00 YouTube + 3 TikTok). Bu yüzden
  **25 Kasım gecesi ve 26 Kasım gecesi çalışmalarında yeni hikaye üretme**: git pull, disk temizliği (bu üç klasörün
  mp4'lerine dokunma), kullanıcıya o günün hazır klasörünü hatırlat ("Günaydın…" mesajı). Yeni üretim 27 Kasım gecesi
  (28 Kasım için) başlar.

### (ESKİ) GÜNLÜK PLAN: günde 3 hikaye, her hikayeye 1 YouTube + 2 kancalı TikTok (16 Kasım 2026, kullanıcı kararı)
Kullanıcı: "YouTube'u günde 3'e çıkaracağız. Yarının videolarını bugün akşamdan YouTube'a saat kurarak yükleyeceğim
(08:00, 12:00, 19:00). TikTok'ları gün içinde yüklerim. Her videoya birden fazla kanca istiyorum: video aynı, ilk
5-15 saniye farklı." Bu görev gece çalışır ve **ertesi günün** içeriğini üretir; kullanıcı akşam üzeri yükleyip zamanlar.
(Rakip verisi, 15 Kasım: Emir her hikayeyi tek ~5:03'lük TikTok olarak 2-3 kez yeniden yüklüyor; Sultan YouTube'a günde
2 uzun video, ~08:00 ve ~12:00.)

Her çalıştırmada **üç hikaye**: `bolumler/<YARININ TARİHİ>-a-konu/`, `-b-konu/`, `-c-konu/` (klasör tarihi = yayın günü).
- YouTube yayın saatleri: A 08:00, B 12:00, C 19:00 (metadata.md'ye yaz).
- Her hikayede **iki TikTok**: `tiktok.txt` (kanca 1 = `hikaye.txt`'nin ilk paragrafı) ve `tiktok2.txt` (kanca 2 =
  hikayenin içinden en çarpıcı an/sır/alıntı, 2-3 cümle, finali vermeden). İkisinde de kancadan sonraki gövde aynı:
  `hikaye.txt`'nin ikinci paragrafından başlayıp ~830-850. kelimeye kadar aynen. Örnek: `bolumler/2026-11-16-a-almanca/tiktok2.txt`.
- metadata.md'de iki TikTok açıklaması (her biri kendi kancasının ilk ~10 kelimesi) ve önerilen TikTok saatleri:
  A 09:00 + 14:00, B 13:00 + 18:00, C 20:00 + 22:00 (kanca 1 önce, kanca 2 sonra).
- Üretim sırası: A, B, C tek arka plan komutunda; teslimde her hikaye için TikTok 1, TikTok 2, YouTube 720p, kapak, metadata.
- `kart.txt` = kanca 1'in ilk cümlesi; YouTube başlığı da bu cümle.

### Rakip hikayelerini okuma (16 Kasım 2026)
Kullanıcı: "Emir'in en popüler içeriklerinin hikayesini çekip benzerlerini yap." YouTube sayfaları bot engeline takılıyor
ve Whisper modeli indirilemiyor; Emir'in TikTok altyazısı tek kelime ve kırmızı olduğu için **OCR** ile okunuyor:
`apt-get install -y tesseract-ocr tesseract-ocr-tur`, sonra `python3 rakip_ocr.py <tiktok_video_url> <çıktı.txt>`
(kırmızı pikselleri ayırıp tesseract'a verir; metin gürültülü ama olay örgüsü anlaşılır). Okunan metin **sadece analiz
içindir**: depoya koyma, kopyalama. Kendi cümlelerinle 3-5 satırlık bir kurulum özeti çıkar, "Sıradaki konular"
listesinde ilgili satırın altına yaz; hikayeyi o kurulumdan yola çıkıp kendi olaylarınla ve finalinle yaz.

- **Konu:** @emirreddit'in (ve Sultan Reddit'in) en çok izlenen hikayelerinden, arşivde olmayan **üç** tanesinin
  **konusunu ve hook yapısını** al; olayları, karakterleri ve finali **kendin yaz** (metni/videoyu kopyalama).
  Liste: `yt-dlp --flat-playlist --print "%(view_count)s|||%(description)s" "https://www.tiktok.com/@emirreddit" | sort -rn`.
  Henüz kullanılmayanlar (15 Kasım): yeğen "gerçek torunlar önce yer" (725 B), kocanın yabancı dilde sırrı (726 B),
  annemin düğünü (524 B), kocamın günlüğü (424 B), nişanlının sesi açık video (419 B), "karım gözlerimin içine
  bakarak…" (360 B), Disney biletleri (201 B), tatil masrafı yeğenler (153 B), trafik kazası sonrası karım (146 B).
  İki hikayenin ana teması birbirinden farklı olsun (ör. biri aile/miras, biri evlilik/iş yeri).
- `arastirma.md` günde bir kez, ilk hikayenin (`-a-`) klasörüne; ikisinin seçim nedenini de yaz.
- Her hikayede **tek** `tiktok.txt` olsun (`tiktok2.txt`/`tiktok3.txt` yazma). TikTok = `hikaye.txt`'nin **ilk
  paragrafı (hook) dahil başından itibaren aynen**, ~830-850 kelimede uçurumda kesilmiş hali. Böylece YouTube videosu
  TikTok'la birebir aynı cümlelerle açılır; TikTok'ta duyulan her şey YouTube'da aynı sırayla vardır.
- `kart.txt` = hook'un ilk cümlesi (sonu "..."); YouTube başlığı da bu cümle (aşağıya bak).

### Sıradaki konular (15 Kasım 2026, kullanıcı: "Bu iki kişinin en çok izlenen hikayelerini bize uyarla")
Sırayla, her gün en üstteki kullanılmamış iki tanesini al; kullanınca satırın başına ✅ ve tarih koy.
**Uyarlama kuralı:** rakibin metnini/videosunu kopyalama (zaten sadece başlık/hook'u görüyoruz). Kurulumu (ilk durum +
haksızlık) ve hook yapısını al; Türkiye'ye taşı, karakterleri, ara olayları, ortadaki şoku ve finali kendin yaz.
Kadın anlatıcılı konuları erkek anlatıcıya çevir (ses: Ahmet), gerekirse rolü kardeş/eş olarak değiştir.
1. ✅ (15.11 vasiyet) Emir 1,9 M — "Babamın vasiyetinde bana maddi değeri olan hiçbir şey bırakılmadığı okunduğunda herkes güldü…"
   (lokanta bölümünde marka mirası kullanıldı; farklı bir miras nesnesiyle yaz: ör. eski bir arsa senedi değil, bir defter/bir anahtar)
2. ✅ (16.11 a) Emir 726 B — "Kocam annesine Korece olarak en iyi arkadaşımı hamile bıraktığını söylemişti…" → erkek: "Karım annesiyle
   Kürtçe/Almanca konuşurken…" (anlatıcı dili bildiğini saklamış)
3. ✅ (16.11 b) Emir 725 B — "Akşam yemeğinde yeğenim 7 yaşındaki oğluma 'Sadece büyükannenin gerçek torunları önce yer' dedi"
4. ✅ (18.11) Emir 524 B — "Annemin düğünündeydim. Orada olduğumdan haberi bile yoktu…" → erkek: "Babamın düğünündeydim…"
5. Sultan 148 B — "Ağabeyim bana ailenin en sıkıcı insanı derdi, çünkü şakalarına hep ağlardım…"
6. ✅ (18.11) Emir 424 B — "Karımın günlüğünü yanlışlıkla okudum ve benimle evlenmenin hayatının en büyük hatası olduğunu yazmıştı…"
7. ✅ (18.11) Emir 419 B — "Nişanlım Instagram'a bir video yükledi ve sesini kapatmayı unuttu…"
8. ✅ (19.11 b) Emir 360 B — "Karım gözlerimin içine bakarak bana şöyle dedi: 'Yemek yapmak, temizlik yapmak…'"
9. Sultan 84 B — "Ailemin bir geleneği var…" (aile sırrı/gelenek)
10. Sultan 77 B — "Evleneceğimi söylediğimde ailem güldü. Düğün günümde annem…"
11. Sultan 66 B — "Kız kardeşim oğluma koymayı seçtiğim ismi yeni doğan bebeğine verdi. Bilmediği şey, o ismin…"
12. Sultan 66 B — "Düğünden dakikalar önce nişanlımdan bir mesaj geldi: 'Bunu yapamam'…"
13. Sultan 64 B — "Bizim ailede kimse teşekkür etmez. Her iyiliği 'Hesap Defteri'ne yazarız…"
14. Sultan 55 B — "Şirketin yıllık yemeğinde şaka niyetine herkese sahte piyango bileti dağıttılar…"
15. ✅ (20.11 b) Emir 201 B — "Ailem neşeli bir aile buluşmasında Disney biletlerini dağıtırken…" → Türkiye: tatil/otel paketi
16. ✅ (19.11 c) Emir 153 B — "Tamamen benim karşıladığım bir tatile yeğenlerimin yanlarında…"
17. ✅ (20.11 a) Emir 146 B — "Korkunç bir trafik kazası geçirdikten sonra karımı aradım ve…"
18. ✅ (19.11 a) Emir 674 B — "Yıldönümü yemeğimizde garson siparişimizi almaya geldiğinde kocam…" (yeni hit, 18.11)
19. ✅ (20.11 c) Emir 194 B — "Erkek arkadaşımın üç erkek ve bir kızdan oluşan bir arkadaş grubu…" → "Kız arkadaşımın en yakın erkek arkadaşı"
20. ✅ (21.11 a) Sultan 38 B (YouTube) — "Okula oğlumu almaya gittiğimde diğerlerine benim onun bakıcısı olduğumu söyledi" → "şoförümüz"
21. ✅ (21.11 b) Sultan 20 B — "Eve sürpriz yapmak için erken döndüm; karımı bir hizmetçi gibi bulaşık yıkarken buldum"
22. ✅ (21.11 c) Sultan 24 B — "Apartmanımızın WhatsApp grubunda bir anda tuhaf bir duyuru çıktı"
**Not (20.11):** Emir'in TikTok konularının hepsi kullanıldı. Yeni konu için Sultan'ın YouTube başlıklarına bak: `yt-dlp --flat-playlist --playlist-end 30 --print "%(view_count)s	%(title)s" "https://www.youtube.com/@sultanreddit/videos" | sort -rn`. Sıradaki adaylar: "Aile yemeğinde babam harçlığımın yetip yetmediğini sordu" (14 B), "Bir müşteri yanlış sos yüzünden işimden atılmamı sağladı" (5,7 B), "Kızlarım babalarından boşanırsam beni görmeyeceklerini söyledi" (8,7 B), "Karımın kızı beni ailenin önünde aşağıladı" (10 B).
**Rakip kurulumları (16 Kasım, TikTok altyazısından OCR; kendi cümlelerimizle özet, birebir kopyalama yok):**
- *Annemin düğünü (Emir 524 B):* Anlatıcıyı bebekken annesi terk etmiş, babası tek başına büyütmüş (saç örmeyi
  videolardan öğrenmiş, çift vardiya çalışmış); sonra üvey anne gerçek anne olmuş. Anlatıcı düğün fotoğrafçısı;
  bir gün çekim için gittiği malikanedeki düğün, hiç tanımadığı öz annesinin düğünü çıkıyor. → Bizde: erkek fotoğrafçı,
  "babamın düğünündeydim", bizi bırakan babanın yeni ailesi.
- *Kocamın günlüğü (Emir 424 B):* On yıllık evlilik, iki çocuk; dolap düzenlerken eşin eski defteri düşüp açılıyor;
  altı yıldır yazdığı satırlarda "seninle evlenmek hayatımın en büyük hatası, sıkıcısın, çocuklar ve boşanmanın
  masrafı yüzünden kalıyorum" yazıyor. Anlatıcı hiçbir şey söylemeden kendi hayatını sessizce yeniden kurmaya başlıyor.
  → Bizde: "Karımın günlüğü", erkek anlatıcı.
- *Nişanlımın Instagram videosu (Emir 419 B):* Anlatıcı aslında zengin bir ailenin varisi, babasının şirketinde
  sıradan biri gibi çalışıyor; nişanlısının sesi açık unuttuğu videoda başka biriyle konuşurken "onunla mı evleneceğim,
  asla, yanımda tuttuğum küçük bir köpek o" dediği duyuluyor. Anlatıcı yüzüğü çıkarıp babasına "görücü usulünü kabul
  ediyorum" yazıyor, düğün organizatörüne "gelini değiştiriyoruz" diyor.
- *Karım gözlerimin içine bakarak… (Emir 379 B):* Çatı ustası koca; karısı eskiden kamyonetin göstergesine "su içmeyi
  unutma" gibi notlar bırakırmış, o hepsini bir kahve kutusunda saklamış; notlar kesilmiş, karısı ona ev arkadaşı gibi
  davranıyor; bir gün "yemek yapmak, temizlik, seninle aynı yatakta yatmak zorunda değilim" diyor. Anlatıcı ona
  "zorunluluksuz" bir evliliğin neye benzediğini gösteriyor.
- *Erkek arkadaşımın arkadaş grubu (Emir 193 B):* Sevgilisi "en yakın kız arkadaşımı üzersen biter" diye uyarıyor;
  o arkadaş grubun dokunulmazı. Tanışma yemeğinde arkadaş beyaz bir elbiseyle masanın ortasında oturuyor. → Bizde:
  "Kız arkadaşımın en yakın erkek arkadaşı".
- *Trafik kazası (Emir 188 B):* Anlatıcıya tır çarpıyor; acilden karısını arıyor; karısı arkada kahkahalar olan bir
  restoranda, "şimdi kalkıp gitmem ayıp olur, birini ara" deyip kapatıyor; anlatıcı kayınbiraderini arayınca
  hepsinin aynı restoranda olduğu çıkıyor.
- *Tatil masrafı (Emir 156 B):* Bütün masrafı anlatıcının karşıladığı tatile yeğenleri bir arkadaşlarını da getirmek
  istiyor, parayı yine onun ödemesini bekliyorlar; "hayır" deyince "o gelmezse biz de gelmeyiz" diyorlar; anlatıcı
  "tamam, evde kalın" diyor; anne kardeşin tarafını tutuyor.
- *İş arkadaşı Madison (Emir 131 B):* Anlatıcı babasının "sahip olduklarını gösterme" öğüdüyle lüks hayatını saklıyor;
  iş arkadaşı aylar sonra annesi ve avukatıyla mahkemeye gelip "kocan beni hamile bıraktı" diye milyonlarca tazminat
  istiyor; anlatıcının kocası beş yıl önce ölmüştür.

Kullanılanlar: ✅ vasiyet (15.11 b), ✅ hediye yok (13.11), ✅ kiracılar (14.11), ✅ babam bunu bilmiyor ama (15.11), ✅ işe yaramazlar (12.11).

### `tiktok.txt` (her hikayeye bir TikTok, hikayenin başı, **~5:00-5:10**)
- `hikaye.txt`'nin ilk paragrafı Emir kalıbında hook olsun: **tek güçlü ilk cümle** + en fazla 2-3 kısa cümle
  (haksızlık/sır + kahramanın hamlesi); sonucu ve finali söyleme. Somut, alıntılı, şaşırtıcı.
- `tiktok.txt` = `hikaye.txt`'nin başı **aynen** (özetleme, kısaltma, ekleme yok). Toplam **~830-850 kelime**
  (duraklamasız +%20 seste dakikada ~165 kelime; kapanışla ~5:00-5:10).
- Olaylar hızlanırken, bir sahnenin ortasında kes (gerekirse cümle ortasında).
- Kapanış cümlesini **yazma**; script otomatik ekler (YouTube yönlendirmesi + paylaş + abone).

### `metadata.md` (her hikaye klasöründe)
- YouTube başlığı = hook'un ilk cümlesi (≤100 karakter, sonu "…", sığarsa `| Reddit Hikayeleri`)
- YouTube açıklaması: ilk satır "TikTok'tan geldiysen 2. bölüm MM:SS'te başlıyor 👇", sonra `bolum2.txt` satırları,
  sonra 3-4 cümle spoiler'sız özet, "Sence…? Yorumlara yaz.", abone cümlesi, `#reddit #reddithikayeleri #redditgunlugu`
- YouTube etiketleri (10-15, virgülle) ve "Kapak: kapak.jpg (özel küçük resim)"
- TikTok açıklaması (Emir formatı): ilk cümlenin ilk ~10 kelimesi BÜYÜK HARFLE + "..." + ` 🛑 Hikâyenin 2. Bölümü
  profilimdeki bağlantıda veya YouTube'da “REDDIT GÜNLÜĞÜ PLUS” kanalını aratarak bulabilirsiniz. 🛑 #redditturkiye`
- TikTok sabitlenmiş yorumu (YouTube başlığı + MM:SS)
- Paylaşım saatleri: **Hikaye A** YouTube 12:00, TikTok 12:30 (+ aynı video 13:30 ve 15:00'te tekrar);
  **Hikaye B** YouTube 19:30, TikTok 20:00 (+ 21:00 ve 22:30'da tekrar). Her ikisinde "yapay zekâ ile oluşturulan içerik" açık.

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

### TikTok arka planı (17 Kasım 2026, kullanıcı: "TikTok arka planını değiştirelim, diğer kanallar gibi")
Rakipler (@emirreddit, @sultan.reddit) makine videolarından **elle yapılan iş yakın çekimlerine** geçti: kaykay/tuval
boyama, pasta süsleme, yemek hazırlama, güzellik/oje. `uret.py` artık `EL_ISI` listesini (51 Mixkit klibi: pasta,
çikolata, boyama, çömlek, oje, hamur/suşi, yemek; ücretsiz lisans) kullanır; klipler `girdi/el_klipler/`, önbellek
`girdi/_tiktok_el_bg*.mp4`. Rakiplerin kendi videolarını/başka içerik üreticilerinin görüntülerini kullanma.

### Rakip incelemesi 2 (20 Kasım 2026, kullanıcı: "Emir, Reddit Kafası, Zengin Reddit, Sultan Reddit'i incele")
Hesaplar ve en çok izlenen TikTok'ları: @sultan.reddit (1,4 M / 1,2 M / 848 B), @zengin.reddit (434 B / 258 B / 182 B),
@emirreddit (2 M vasiyet, 1 M kiracılar, 931 B hediye, 846 B yıldönümü), Reddit Kafası = @redditkafa (en çok 64 B, küçük).
YouTube: @sultanreddit, @zenginreddit, @emirreddit (Emir YouTube'a İngilizce başlıkla da yüklüyor).
- **Görünüm:** Sultan ve Zengin'in en çok izlenen TikTok'larında **altyazı yok**; sadece ses + arka plan. Arka planda
  her sahne 30-75 sn sürüyor: yüz bakımı/cilt, pasta ganaj kaplama, berber, saç örme, beton döküm, mobilya boyama,
  koyun kırkma, sörf tahtası boyama, kokteyl. Emir'de kırmızı tek kelime altyazı var (o da 2 M alıyor), biz altyazıyı koruyoruz.
- **Uygulandı:** `uret.py` `SAHNE` listesi (68 Mixkit klibi: berber, oto cila, marangoz, temizlik, spa, dövme, pasta,
  çikolata, boyama, çömlek, oje, suşi) ve `UZUN_KLIP_SN = 20` (her klip bütün olarak, 20 sn'ye kadar). Klipler
  `girdi/sahne_klipler/`, önbellek `girdi/_tiktok_sahne_bg*.mp4`.
- **En çok izlenen hikaye kurulumları (YouTube başlıklarından; gerçekçi olanlar, sırayla kullan):**
  1. ✅ (22.11) Sultan 150 B — "Ağabeyim bana ailenin en sıkıcı insanı derdi, çünkü şakalarına hep ağlardım. Saçıma sakız…"
  2. ✅ (22.11) Sultan 81 B — "Evleneceğimi söylediğimde ailem güldü. Düğün günümde annem…"
  3. ✅ (23.11) Sultan 68 B — "Düğünden dakikalar önce nişanlımdan bir mesaj geldi: 'Bunu yapamam'…"
  4. Sultan 68 B — "Üç yıldır birlikteydim ve ondan aldığım en pahalı hediye üç bin liralık…"
  5. ✅ (23.11) Sultan 67 B — "Kız kardeşim oğluma koymayı seçtiğim ismi yeni doğan bebeğine verdi…"
  6. ✅ (22.11) Sultan 64 B — "Bizim ailede kimse teşekkür etmez. Her iyiliği 'Hesap Defteri'ne yazarız…"
  7. ✅ (23.11) Sultan 56 B — "Şirketin yıllık yemeğinde şaka niyetine herkese sahte piyango bileti dağıttılar…"
  8. ✅ (25.11) Sultan 50 B — "Şoförüm beni her işe götürdüğünde yanında sevgilisini de getiriyordu…"
  9. ✅ (24.11) Zengin 39 B — "Kocamın 'sevgim onu boğuyor' dediğini duydum ve ona bir daha dokunmamaya karar verdim…" → erkek: karım
  10. Zengin 17 B — "İnternetten tanıştığım sevgilim birden bana öğle yemeğinin fotoğrafını attı…"
  11. Zengin 14 B — "Erkek arkadaşım beni çocukluk arkadaşıyla değiştirdi. Şikâyet etmedim…"
  12. ✅ (24.11) Sultan 14 B — "Aile yemeğinde babam harçlığımın yetip yetmediğini sordu. 'Ne harçlığı?'…"
  13. ✅ (24.11) Emir YouTube 42 B — "Görümcem ıstakoz ve pahalı şarap ısmarladı. 'Hesabı ayıralım' dedim…"
  14. ✅ (25.11) Emir YouTube 63 B — "Benzin alırken yerel bir paylaşım viral oldu: 'Birini eve getirmek istiyorum…'"
  15. ✅ (25.11) Sultan YT 30 B (Kasım sonu en yükseği) — "Bir trafik kazasından sonra hastanede yatıyordum. Erkek arkadaşıma küçük…" (başlık kesik)
  16. Sultan YT 18 B — "Kocam benden boşanmak istediğinde ben gizli gizli yılda yirmi milyon lira kazanıyordum…"
  17. Sultan YT 17 B — "Üç yakın arkadaşım bana haber vermeden uçuşlarını değiştirdi. 'Sen grubu geciktiriyorsun'…"
  18. Sultan YT 12 B — "Mezun olduktan sonra yengem hamile kaldı ve ağabeyim, annemle babamı beni evden atmaya…"

### TikTok kapanışı (14 Kasım 2026)
Emir kapanışta izleyiciye "paylaş seçeneğine" bastırıyor (paylaşım TikTok'ta en güçlü sinyal). Bizim kapanış
(`KAPANIS`): YouTube yönlendirmesi + "Önce sağdaki paylaş butonuna bas ve bu hikayeyi bir arkadaşına gönder" +
abone hatırlatması; kapanış boyunca sağda paylaş butonunu gösteren sallanan "PAYLAŞ ➜" oku.

### TikTok → YouTube geçişi (15 Kasım 2026, kullanıcı: "İnsanlar YouTube TikTok'takiyle farklı diyor")
- **YouTube başlığı = TikTok 1'in ilk cümlesi** (aynı kelimelerle, ≤100 karakter, sonu "…"; sığarsa `| Reddit Hikayeleri`).
  İzleyici TikTok'ta duyduğu cümleyi YouTube'da arıyor; farklı başlık "başka video" sanılıyor. `kart.txt` de aynı cümle.
- `uret.py youtube` TikTok'un kesildiği yeri YouTube sesinde bulur, o anda 8 sn "2. BÖLÜM BURADAN BAŞLIYOR"
  rozeti gösterir ve `bolum2.txt`'ye bölüm satırlarını yazar. **YouTube açıklamasının ilk satırı:**
  "TikTok'tan geldiysen 2. bölüm MM:SS'te başlıyor 👇" ve açıklamada `bolum2.txt` satırları (YouTube bölümleri).
- TikTok metni `hikaye.txt`'nin başıyla kelimesi kelimesine aynı olmalı (hook hariç); TikTok'a hikayede olmayan cümle ekleme.
- metadata.md'ye TikTok için **sabitlenmiş yorum** ekle: "2. bölüm YouTube'da: Reddit Günlüğü Plus kanalında '<YouTube başlığı>' videosu, MM:SS'ten itibaren 👆"
- Son mesajda hatırlat: TikTok profil bağlantısı o günün YouTube videosunu göstersin.

## 3. Videoları üret
```bash
cd reddit-gunlugu
K=bolumler/<bugünün klasörü>
python3 uret.py tiktok  --klasor $K
python3 uret.py youtube --klasor $K
python3 uret.py teslim  --klasor $K     # tiktok-gonder.mp4, youtube-gonder.mp4 (<380 MiB)
```
**İki hikaye için de** (a ve b) çalıştır; ikisini tek arka plan komutunda sırayla üret (toplam ~1-1,5 saat).
Uzun süren komutları arka planda çalıştır (YouTube render ~12 dk). Seslendirme kesilirse script kendisi tekrar dener.

## 4. Kontrol et
- `ffprobe` ile süreler (her hikaye): YouTube **≥ 30 dk**, TikTok **4:55-5:15**. Dışındaysa metni uzat/kısalt,
  `$K/_*ses*` dosyalarını sil ve tekrar üret.
- Her videonun başından, ortasından ve sonundan birer kare al ve bak: altyazı okunuyor mu, logo yerinde mi,
  Türkçe harfler (İ, Ş, Ğ) doğru mu, TikTok'un son karesinde kapanış cümlesi var mı.

## 5. Teslim et
1. Her hikaye için ayrı ayrı `SendUserFile`: TikTok (açıklaması dosya notunda), YouTube 720p (başlığı dosya notunda), `kapak.jpg`, `metadata.md`, `hikaye.txt`. Önce Hikaye A, sonra Hikaye B.
   Kullanıcı telefonda 368 MB'lık YouTube dosyasını indiremedi: önce 720p küçük kopyayı gönder
   (`ffmpeg -i youtube.mp4 -vf scale=1280:720 -c:v libx264 -preset veryfast -b:v 420k -maxrate 600k -bufsize 1200k -c:a aac -b:a 96k -movflags +faststart youtube-kucuk.mp4`, ~155 MB),
   sonra ayrıca `youtube-gonder.mp4`'ü
   (`status: "proactive"`, `display: "attach"`). Bir dosya sınırı aşarsa `teslim`'i daha düşük `sinir_mb` ile çalıştır.
2. Google Drive'daki **"Reddit Günlüğü"** klasörüne (id `1sI2YL12nqI-Wj9PToB66bBJUsZYAwqJf`) o günün adıyla
   `metadata.md`'yi metin dosyası olarak yükle. Drive 10 MB üstünü kabul etmez; videoları Drive'a yükleme.
   Drive bağlantısı yoksa veya izin hatası verirse bu adımı atla ve son mesajda söyle.
3. `bolumler/ARSIV.md`'ye yeni satır ekle. İki hikayenin metin dosyalarını (`hikaye.txt`, `tiktok.txt`, `kart.txt`, `bolum2.txt`, `metadata.md`, `kapak.jpg`, `arastirma.md`) ve
   arşivi commit edip `main`'e push et. Video ve ara dosyalar `.gitignore`'da; onları ekleme.

## 6. Son mesaj (kullanıcıya, Türkçe, kısa)
- "Günaydın" ile başla; iki hikayenin adı ve birer cümlelik özeti
- Araştırmadan tek cümle: bu temaları neden seçtin (ör. hangi başlık kaç izlenme almış)
- Video süreleri (her hikaye için TikTok ve YouTube)
- Yükleme hatırlatması: Hikaye A öğlen (YouTube 12:00, TikTok 12:30 + 2 tekrar), Hikaye B akşam (YouTube 19:30,
  TikTok 20:00 + 2 tekrar); TikTok profil bağlantısını o an yayındaki YouTube videosuna çevirmesi; başlık ve açıklamaların metadata.md'de olduğu
- Bir adım başarısız olduysa ne olduğu, dürüstçe
