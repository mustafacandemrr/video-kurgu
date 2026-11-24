# TikTok rakip analizi (11 Kasım 2026)

Kaynak: yt-dlp ile hesap listeleri; en çok izlenen 3'er videonun ilk 22 ve son 25 saniyesi Whisper ile yazıya
döküldü, kareler incelendi. Videolar sadece analiz için indirildi, kullanılmadı.

## Hesaplar
| Hesap | Video | Ort. izlenme | Medyan | Zirve | TikTok süresi | Sıklık |
|---|---|---|---|---|---|---|
| @sultan.reddit | 104 (26 Eyl–11 Kas) | 366.055 | 249.300 | 2.500.000 | 4–9 dk (medyan 7:16) | günde ~2 |
| @emirreddit | 20 (31 Tem–10 Kas) | 436.430 | 347.000 | 1.700.000 | **hep ~5:00-5:10** | haftada 1-2 |
| Reddit Kafası | bulunamadı (@redditkafasi, @reddit.kafasi, @redditkafa küçük hesaplar) | | | | | |

## En çok izlenenler
- @emirreddit 1,7 M: "BABAMIN VASİYETİNDE BANA MADDİ DEĞERİ OLAN HİÇBİR ŞEY BIRAKILMADIĞI..."
- @emirreddit 925 B: "BABAM, 'BU YIL HEDİYE YOK,' DEDİ, KIZ KARDEŞİM İSE BİR İPHONE, 5.000 DOLARLIK..."
- @emirreddit 797 B: "KARDEŞİM DEDİ Kİ: 'AİLENİN İŞE YARAMAZ İNSANLARINI ATALIM. SEN ÖNCE GİDERSİN'..."
- @emirreddit 724 B: "AKŞAM YEMEĞİNDE YEĞENİM 7 YAŞINDAKİ OĞLUMA BAKIP, 'SADECE BÜYÜKANNENİN GERÇEK TORUNLARI ÖNCE YER'"
- @sultan.reddit 2,5 M / 2,2 M / 2,1 M: "Düğünden dakikalar önce nişanlımdan mesaj geldi…", "Ağabeyim bana ailenin
  en sıkıcı insanı derdi…", "3 yıldır Mert ile beraberdim, en pahalı hediyesi 99 liralık beyaz güller…"

## Kalıplar
1. **Hook (ilk 10-20 sn):** Hikayenin özeti + kahramanın karşı hamlesi, 2-4 cümle. Sonra sahne baştan anlatılır.
2. **Kesim:** Olay hızlanırken, sahne ortasında, bazen cümle ortasında.
3. **Kapanış:** "İkinci bölümü beklemek istemiyorsan, hikayenin tamamını YouTube kanalımda izleyebilirsin…
   profilimdeki YouTube bağlantısına tıkla ya da YouTube'da X kanalını arat."
4. **Açıklama:** İlk cümle BÜYÜK HARFLE + "..." + 🛑 + "Hikâyenin 2. bölümü profilimdeki bağlantıda…" (Emir) /
   "Bu profilin açıklamasında 2. bölüm 🚨YouTube SULTAN REDDIT🚨 #redditturkie #reddithikayeleri" (Sultan).
5. **Görsel:** Çeşitli "satisfying" klip derlemesi (reçine, kesme, slime, boya, araba), ortada tek kelimelik
   kalın kırmızı/beyaz altyazı. Logo yok.
6. **Konu:** Aile içi haksızlık ve ezici karşı hamle (vasiyet, hediye ayrımcılığı, düğün iptali, aldatma,
   "işe yaramaz" sanılan kişinin herkesi finanse etmesi). Hikayeler çoğunlukla çeviri (Nathan, Manhattan,
   dolar); bizimkiler özgün ve Türkiye'de geçiyor.

## 13 Kasım 2026 güncellemesi: @emirreddit ile bizim TikTok'ların ölçümlü karşılaştırması

Kullanıcı "şu an izlenmiyor, Emir Reddit'in hook'larını kullan" dedi. En çok izlenen 6 Emir videosu sadece analiz için
indirildi (kullanılmadı); Whisper modeli bu ortamda indirilemediği için ses ve kare ölçümü yapıldı.

