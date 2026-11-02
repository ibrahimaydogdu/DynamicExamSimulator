# İNM 203 Dinamik - Ünite 2, 3, 4 ve 5 Sayısal Soruları Parametreleştirme Önerileri

> [!IMPORTANT]
> Bu belge, İNM 203 Dinamik soru bankasında yer alan **Ünite 2, 3, 4 ve 5 sayısal sorularının (toplam 96 soru)** dinamik sınav sistemi için parametrelendirilmesi amacıyla hazırlanmıştır. Pilot solver (`solvers/u6_s1.py`) kalıbına uygun olarak her sorunun sabitleri, parametre adayları, şekil gereksinimleri ve solver hesaplama iskeleti modellenmiştir.

## Genel İstatistik ve Yönetici Özeti

- **İncelenen Toplam Soru Sayısı:** 96 adet (Ü2: 30, Ü3: 20, Ü4: 20, Ü5: 26)
- **Parametreleştirilebilir Soru Sayısı:** 96 adet (%100)
- **Şekil Durumu 'Yalnız Etiket Değişir' Olan Soru Sayısı:** 27 adet (Şekil üstündeki sayısal etiket boyanıp güncellenir)
- **Şekil Durumu 'Şekil Yok' (Metin Bazlı) Olan Soru Sayısı:** 64 adet (Grafiksiz veya şekil üzerinde sayı bulunmayan sorular)
- **Şekil Durumu 'Şekil Yeniden Çizilmeli / Tutarsız' Olan Soru Sayısı:** 5 adet (Metin ile görsel içeriği uyumsuz veya grafik yeniden üretilmeli)
- **Şekilde Sayısı Olup Kutusu Eksik Olan Soru Sayısı:** 5 adet (`sayilar_duzeltilmis.json` içinde `kutu: null` olanlar)
- **Çözüm Hatası / Metin-Görsel Tutarsızlığı Bildirilen Soru Sayısı:** 13 adet

## Özet Karşılaştırma Tablosu

| Soru No | Parametre Sayısı | Şekil Durumu | Zorluk | Uyarı / Not |
| :--- | :---: | :--- | :---: | :--- |
| S2.1 | 3 | şekil yok | kolay | - |
| S2.2 | 3 | şekil yok | kolay | - |
| S2.3 | 2 | şekil yok | orta | - |
| S2.4 | 2 | şekil yok | orta | - |
| S2.5 | 2 | şekil yok | orta | - |
| S2.6 | 2 | şekil yok | kolay | - |
| S2.7 | 2 | şekil yok | kolay | - |
| S2.8 | 2 | şekil yok | kolay | - |
| S2.9 | 2 | şekil yok | kolay | - |
| S2.10 | 2 | yalnız etiket değişir | orta | - |
| S2.11 | 2 | yalnız etiket değişir | orta | - |
| S2.12 | 2 | yalnız etiket değişir | kolay | - |
| S2.13 | 2 | yalnız etiket değişir | kolay | - |
| S2.14 | 2 | yalnız etiket değişir | kolay | - |
| S2.15 | 2 | şekil yeniden çizilmeli | orta | TUTARSIZLIK: Metinde motosiklet 30° rampa anlatılırken, bağlanan görsel S15_1 çuval kaydırağıdır (S13/S14 ile aynı görsel). |
| S2.16 | 2 | şekil yok | kolay | - |
| S2.17 | 2 | şekil yok | kolay | - |
| S2.18 | 2 | yalnız etiket değişir | orta | - |
| S2.19 | 2 | yalnız etiket değişir | zor | - |
| S2.20 | 2 | şekil yok | kolay | - |
| S2.21 | 2 | şekil yok | orta | - |
| S2.22 | 1 | şekil yok | kolay | - |
| S2.23 | 2 | şekil yok | orta | - |
| S2.24 | 2 | şekil yeniden çizilmeli | kolay | TUTARSIZLIK: Soru metninde A ve B motorlarının kablo çekmesi anlatılırken, bağlanan görsel S24_1 kanalda hareket eden teknelerdir. |
| S2.25 | 3 | şekil yeniden çizilmeli | zor | TUTARSIZLIK: Metinde C ve D motorları blokları çekerken, görsel S25_1 tekneler şemasıdır. |
| S2.26 | 2 | şekil yok | kolay | - |
| S2.27 | 2 | şekil yok | kolay | - |
| S2.28 | 3 | şekil yok | kolay | - |
| S2.29 | 3 | şekil yok | zor | - |
| S2.30 | 3 | şekil yok | orta | - |
| S3.1 | 1 | yalnız etiket değişir | kolay | - |
| S3.2 | 2 | yalnız etiket değişir (KUTU EKSİK: 1) | kolay | - |
| S3.3 | 2 | yalnız etiket değişir | kolay | - |
| S3.4 | 3 | şekil yok | kolay | - |
| S3.5 | 2 | yalnız etiket değişir (KUTU EKSİK: 1.5 kN) | kolay | - |
| S3.6 | 1 | yalnız etiket değişir | kolay | - |
| S3.7 | 2 | yalnız etiket değişir | orta | - |
| S3.8 | 1 | yalnız etiket değişir | kolay | - |
| S3.9 | 2 | yalnız etiket değişir | kolay | NOT: Şekilde θ = 20° viraj eğimi varken, soru metni ve çözümü sadece düz yolda a_n = v²/ρ hesaplamaktadır. |
| S3.10 | 3 | şekil yok | kolay | - |
| S3.11 | 1 | şekil yok | kolay | - |
| S3.12 | 2 | şekil yok | kolay | - |
| S3.13 | 3 | şekil yeniden çizilmeli | kolay | TUTARSIZLIK: Soru basit kamyon fren mesafesi iken, bağlanan görsel S13_1 tekne römorku çeken kamyonettir. |
| S3.14 | 2 | şekil yok | orta | Çözümde makara kuvvet çarpanı (4 kat) basitleştirilerek yorumlanmıştır. |
| S3.15 | 2 | şekil yok | kolay | - |
| S3.16 | 2 | yalnız etiket değişir | kolay | - |
| S3.17 | 3 | yalnız etiket değişir | kolay | Şekildeki 400 mm ve 300 mm koni ölçüleri metinde verilen r=0.120 m ile doğrudan eşleştirilmemiştir. |
| S3.18 | 2 | şekil yok | kolay | - |
| S3.19 | 3 | yalnız etiket değişir | kolay | - |
| S3.20 | 1 | yalnız etiket değişir | kolay | - |
| S4.1 | 2 | yalnız etiket değişir | kolay | - |
| S4.2 | 2 | şekil yok | kolay | - |
| S4.3 | 2 | yalnız etiket değişir | kolay | - |
| S4.4 | 3 | yalnız etiket değişir | kolay | - |
| S4.5 | 2 | yalnız etiket değişir | kolay | - |
| S4.6 | 2 | yalnız etiket değişir (KUTU EKSİK: 46 m) | kolay | - |
| S4.7 | 2 | şekil yok | kolay | - |
| S4.8 | 2 | yalnız etiket değişir (KUTU EKSİK: 7°) | kolay | - |
| S4.9 | 2 | şekil yok | kolay | - |
| S4.10 | 2 | yalnız etiket değişir | kolay | - |
| S4.11 | 3 | şekil yok | kolay | - |
| S4.12 | 2 | şekil yok | kolay | - |
| S4.13 | 2 | yalnız etiket değişir (KUTU EKSİK: 3 m, 2 m) | kolay | - |
| S4.14 | 2 | yalnız etiket değişir | kolay | - |
| S4.15 | 3 | yalnız etiket değişir | kolay | - |
| S4.16 | 2 | şekil yok | kolay | - |
| S4.17 | 2 | şekil yok | kolay | - |
| S4.18 | 2 | yalnız etiket değişir | kolay | TUTARSIZLIK / BİRİM HATASI: Metinde kuvvet '1285 N' yazılmışken sıkışma '2 ft' verilmiştir. Çözüm notunda orijinal sorunun F = 1284 lb olduğu belirtilmiştir. |
| S4.19 | 2 | yalnız etiket değişir | kolay | - |
| S4.20 | 2 | yalnız etiket değişir | kolay | - |
| S5.1 | 2 | yalnız etiket değişir | kolay | - |
| S5.2 | 3 | yalnız etiket değişir | kolay | - |
| S5.3 | 2 | şekil yok | kolay | - |
| S5.4 | 3 | şekil yok | kolay | - |
| S5.5 | 3 | şekil yok | kolay | - |
| S5.6 | 3 | şekil yok | kolay | - |
| S5.7 | 3 | şekil yok | kolay | - |
| S5.8 | 2 | şekil yok | orta | - |
| S5.9 | 2 | şekil yok | orta | - |
| S5.10 | 2 | yalnız etiket değişir | kolay | - |
| S5.11 | 3 | yalnız etiket değişir | orta | - |
| S5.12 | 2 | şekil yok | orta | - |
| S5.13 | 3 | şekil yok | kolay | - |
| S5.14 | 3 | şekil yok | orta | - |
| S5.15 | 2 | şekil yok | kolay | - |
| S5.16 | 3 | yalnız etiket değişir | kolay | Soru sadece impuls-momentum denklemini yazdırmaktadır; sayısal tek bir değer sormamaktadır. |
| S5.17 | 3 | yalnız etiket değişir | kolay | BİRİM TUTARSIZLIĞI: Metinde ve çözümde bloklar '10 kg' ve '50 kg' iken, görsel S17_1 üzerinde etiketler '10 lb' ve '50 lb' yazmaktadır. |
| S5.18 | 3 | yalnız etiket değişir | kolay | - |
| S5.19 | 3 | yalnız etiket değişir | orta | - |
| S5.20 | 3 | şekil yeniden çizilmeli | kolay | TUTARSIZLIK: Metinde kuvvetler '0-2 sn 10 kN, 2-4 sn 20 kN' iken, görsel S20_1 üzerinde kademeler 30, 60, 90 kN ve zaman 2.5 saniyedir. |
| S5.21 | 3 | şekil yok | kolay | - |
| S5.22 | 2 | yalnız etiket değişir | zor | Çözümde A parçasının sola doğru fırladığı metinde söylenmesine rağmen yatay momentum ilk satırda pozitif yazılıp alt satırda -1.061v_A'ya dönüştürülmüştür. |
| S5.23 | 3 | yalnız etiket değişir | orta | - |
| S5.24 | 2 | yalnız etiket değişir | zor | - |
| S5.25 | 3 | yalnız etiket değişir | kolay | BİRİM TUTARSIZLIĞI: Soru metninde ve çözümde eğrilik yarıçapı '10 m' iken, görsel S25_1 üzerinde '10 ft' yazmaktadır. |
| S5.26 | 3 | şekil yok | kolay | - |



---

## Ünite 2: Parçacık Kinematiği (Doğrusal ve Eğrisel Hareket)

