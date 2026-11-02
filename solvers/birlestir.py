"""Birleşik soru bankasını (md/INM_203_Dinamik_Tum_Soru_Bankasi.md) ve README.md'yi md/ klasöründen yeniden üretir.

Çalıştır: python birlestir.py
Soru sayıları aşağıdaki SAYILAR tablosundan gelir (toplamlar ve içindekiler buradan hesaplanır).
"""
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "md"
BIRLESIK = MD / "INM_203_Dinamik_Tum_Soru_Bankasi.md"

# (no, konu, sözel soru sayısı, sayısal soru sayısı)
UNITELER = [
    (1, "Giriş ve Temel Kavramlar", 20, 0),
    (2, "Parçacığın Kinematiği", 30, 30),
    (3, "Parçacığın Kinetiği - Kuvvet ve İvme", 30, 20),
    (4, "Parçacığın Kinetiği - İş ve Enerji", 20, 20),
    (5, "Parçacığın Kinetiği - İtme ve Momentum", 10, 26),
    (6, "Rijit Cismin Düzlemsel Kinematiği", 10, 27),
    (7, "Rijit Cismin Düzlemsel Kinetiği", 11, 31),
    (8, "Mekanik Titreşimler", 18, 14),
]
SOZEL, SAYISAL = "Sözel Sorular", "Sayısal Sorular ve Çözümleri"


def dosya(no, tur):
    ad = "Sözel" if tur == SOZEL else "Sayısal"
    adaylar = sorted(MD.glob(f"Dinamik {no}. Ünite {ad} Sorular*.md"))
    if not adaylar:
        raise FileNotFoundError(f"Dinamik {no}. Ünite {ad}")
    return adaylar[0]


def anchor(s):
    """GitHub başlık bağlantısı: küçük harf; harf/işaret/rakam/_/-/boşluk dışını at; her boşluk '-' olur.
    'İ' küçültülünce i + birleşik nokta (U+0307) olur ve GitHub bunu korur."""
    s = s.lower()
    s = "".join(c for c in s if c in " -_" or unicodedata.category(c)[0] in "LMN")
    return s.replace(" ", "-")


def bolumler():
    for no, konu, soz, say in UNITELER:
        parcalar = [(SOZEL, soz)] + ([(SAYISAL, say)] if say else [])
        yield no, konu, parcalar


def birlesik():
    toplam_soz = sum(u[2] for u in UNITELER)
    toplam_say = sum(u[3] for u in UNITELER)
    out = [
        "# İNM 203 Dinamik - Tam Soru Bankası\n",
        f"> **Ders:** İNM 203 Dinamik  \n> **Toplam Soru Sayısı:** {toplam_soz + toplam_say} Soru ({toplam_soz} Sözel Test Sorusu, {toplam_say} Çözümlü Sayısal Problem)  \n> **Biçim:** Markdown + GitHub Flavored Math (LaTeX)  \n",
        "---\n",
        "## İçindekiler\n",
    ]
    for no, konu, parcalar in bolumler():
        b = f"Ünite {no}: {konu}"
        out.append(f"{no}. [{b}](#{anchor(b)})")
        for tur, n in parcalar:
            out.append(f"   - [{tur} ({n} Soru)](#{anchor(b + ' ' + tur)})")
    out.append("\n---\n")
    for no, konu, parcalar in bolumler():
        out.append(f"\n# Ünite {no}: {konu}\n")
        for tur, n in parcalar:
            out.append(f"\n## Ünite {no}: {konu} - {tur}\n")
            out.append(dosya(no, tur).read_text(encoding="utf-8").strip() + "\n")
            out.append("\n---\n")
    BIRLESIK.write_text("\n".join(out), encoding="utf-8")
    return toplam_soz, toplam_say


def readme(toplam_soz, toplam_say):
    satirlar = []
    n_bolum = 0
    for no, konu, parcalar in bolumler():
        for tur, n in parcalar:
            n_bolum += 1
            f = dosya(no, tur).name
            satirlar.append(f"| Ünite {no} | {konu} | {tur.replace('Sorular ve Çözümleri', 'Sorular ve Çözümleri')} | {n} | [md/{f}](md/{quote(f)}) |")
    tablo = "\n".join(satirlar)
    toplam = toplam_soz + toplam_say
    metin = f"""# İNM 203 Dinamik - Test Soru Bankası

Bu depo, İNM 203 Dinamik dersine ait sözel ve çözümlü sayısal test sorularının Markdown formatındaki soru bankasını ve Ünite 2–5 sayısal soruları için parametrik (dinamik) soru üreticilerini içerir.

## 📚 İçindekiler Tablosu

| Ünite | Konu | Bölüm | Soru Sayısı | Markdown Dosyası |
| :--- | :--- | :--- | :---: | :--- |
{tablo}
| **TOPLAM** | | **{n_bolum} Bölüm** | **{toplam} Soru** | |

## 📖 Birleşik Soru Bankası
Tüm ünitelerin ve {toplam} sorunun tek bir belgede toplandığı dosya: [INM_203_Dinamik_Tum_Soru_Bankasi.md](md/INM_203_Dinamik_Tum_Soru_Bankasi.md)

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
"""
    (ROOT / "README.md").write_text(metin, encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    soz, say = birlesik()
    readme(soz, say)
    print(f"Birleşik banka ve README üretildi: {soz} sözel + {say} sayısal = {soz + say}")
