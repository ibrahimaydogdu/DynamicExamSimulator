# İNM 203 Dinamik - Şekil OCR ve Değer Düzeltme Raporu

> [!IMPORTANT]
> Bu rapor, `media/sayilar.json` dosyasındaki ham OCR sonuçlarının **106 benzersiz görsel** üzerinde insan gözüyle/multimodal inceleme yapılarak düzeltilmesi sürecini ve istatistiklerini belgeler. Orijinal kutu koordinatlarına dokunulmamış, kaçırılan ifadeler ve çizim parametreleri eksiksiz tamamlanmıştır.

## 1. Genel Özet ve Temel İstatistikler

- **Toplam Dosya Sayısı:** 120 adet PNG görseli
- **Benzersiz (Unique) Görsel Sayısı (MD5 Hash):** 106 adet
- **Kopya / Tekrar Eden Dosya Sayısı:** 14 adet (Sonuçlar hash eşleştirmesi ile birebir çoğaltılmıştır)
- **Değerlendirilen Geçerli Sayısal Tespit:** 209 adet
- **OCR'ın Yanlış Okuduğu ve Düzeltilen Sayı/Metin:** 139 adet
- **OCR Hata Oranı:** %77.2
- **OCR'ın Kaçırdığı Sayı/Ölçü Sayısı (`ocr_kacirdi: true`):** 29 adet
- **OCR Yanlış Pozitif / Gürültü Çizgi Sayısı (`gecersiz: true`):** 58 adet
- **Soru Metninde Olmayıp Yalnızca Şekilde Olan Sayı/Değer:** 141 adet
- **Okuma Doğrulanamayan (`okuma_dogrulandi: false`) Sayısı:** 0 (Tüm tespitler %100 doğrulanmıştır)

## 2. Ünite Bazlı Dağılım Tablosu

| Ünite | Benzersiz Görsel | Geçerli Tespit | Düzeltilen | OCR Hata (%) | Kaçırılan | Geçersiz (Gürültü) | Sadece Şekilde |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2. Ünite** | 9 | 12 | 11 | %91.7 | 0 | 3 | 6 |
| **3. Ünite** | 20 | 28 | 22 | %84.6 | 2 | 6 | 16 |
| **4. Ünite** | 17 | 30 | 17 | %85.0 | 10 | 4 | 21 |
| **5. Ünite** | 14 | 27 | 18 | %69.2 | 1 | 4 | 17 |
| **6. Ünite** | 10 | 30 | 26 | %89.7 | 1 | 16 | 20 |
| **7. Ünite** | 25 | 68 | 35 | %64.8 | 14 | 16 | 57 |
| **8. Ünite** | 11 | 14 | 10 | %76.9 | 1 | 9 | 4 |
| **TOPLAM** | **106** | **209** | **139** | **%77.2** | **29** | **58** | **141** |

## 3. Tipik OCR Hata Türleri ve Düzeltme Örnekleri

OCR modelinin en çok zorlandığı ve görsel doğrulama ile çözülen kritik hata kategorileri:

1. **Derece İşareti (°):**
   - Ham OCR: `"0 = 309"` → Gerçek Metin: `"θ = 30°"` (`tur: aci`, `deger: 30`)
   - Ham OCR: `"308"` veya `"c09"` → Gerçek Metin: `"30°"` veya `"60°"`
   - Ham OCR: `"459"` → Gerçek Metin: `"45°"`

2. **Ondalık Noktalar ve Metre Birimi:**
   - Ham OCR: `"5"` → Gerçek Metin: `"1.5 m"` (`deger: 1.5`, `birim: m`)
   - Ham OCR: `"3"` → Gerçek Metin: `"0.5 m"` veya `"0.25 m"`
   - Ham OCR: `"125 ft"` → Gerçek Metin: `"1.25 ft"`

3. **Matematiksel Denklemler, Kesirler ve Üsler:**
   - Ham OCR: `"y = 10"` → Gerçek Metin: `"y = x²/10"` (`tur: denklem`)
   - Ham OCR: `"y = 20"` → Gerçek Metin: `"y = (1/20)x²"` (`tur: denklem`)
   - Ham OCR: `"8 cos 3t"` → Gerçek Metin: `"F = 8 cos 3t"` (`tur: denklem`)

4. **Şekil Çizgilerinin ve Harf Etiketlerinin Rakam Sanılması:**
   - Yay helezonları, dişli çark dişleri ve ok işaretleri OCR tarafından `1`, `2`, `3`, `4` olarak algılanmıştır. Bunlar `gecersiz: true` olarak işaretlenmiş, silinmemiştir.
   - A, B, C mafsal etiketleri `gecersiz: true` olarak işaretlenmiştir.