### Soru 2.1
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 (t² katsayısı), 2 (t katsayısı), 3 (zaman)
  - *Çözüm:* t=0 alt sınır, 1/3 ve 1/2 integral katsayıları
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Hız fonksiyonu t² katsayısı (Güncel: **3 m/s³**, Aralık: `[1, 6]`, Adım: `1`)
  - `b`: Hız fonksiyonu t katsayısı (Güncel: **2 m/s²**, Aralık: `[1, 5]`, Adım: `1`)
  - `c`: Hesaplama zamanı t (Güncel: **3 s**, Aralık: `[1, 5]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** İntegral katsayıları (1/3, 1/2) analitik integrasyon kurallarından gelir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0 (hareket ileri yönde kalmalı).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İntegral bağıntısını kur: x(t) = ∫ (a*t² + b*t) dt = (a/3)*t³ + (b/2)*t²
  2) Belirli integrali hesapla: x(c) = (a/3)*c³ + (b/2)*c²
  3) Toplam yer değiştirmeyi döndür.
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.2
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 (t² katsayısı), 2 (t katsayısı), 3 (zaman)
  - *Çözüm:* Türev katsayıları 2 ve 1
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Hız fonksiyonu t² katsayısı (Güncel: **3 m/s³**, Aralık: `[1, 6]`, Adım: `1`)
  - `b`: Hız fonksiyonu t katsayısı (Güncel: **2 m/s²**, Aralık: `[1, 5]`, Adım: `1`)
  - `c`: Hesaplama zamanı t (Güncel: **3 s**, Aralık: `[1, 6]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Türev üs kuralları matematiktir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hız fonksiyonunun zamana göre türevini al: a(t) = d/dt (a*t² + b*t) = 2*a*t + b
  2) t = c değerini denklemde yerine koy: a(c) = 2*a*c + b
  3) İvme değerini döndür.
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.3
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 8 (t katsayısı), 1 (t² katsayısı), 5 (zaman)
  - *Çözüm:* v=0 anı t_dur = a/2 = 4 s, t=0 ve t=b anındaki konumlar
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Konum t katsayısı (Güncel: **8 m/s**, Aralık: `[4, 12]`, Adım: `2`)
  - `b`: Hesaplama zamanı t (Güncel: **5 s**, Aralık: `[4, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** t² katsayısı 1 olarak tutularak türev v(t)=a - 2t sade tutulur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** b > a/2 olmalıdır; parçacık yön değiştirdikten sonraki kat edilen mesafeyi test etmek için zaman dönüm noktasından büyük seçilmelidir.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hız fonksiyonunu türet: v(t) = a - 2t
  2) Dönüm noktasını bul: v(t)=0 => t_don = a / 2
  3) Konumları hesapla: x(0) = 0, x(t_don) = a*t_don - t_don², x(b) = a*b - b²
  4) Toplam yol = |x(t_don) - x(0)| + |x(b) - x(t_don)|
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.4
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 (ivme katsayısı), 25 (süre)
  - *Çözüm:* v₀ = 0, v dv = a dt integrali
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İvme fonksiyon katsayısı (Güncel: **0.5 m²/s³**, Aralık: `[0.2, 1.0]`, Adım: `0.1`)
  - `b`: Süre t (Güncel: **25 s**, Aralık: `[9, 36]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** v⁻¹ üssü sabit kalmalı (diferansiyel denklem formu).
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Diferansiyel denklemi düzenle: v dv = a dt
  2) İki tarafın integralini al: v²/2 = a*t
  3) Hızı çöz: v = √(2 * a * b)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.5
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 (hız katsayısı), 25 (süre)
  - *Çözüm:* x₀ = 0, x dx = a dt
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Hız fonksiyon katsayısı (Güncel: **0.5 m²/s**, Aralık: `[0.2, 1.0]`, Adım: `0.1`)
  - `b`: Süre t (Güncel: **25 s**, Aralık: `[9, 36]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** x⁻¹ fonksiyon yapısı korunmalıdır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Diferansiyel denklemi düzenle: x dx = a dt
  2) İntegral al: x²/2 = a*t
  3) Konumu çöz: x = √(2 * a * b)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.6
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 (ivme katsayısı), 4 (ilk hız), 5 (son hız)
  - *Çözüm:* k = 0.5 sabit
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İlk hız v₀ (Güncel: **4 m/s**, Aralık: `[2, 6]`, Adım: `1`)
  - `b`: Son hız v (Güncel: **5 m/s**, Aralık: `[6, 10]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** İvme katsayısı 0.5 sabit tutularak soru hız limitlerine odaklanır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** b > a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İntegral denklemini kur: ∫_{a}^{b} v dv = ∫₀ᵗ 0.5 dt
  2) Sol tarafı çöz: (b² - a²) / 2
  3) Zamanı bul: t = (b² - a²) / (2 * 0.5) = b² - a²
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.7
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 (hız katsayısı), 3 (ilk konum), 5 (son konum)
  - *Çözüm:* k = 0.5 sabit
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İlk konum x₀ (Güncel: **3 m**, Aralık: `[1, 4]`, Adım: `1`)
  - `b`: Son konum x (Güncel: **5 m**, Aralık: `[5, 9]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Hız katsayısı 0.5 korunmalıdır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** b > a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İntegrali kur: ∫_{a}^{b} x dx = ∫₀ᵗ 0.5 dt
  2) Sol tarafı hesapla: (b² - a²) / 2
  3) Zamanı bul: t = (b² - a²)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.8
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 4 (ivme katsayısı), 2 (yer değiştirme)
  - *Çözüm:* v₀ = 0, a dx = v dv ilişkisi
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İvme katsayısı c (a = c*x) (Güncel: **4 s⁻²**, Aralık: `[2, 8]`, Adım: `1`)
  - `b`: Yer değiştirme mesafesi x (Güncel: **2 m**, Aralık: `[1, 5]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** v₀ = 0 başlangıç koşulu.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Zamandan bağımsız formülü kur: ∫₀ᵇ (a*x) dx = ∫₀ᵛ v dv
  2) İntegralleri çöz: (a/2)*b² = v²/2
  3) Hızı hesapla: v = √(a * b²)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.9
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 4 (ivme katsayısı), 36 (hız)
  - *Çözüm:* x₀ = 0, v₀ = 0
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İvme katsayısı c (a = c*x) (Güncel: **4 s⁻²**, Aralık: `[2, 6]`, Adım: `1`)
  - `b`: Ulaşılan hız v (Güncel: **36 m/s**, Aralık: `[10, 50]`, Adım: `2`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Başlangıç durgunluk hali.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Zamandan bağımsız bağıntı: (a/2)*x² = b²/2
  2) Konum karesi: x² = b² / a
  3) Konumu çöz: x = b / √a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.10
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S10_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 8 (x denklemi), 10 (y = x²/10 paydası), 2 (zaman)
  - *Çözüm:* dy/dx = 2x/10 = x/5
  - *Şekil:* 16 m (koordinat), y = x²/10
- **Önerilen Parametreler:**
  - `a`: Yatay hız katsayısı (x = a*t) (Güncel: **8 m/s**, Aralık: `[4, 12]`, Adım: `1`)
  - `b`: Hesaplama zamanı t (Güncel: **2 s**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** y = x²/10 parabolik yörüngesi şekilde çizilidir; payda 10 değişirse eğri geometrisi bozulur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yatay hız: v_x = dx/dt = a
  2) Anlık konum: x = a * b
  3) Düşey hız zincir kuralı: v_y = (dy/dx)*v_x = (2*x/10)*a = 0.2 * x * a
  4) Bileşke hız: v = √(v_x² + v_y²)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.11
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S11_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* Önceki soru verileri (x = 8t, y = x²/10, t = 2 s)
  - *Çözüm:* v_x = 8, v_y = 25.6, tan(θ) = v_y/v_x
  - *Şekil:* 16 m, y = x²/10
- **Önerilen Parametreler:**
  - `a`: Yatay hız katsayısı (x = a*t) (Güncel: **8 m/s**, Aralık: `[4, 12]`, Adım: `1`)
  - `b`: Hesaplama zamanı t (Güncel: **2 s**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Parabol geometrisi korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) v_x = a, x = a*b
  2) v_y = (2*x/10)*v_x
  3) Açı: θ = arctan(v_y / v_x) * (180/π)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.12
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S12_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* Önceki soru verileri
  - *Çözüm:* v_y = (x/5)*8
  - *Şekil:* 16 m, y = x²/10
- **Önerilen Parametreler:**
  - `a`: Yatay hız katsayısı (x = a*t) (Güncel: **8 m/s**, Aralık: `[4, 12]`, Adım: `1`)
  - `b`: Hesaplama zamanı t (Güncel: **2 s**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Parabol geometrisi korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) x = a * b
  2) v_y = 0.2 * x * a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.13
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S13_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 12 m/s (hız), 6 m (yükseklik), g = 9.81 m/s²
  - *Çözüm:* g = 9.81 m/s², v_y0 = 0
  - *Şekil:* 6 m, v_A = 12 m/s
- **Önerilen Parametreler:**
  - `a`: Rampa yüksekliği h (Güncel: **6 m**, Aralık: `[3, 12]`, Adım: `1`)
  - `b`: Yatay fırlatma hızı v₀ (Güncel: **12 m/s**, Aralık: `[8, 20]`, Adım: `2`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 yerçekimi sabiti.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Düşey serbest düşme bağıntısı: h = 0.5 * g * t²
  2) Düşme süresini çöz: t = √(2*a / 9.81)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.14
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S14_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* Önceki soru verileri (h = 6 m, v₀ = 12 m/s)
  - *Çözüm:* t = √(2*h/g), R = v₀ * t
  - *Şekil:* 6 m, v_A = 12 m/s
- **Önerilen Parametreler:**
  - `a`: Rampa yüksekliği h (Güncel: **6 m**, Aralık: `[3, 12]`, Adım: `1`)
  - `b`: Yatay fırlatma hızı v₀ (Güncel: **12 m/s**, Aralık: `[8, 20]`, Adım: `2`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 sabiti.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Uçuş süresini bul: t = √(2*a / 9.81)
  2) Yatay menzil: R = b * t
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.15
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S15_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 m, 30° eğim açısı, 2 s süre, g = 10 m/s²
  - *Çözüm:* g = 10 m/s², sin(30°) = 0.5
  - *Şekil:* Görsel S15_1 çuval rampasıdır (tutarsız)
