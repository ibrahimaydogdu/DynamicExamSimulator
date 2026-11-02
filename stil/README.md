# İNM 203 Dinamik - Sınav Dokümanı DOCX Format ve Pandoc Stil Rehberi

Bu rehber, [VizeSınavıA.docx](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/VizeSınavıA.docx) sınav formatı temel alınarak hazırlanan **Pandoc DOCX Referans Şablonu** (`stil/sinav_stili_referans.docx`) ve kullanım yönergelerini içerir.

---

## 1. Sayfa Düzeni ve Tipografi Standartları

[VizeSınavıA.docx](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/VizeSınavıA.docx) dokümanının tüm mizanpaj ve stil parametreleri birebir çözümlenerek [stil/sinav_stili_referans.docx](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/sinav_stili_referans.docx) içine işlenmiştir:

| Parametre | Orijinal Değer (VizeSınavıA) | Açıklama |
| :--- | :---: | :--- |
| **Sayfa Boyutu** | **Letter** (8.50" x 11.00" / $21.59 \times 27.94\text{ cm}$) | 612 x 792 pt ($12240 \times 15840\text{ dxa}$) |
| **Kenar Boşlukları** | **0.50 inç** ($1.27\text{ cm}$ / 36 pt / 720 dxa) | Üst, Alt, Sol, Sağ tüm kenarlarda dar boşluk |
| **Sütun Yapısı** | **2 Sütunlu** (`w:cols num="2" space="144" sep="1"`) | Sütunlar arası $0.1\text{ inç}$ boşluk ve **dikey ayırıcı çizgi** |
| **Sütun Genişliği** | **3.70 inç** ($\approx 9.40\text{ cm}$) | Görseller bu genişliği aşmayacak şekilde ölçeklenmelidir |
| **Ana Yazı Tipi** | **Times New Roman** | Metin gövdesi, başlıklar ve şıklar |
| **Gövde Metin Boyutu** | **10.0 pt** (Kompakt Sınav Düzeni) | $1.05$ tek satır aralığı, iki yana yaslı (`w:jc val="both"`) |
| **Paragraf Boşluğu** | Öncesi 1 pt, Sonrası 2 pt | `contextualSpacing` aktif (şıklar arası gereksiz boşluk bırakmaz) |
| **Sayfa Üstbilgisi** | Ortalanmış, 10.5 pt kalın, altı çizgili | `AKDENİZ ÜNİVERSİTESİ İNŞAAT MÜHENDİSLİĞİ BÖLÜMÜ`<br>`İNM 203 Dinamik dersi, Vize sınavı` |
| **Formül Tablosu** | 2 Sütunlu kompakt grid | $9.5\text{ pt}$ Times New Roman |

---

## 2. Pandoc ile Derleme Yöntemi

Sistemde Pandoc kurulu olduğu için herhangi bir `.md` sınav metni tek komutla Word formatına dönüştürülebilir:

### Temel Terminal Komutu
```bash
pandoc stil/sinav_sablonu.md -o Sinav.docx --reference-doc=stil/sinav_stili_referans.docx --wrap=none
```

### Python Yardımcı Betiği ile Derleme
`stil/` klasöründeki [derle_sinav.py](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/derle_sinav.py) betiği ile:
```bash
python stil/derle_sinav.py stil/sinav_sablonu.md -o SinavA.docx
```

---

## 3. Sınav Markdown Yazım Kuralları

Hazırlanan [sinav_sablonu.md](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/sinav_sablonu.md) dosyasındaki standart kalıplar:

### A. Grup Başlığı
Dokümanın en başına sınav grup bilgisi eklenir (sayfa üstbilgisinde üniversite adı zaten yer aldığından gövdeye başlık tekrar yazılmaz):
```markdown
**GRUP A**
```

### B. Çoktan Seçmeli Test Sorusu
Soru numarası kalın, soru kökü sonrasında iki boşluk bırakılarak şıklar alt alta listelenir:
```markdown
**1.** Aşağıdakilerden hangisi skaler bir büyüklük örneğidir?  
a) Zaman  
b) Hız  
c) Kuvvet  
d) İvme  
e) Yer değiştirme  
```

### C. Matematiksel Denklemler
Pandoc, standart LaTeX formüllerini Word'ün yerel **OMath** denklem nesnelerine otomatik olarak dönüştürür:
- Satır içi denklem: `$v(t) = 3t^2 + 2t$` veya `$a_n = \frac{v^2}{\rho}$`
- Blok denklem:
  ```markdown
  $$
  T_1 + V_1 = T_2 + V_2
  $$
  ```

### D. Şekil ve Çizim Ekleme
2 sütunlu mizanpajda sütun genişliği **3.7 inç**tir. Görsellerin taşmaması ve orijinal sınavdaki gibi net oturması için `{width=...}` özelliği kullanılmalıdır:
```markdown
**Soru 4.** Şekildeki çuval 12 m/s yatay hızla kaymaktadır...  
![](media/Dinamik 2. Ünite Sayısal Sorular/S13_1.png){width=2.5in}  
a) 1.11 s  
b) 2.00 s  
...
```

### E. Klasik / Açık Uçlu Sorular
```markdown
**9. (Klasik Soru - 20 Puan)**  
Kütlesi $100\text{ kg}$ olan küçük bir yarış arabası sürtünmesiz pistte hareket etmektedir. Araç B noktasına ulaştığında ($g = 9.81\text{ m/s}^2$):  
a) Aracın B noktasındaki hızını ($v_B$),  
b) Pistin uyguladığı normal tepki kuvvetini ($N$),  
c) Teğetsel ivmeyi ($a_t$) hesaplayınız.  
```

### F. Formül Tablosu (Sınav Sonu)
Sayfanın sonunda 2 sütunlu tablo ile formül kağıdı formatı oluşturulur:
```markdown
### Formüller

| | |
| :--- | :--- |
| $v = \frac{ds}{dt}$ | $a = \frac{dv}{dt}$ |
| $a\,dx = v\,dv$ | $v = v_0 + a_0 t$ |
| $a_n = \frac{v^2}{\rho}$ | $\Sigma F = m \cdot a$ |
| $T = \frac{1}{2}mv^2$ | $V_g = mgh$ |
```

---

## 4. Dosya Haritası (stil/ Klasörü)

- **Referans Şablon Dosyası:** [stil/sinav_stili_referans.docx](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/sinav_stili_referans.docx) (Pandoc için 2 sütunlu, Times New Roman sınav şablonu)
- **Örnek Sınav Markdown Dosyası:** [stil/sinav_sablonu.md](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/sinav_sablonu.md) (Test ve klasik sorular içeren örnek sınav)
- **Derlenmiş Örnek DOCX Çıktısı:** [stil/sinav_ornek.docx](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/sinav_ornek.docx) (Pandoc ile üretilmiş, doğrulanmış sınav belgesi)
- **Derleme Betiği:** [stil/derle_sinav.py](file:///G:/Drive'ım/Classroom/İNM%20203%20Dinamik/TestSoruBankasi/stil/derle_sinav.py) (Tek tıkla derleme aracı)
