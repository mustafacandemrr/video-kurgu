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