| Ölçü | @emirreddit | Bizim (12-13 Kasım) | Şimdi |
|---|---|---|---|
| Süre | 300-310 sn (hepsi) | 345 sn | ~300 sn |
| 60 sn'de 0,25 sn üstü duraklama | 0 | 15 (ort. 1,2 sn, toplam 18 sn) | 0 |
| Konuşma hızı (hece/sn, kaba ölçüm) | 5,4-5,7 | 3,5 | 4,9 |
| Altyazı | tek kelime, kırmızı, ince siyah kenar, ortada | 2-3 kelime, beyaz+turkuaz, büyük | tek kelime, kırmızı |
| Logo | yok / sağ altta küçük "RB" | ekranın ortasında büyük | sağ altta küçük |
| Arka plan | endüstriyel satisfying (fabrika, ahşap, kar üfleme, araba boyama, pasta) | slime, çömlek, araba yıkama | aynı |
| Açıklama | ilk cümlenin ~10 kelimesi... 🛑 2. Bölüm… aratarak bulabilirsiniz. 🛑 #redditturkiye | 3 hashtag | Emir formatı |
| Yeniden yükleme | aynı videoyu 2-3 kez | yok | öneriliyor |

En büyük fark: edge-tts her cümle sonunda ~1 sn susuyor; videonun ~%30'u sessizlikti. TikTok'ta bu boşluklar kaydırmaya yol açar.
`uret.py` → `sessizlik_kisalt()` sessizliği sesten ölçüp 0,1 sn'ye indiriyor, kelime zamanlarını kaydırıyor.

En çok izlenen Emir açıklamaları (ilk cümle = hook):
1,8 M VASİYETİNDE BANA MADDİ DEĞERİ OLAN HİÇBİR ŞEY… · 926 B "BU YIL HEDİYE YOK" DEDİ, KIZ KARDEŞİM İSE BİR İPHONE… ·
902 B KİRACILARIM KİRAYI DÜŞÜRMEMİ İSTEDİ. BEN DE KİRADAN 400 DOLAR… · 798 B "AİLENİN İŞE YARAMAZ İNSANLARINI ATALIM. SEN ÖNCE GİDERSİN" ·
777 B BABAM BUNU BİLMİYOR AMA BİR ADAMA, ÇOCUĞUNUN KENDİ OĞLU OLMASINI… · 724 B YEĞENİM 7 YAŞINDAKİ OĞLUMA BAKIP "SADECE BÜYÜKANNENİN GERÇEK TORUNLARI ÖNCE YER" ·
722 B KOCAM, ANNESİNE KORECE OLARAK EN İYİ ARKADAŞIMI HAMİLE BIRAKTIĞINI SÖYLEMİŞTİ · 493 B ANNEMİN DÜĞÜNÜNDEYDİM. ORADA OLDUĞUMDAN HABERİ BİLE YOKTU

## 24 Kasım 2026: Paylaşım saati ve yükleme mekanizması

Kaynak: yt-dlp ile hesap listeleri (video indirilmedi). Yükleme zamanı TikTok video kimliğinden (ilk 32 bit = Unix
saniyesi) hesaplandı, Türkiye saati. 30 dakikadan yakın yüklemeler tek "oturum" sayıldı.

| | @sultan.reddit | @emirreddit |
|---|---|---|
| Örneklem | 144 video, 47 oturum (26 Eyl–23 Kas) | 29 video, 18 oturum (31 Tem–16 Kas) |
| Oturum başına video | çoğunlukla 2-5 farklı video, 1-3 dk içinde | son 2 ayda hep **aynı video 3 kez**, 1-3 dk içinde |
| Oturum saatleri | Kasım'da 22 oturumun 17'si 02:00-09:00, en sık 08:00 | dağınık: 10-13, 15-16, 20-23 |
| Aynı oturumda en iyi/en kötü video | medyan 7,4 kat fark | medyan 5,4 kat fark |
| Oturum bloğu → medyan izlenme | 00-05: 224 B · 06-09: 267 B · 10-14: 211 B · 15-19: 354 B (2 oturum) · 20-23: 258 B | 06-09: 729 B (2) · 10-14: 427 B · 15-19: 165 B · 20-23: 503 B |

Çıkarımlar (hipotez, garanti değil):
1. İkisi de kopyaları gün içine yaymıyor; hepsini aynı anda yüklüyor. Aynı videonun üç kopyası bile 5-7 kat farklı
   izleniyor. Her yükleme ayrı bir "deneme" gibi davranıyor, saatten çok bu şans belirleyici görünüyor.
2. Saat etkisi kopyalar arasındaki farktan çok küçük; örneklem az. En tutarlı sinyal: Sultan sabah 06-09'da
   yoğunlaşmış ve en iyi sonuçlarının çoğu bu blokta. 15-19 iki hesapta da zayıf (az örnek).
3. Karar: YouTube 08:00 yayında → üç TikTok 08:15-08:17'de arka arkaya. İki hafta sonra bir hafta akşam
   (20:30) oturumu ile karşılaştır.