- **Önerilen Parametreler:**
  - `a`: Fırlatma yüksekliği h (Güncel: **3 m**, Aralık: `[2, 6]`, Adım: `0.5`)
  - `b`: Uçuş süresi t (Güncel: **2 s**, Aralık: `[1.5, 3.5]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° fırlatma açısı ve g=10 soru yapısını korur.
- **Şekil Durumu:** `şekil yeniden çizilmeli`
- **Fiziksel Geçerlilik Kısıtları:** 0.5*g*t² > h (motosiklet yukarı fırlatılıp sonra yere inmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Dikey hareket denklemi: 0 = a + (v_A * sin(30°)) * b - 0.5 * 10 * b²
  2) Hızı çek: v_A = (5 * b² - a) / (b * 0.5)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK: Metinde motosiklet 30° rampa anlatılırken, bağlanan görsel S15_1 çuval kaydırağıdır (S13/S14 ile aynı görsel).

### Soru 2.16
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S16_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* g = 9.81 m/s²
  - *Çözüm:* a = g sin(θ)
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Kayakçı kütlesi m (Güncel: **60 kg**, Aralık: `[50, 90]`, Adım: `5`)
  - `b`: Eğim açısı θ (Güncel: **20 °**, Aralık: `[15, 35]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** θ ∈ (0°, 90°).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Eğim doğrultusundaki ivme: a = 9.81 * sin(radians(b))
  2) İvme kütleden bağımsızdır.
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.17
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S17_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* g = 9.81 m/s²
  - *Çözüm:* a = g (sinθ - μ_k cosθ)
  - *Şekil:* Şekilde sayısal etiket yok
- **Önerilen Parametreler:**
  - `a`: Eğim açısı θ (Güncel: **20 °**, Aralık: `[15, 30]`, Adım: `5`)
  - `b`: Sürtünme katsayısı μ_k (Güncel: **0.1 **, Aralık: `[0.05, 0.25]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** tan(θ) > μ_k (cisim aşağı ivmelenmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Net ivme: a = 9.81 * (sin(radians(a)) - b * cos(radians(a)))
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.18
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S18_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* y = (1/20)x², x = 10 m, 5 m (düşey kot)
  - *Çözüm:* y = (1/20)*10² = 5 m, dy/dx = 2x/20 = 1
  - *Şekil:* y = (1/20)x², 5 m, 10 m
- **Önerilen Parametreler:**
  - `a`: A noktası yatay konumu x (Güncel: **10 m**, Aralık: `[6, 15]`, Adım: `1`)
  - `b`: Parabol katsayısı c (y = (1/c)x²) (Güncel: **20 **, Aralık: `[10, 30]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** y(x) = x²/c bağıntısından ötürü yükseklik h = a²/b olarak türetilir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kot: y = a² / b
  2) Eğim: dy/dx = 2*a / b
  3) Eğim açısı: θ = arctan(dy/dx) * (180/π)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.19
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S19_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* Önceki soru verileri, eğim açısı 45°
  - *Çözüm:* a_n = v²/ρ, a_t = g sin(45°)
  - *Şekil:* y = (1/20)x², 5 m, 10 m
- **Önerilen Parametreler:**
  - `a`: A noktasındaki hız v (Güncel: **10 m/s**, Aralık: `[6, 16]`, Adım: `2`)
  - `b`: Eğrilik yarıçapı ρ (Güncel: **28.28 m**, Aralık: `[15, 40]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° eğim açısı türevden (dy/dx = 1) gelir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Normal ivme: a_n = a² / b
  2) Teğetsel ivme: a_t = 9.81 * sin(radians(45))
  3) İvme bileşkesi ve x ekseni ile açısı hesaplanır.
- **Zorluk Seviyesi:** Zor
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.20
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S20_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 10 m (yarıçap), 0.1 rad (katsayı), 1 s (zaman)
  - *Çözüm:* ṙ = 0, v_r = 0, v_θ = r*ω
  - *Şekil:* Şekilde sadece semboller var (r, θ_B)
- **Önerilen Parametreler:**
  - `a`: Dönme dolap yarıçapı r (Güncel: **10 m**, Aralık: `[5, 20]`, Adım: `1`)
  - `b`: Açısal hız ω (θ = ω*t) (Güncel: **0.1 rad/s**, Aralık: `[0.05, 0.3]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Dairesel yörüngede r sabittir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Radyal hız: v_r = 0
  2) Enine hız: v_θ = a * b
  3) Bileşke hız: v = v_θ = a * b
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.21
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S21_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 100 (r katsayısı), 1 (t³ katsayısı), 1 s (zaman)
  - *Çözüm:* r = a*t², ṙ = 2*a*t, θ = t³, θ̇ = 3*t²
  - *Şekil:* Şekilde sadece mekanizma şeması var
- **Önerilen Parametreler:**
  - `a`: Radyal konum katsayısı c (r = c*t²) (Güncel: **100 mm/s²**, Aralık: `[50, 200]`, Adım: `25`)
  - `b`: Hesaplama anı t (Güncel: **1 s**, Aralık: `[0.5, 2.0]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Açısal bağıntı θ = t³ sabit tutulur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) r(b) = a * b²
  2) v_r = 2 * a * b
  3) θ̇ = 3 * b²
  4) v_θ = r * θ̇ = (a * b²) * (3 * b²)
  5) v = √(v_r² + v_θ²)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.22
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S22_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 10 m/s
  - *Çözüm:* L = 3*s_A + s_M => 3*v_A + v_M = 0
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Motor çekme hızı v_M (Güncel: **10 m/s**, Aralık: `[3, 15]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Makara donatım oranı 3:1 sabittir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kinematik bağıntı: 3 * v_A + a = 0
  2) Silindir hızı: v_A = a / 3 (yukarı)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.23
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S23_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.2 (ivme katsayısı), 4 m (yükseklik)
  - *Çözüm:* 4 v_yük = 3 v_motor => a_yük = 0.75 a_motor
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Motor ivme katsayısı (a = c*t) (Güncel: **0.2 m/s³**, Aralık: `[0.1, 0.5]`, Adım: `0.05`)
  - `b`: Hedef yükselme h (Güncel: **4 m**, Aralık: `[2, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Makaralar arası 3/4 oran geometriden gelir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yük ivmesi: a_yük = 0.75 * a * t
  2) Entegrasyon ile hız: v = 0.75 * a * t² / 2
  3) Entegrasyon ile konum: h(t) = 0.75 * a * t³ / 6
  4) Zaman: t = (6 * b / (0.75 * a))^(1/3)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.24
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S24_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2 ft/s, 4 ft/s
  - *Çözüm:* v_sol = v_A/2, v_sağ = v_B/2, v_merkez = (v_sol + v_sağ)/2
  - *Şekil:* Görselde tekneler var (tutarsız)
- **Önerilen Parametreler:**
  - `a`: A motoru çekme hızı v_A (Güncel: **2 ft/s**, Aralık: `[1, 6]`, Adım: `1`)
  - `b`: B motoru çekme hızı v_B (Güncel: **4 ft/s**, Aralık: `[2, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 2:1 makara donanımları.
- **Şekil Durumu:** `şekil yeniden çizilmeli`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Sol uç hızı: v_sol = a / 2
  2) Sağ uç hızı: v_sag = b / 2
  3) Merkez hızı: v_merkez = (v_sol + v_sag) / 2 = (a + b) / 4
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK: Soru metninde A ve B motorlarının kablo çekmesi anlatılırken, bağlanan görsel S24_1 kanalda hareket eden teknelerdir.

### Soru 2.25
- **Görsel:** `media/Dinamik 2. Ünite Sayısal Sorular/S25_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 (ivme t² katsayısı), 5 m/s², 3 m (aralık)
  - *Çözüm:* a_A = a_C/2 = 1.5t², a_B = -5
  - *Şekil:* Görsel teknelerdir (tutarsız)
- **Önerilen Parametreler:**
  - `a`: C motor ivme katsayısı c (a_C = c*t²) (Güncel: **3 m/s⁴**, Aralık: `[1, 5]`, Adım: `1`)
  - `b`: D motor sabit ivmesi a_D (Güncel: **5 m/s²**, Aralık: `[2, 8]`, Adım: `1`)
  - `c`: Başlangıç aralık mesafesi d (Güncel: **3 m**, Aralık: `[2, 6]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Makaradan gelen 1/2 çarpanı.
- **Şekil Durumu:** `şekil yeniden çizilmeli`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Blok A konumu: x_A(t) = (a / 24) * t⁴
  2) Blok B konumu: x_B(t) = c - 0.5 * b * t²
  3) Kesişim denklemi: (a/24)*t⁴ + 0.5*b*t² - c = 0
  4) u = t² karesel denklemini çöz, pozitif kökten t = √u bul.
- **Zorluk Seviyesi:** Zor
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK: Metinde C ve D motorları blokları çekerken, görsel S25_1 tekneler şemasıdır.

### Soru 2.26
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 4 m/s (batı), 3 m/s (doğu)
  - *Çözüm:* v_bağıl = (+b) - (-a)
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Batıya giden araba hızı v_1 (Güncel: **4 m/s**, Aralık: `[2, 10]`, Adım: `1`)
  - `b`: Doğuya giden araba hızı v_2 (Güncel: **3 m/s**, Aralık: `[2, 10]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Doğu (+) ve Batı (-) koordinat eksen tanımı.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Referans yönü belirle: Doğu (+)
  2) Gözlemci hızı: v_gozlemci = -a
  3) Gözlenen araç hızı: v_gozlenen = +b
  4) Bağıl hız: v_bagil = v_gozlenen - v_gozlemci = b - (-a) = a + b (Doğuya doğru)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.27
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 400 km/h, 300 km/h
  - *Çözüm:* v_A = -400i, v_B = 300j
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: A uçağı hızı (Batı) (Güncel: **400 km/h**, Aralık: `[200, 600]`, Adım: `50`)
  - `b`: B uçağı hızı (Kuzey) (Güncel: **300 km/h**, Aralık: `[150, 500]`, Adım: `50`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Kuzey-Batı dik koordinat ekseni.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Vektörel hızlar: v_A = -a * i, v_B = b * j
  2) Bağıl hız: v_{A/B} = v_A - v_B = -a * i - b * j
  3) Büyüklük: |v_{A/B}| = √(a² + b²)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.28
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* Zaman aralıkları 0, 20, 40, 60 s; hızlar 0, 16, 21, 24
  - *Çözüm:* Yamuk alanı = (v1 + v2)/2 * Δt
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: t=20 anındaki hız (Güncel: **16 m/s**, Aralık: `[10, 25]`, Adım: `1`)
  - `b`: t=40 anındaki hız (Güncel: **21 m/s**, Aralık: `[18, 30]`, Adım: `1`)
  - `c`: t=60 anındaki hız (Güncel: **24 m/s**, Aralık: `[22, 35]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 20 saniyelik eşit zaman aralıkları.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** c > b > a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) 0-20 s alanı: A1 = 0.5 * (0 + a) * 20 = 10 * a
  2) 20-40 s alanı: A2 = 0.5 * (a + b) * 20 = 10 * (a + b)
  3) 40-60 s alanı: A3 = 0.5 * (b + c) * 20 = 10 * (b + c)
  4) Toplam yol: x = A1 + A2 + A3
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.29
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* y² = 4x, v = 4 m/s, x = 4 m
  - *Çözüm:* a_t = 0 (hız sabit), a = a_n = v²/ρ
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Parabol katsayısı c (y² = c*x) (Güncel: **4 m**, Aralık: `[2, 8]`, Adım: `1`)
  - `b`: Sabit hız v (Güncel: **4 m/s**, Aralık: `[2, 10]`, Adım: `1`)
  - `c`: Konum x (Güncel: **4 m**, Aralık: `[1, 9]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Teğetsel ivmenin sıfır oluşu (hızın sabitliği).
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) y = √(a * c)
  2) dy/dx = a / (2*y)
  3) d²y/dx² = -a² / (4*y³)
  4) ρ = [1 + (dy/dx)²]^(1.5) / |d²y/dx²|
  5) İvme: a_n = b² / ρ
- **Zorluk Seviyesi:** Zor
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 2.30
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 12 (t katsayısı), 3 (t^0.5 katsayısı), s=15, t=4
  - *Çözüm:* v(0)=0 => C1=0, s(0)=b => C2=b
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İvme t katsayısı (Güncel: **12 ft/s³**, Aralık: `[6, 18]`, Adım: `2`)
  - `b`: İlk konum s₀ (Güncel: **15 ft**, Aralık: `[5, 25]`, Adım: `5`)
  - `c`: Hesaplama zamanı t (Güncel: **4 s**, Aralık: `[1, 9]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** t^(1/2) terimi integrallerde rasyonel kök kalması için 3 katsayısı korunmalıdır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0 (kareköklü ifade pozitif t gerektirir).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hız: v(t) = ∫ (a*t - 3*t^(0.5)) dt = (a/2)*t² - 2*t^(1.5)
  2) Konum: s(t) = ∫ v(t) dt = (a/6)*t³ - (4/5)*t^(2.5) + b
  3) s(c) değerini hesapla.
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok


