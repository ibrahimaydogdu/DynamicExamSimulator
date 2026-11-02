# İNM 203 Dinamik - Test Soru Bankası

Bu depo, İNM 203 Dinamik dersine ait sözel ve çözümlü sayısal test sorularının Markdown formatındaki soru bankasını ve Ünite 2–5 sayısal soruları için parametrik (dinamik) soru üreticilerini içerir.

## 📚 İçindekiler Tablosu

| Ünite | Konu | Bölüm | Soru Sayısı | Markdown Dosyası |
| :--- | :--- | :--- | :---: | :--- |
| Ünite 1 | Giriş ve Temel Kavramlar | Sözel Sorular | 20 | [md/Dinamik 1. Ünite Sözel Sorular.md](md/Dinamik%201.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 2 | Parçacığın Kinematiği | Sözel Sorular | 30 | [md/Dinamik 2. Ünite Sözel Sorular.md](md/Dinamik%202.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 2 | Parçacığın Kinematiği | Sayısal Sorular ve Çözümleri | 30 | [md/Dinamik 2. Ünite Sayısal Sorular.md](md/Dinamik%202.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 3 | Parçacığın Kinetiği - Kuvvet ve İvme | Sözel Sorular | 30 | [md/Dinamik 3. Ünite Sözel Sorular.md](md/Dinamik%203.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 3 | Parçacığın Kinetiği - Kuvvet ve İvme | Sayısal Sorular ve Çözümleri | 20 | [md/Dinamik 3. Ünite Sayısal Sorular.md](md/Dinamik%203.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 4 | Parçacığın Kinetiği - İş ve Enerji | Sözel Sorular | 20 | [md/Dinamik 4. Ünite Sözel Sorular.md](md/Dinamik%204.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 4 | Parçacığın Kinetiği - İş ve Enerji | Sayısal Sorular ve Çözümleri | 20 | [md/Dinamik 4. Ünite Sayısal Sorular.md](md/Dinamik%204.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 5 | Parçacığın Kinetiği - İtme ve Momentum | Sözel Sorular | 10 | [md/Dinamik 5. Ünite Sözel Sorular.md](md/Dinamik%205.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 5 | Parçacığın Kinetiği - İtme ve Momentum | Sayısal Sorular ve Çözümleri | 26 | [md/Dinamik 5. Ünite Sayısal Sorular.md](md/Dinamik%205.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 6 | Rijit Cismin Düzlemsel Kinematiği | Sözel Sorular | 10 | [md/Dinamik 6. Ünite Sözel Sorular.md](md/Dinamik%206.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 6 | Rijit Cismin Düzlemsel Kinematiği | Sayısal Sorular ve Çözümleri | 27 | [md/Dinamik 6. Ünite Sayısal Sorular.md](md/Dinamik%206.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 7 | Rijit Cismin Düzlemsel Kinetiği | Sözel Sorular | 11 | [md/Dinamik 7. Ünite Sözel Sorular..md](md/Dinamik%207.%20%C3%9Cnite%20S%C3%B6zel%20Sorular..md) |
| Ünite 7 | Rijit Cismin Düzlemsel Kinetiği | Sayısal Sorular ve Çözümleri | 31 | [md/Dinamik 7. Ünite Sayısal Sorular.md](md/Dinamik%207.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| Ünite 8 | Mekanik Titreşimler | Sözel Sorular | 18 | [md/Dinamik 8. Ünite Sözel Sorular.md](md/Dinamik%208.%20%C3%9Cnite%20S%C3%B6zel%20Sorular.md) |
| Ünite 8 | Mekanik Titreşimler | Sayısal Sorular ve Çözümleri | 14 | [md/Dinamik 8. Ünite Sayısal Sorular.md](md/Dinamik%208.%20%C3%9Cnite%20Say%C4%B1sal%20Sorular.md) |
| **TOPLAM** | | **15 Bölüm** | **317 Soru** | |

## 📖 Birleşik Soru Bankası
Tüm ünitelerin ve 317 sorunun tek bir belgede toplandığı dosya: [INM_203_Dinamik_Tum_Soru_Bankasi.md](md/INM_203_Dinamik_Tum_Soru_Bankasi.md)

## 🎲 Dinamik (Parametrik) Sorular
Ünite 2–5 sayısal soruları (toplam 96) için her soruya ait Python çözücüsü bulunur. Çözücü; sayıları rastgele ama sade değerlerden seçer, soru metnini, çözümü ve şekil üzerindeki etiketleri yeniden üretir. Tüm sorular birbirinden bağımsızdır (zincirli sorular parçalandı).

| Ünite | Dosya | Soru |
| :--- | :--- | :---: |
| Ünite 2 | [solvers/u2.py](solvers/u2.py) | 30 |
| Ünite 3 | [solvers/u3.py](solvers/u3.py) | 20 |
| Ünite 4 | [solvers/u4.py](solvers/u4.py) | 20 |
| Ünite 5 | [solvers/u5.py](solvers/u5.py) | 26 |

- Doğrulama ve örnek üretim: `cd solvers && python u2.py` (her soru için orijinal değerlerle md metni ve sonuç karşılaştırılır; örnek varyantlar `solvers/_out/` altına yazılır).
- Çekirdek: [solvers/core.py](solvers/core.py); şematik şekiller: [solvers/cizimler.py](solvers/cizimler.py).
- Zorluk sınıflandırması: [zorluk_tablosu.md](zorluk_tablosu.md) (Kolay / Orta / Zor).
- Bu dosyayı ve birleşik bankayı yeniden üretmek için: `python solvers/birlestir.py`.

## 📝 Sınav Üretimi
Vize sınavı ve cevap anahtarı üretici: [solvers/sinav_uret.py](solvers/sinav_uret.py). Varsayılan yapı (15 sorunun 14'ü; 15. soru klasik, elle eklenir): 4 sözel çoktan seçmeli, 5 sayısal çoktan seçmeli, 5 boşluk doldurmalı (hata payı %5; %5–%10 arası yarım puan).
```bash
cd solvers
python sinav_uret.py --grup A,B --seed 1 --ad vize
python sinav_uret.py --sozel 1,2,1 --secmeli 2,2,1 --bosluk 1,2,2   # kolay,orta,zor sayıları
python sinav_uret.py --grup A,B,C,D --tarih 05.11.2026 --ad vize_final   # 4 gruplu optik formlu sınav
```
Çıktı `sinavlar/<ad>/` altına yazılır (`sinav_A.docx`, `cevap_anahtari_A.docx`, şekiller). Sayfa düzeni [stil/](stil/) içindeki Pandoc şablonundan gelir ([stil/docx_style_rehberi.md](stil/docx_style_rehberi.md)). Gruplar aynı soruları farklı sayılarla ve farklı şık sırasıyla alır. Sözel sorular [solvers/sozel.py](solvers/sozel.py) ile md dosyalarından okunur.

## 🖥️ Sınav Simülatörü (tarayıcıda)
[docs/index.html](docs/index.html): Python çözücüleri tarayıcıda (Pyodide) çalıştırarak rastgele deneme sınavı üretir; süreli, otomatik puanlamalı, çözümlü, "PDF olarak kaydet" destekli. Sunucu gerekmez; GitHub Pages ile yayınlanır (Settings → Pages → Branch: main, klasör: /docs).
Çözücüler veya sorular değişirse paketi yeniden üretin: `python solvers/web_paketle.py` (docs/paket.zip).

## 📁 Klasör Yapısı
- `md/`: Tüm ünite soru bankası Markdown dosyaları (`.md`) ve birleşik banka.
- `media/`: Sorulara ait problem diyagramları (`S<soru_no>_<sıra>.png`) ve şekil üzerindeki sayıların konumları (`sayilar_duzeltilmis.json`).
- `solvers/`: Parametrik soru çözücüleri, sınav üretici ve üretilen örnekler.
- `stil/`: Sınav sayfa düzeni (Pandoc DOCX şablonu) ve rehberi.
- `sinavlar/`: Üretilen sınavlar.

## ⚙️ Teknik Özellikler
- **Matematik Denklemleri:** LaTeX formatında `$inline$` ve `$$display$$` olarak kodlanmıştır.
- **Görsel Yolları:** Göreli yol (`![](../media/<ünite>/S...png)`) kullanılmıştır.
- **Şık Formatı:** Tüm sözel sorularda standart `- A)`, `- B)` liste biçimi uygulanmıştır.
- **Birimler:** Sayısal sorular metrik (SI) birimlerle yazılmıştır.