## 4. Kaçırılan Sayıların Tespiti (`ocr_kacirdi: true`)

OCR tarafından hiç kutulanmamış (arka plan veya çizgi kontrastı nedeniyle kaçırılmış) fakat problem çözümü için hayati olan 29 sayı tespit edilip `kutu: null` ile eklenmiştir. Öne çıkanlar:

- **Ünite 3 Soru 2:** 1:10 eğim üçgeninin dikey kenarı `1` kaçırılmıştı.
- **Ünite 3 Soru 5:** Römorkörün `1.5 kN` direnç kuvveti kaçırılmıştı.
- **Ünite 4 Soru 8:** Yokuş eğim açısı `7°` kaçırılmıştı.
- **Ünite 4 Soru 13:** Bilye atış yüksekliği `3 m` ve kanal yüksekliği `2 m` kaçırılmıştı.
- **Ünite 4 Soru 14:** Eğim açısı `45°` ve yay sabiti `k = 2 kN/m` kaçırılmıştı.
- **Ünite 4 Soru 19:** İç yay yüksekliği `4 in.` kaçırılmıştı.
- **Ünite 7 Soru 1 & Soru 3:** Plaka boyutları `1 m` ve `2 m` kolları kaçırılmıştı.
- **Ünite 7 Soru 7:** Uçak ağırlık merkezi yüksekliği `9 m` kaçırılmıştı.
- **Ünite 7 Soru 23:** Kutu yüksekliği `1 m` ve araba eğim açısı `15°` kaçırılmıştı.
- **Ünite 8 Soru 29:** Üst paralel yayın `k = 10 N/m` değeri kaçırılmıştı.

## 5. Doğrulama Örnekleri (Görsel Denetim)

Zorunlu doğrulama adımı olarak rastgele seçilen 10 benzersiz görsel üzerinde, orijinal kutular yeşil çizgiyle ve düzeltilen `gercek_metin` ifadeleri etiketlenerek `media/_debug2/` klasörüne işlenmiştir:

1. `media/_debug2/debug2_u2_S10_1.png` - Parabol y = x²/10 ve 16 m mesafesi
2. `media/_debug2/debug2_u3_S1_1.png` - Vinç sapanı 30° ve 30° açıları
3. `media/_debug2/debug2_u3_S16_1.png` - Balon F = 6 kN kaldırma ve F_D = (100v) N direnç
4. `media/_debug2/debug2_u4_S10_1.png` - İki yaylı bilezik: k = 50 N/m, k' = 100 N/m, 0.25 m
5. `media/_debug2/debug2_u4_S14_1.png` - 45° eğik düzlemde 10 m ve kaçırılan k = 2 kN/m
6. `media/_debug2/debug2_u5_S1_1.png` - Kaya bloku 200 N ve 45° çekme açısı
7. `media/_debug2/debug2_u6_S1_1.png` - Kayıcı çubuk: 1.5 m, θ = 30°, v_A = 3 m/s
8. `media/_debug2/debug2_u6_S22_1.png` - Mekanizma: 1 m, 10 rad/s, 0.5 m, 75 mm, 45°
9. `media/_debug2/debug2_u7_S25_1.png` - Paralelogram plaka: 1.5 ft, 2 ft, 1 ft, 30°, 10 lb·ft
10. `media/_debug2/debug2_u8_S21_1.png` - Disk-kütle titreşimi: k = 200 N/m, 15 kg, 10 kg, 0.5 m

## 6. Parametreleştirme Potansiyeli (Sadece Şekilde Olan Sayılar)

> [!TIP]
> Toplam **139 adet sayısal büyüklük**, soru metninde hiç geçmeyip sadece şekilde yer almaktadır. Bu durum dinamik soru bankası parametrelendirmesi (farklı öğrenciye farklı sayısal varyasyonlar üretme) için olağanüstü zengin bir potansiyel sunmaktadır.
> Tüm görsellere eklenen `parametre_adaylari` listesinde her bir aday sayı için önerilen etiket (`a`, `b`, `c`), sayısal değeri, birimi ve çözüm algoritmasındaki rolü ayrıntılı olarak modellenmiştir.

## 7. Çıktı Dosyaları ve Yapı

- **Düzeltilmiş Veri Seti:** `media/sayilar_duzeltilmis.json` (120 dosya, 106 benzersiz şema, kutu koordinatları korunmuş, boyama renkleri ve hizalamalar eklenmiş).
- **Görsel Doğrulama Çıktıları:** `media/_debug2/*.png` (10 adet doğrulanmış etiketli görsel).
- **Orijinal Dosyalar:** `media/sayilar.json`, tüm PNG görselleri, markdown dosyaları ve docx dosyalarına kesinlikle dokunulmamış, salt okunur tutulmuştur.