---

## Ünite 3: Parçacık Kinetiği (Kuvvet ve İvme - Newton'un 2. Yasası)

### Soru 3.1
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S1_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 500 kg, 30° açı, g = 9.81 m/s²
  - *Çözüm:* 2 T cos(30°) = mg => T = mg / (2 cos 30°)
  - *Şekil:* 30°, 30° (açılar)
- **Önerilen Parametreler:**
  - `a`: Yük kütlesi m (Güncel: **500 kg**, Aralık: `[200, 1000]`, Adım: `50`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Halatların 30° simetrik açısı korunmalıdır; açı değişirse sapan geometrisi yanıltıcı olur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Düşey kuvvet dengesi: 2 * T * cos(radians(30)) = a * 9.81
  2) Halat gerilmesi: T = (a * 9.81) / (2 * cos(radians(30)))
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.2
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S2_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 kg, 3000 N, 1:10 eğim, g = 9.81 m/s²
  - *Çözüm:* sinθ ≈ 1/10 = 0.1, a = (F - mg sinθ)/m
  - *Şekil:* 10 (kutu var), 1 (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Kamyon kütlesi m (Güncel: **2000 kg**, Aralık: `[1500, 4000]`, Adım: `250`)
  - `b`: Çekiş kuvveti F (Güncel: **3000 N**, Aralık: `[2000, 6000]`, Adım: `500`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 1:10 üçgen eğim oranı sabit kalmalıdır; üçgen geometrisi çizimde sabittir.
- **Şekil Durumu:** `yalnız etiket değişir (KUTU EKSİK: 1)`
- **Fiziksel Geçerlilik Kısıtları:** b > a * 9.81 * 0.1 (çekiş kuvveti eğim aşağı ağırlık bileşenini yenmelidir).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Eğim açısı bileşeni: sin(θ) = 1 / 10 = 0.1
  2) Eğim aşağı ağırlık: W_paralel = a * 9.81 * 0.1
  3) Net ivme: a_ivme = (b - W_paralel) / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.3
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S3_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 50 kg, 400 N, 30° eğim açısı, g = 9.81 m/s²
  - *Çözüm:* ΣF_x = P - mg sin(30°) = m*a
  - *Şekil:* 30°
- **Önerilen Parametreler:**
  - `a`: Kutu kütlesi m (Güncel: **50 kg**, Aralık: `[20, 80]`, Adım: `5`)
  - `b`: Çekme kuvveti P (Güncel: **400 N**, Aralık: `[250, 600]`, Adım: `25`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° eğik düzlem açısı sabit tutulur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** b > a * 9.81 * sin(30°) (kutu yukarı ivmelenmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Ağırlık eğim bileşeni: F_g = a * 9.81 * sin(radians(30))
  2) Net kuvvet: F_net = b - F_g
  3) İvme: a_ivme = F_net / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.4
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S4_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 10 kg, 50 N, μ_k = 0.2, g = 9.81 m/s²
  - *Çözüm:* N = mg, F_s = μ_k N, a = (P - F_s)/m
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Blok kütlesi m (Güncel: **10 kg**, Aralık: `[5, 25]`, Adım: `1`)
  - `b`: Yatay çekme kuvveti P (Güncel: **50 N**, Aralık: `[30, 100]`, Adım: `5`)
  - `c`: Kinetik sürtünme katsayısı μ_k (Güncel: **0.2 **, Aralık: `[0.1, 0.4]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** b > c * a * 9.81 (uygulanan kuvvet sürtünmeyi yenmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Normal kuvvet: N = a * 9.81
  2) Sürtünme kuvveti: F_s = c * N
  3) İvme: a_ivme = (b - F_s) / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.5
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S5_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 barç, 2 kN direnç, 4 m/s hız, 1.5 kN römorkör direnci
  - *Çözüm:* Toplam direnç = 3 * 2 + 1.5 = 7.5 kN, Güç = F * v
  - *Şekil:* 4 m/s (kutu var), 2 kN (3 adet kutu var), 1.5 kN (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Her barcın su direnci F_direnc (Güncel: **2 kN**, Aralık: `[1, 5]`, Adım: `0.5`)
  - `b`: Çekme hızı v (Güncel: **4 m/s**, Aralık: `[2, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 3 adet barç geometrisi sabittir.
- **Şekil Durumu:** `yalnız etiket değişir (KUTU EKSİK: 1.5 kN)`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Toplam direnç kuvveti: F_top = 3 * a + 1.5 (kN)
  2) Gerekli güç: P = F_top * b (kW)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.6
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S6_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 100 kg, 60° halat açıları, g = 9.81 m/s²
  - *Çözüm:* 2 T cos(60°) = mg => T = mg / (2 cos 60°)
  - *Şekil:* 60°, 60° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Sandık kütlesi m (Güncel: **100 kg**, Aralık: `[50, 200]`, Adım: `10`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 60° açı simetrisi çizimde sabittir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Düşey denge: 2 * T * cos(radians(60)) = a * 9.81
  2) cos(60°) = 0.5 olduğundan: T = a * 9.81 (N)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.7
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S7_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2 kg, 6 m/s, 30° açı, ρ = 4 m, g = 9.81 m/s²
  - *Çözüm:* N - mg cos(30°) = m (v²/ρ)
  - *Şekil:* 30° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Parçacık kütlesi m (Güncel: **2 kg**, Aralık: `[1, 5]`, Adım: `0.5`)
  - `b`: Anlık hız v (Güncel: **6 m/s**, Aralık: `[3, 10]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° eğim açısı ve 4 m eğrilik yarıçapı korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Normal ivme: a_n = b² / 4
  2) Ağırlık normal bileşeni: W_n = a * 9.81 * cos(radians(30))
  3) Ray tepki kuvveti: N = W_n + a * a_n
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.8
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S8_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 5 kg, 30° eğim, g = 9.81 m/s²
  - *Çözüm:* a_t = -g sin(30°) = -4.905 m/s²
  - *Şekil:* 30° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Kütle m (Güncel: **5 kg**, Aralık: `[2, 10]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° açı sabittir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Teğetsel kuvvet: ΣF_t = -m * g * sin(30°)
  2) Teğetsel ivme: a_t = -9.81 * sin(radians(30)) = -4.905 m/s² (kütleden bağımsızdır)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.9
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S9_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 100 m (yarıçap), 20 m/s (hız)
  - *Çözüm:* a_n = v²/ρ
  - *Şekil:* θ = 20° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Pist yarıçapı ρ (Güncel: **100 m**, Aralık: `[50, 200]`, Adım: `25`)
  - `b`: Araç hızı v (Güncel: **20 m/s**, Aralık: `[10, 35]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Şekildeki viraj eğim açısı 20° bu soruda kullanılmamaktadır (salt kinematik merkezcil ivme sorulmaktadır).
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Merkezcil ivme: a_n = b² / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ NOT: Şekilde θ = 20° viraj eğimi varken, soru metni ve çözümü sadece düz yolda a_n = v²/ρ hesaplamaktadır.

### Soru 3.10
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S10_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 4 m (boy), 30 kg (kütle), 4 m/s (hız), g = 9.81 m/s²
  - *Çözüm:* T - mg = m(v²/r) => T = mg + m(v²/r)
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: İp boyu L (Güncel: **4 m**, Aralık: `[2, 6]`, Adım: `0.5`)
  - `b`: Top kütlesi m (Güncel: **30 kg**, Aralık: `[10, 50]`, Adım: `5`)
  - `c`: En alt noktadaki hız v (Güncel: **4 m/s**, Aralık: `[2, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Ağırlık: W = b * 9.81
  2) Merkezcil kuvvet: F_n = b * (c² / a)
  3) İp gerilmesi: T = W + F_n
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.11
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S11_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* m kütlesi, r yarıçapı, g = 9.81 m/s²
  - *Çözüm:* N = 0 sınır koşulu, v_max = √(gr)
  - *Şekil:* Şekilde sadece semboller var
- **Önerilen Parametreler:**
  - `a`: Tepe yarıçapı r (Güncel: **50 m**, Aralık: `[20, 100]`, Adım: `10`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** N = 0 fiziksel temas kesilme koşulu.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Temas kesilme koşulu: N = 0
  2) mg = m * v_max² / a
  3) Maksimum hız: v_max = √(9.81 * a)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.12
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S12_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 kg, 0.6 m, 2 rad/s
  - *Çözüm:* a_r = r̈ - r θ̇² = 0 - r θ̇²
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Bilezik konumu r (Güncel: **0.6 m**, Aralık: `[0.3, 1.2]`, Adım: `0.1`)
  - `b`: Açısal hız θ̇ (Güncel: **2 rad/s**, Aralık: `[1, 5]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** ṙ = 0 ve r̈ = 0 (bilezik konumu sabit).
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Radyal ivme formülü: a_r = -a * b²
  2) Büyüklük: |a_r| = a * b² (merkeze doğru)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.13
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S13_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 kg, 15 m/s, 10 m
  - *Çözüm:* v² = v₀² + 2as => a = -v₀²/(2s)
  - *Şekil:* Görselde tekne çeken kamyonet var (tutarsız)
- **Önerilen Parametreler:**
  - `a`: Kamyon kütlesi m (Güncel: **2000 kg**, Aralık: `[1500, 3500]`, Adım: `250`)
  - `b`: Fren öncesi ilk hız v₀ (Güncel: **15 m/s**, Aralık: `[10, 25]`, Adım: `2.5`)
  - `c`: Durma mesafesi s (Güncel: **10 m**, Aralık: `[8, 20]`, Adım: `2`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Son hız v = 0.
- **Şekil Durumu:** `şekil yeniden çizilmeli`
- **Fiziksel Geçerlilik Kısıtları:** b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kinematik bağıntı: 0 = b² + 2 * a * c
  2) Yavaşlama ivmesi büyüklüğü: |a| = b² / (2 * c)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK: Soru basit kamyon fren mesafesi iken, bağlanan görsel S13_1 tekne römorku çeken kamyonettir.

### Soru 3.14
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S14_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 30 lb, 15 lb
  - *Çözüm:* Kuvvet çarpanı = 4 (F_yukarı = 4*F = 60 lb), Net = 60 - 30 = 30 lb
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: A bloğu ağırlığı W (Güncel: **30 lb**, Aralık: `[20, 50]`, Adım: `5`)
  - `b`: Uygulanan çekme kuvveti F (Güncel: **15 lb**, Aralık: `[10, 25]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Makara donanımının 4 kat kuvvet kazancı oranı sabittir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** 4 * b > a (yük yukarı ivmelenmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Makara sisteminden yukarı çekiş kuvveti: F_yukari = 4 * b
  2) Net kuvvet: F_net = F_yukari - a = 4 * b - a
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ Çözümde makara kuvvet çarpanı (4 kat) basitleştirilerek yorumlanmıştır.

### Soru 3.15
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S15_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* m kütlesi, θ açısı, g = 9.81 m/s²
  - *Çözüm:* N_B = mg cos(θ)
  - *Şekil:* Şekilde sadece semboller var
- **Önerilen Parametreler:**
  - `a`: B bloğu kütlesi m (Güncel: **5 kg**, Aralık: `[2, 10]`, Adım: `1`)
  - `b`: Kama eğim açısı θ (Güncel: **30 °**, Aralık: `[20, 45]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Dikeye dik doğrultuda ivme olmaması koşulu.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b ∈ (0°, 90°).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yüzeye dik kuvvet dengesi: N_B = a * 9.81 * cos(radians(b))
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.16
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S16_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 500 kg, 6000 N (6 kN), g = 9.81 m/s²
  - *Çözüm:* ΣF_y = F - mg = 6000 - 500*9.81 = 1095 N, a = 1095/500
  - *Şekil:* F = 6 kN (kutu var), F_D = (100v) N (kutu var)
- **Önerilen Parametreler:**
  - `a`: Balon kütlesi m (Güncel: **500 kg**, Aralık: `[300, 800]`, Adım: `50`)
  - `b`: Kaldırma kuvveti F (Güncel: **6 kN**, Aralık: `[5, 10]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Başlangıç ivmesi sorulduğu için v=0 anında F_D direnci 0 alınır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** b * 1000 > a * 9.81 (balon yukarı yükselmeli).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kaldırma kuvveti (N): F_k = b * 1000
  2) Ağırlık (N): W = a * 9.81
  3) Net düşey kuvvet: F_net = F_k - W
  4) Başlangıç ivmesi: a_ivme = F_net / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.17
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S17_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.2 kg, 0.120 m, 0.5 m/s
  - *Çözüm:* F_n = m (v²/r)
  - *Şekil:* 400 mm (kutu var), 300 mm (kutu var), 200 mm (kutu var)
- **Önerilen Parametreler:**
  - `a`: Blok kütlesi m (Güncel: **0.2 kg**, Aralık: `[0.1, 0.5]`, Adım: `0.05`)
  - `b`: Dönme yarıçapı r (Güncel: **0.12 m**, Aralık: `[0.08, 0.25]`, Adım: `0.02`)
  - `c`: Çizgisel hız v (Güncel: **0.5 m/s**, Aralık: `[0.3, 1.2]`, Adım: `0.1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Koni boyutları soru metninde doğrudan r=0.120 m verildiği için hesapta kullanılmamaktadır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Merkezcil ivme: a_n = c² / b
  2) Net merkezcil kuvvet: F_n = a * a_n
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ Şekildeki 400 mm ve 300 mm koni ölçüleri metinde verilen r=0.120 m ile doğrudan eşleştirilmemiştir.

### Soru 3.18
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S18_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 5000 kg, 3000 m, 97 m/s
  - *Çözüm:* a_n = v²/r
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Dairesel yörünge yarıçapı r (Güncel: **3000 m**, Aralık: `[1500, 5000]`, Adım: `500`)
  - `b`: Uçak hızı v (Güncel: **97 m/s**, Aralık: `[60, 150]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Uçak kütlesi merkezcil ivme hesabında sadeleşir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Merkezcil ivme: a_n = b² / a
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.19
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S19_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 80 kg, 20° açı, μ_k = 0.3, N = 664 N
  - *Çözüm:* F_s = μ_k * N = 0.3 * 664 = 199.2 N
  - *Şekil:* 20° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Sandık kütlesi m (Güncel: **80 kg**, Aralık: `[40, 120]`, Adım: `10`)
  - `b`: Kinetik sürtünme katsayısı μ_k (Güncel: **0.3 **, Aralık: `[0.15, 0.45]`, Adım: `0.05`)
  - `c`: Ölçülen normal kuvvet N (Güncel: **664 N**, Aralık: `[400, 900]`, Adım: `20`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 20° çekme açısı şekilde çizilidir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** b ∈ (0, 1), c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Sürtünme kuvveti: F_s = b * c
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 3.20
- **Görsel:** `media/Dinamik 3. Ünite Sayısal Sorular/S20_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* A = 25 kg, C = 10 kg, g = 9.81 m/s²
  - *Çözüm:* N_C = m_C * g = 10 * 9.81 = 98.1 N
  - *Şekil:* 25 kg, 10 kg, 5 kg, 30°, (μ_k)_C = 0.2
- **Önerilen Parametreler:**
  - `a`: C bloğu kütlesi m_C (Güncel: **10 kg**, Aralık: `[5, 25]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° eğik düzlem açısı ve diğer blok kütleleri korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Düşey statik denge: ΣF_y = 0
  2) Normal kuvvet: N_C = a * 9.81
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok


---

## Ünite 4: Parçacık Kinetiği (İş ve Enerji Yöntemi)

### Soru 4.1
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S1_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 1500 lb (ağırlık), 15° açı, 744 lb, 25 ft
  - *Çözüm:* U = F * s * cos(15°)
  - *Şekil:* 15° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Kablo çekme kuvveti F (Güncel: **744 lb**, Aralık: `[400, 1000]`, Adım: `50`)
  - `b`: Çekilme mesafesi s (Güncel: **25 ft**, Aralık: `[10, 50]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 15° çekme açısı şekilde sabit kalmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, a * sin(15°) < 1500 (sandık yerden kalkmamalı).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yatay kuvvet bileşeni: F_x = a * cos(radians(15))
  2) Yapılan iş: U = F_x * b
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.2
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S2_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 1.5 kg, Fs = 900s², s = 0.2 m
  - *Çözüm:* U = -∫ 900s² ds = -[300 s³]
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Yay direnç katsayısı c (F = c*s²) (Güncel: **900 N/m²**, Aralık: `[400, 1500]`, Adım: `100`)
  - `b`: Sıkışma mesafesi s (Güncel: **0.2 m**, Aralık: `[0.1, 0.4]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Kuvvetin s² fonksiyonel formu.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Entegrasyon katsayısı: a / 3
  2) Yapılan iş (negatif): U = -(a / 3) * b³
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.3
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S3_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 kg, 100 km/h, μ_k = 0.25, g = 9.81 m/s²
  - *Çözüm:* N = mg, F_s = μ_k mg, U = -F_s * s'
  - *Şekil:* 100 km/h (kutu var)
- **Önerilen Parametreler:**
  - `a`: Araba kütlesi m (Güncel: **2000 kg**, Aralık: `[1200, 3000]`, Adım: `200`)
  - `b`: Kinetik sürtünme katsayısı μ_k (Güncel: **0.25 **, Aralık: `[0.15, 0.45]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 100 km/h ilk hız çizimde etiketlidir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b ∈ (0, 1).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Normal kuvvet: N = a * 9.81
  2) Sürtünme kuvveti: F_s = b * N
  3) İş ifadesi: U = -F_s * s' (J)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.4
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S4_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 N/m, 0.05 m, 0.0375 m
  - *Çözüm:* Ve = 0.5 * k * s², ΔVe = Ve₂ - Ve₁
  - *Şekil:* 50 mm (kutu var), 150 mm (kutu var), k = 2 kN/m (kutu var)
- **Önerilen Parametreler:**
  - `a`: Yay sabiti k (Güncel: **2000 N/m**, Aralık: `[1000, 4000]`, Adım: `500`)
  - `b`: İlk sıkışma s₁ (Güncel: **0.05 m**, Aralık: `[0.03, 0.08]`, Adım: `0.01`)
  - `c`: Son sıkışma s₂ (Güncel: **0.0375 m**, Aralık: `[0.01, 0.035]`, Adım: `0.005`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Yay potansiyel enerjisi karesel formülü.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İlk potansiyel enerji: Ve1 = 0.5 * a * b²
  2) Son potansiyel enerji: Ve2 = 0.5 * a * c²
  3) Değişim: ΔVe = Ve2 - Ve1
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.5
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S5_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 kg, 100 km/h (27.78 m/s)
  - *Çözüm:* T = 0.5 * m * v²
  - *Şekil:* 100 km/h (kutu var)
- **Önerilen Parametreler:**
  - `a`: Araba kütlesi m (Güncel: **2000 kg**, Aralık: `[1200, 3000]`, Adım: `200`)
  - `b`: Hız v (Güncel: **100 km/h**, Aralık: `[60, 140]`, Adım: `10`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 100 km/h etiketli hız.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hızı m/s birimine dönüştür: v_ms = b / 3.6
  2) Kinetik enerji: T = 0.5 * a * v_ms² (J)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.6
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S6_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 70 kg, 46 m, g = 9.81 m/s²
  - *Çözüm:* v = √(2gh)
  - *Şekil:* 4 m (kutu var), 30° (kutu var), 46 m (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Kayakçı kütlesi m (Güncel: **70 kg**, Aralık: `[50, 100]`, Adım: `5`)
  - `b`: Yükseklik farkı h (Güncel: **46 m**, Aralık: `[25, 65]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° rampa açısı korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir (KUTU EKSİK: 46 m)`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Enerji korunumu: mgh = 0.5 * m * v²
  2) Hız: v = √(2 * 9.81 * b)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.7
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 300 lb, 5 ft/s, 1 hp = 550 ft·lb/s
  - *Çözüm:* P = W * v, P_hp = P / 550
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Yük ağırlığı W (Güncel: **300 lb**, Aralık: `[150, 600]`, Adım: `50`)
  - `b`: Kaldırma hızı v (Güncel: **5 ft/s**, Aralık: `[2, 10]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 550 ft·lb/s = 1 hp birim çevrim sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Güç (ft·lb/s): P = a * b
  2) Beygir gücü: P_hp = P / 550
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.8
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S8_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3500 lb, 7° eğim, 40 ft/s
  - *Çözüm:* F = W sin(7°), P = F * v
  - *Şekil:* 7° (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Otomobil ağırlığı W (Güncel: **3500 lb**, Aralık: `[2500, 5000]`, Adım: `250`)
  - `b`: Tırmanma hızı v (Güncel: **40 ft/s**, Aralık: `[20, 60]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 7° eğim açısı korunmalıdır (çizim geometrisi).
- **Şekil Durumu:** `yalnız etiket değişir (KUTU EKSİK: 7°)`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Gerekli çekiş kuvveti: F = a * sin(radians(7))
  2) Motor gücü: P = F * b (ft·lb/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.9
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S9_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* %80 verim, 19.5 kW giriş gücü
  - *Çözüm:* P_çıkış = ε * P_giriş
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Motor verimi ε (Güncel: **0.8 **, Aralık: `[0.65, 0.95]`, Adım: `0.05`)
  - `b`: Giriş gücü P_giris (Güncel: **19.5 kW**, Aralık: `[10.0, 30.0]`, Adım: `1.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Verim formülü.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a ∈ (0, 1), b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Çıkış gücü: P_cikis = a * b (kW)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.10
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S10_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 20 kg, 18.75 J
  - *Çözüm:* V₁ = 0.5 * m * v² => v = √(2 V₁ / m)
  - *Şekil:* k = 50 N/m (kutu var), k' = 100 N/m (kutu var), 0.25 m (kutu var)
- **Önerilen Parametreler:**
  - `a`: Yaka kütlesi m (Güncel: **20 kg**, Aralık: `[10, 40]`, Adım: `5`)
  - `b`: Toplam başlangıç potansiyel enerjisi V₁ (Güncel: **18.75 J**, Aralık: `[10, 40]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Yay sabitleri (50 ve 100 N/m) ve 0.25 m sıkışma çizimde sabittir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Enerji korunumu: b = 0.5 * a * v²
  2) Hız: v = √(2 * b / a)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.11
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S11_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 60 kg, 5 m, 2 s, g = 9.81 m/s²
  - *Çözüm:* U = mgh, P_ort = U / t
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Sandık kütlesi m (Güncel: **60 kg**, Aralık: `[30, 120]`, Adım: `10`)
  - `b`: Kaldırma yüksekliği h (Güncel: **5 m**, Aralık: `[3, 10]`, Adım: `1`)
  - `c`: Kaldırma süresi t (Güncel: **2 s**, Aralık: `[1.5, 5.0]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** g = 9.81 sabiti.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yapılan potansiyel iş: U = a * 9.81 * b
  2) Ortalama güç: P_ort = U / c (W)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.12
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S12_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 1000 kg, 20 kN, 50 m/s
  - *Çözüm:* P = F * v = 20000 * 50 = 1 MW
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: İtki kuvveti F (Güncel: **20 kN**, Aralık: `[10, 40]`, Adım: `5`)
  - `b`: Anlık hız v (Güncel: **50 m/s**, Aralık: `[30, 80]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Kütle anlık güçte sadeleşir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kuvvet (N): F_N = a * 1000
  2) Anlık güç (W): P = F_N * b
  3) MW cinsinden: P_MW = P / 1e6
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.13
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S13_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 5 g (0.005 kg), 3 m, g = 9.81 m/s²
  - *Çözüm:* v = √(2gh)
  - *Şekil:* 3 m (kutu eksik), 2 m (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Bilye kütlesi m (Güncel: **0.005 kg**, Aralık: `[0.002, 0.02]`, Adım: `0.002`)
  - `b`: Düşme yüksekliği h (Güncel: **3 m**, Aralık: `[1.5, 6.0]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Kütle serbest düşme hızında sadeleşir.
- **Şekil Durumu:** `yalnız etiket değişir (KUTU EKSİK: 3 m, 2 m)`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hız: v = √(2 * 9.81 * b)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.14
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S14_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 100 kg, 45° eğim, 10 m, g = 9.81 m/s²
  - *Çözüm:* h = s * sin(45°), U_g = mgh
  - *Şekil:* 10 m (kutu var), 45° (kutu eksik), k = 2 kN/m (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Sandık kütlesi m (Güncel: **100 kg**, Aralık: `[50, 200]`, Adım: `20`)
  - `b`: Kayma mesafesi s (Güncel: **10 m**, Aralık: `[5, 20]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° eğim açısı korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Düşey yer değiştirme: h = b * sin(radians(45))
  2) Yerçekimi işi: U_g = a * 9.81 * h (J)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.15
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S15_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 200 mm, 50 N/m, 245 mm
  - *Çözüm:* s = (L - L₀)/1000, Ve = 0.5 * k * s²
  - *Şekil:* 50 mm (kutu var), 240 mm (kutu var)
- **Önerilen Parametreler:**
  - `a`: Yay sabiti k (Güncel: **50 N/m**, Aralık: `[25, 120]`, Adım: `10`)
  - `b`: İlk gerilmemiş uzunluk L₀ (Güncel: **200 mm**, Aralık: `[150, 250]`, Adım: `25`)
  - `c`: Gerilmiş son uzunluk L (Güncel: **245 mm**, Aralık: `[230, 320]`, Adım: `15`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Sapan çatal geometrisi korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, c > b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Uzama mesafesi (m): s = (c - b) / 1000
  2) Elastik potansiyel enerji: Ve = 0.5 * a * s² (J)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.16
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 400 Mg (400,000 kg), 100 s, 10 m/s
  - *Çözüm:* ΣU = 0.5 * m * v²
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Tren kütlesi m (Güncel: **400 Mg**, Aralık: `[200, 600]`, Adım: `50`)
  - `b`: Son hız v (Güncel: **10 m/s**, Aralık: `[5, 25]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 100 saniye süresi sabit ivmeyle hızlanmayı açıklar, iş sadece son kinetik enerjiye bağlıdır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Kütle (kg): m_kg = a * 1000
  2) Aktarılan iş (J): U = 0.5 * m_kg * b²
  3) MJ cinsinden: U_MJ = U / 1e6
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.17
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S17_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 15 kW, 10 m/s
  - *Çözüm:* F = P / v = 15000 / 10 = 1500 N
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Motor gücü P (Güncel: **15 kW**, Aralık: `[10, 40]`, Adım: `5`)
  - `b`: Araba hızı v (Güncel: **10 m/s**, Aralık: `[5, 25]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** P = F * v formülü.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Güç (W): P_W = a * 1000
  2) İtki kuvveti: F = P_W / b (N)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.18
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S18_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 1284 lb, 2 ft (metinde sehven 1285 N yazılmış)
  - *Çözüm:* k = F / s = 1284 / 2 = 642 lb/ft
  - *Şekil:* d = 8 ft (kutu var), 45° (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Gereken sıkıştırma kuvveti F (Güncel: **1284 lb**, Aralık: `[800, 2000]`, Adım: `100`)
  - `b`: Yay sıkışması s (Güncel: **2 ft**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Hooke yasası.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yay sabiti: k = a / b (lb/ft)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK / BİRİM HATASI: Metinde kuvvet '1285 N' yazılmışken sıkışma '2 ft' verilmiştir. Çözüm notunda orijinal sorunun F = 1284 lb olduğu belirtilmiştir.

### Soru 4.19
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S19_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 30 lb, 113 inç
  - *Çözüm:* h_ft = 113 / 12, U_g = W * h_ft
  - *Şekil:* 6 in. (kutu var), 200 lb/in. (kutu var), k_C = 100 lb/in. (kutu var), 4 in. (kutu eksik)
- **Önerilen Parametreler:**
  - `a`: Blok ağırlığı W (Güncel: **30 lb**, Aralık: `[15, 60]`, Adım: `5`)
  - `b`: Geri fırlama yüksekliği h (Güncel: **113 in.**, Aralık: `[60, 180]`, Adım: `10`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Yay katsayıları korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yüksekliği ft birimine çevir: h_ft = b / 12
  2) Yerçekimine karşı yapılan iş: U_g = a * h_ft (ft·lb)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 4.20
- **Görsel:** `media/Dinamik 4. Ünite Sayısal Sorular/S20_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* V = -1.19x10⁹ J, T = 0.37x10⁹ J
  - *Çözüm:* E = T + V = 0.37 + (-1.19) = -0.82x10⁹ J
  - *Şekil:* r_A = 20 Mm (kutu var), r_B = 80 Mm (kutu var)
- **Önerilen Parametreler:**
  - `a`: Potansiyel enerji V_A (Güncel: **-1.19 GJ**, Aralık: `[-2.5, -0.8]`, Adım: `0.1`)
  - `b`: Kinetik enerji T_A (Güncel: **0.37 GJ**, Aralık: `[0.2, 0.8]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Eliptik yörüngede toplam enerji korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** b > 0, a < 0, a + b < 0 (bağlı yörünge şartı).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Toplam mekanik enerji: E = a + b (GJ)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok


---

## Ünite 5: Parçacık Kinetiği (İmpuls ve Momentum Yöntemi)

### Soru 5.1
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S1_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 200 N, 45° açı, 10 s
  - *Çözüm:* I = F_x * t = F * cos(45°) * t
  - *Şekil:* 200 N (kutu var), 45° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Çekme kuvveti F (Güncel: **200 N**, Aralık: `[100, 400]`, Adım: `25`)
  - `b`: Kuvvet uygulama süresi t (Güncel: **10 s**, Aralık: `[5, 20]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° çekme açısı şekilde sabittir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yatay kuvvet bileşeni: F_x = a * cos(radians(45))
  2) Yatay impuls (itme): I_x = F_x * b (N·s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.2
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S2_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 100 kg, 200 N, 45° açı, 10 s
  - *Çözüm:* I = m * v_son => v_son = I / m
  - *Şekil:* 200 N (kutu var), 45° (kutu var)
- **Önerilen Parametreler:**
  - `a`: Taş kütlesi m (Güncel: **100 kg**, Aralık: `[50, 200]`, Adım: `25`)
  - `b`: Çekme kuvveti F (Güncel: **200 N**, Aralık: `[100, 400]`, Adım: `25`)
  - `c`: Süre t (Güncel: **10 s**, Aralık: `[5, 20]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° açısı korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0, b * sin(45°) < a * 9.81 (taş yerden havalanmamalı).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İtme: I = b * cos(radians(45)) * c
  2) Son hız: v_son = I / a (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.3
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 2 kg, 45° eğim, 3 m/s, g = 9.81 m/s²
  - *Çözüm:* m*v₁ - m*g*sin(45°)*t = 0 => t = v₁ / (g sin 45°)
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Blok kütlesi m (Güncel: **2 kg**, Aralık: `[1, 5]`, Adım: `0.5`)
  - `b`: İlk fırlatma hızı v₁ (Güncel: **3 m/s**, Aralık: `[2, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° eğim açısı korunur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Eğim aşağı yerçekimi ivmesi: a_g = 9.81 * sin(radians(45))
  2) Durma süresi: t = b / a_g (s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.4
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0-2 s arası 0-10 N, 2-4 s arası 10 N
  - *Çözüm:* Alan 1 (üçgen) = (2*10)/2, Alan 2 (dikdörtgen) = (4-2)*10
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Maksimum kuvvet F_max (Güncel: **10 N**, Aralık: `[5, 30]`, Adım: `5`)
  - `b`: Üçgen yükselme süresi t₁ (Güncel: **2 s**, Aralık: `[1, 4]`, Adım: `1`)
  - `c`: Sabit kuvvet son süresi t₂ (Güncel: **4 s**, Aralık: `[3, 8]`, Adım: `1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Doğrusal artış ve sabit plato grafiği formu.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, c > b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Üçgen bölge itmesi: I1 = 0.5 * b * a
  2) Dikdörtgen bölge itmesi: I2 = (c - b) * a
  3) Toplam itme: I = I1 + I2 (N·s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.5
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 15000 kg, 1.5 m/s, 12000 kg, 0.75 m/s
  - *Çözüm:* m₁*v₁ - m₂*v₂ = (m₁ + m₂)*v_ortak
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İlk vagon kütlesi m₁ (Güncel: **15000 kg**, Aralık: `[10000, 25000]`, Adım: `2500`)
  - `b`: İlk vagon hızı v₁ (Güncel: **1.5 m/s**, Aralık: `[1.0, 3.0]`, Adım: `0.5`)
  - `c`: İkinci vagon hızı (ters yön) v₂ (Güncel: **0.75 m/s**, Aralık: `[0.5, 2.0]`, Adım: `0.25`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** m₂ = 12000 kg vagon kütlesi referans tutulur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Toplam başlangıç momentumu: P = a * b - 12000 * c
  2) Ortak kütle: M = a + 12000
  3) Ortak hız: v_ortak = P / M (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.6
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 2000 kg, 2 m/s, 1500 kg, 4 m/s
  - *Çözüm:* m_A*v_A - m_B*v_B = (m_A + m_B)*v_ortak
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: A aracı kütlesi m_A (Güncel: **2000 kg**, Aralık: `[1200, 3000]`, Adım: `200`)
  - `b`: A aracı hızı (sağa) v_A (Güncel: **2 m/s**, Aralık: `[1, 5]`, Adım: `0.5`)
  - `c`: B aracı hızı (sola) v_B (Güncel: **4 m/s**, Aralık: `[2, 6]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** B aracı kütlesi 1500 kg sabit referans.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Sağa doğru net momentum: P = a * b - 1500 * c
  2) Ortak hız: v_ortak = P / (a + 1500)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.7
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 500 m/s, 0.002 kg, 0.001 s
  - *Çözüm:* F_ort * Δt = m * Δv => F_ort = m*v / Δt
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Mermi kütlesi m (Güncel: **0.002 kg**, Aralık: `[0.001, 0.01]`, Adım: `0.001`)
  - `b`: Namlu çıkış hızı v (Güncel: **500 m/s**, Aralık: `[300, 800]`, Adım: `50`)
  - `c`: Namluda kalma süresi Δt (Güncel: **0.001 s**, Aralık: `[0.0005, 0.003]`, Adım: `0.0005`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** İlk hız sıfır.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Momentum değişimi: ΔP = a * b
  2) Ortalama kuvvet: F_ort = ΔP / c (N)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.8
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S8_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 50 kg (araç), 75 kg (çocuk), 3 m/s
  - *Çözüm:* 0 = m_c(v_a + v_{c/a}) + m_a * v_a, v_c = v_a + v_{c/a}
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Çocuk kütlesi m_c (Güncel: **75 kg**, Aralık: `[40, 90]`, Adım: `5`)
  - `b`: Çocuğun araca göre bağıl hızı v_{c/a} (Güncel: **3 m/s**, Aralık: `[1.5, 5.0]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Araç kütlesi 50 kg sabittir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Araç hızı: v_a = -(a * b) / (a + 50)
  2) Çocuğun yere göre hızı: v_c = v_a + b
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.9
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S9_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* Önceki soru verileri
  - *Çözüm:* |v_a| = 1.8 m/s
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Çocuk kütlesi m_c (Güncel: **75 kg**, Aralık: `[40, 90]`, Adım: `5`)
  - `b`: Çocuğun araca göre bağıl hızı v_{c/a} (Güncel: **3 m/s**, Aralık: `[1.5, 5.0]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 50 kg araç kütlesi.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Araç hız büyüklüğü: |v_a| = (a * b) / (a + 50)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.10
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S10_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 50 ton (lokomotif), 3 vagon x 30 ton = 90 ton, toplam 140 ton, 80 s, 40 km/h
  - *Çözüm:* Toplam kütle = 140,000 kg, v = 40/3.6 = 11.11 m/s, F = m*v / t
  - *Şekil:* F = 30 kN (kutu var)
- **Önerilen Parametreler:**
  - `a`: Hedef son hız v (Güncel: **40 km/h**, Aralık: `[20, 60]`, Adım: `5`)
  - `b`: Hızlanma süresi t (Güncel: **80 s**, Aralık: `[40, 120]`, Adım: `10`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Tren katar kütlesi (140 ton) sabittir.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hızı m/s'ye çevir: v_ms = a / 3.6
  2) Ortalama çekiş kuvveti (N): F = (140000 * v_ms) / b
  3) kN cinsinden: F_kN = F / 1000
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.11
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S11_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2500 kg, 1250 kg, 2 m/s
  - *Çözüm:* m_A*v_A + m_B*v_B = 0 => v_B = -(m_A/m_B)*v_A, v_A - v_B = c
  - *Şekil:* 5 m (kutu var)
- **Önerilen Parametreler:**
  - `a`: Cip kütlesi m_A (Güncel: **2500 kg**, Aralık: `[1800, 3500]`, Adım: `250`)
  - `b`: Araba kütlesi m_B (Güncel: **1250 kg**, Aralık: `[800, 1600]`, Adım: `100`)
  - `c`: Halat sarma hızı v_{A/B} (Güncel: **2 m/s**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Halat sarma kinematiği.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Momentum oranı: k = a / b
  2) Bağıl hız denklemi: v_A - (-k * v_A) = c => v_A * (1 + k) = c
  3) Cip hızı: v_A = c / (1 + k)
  4) Araba hızı: v_B = -k * v_A
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.12
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S12_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 300 kg (araba), 75 kg (adam), 0.1 kg, 900 m/s
  - *Çözüm:* Toplam kütle = 375 kg, 0 = m_m*(v_a + v_{m/a}) + 375*v_a
  - *Şekil:* Şekilde sayı etiketi yok
- **Önerilen Parametreler:**
  - `a`: Mermi kütlesi m_m (Güncel: **0.1 kg**, Aralık: `[0.05, 0.3]`, Adım: `0.05`)
  - `b`: Mermi bağıl hızı v_{m/a} (Güncel: **900 m/s**, Aralık: `[500, 1200]`, Adım: `100`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Araba+adam kütlesi (375 kg) korunur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Geri tepme hızı: v_a = -(a * b) / (375 + a)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.13
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 70 kg, 8 kg, 2 m/s
  - *Çözüm:* 0 = m_b*(v_s + c) + m_s*v_s => v_s = -m_b*c / (m_b + m_s)
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Sporcu kütlesi m_s (Güncel: **70 kg**, Aralık: `[50, 90]`, Adım: `5`)
  - `b`: Blok kütlesi m_b (Güncel: **8 kg**, Aralık: `[4, 15]`, Adım: `1`)
  - `c`: Fırlatma bağıl hızı v_{b/s} (Güncel: **2 m/s**, Aralık: `[1, 5]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Sürtünmesiz buz yüzeyi.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Sporcu geri tepme hızı: v_s = -(b * c) / (a + b)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.14
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.5 kg, 6 m/s, 5 kg (B bloğu), e = 0.6
  - *Çözüm:* m_A*v_{A1} = m_A*v_{A2} + m_B*v_{B2}, e*(v_{A1} - 0) = v_{B2} - v_{A2}
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: A topu kütlesi m_A (Güncel: **0.5 kg**, Aralık: `[0.2, 1.0]`, Adım: `0.1`)
  - `b`: A topu ilk hızı v_{A1} (Güncel: **6 m/s**, Aralık: `[3, 10]`, Adım: `1`)
  - `c`: Restitüsyon katsayısı e (Güncel: **0.6 **, Aralık: `[0.3, 0.9]`, Adım: `0.1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** m_B = 5 kg duran blok.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c ∈ (0, 1).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Restitüsyon: v_{A2} = v_{B2} - c * b
  2) Momentum: a * b = a * (v_{B2} - c * b) + 5 * v_{B2}
  3) B hızı: v_{B2} = (a * b * (1 + c)) / (a + 5)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.15
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 5000 kg, 30 km/h, 2000 kg, 10 km/h
  - *Çözüm:* (5000*v₁ + 2000*v₂)/7000
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: Kamyon ilk hızı v₁ (Güncel: **30 km/h**, Aralık: `[20, 50]`, Adım: `5`)
  - `b`: Araç ilk hızı v₂ (Güncel: **10 km/h**, Aralık: `[5, 20]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Tam plastik kenetlenme.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > b > 0 (kamyon arkadan çarpmalı).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Hızları m/s'ye çevir: v1 = a / 3.6, v2 = b / 3.6
  2) Ortak hız: v_ortak = (5000 * v1 + 2000 * v2) / 7000 (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.16
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S16_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 10 kg, 8 kg, 2 m/s, t = 3 s, g = 9.81 m/s²
  - *Çözüm:* m_A*v_{A1} + (m_A*g*t) - (T*t) = m_A*v_{A2}
  - *Şekil:* 8 kg (kutu var), 10 kg (kutu var)
- **Önerilen Parametreler:**
  - `a`: A silindiri kütlesi m_A (Güncel: **10 kg**, Aralık: `[8, 16]`, Adım: `2`)
  - `b`: B silindiri kütlesi m_B (Güncel: **8 kg**, Aralık: `[4, 10]`, Adım: `1`)
  - `c`: A ilk hızı v_{A1} (Güncel: **2 m/s**, Aralık: `[1, 5]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Süre t = 3 s sabit.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > b > 0 (A aşağı inebilmeli), c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) İmpuls-momentum denklemini yaz: a * c + a * 9.81 * 3 - 3 * T = a * v_{A2}
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ Soru sadece impuls-momentum denklemini yazdırmaktadır; sayısal tek bir değer sormamaktadır.

### Soru 5.17
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S17_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 10 kg, 50 kg, 2 s, g = 9.81 m/s²
  - *Çözüm:* a = (m_B - m_A)*g / (m_B + m_A), v = a*t
  - *Şekil:* 10 lb (kutu var), 50 lb (kutu var)
- **Önerilen Parametreler:**
  - `a`: A bloğu kütlesi m_A (Güncel: **10 kg**, Aralık: `[5, 20]`, Adım: `2.5`)
  - `b`: B bloğu kütlesi m_B (Güncel: **50 kg**, Aralık: `[30, 80]`, Adım: `5`)
  - `c`: Süre t (Güncel: **2 s**, Aralık: `[1, 4]`, Adım: `0.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Makaralı atwood düzeni.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** b > a > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Sistem ivmesi: a_ivme = (b - a) * 9.81 / (a + b)
  2) B bloğunun hızı: v = a_ivme * c (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ BİRİM TUTARSIZLIĞI: Metinde ve çözümde bloklar '10 kg' ve '50 kg' iken, görsel S17_1 üzerinde etiketler '10 lb' ve '50 lb' yazmaktadır.

### Soru 5.18
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S18_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 kg, r₁ = 1.5 m, v₁ = 5 m/s, r₂ = 1.2 m
  - *Çözüm:* m * v₁ * r₁ = m * v₂ * r₂ => v₂ = v₁ * r₁ / r₂
  - *Şekil:* k = 200 N/m (kutu var), v = 5 m/s (kutu var)
- **Önerilen Parametreler:**
  - `a`: Disk kütlesi m (Güncel: **3 kg**, Aralık: `[1.5, 6.0]`, Adım: `0.5`)
  - `b`: İlk hız v₁ (Güncel: **5 m/s**, Aralık: `[3, 8]`, Adım: `1`)
  - `c`: İkinci yarıçap r₂ (Güncel: **1.2 m**, Aralık: `[0.8, 1.4]`, Adım: `0.1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** r₁ = 1.5 m başlangıç geometrisi.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Açısal momentum korunumu: v₂ = (b * 1.5) / c (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.19
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S19_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 2 kg, 20 kg (blok), 4 m/s, e = 0.8
  - *Çözüm:* m*v₁ = m*v_{A2} + M*v_{B2}, e*v₁ = v_{B2} - v_{A2}
  - *Şekil:* 4 m/s (kutu var)
- **Önerilen Parametreler:**
  - `a`: Top kütlesi m (Güncel: **2 kg**, Aralık: `[1, 5]`, Adım: `0.5`)
  - `b`: Top ilk hızı v₁ (Güncel: **4 m/s**, Aralık: `[2, 8]`, Adım: `1`)
  - `c`: Restitüsyon katsayısı e (Güncel: **0.8 **, Aralık: `[0.5, 0.95]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** M = 20 kg blok kütlesi sabit.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c ∈ (0, 1).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) v_{A2} = v_{B2} - c * b
  2) a * b = a * (v_{B2} - c * b) + 20 * v_{B2}
  3) Blok hızı: v_{B2} = (a * b * (1 + c)) / (a + 20) (m/s)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.20
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S20_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 1500 kg, 0-2 sn 10 kN, 2-4 sn 20 kN
  - *Çözüm:* İmpuls = 2*10000 + 2*20000 = 60000 N·s, v = 60000/1500 = 40 m/s
  - *Şekil:* 30, 60, 90 kN; 0.5, 1.5, 2, 2.5 s (grafik değerleri farklı)
- **Önerilen Parametreler:**
  - `a`: Kızak kütlesi m (Güncel: **1500 kg**, Aralık: `[1000, 2500]`, Adım: `250`)
  - `b`: İlk kademe kuvvet F₁ (Güncel: **10 kN**, Aralık: `[5, 20]`, Adım: `2.5`)
  - `c`: İkinci kademe kuvvet F₂ (Güncel: **20 kN**, Aralık: `[15, 35]`, Adım: `2.5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Zaman kademeleri 2'şer saniye sabittir.
- **Şekil Durumu:** `şekil yeniden çizilmeli`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Toplam itme: I = (2 * b * 1000) + (2 * c * 1000) (N·s)
  2) Son hız: v_son = I / a (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ TUTARSIZLIK: Metinde kuvvetler '0-2 sn 10 kN, 2-4 sn 20 kN' iken, görsel S20_1 üzerinde kademeler 30, 60, 90 kN ve zaman 2.5 saniyedir.

### Soru 5.21
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 2 kg, 0.5 m, 5 m/s, 0.25 m
  - *Çözüm:* m v₁ r₁ = m v₂ r₂ => v₂ = v₁ * r₁ / r₂
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İlk hız v₁ (Güncel: **5 m/s**, Aralık: `[3, 10]`, Adım: `1`)
  - `b`: İlk yarıçap r₁ (Güncel: **0.5 m**, Aralık: `[0.3, 0.8]`, Adım: `0.1`)
  - `c`: Son yarıçap r₂ (Güncel: **0.25 m**, Aralık: `[0.15, 0.4]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Kütle sadeleşir.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Yeni çizgisel hız: v₂ = (a * b) / c (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.22
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S22_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 4 kg (toplam), 600 m/s, m_A = 1.5, m_B = 2.5, 45° yukarı-sol, 30° aşağı-sağ
  - *Çözüm:* Dikey: 1.5*v_A*sin(45°) = 2.5*v_B*sin(30°), Yatay: 4*600 = -1.5*v_A*cos(45°) + 2.5*v_B*cos(30°)
  - *Şekil:* 600 m/s (kutu var), 45° (kutu var), 30° (kutu var), 60 m (kutu var)
- **Önerilen Parametreler:**
  - `a`: Mermi ilk hızı v₀ (Güncel: **600 m/s**, Aralık: `[400, 800]`, Adım: `50`)
  - `b`: A parçası kütlesi m_A (Güncel: **1.5 kg**, Aralık: `[1.0, 2.0]`, Adım: `0.25`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 45° ve 30° saçılma açıları çizimde korunmalıdır.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b ∈ (0.5, 3.5).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) B kütlesi: m_B = 4 - b
  2) Dikey momentumdan ilişki: v_B = (b * sin(radians(45))) / (m_B * sin(radians(30))) * v_A
  3) Yatay momentum: 4 * a = -b * cos(radians(45)) * v_A + m_B * cos(radians(30)) * v_B
  4) v_A çözülür.
- **Zorluk Seviyesi:** Zor
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ Çözümde A parçasının sola doğru fırladığı metinde söylenmesine rağmen yatay momentum ilk satırda pozitif yazılıp alt satırda -1.061v_A'ya dönüştürülmüştür.

### Soru 5.23
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S23_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 800 kg, 300 kg, 0.5 m, e = 0.1, g = 9.81 m/s²
  - *Çözüm:* v_{c1} = √(2*9.81*h), e = (v_{p2} - v_{c2})/v_{c1}, Momentum korunumu
  - *Şekil:* 0.5 m (kutu var)
- **Önerilen Parametreler:**
  - `a`: Kazık kütlesi m_p (Güncel: **800 kg**, Aralık: `[500, 1500]`, Adım: `100`)
  - `b`: Çekiç kütlesi m_c (Güncel: **300 kg**, Aralık: `[150, 500]`, Adım: `50`)
  - `c`: Düşme yüksekliği h (Güncel: **0.5 m**, Aralık: `[0.3, 1.2]`, Adım: `0.1`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Restitüsyon e = 0.1 ve yerçekimi sabiti g=9.81.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Çekiç çarpma hızı: v_{c1} = √(2 * 9.81 * c)
  2) Restitüsyon bağıntısı: v_{c2} = v_{p2} - 0.1 * v_{c1}
  3) Momentum korunumu: b * v_{c1} = b * (v_{p2} - 0.1 * v_{c1}) + a * v_{p2}
  4) Kazık hızı: v_{p2} = (b * v_{c1} * 1.1) / (a + b) (m/s)
- **Zorluk Seviyesi:** Orta
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.24
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S24_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 0.4 kg (A topu), 5 m/s, 30° eğik açı, e = 0.8
  - *Çözüm:* v_{At1} = 5 sin(30°), v_{An1} = 5 cos(30°), e = (v_{Bn2} - v_{An2})/v_{An1}
  - *Şekil:* (v_A)_1 = 5 m/s (kutu var), 30° (kutu var)
- **Önerilen Parametreler:**
  - `a`: A topu ilk hızı (v_A)₁ (Güncel: **5 m/s**, Aralık: `[3, 9]`, Adım: `1`)
  - `b`: Restitüsyon katsayısı e (Güncel: **0.8 **, Aralık: `[0.5, 0.95]`, Adım: `0.05`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** 30° çarpışma normal açısı korunur.
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b ∈ (0, 1).
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Normal bileşen ilk hız: v_{An1} = a * cos(radians(30))
  2) Eşit kütleli merkezi çarpışma restitüsyon formülü: v_{Bn2} = 0.5 * v_{An1} * (1 + b)
  3) B topu hız büyüklüğü: v_{B2} = v_{Bn2}
- **Zorluk Seviyesi:** Zor
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok

### Soru 5.25
- **Görsel:** `media/Dinamik 5. Ünite Sayısal Sorular/S25_1.png`
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 kg, 10 m (yarıçap), 20 m/s
  - *Çözüm:* H_O = m * v * r = 3 * 20 * 10 = 600 kg·m²/s
  - *Şekil:* 10 ft (kutu var)
- **Önerilen Parametreler:**
  - `a`: Top kütlesi m (Güncel: **3 kg**, Aralık: `[1, 6]`, Adım: `0.5`)
  - `b`: Eğrilik yarıçapı ρ (Güncel: **10 m**, Aralık: `[5, 20]`, Adım: `2.5`)
  - `c`: Top hızı v (Güncel: **20 m/s**, Aralık: `[10, 35]`, Adım: `5`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Hız vektörünün yarıçapa dikliği (yatay teğetlik).
- **Şekil Durumu:** `yalnız etiket değişir`
- **Fiziksel Geçerlilik Kısıtları:** a > 0, b > 0, c > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Açısal momentum: H_O = a * c * b (kg·m²/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** ⚠️ BİRİM TUTARSIZLIĞI: Soru metninde ve çözümde eğrilik yarıçapı '10 m' iken, görsel S25_1 üzerinde '10 ft' yazmaktadır.

### Soru 5.26
- **Görsel:** Yok (Şekilsiz Soru)
- **Tüm Sabit Sayılar:**
  - *Metin:* 3 m, 10 m/s, 1 m/s kısaltma hızı, 2 m son yarıçap
  - *Çözüm:* m * v₁ * r₁ = m * v₂ * r₂ => v₂ = (v₁ * r₁) / r₂
  - *Şekil:* Yok
- **Önerilen Parametreler:**
  - `a`: İlk yörünge yarıçapı r₁ (Güncel: **3 m**, Aralık: `[2, 5]`, Adım: `0.5`)
  - `b`: İlk teğetsel hız v₁ (Güncel: **10 m/s**, Aralık: `[5, 15]`, Adım: `1`)
  - `c`: Son yarıçap r₂ (Güncel: **2 m**, Aralık: `[1.0, 2.5]`, Adım: `0.25`)
- **Sabit Kalması Gereken Sayılar ve Nedeni:** Merkezi kuvvet tork oluşturmaz, açısal momentum korunur.
- **Şekil Durumu:** `şekil yok`
- **Fiziksel Geçerlilik Kısıtları:** a > c > 0, b > 0.
- **Çözümün Ara Adımları (Solver İskeleti):**
  1) Açısal momentum korunumu: v₂ = (b * a) / c (m/s)
- **Zorluk Seviyesi:** Kolay
- **Çözüm Hatası Şüphesi / Tutarsızlık:** Yok
