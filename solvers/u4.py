"""Ünite 4 (İş ve Enerji) sayısal soru solver'ları. Çalıştır: python -I u4.py"""
import math
import sys
from pathlib import Path

from core import P, Soru, calistir

U = 4
g = 9.81
S = []


def ekle(**kw):
    S.append(Soru(unite=U, **kw))


ekle(no=1, zorluk="kolay",
     params={"a": P(500, "N", 400, 800, 50), "b": P(10, "m", 5, 20, 5)},
     metin="100 kg kütleli bir sandık, yatayla 15° açı yapan bir kablo ile {a} N'luk sabit bir kuvvet uygulanarak çekilmektedir. Kablo kuvvetinin sandığı {b} m hareket ettirdiğinde yaptığı iş ne kadardır?",
     hesap=lambda a, b: dict(ab=a * b, U=a * b * 0.966, Ukj=a * b * 0.966 / 1000),
          cevap=("U", "J", 0),
     celdirici=lambda v: [float(v["a"] * v["b"]),                                              # açı cos15 ihmal edildi
                          v["a"] * v["b"] * math.sin(math.radians(15)),                        # cos15 yerine sin15 kullanıldı
                          0.5 * v["U"],                                                        # 1/2 çarpanı eklendi
                          2 * v["U"],                                                          # 2 ile çarpıldı
                          v["a"] * v["b"] * math.tan(math.radians(15))],                       # tan15 kullanıldı
     beklenen={"U": 4830},
     cozum=r"""Sabit bir kuvvetin yaptığı iş U = F \* s \* cos(θ) formülü ile hesaplanır.

- Kuvvet (F) = {a} N

- Mesafe (s) = {b} m

- Açı (θ) = 15°

U = {a} \* {b} \* cos(15°)\
U = {ab} \* 0.966\
U = {U:.0f} J ≈ {Ukj:.2f} kJ""")

ekle(no=2, zorluk="kolay",
     params={"a": P(900, "N/m²", 300, 1500, 300), "b": P(0.2, "m", 0.1, 0.4, 0.05)},
     metin="1.5 kg kütleli bir blok, Fs = {a}s² (N) direncine sahip doğrusal olmayan bir yaya çarpmaktadır. Yayın {b} m sıkışması sırasında yay kuvvetinin yaptığı iş ne kadardır?",
     hesap=lambda a, b: dict(k3=a / 3, b3=b ** 3, U=-(a / 3) * b ** 3),
          cevap=("U", "J", 2),
     celdirici=lambda v: [(v["a"] / 3) * v["b"]**3,                                           # iş pozitif alındı (işaret hatası)
                          -v["a"] * v["b"]**3,                                                 # integral paydası 3 unutuldu
                          -(v["a"] / 2) * v["b"]**2,                                           # kuvvet s² yerine s gibi entegre edildi
                          -v["a"] * v["b"]**2,                                                 # kuvvet değeri iş sanıldı
                          (v["a"] / 3) * v["b"]**3 / 2],                                       # fazladan 1/2 çarpanı
     beklenen={"U": -2.4},   # md'deki "-24 J" hatalı: 300 * 0.008 = 2.4
     cozum=r"""Değişken bir kuvvetin yaptığı iş, kuvvetin mesafeye göre integralini alarak bulunur. Yay kuvveti harekete zıt yönde olduğu için iş negatiftir.\
U_yay = -∫ Fs ds\
U_yay = -∫₀^{b} {a}s² ds\
U_yay = -[{k3:g}s³]₀^{b}\
U_yay = -[{k3:g} \* ({b})³] = -[{k3:g} \* {b3:g}]\
U_yay = {U:.4g} J""")

ekle(no=3, zorluk="kolay",
     params={"a": P(2000, "kg", 1000, 3000, 500), "b": P(0.25, "", 0.15, 0.45, 0.05)},
     metin="{a} kg kütleli bir araba, yatay bir yolda 100 km/h (27.78 m/s) hızla giderken fren yaparak duruyor. Lastikler ile yol arasındaki kinetik sürtünme katsayısı {b} olarak verilmiştir. Arabayı durdurmak için sürtünme kuvvetinin yaptığı işi, durma mesafesi (s') cinsinden ifade ediniz. (g = 9.81 m/s²)",
     hesap=lambda a, b: dict(N=a * g, Ff=b * a * g),
          cevap=None,  # test dışı: denklem veya sembolik cevaplı (s' parametresi)
     beklenen={"Ff": 4905},
     cozum=r"""Önce sürtünme kuvvetinin büyüklüğü bulunur. Yatay düzlemde N = mg'dir.

- Normal Kuvvet (N) = {a} kg \* 9.81 m/s² = {N:.0f} N

- Sürtünme Kuvveti (Ff) = μk \* N = {b} \* {N:.0f} = {Ff:.0f} N

Sürtünme kuvveti harekete zıt olduğu için yaptığı iş negatiftir.\
U_sürtünme = -Ff \* s'\
U_sürtünme = -{Ff:.0f}s' J""")

ekle(no=4, zorluk="orta",
     params={"a": P(2000, "N/m", 1000, 4000, 500), "c": P(0.0375, "m", 0.0125, 0.04, 0.0025)},
     metin="Yay sabiti {a} N/m olan bir tabanca yayının ilk sıkışma miktarı 0.05 m'dir. Yay serbest bırakıldığında son sıkışma miktarı {c} m oluyor. Bu esnada yayın potansiyel enerjisindeki değişim ne kadardır?",
     hesap=lambda a, c: dict(Ve1=0.5 * a * 0.05 ** 2, Ve2=0.5 * a * c ** 2, dVe=0.5 * a * c ** 2 - 0.5 * a * 0.05 ** 2, h=a / 2),
          cevap=("dVe", "J", 3),
     celdirici=lambda v: [abs(v["dVe"]),                                                       # değişim pozitif alındı
                          2 * v["dVe"],                                                        # 1/2 çarpanı unutuldu
                          0.5 * v["dVe"],                                                      # fazladan 1/2 eklendi
                          0.5 * v["a"] * 0.05**2,                                              # sadece ilk potansiyel enerji alındı
                          0.5 * v["a"] * v["c"]**2],                                           # sadece son potansiyel enerji alındı
     beklenen={"dVe": -1.09375},
     sekil={"dosya": "S4_1.png", "etiketler": [("a", "k = 2 kN/m", lambda a: f"k = {a / 1000:g} kN/m")]},
     cozum=r"""Yayın potansiyel enerjisi Ve = ½ks² dir. Potansiyel enerjideki değişim, yayın yaptığı işin negatifidir.

- İlk Potansiyel Enerji (Ve₁) = ½ \* {a} \* (0.05)² = {Ve1:.4g} J

- Son Potansiyel Enerji (Ve₂) = ½ \* {a} \* ({c})² = {Ve2:.4g} J

- Potansiyel Enerji Değişimi (ΔVe) = Ve₂ - Ve₁ = {Ve2:.4g} - {Ve1:.4g} = {dVe:.4g} J""")

ekle(no=5, zorluk="kolay",
     params={"a": P(2000, "kg", 1000, 3000, 500), "b": P(100, "km/h", 60, 140, 10)},
     metin="{a} kg'lık bir arabanın kinetik enerjisi, hızı {b} km/h ({v:.2f} m/s) iken ne kadardır?",
     hesap=lambda a, b: (lambda v: dict(v=v, T=0.5 * a * v ** 2, Tkj=0.5 * a * v ** 2 / 1000, h=a / 2))(round(b / 3.6, 2)),
          cevap=("T", "J", 0),
     celdirici=lambda v: [2 * v["T"],                                                          # 1/2 çarpanı unutuldu
                          0.5 * v["a"] * v["b"]**2,                                            # km/h m/s'ye çevrilmedi
                          v["a"] * v["v"],                                                     # momentum hesaplandı (mv)
                          0.5 * v["T"],                                                        # fazladan 1/2 eklendi
                          1.5 * v["T"]],                                                       # katsayı hatası
     beklenen={"T": 771730},
     sekil={"dosya": "S5_1.png", "etiketler": [("b", "100 km/h", lambda b: f"{b:g} km/h")]},
     cozum=r"""Kinetik enerji T = ½mv² formülü ile hesaplanır.

- Kütle (m) = {a} kg

- Hız (v) = {v:.2f} m/s

T = ½ \* {a} \* ({v:.2f})²\
T = {h:g} \* {v2:.2f}\
T = {T:.0f} J ≈ {Tkj:.0f} kJ""".replace("{v2:.2f}", "{v2:.2f}"))

# Q5 çözümü v² gerektirir; hesap'a ekle
S[-1].hesap = lambda a, b: (lambda v: dict(v=v, v2=v * v, T=0.5 * a * v * v, Tkj=0.5 * a * v * v / 1000, h=a / 2))(round(b / 3.6, 2))

ekle(no=6, zorluk="orta",
     params={"a": P(70, "kg", 50, 100, 10), "b": P(46, "m", 26, 66, 5)},
     metin="{a} kg kütleli bir kayakçı, durgun halden kaymaya başlayarak B noktasına ulaşıyor. A ve B noktaları arasındaki dikey yükseklik farkı {b} m olduğuna göre, kayakçının B noktasındaki hızı nedir? (Sürtünme ihmal edilmiştir, g = 9.81 m/s²)",
     hesap=lambda a, b: dict(gh2=2 * g * b, v=math.sqrt(2 * g * b)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [math.sqrt(9.81 * v["b"]),                                            # kök içindeki 2 çarpanı unutuldu
                          2 * 9.81 * v["b"],                                                   # karekök alınmadı
                          math.sqrt(2 * 10 * v["b"]),                                          # g=10 kullanıldı
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          2 * v["v"]],                                                         # 2 ile çarpıldı
     beklenen={"v": 30.04},
     sekil={"dosya": "S6_1.png", "etiketler": [("b", [0, 31, 14, 42], lambda b: f"{b:g}m")]},
     cozum=r"""Enerjinin korunumu ilkesi kullanılır: T₁ + V₁ = T₂ + V₂. Başlangıç noktası (A) potansiyel enerji için referans (datum) alınırsa V₁ = 0. Durgun halden başladığı için T₁ = 0.\
0 + mgh = ½mv₂² + 0\
g \* h = ½ \* v₂²\
v₂ = √(2gh)\
v₂ = √(2 \* 9.81 \* {b})\
v₂ = √({gh2:.2f}) = {v:.2f} m/s""")

ekle(no=7, zorluk="kolay",
     params={"a": P(2000, "N", 1000, 4000, 500), "b": P(2, "m/s", 1, 5, 1)},
     metin="Bir motor, {a} N ağırlığındaki bir yükü {b} m/s sabit hızla yukarı kaldırıyor. Motorun çıkış gücü kaç kW'tır?",
     hesap=lambda a, b: dict(P=a * b, kW=a * b / 1000),
          cevap=("kW", "kW", 1),
     celdirici=lambda v: [0.5 * v["kW"],                                                       # 1/2 çarpanı eklendi
                          2.0 * v["kW"],                                                       # 2 ile çarpıldı
                          v["kW"] / 4,                                                         # 4'e bölündü
                          1.5 * v["kW"],                                                       # 1.5 ile çarpıldı
                          3.0 * v["kW"]],                                                      # 3 ile çarpıldı
     beklenen={"kW": 4},
     cozum=r"""Güç P = F \* v formülü ile hesaplanır. Sabit hızla kaldırmak için gereken kuvvet, yükün ağırlığına eşittir (F = {a} N).\
P_out = {a} N \* {b} m/s = {P:.0f} W = {kW:g} kW""")

ekle(no=8, zorluk="kolay",
     params={"a": P(10, "kN", 5, 20, 5), "b": P(20, "m/s", 10, 30, 5)},
     metin="{a} kN ağırlığındaki bir otomobil, 7°'lik bir yokuşu {b} m/s sabit hızla tırmanıyor. Motorun bu hızı korumak için ürettiği güç ne kadardır? (Sürtünme ihmal edilmiştir).",
     hesap=lambda a, b: dict(W=a * 1000, F=a * 1000 * 0.1219, P=a * 1000 * 0.1219 * b, Pkw=a * 1000 * 0.1219 * b / 1000),
          cevap=("P", "W", 0),
     celdirici=lambda v: [v["a"] * 1000 * v["b"],                                              # eğim açısı sin7 ihmal edildi
                          v["a"] * 1000 * math.cos(math.radians(7)) * v["b"],                  # sin7 yerine cos7 kullanıldı
                          0.5 * v["P"],                                                        # 1/2 çarpanı eklendi
                          2.0 * v["P"],                                                        # 2 ile çarpıldı
                          1.5 * v["P"]],                                                       # 1.5 ile çarpıldı
     beklenen={"P": 24380},
     cozum=r"""Sabit hızla yokuş yukarı çıkmak için motorun, ağırlığın yokuşa paralel bileşenini yenmesi gerekir.\
F = W \* sin(θ) = {W:.0f} \* sin(7°) = {W:.0f} \* 0.1219 = {F:.0f} N\
Güç:\
P = F \* v = {F:.0f} \* {b} = {P:.0f} W ≈ {Pkw:.1f} kW""")

ekle(no=9, zorluk="kolay",
     params={"a": P(0.8, "", 0.65, 0.95, 0.05), "b": P(19.5, "kW", 10.5, 28.5, 1.5)},
     metin="Verimi %{pct} (ε = {a}) olan bir motorun {b} kW'lık giriş gücü vardır. Motorun ürettiği çıkış gücü ne kadardır?",
     hesap=lambda a, b: dict(pct=norm_pct(a), Pc=a * b),
          cevap=("Pc", "kW", 2),
     celdirici=lambda v: [v["b"] / v["a"],                                                     # verime bölündü (giriş/verim)
                          (1 - v["a"]) * v["b"],                                               # kayıp güç hesaplandı
                          0.5 * v["Pc"],                                                       # 1/2 çarpanı eklendi
                          float(v["b"]),                                                       # verim %100 varsayıldı
                          2.0 * v["Pc"]],                                                      # 2 ile çarpıldı
     beklenen={"Pc": 15.6},
     cozum=r"""Verim ε = P_çıkış / P_giriş formülü ile bulunur.\
P_çıkış = ε \* P_giriş\
P_çıkış = {a} \* {b} kW\
P_çıkış = {Pc:.4g} kW""")


def norm_pct(a):
    return round(a * 100)


ekle(no=10, zorluk="orta",
     params={"a": P(20, "kg", 10, 40, 5), "b": P(18.75, "J", 12.5, 37.5, 6.25)},
     metin="Yatay düzlemdeki {a} kg'lık bir yaka, sıkıştırılmış iki yaya bağlıdır. Yayların toplam potansiyel enerjisi {b} J iken sistem serbest bırakılıyor. Yaylar tamamen gevşediğinde (potansiyel enerji sıfırlandığında) yakanın hızı ne olur?",
     hesap=lambda a, b: dict(half=a / 2, v2=b / (a / 2), v=math.sqrt(b / (a / 2))),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [math.sqrt(v["b"] / v["a"]),                                          # kütledeki 1/2 unutuldu
                          2 * v["b"] / v["a"],                                                 # karekök alınmadı (v² bulundu)
                          math.sqrt(v["a"] / (2 * v["b"])),                                    # kesir ters çevrildi
                          2 * v["v"],                                                          # 2 ile çarpıldı
                          0.5 * v["v"]],                                                       # 1/2 çarpanı eklendi
     beklenen={"v": 1.369},
     cozum=r"""Enerjinin korunumu ilkesi kullanılır: T₁ + V₁ = T₂ + V₂. Başlangıçta sistem durduğu için T₁ = 0.

- V₁ (elastik potansiyel enerji) = {b} J

- V₂ (son potansiyel enerji) = 0

- T₂ (son kinetik enerji) = ½mv₂²

0 + {b} = ½ \* ({a}) \* v₂² + 0\
{b} = {half:g} \* v₂²\
v₂² = {v2:.4g}\
v₂ = {v:.2f} m/s""")

ekle(no=11, zorluk="orta",
     params={"a": P(60, "kg", 30, 120, 10), "b": P(5, "m", 3, 10, 1), "c": P(2, "s", 1, 5, 1)},
     metin="Bir motor, {a} kg'lık bir sandığı {b} metrelik bir yüksekliğe {c} saniyede sabit hızla çıkarıyor. Motorun ortalama çıkış gücü ne kadardır? (g = 9.81 m/s²)",
     hesap=lambda a, b, c: dict(U=a * g * b, Pa=a * g * b / c, Pkw=a * g * b / c / 1000),
          cevap=("Pa", "W", 1),
     celdirici=lambda v: [v["a"] * v["b"] / v["c"],                                            # yer çekimi ivmesi unutuldu
                          v["a"] * 10 * v["b"] / v["c"],                                       # g=10 kullanıldı
                          0.5 * v["Pa"],                                                       # 1/2 çarpanı eklendi
                          2.0 * v["Pa"],                                                       # 2 ile çarpıldı
                          1.5 * v["Pa"]],                                                      # 1.5 ile çarpıldı
     beklenen={"Pa": 1471.5},
     cozum=r"""Yapılan iş, potansiyel enerjideki değişime eşittir:\
İş (U) = mgh = {a} \* 9.81 \* {b} = {U:.1f} J\
Ortalama güç, yapılan işin zamana bölünmesiyle bulunur:\
P_ort = U / t = {U:.1f} J / {c} s = {Pa:.1f} W ≈ {Pkw:.2f} kW""")

ekle(no=12, zorluk="kolay",
     params={"a": P(20, "kN", 10, 40, 5), "b": P(50, "m/s", 30, 80, 10)},
     metin="1000 kg'lık bir dragster'a {a} kN'luk sabit bir itki kuvveti uygulanıyor. Dragster {b} m/s hıza ulaştığı anda, motorun anlık gücü ne kadardır?",
     hesap=lambda a, b: dict(Fn=a * 1000, P=a * 1000 * b, PMW=a * b / 1000),
          cevap=("PMW", "MW", 2),
     celdirici=lambda v: [0.5 * v["PMW"],                                                      # 1/2 çarpanı eklendi
                          2.0 * v["PMW"],                                                      # 2 ile çarpıldı
                          1.5 * v["PMW"],                                                      # 1.5 ile çarpıldı
                          v["PMW"] / 4,                                                        # 4'e bölündü
                          3.0 * v["PMW"]],                                                     # 3 ile çarpıldı
     beklenen={"PMW": 1},
     cozum=r"""Anlık güç P = F \* v formülüyle hesaplanır.

- Kuvvet (F) = {a} kN = {Fn:.0f} N

- Hız (v) = {b} m/s

P = {Fn:.0f} N \* {b} m/s = {P:,.0f} W = {PMW:g} MW""")

ekle(no=13, zorluk="kolay",
     params={"b": P(3, "m", 1.5, 6, 0.5)},
     metin="5 gramlık (0.005 kg) bir bilye, {b} m yükseklikten serbest bırakılıyor. Tam yere çarpmadan önceki hızı nedir? (Sürtünme ihmal edilmiştir, g = 9.81 m/s²)",
     hesap=lambda b: dict(gh2=2 * g * b, v=math.sqrt(2 * g * b)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [math.sqrt(9.81 * v["b"]),                                            # kök içindeki 2 çarpanı unutuldu
                          2 * 9.81 * v["b"],                                                   # karekök alınmadı
                          math.sqrt(2 * 10 * v["b"]),                                          # g=10 kullanıldı
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          2 * v["v"]],                                                         # 2 ile çarpıldı
     beklenen={"v": 7.67},
     sekil={"dosya": "S13_1.png", "etiketler": [("b", [13, 72, 37, 87], lambda b: f"{b:g} m")]},
     cozum=r"""Enerjinin korunumu kullanılır. Başlangıçtaki potansiyel enerji, sondaki kinetik enerjiye dönüşür.\
mgh = ½mv²\
gh = ½v²\
v = √(2gh)\
v = √(2 \* 9.81 \* {b})\
v = √({gh2:.2f}) ≈ {v:.2f} m/s""")

ekle(no=14, zorluk="orta",
     params={"a": P(100, "kg", 50, 200, 25), "b": P(10, "m", 5, 20, 5)},
     metin="{a} kg'lık bir sandık, 45°'lik eğik düzlemde {b} m yukarıda durmaktadır. Sandık serbest bırakıldığında, aşağı kayarken {b} metrelik yolu kat ettiğinde yer çekimi kuvvetinin yaptığı iş ne kadardır? (g = 9.81 m/s²)",
     hesap=lambda a, b: (lambda h: dict(h=h, W=a * g, U=a * g * h))(round(b * math.sin(math.radians(45)), 2)),
          cevap=("U", "J", 0),
     celdirici=lambda v: [v["a"] * 9.81 * v["b"],                                              # eğim sin45 ihmal edildi
                          v["a"] * 10 * v["h"],                                                # g=10 kullanıldı
                          0.5 * v["U"],                                                        # 1/2 çarpanı eklendi
                          2 * v["U"],                                                          # 2 ile çarpıldı
                          1.5 * v["U"]],                                                       # 1.5 ile çarpıldı
     beklenen={"U": 6936},
     sekil={"dosya": "S14_1.png", "etiketler": [("b", "10 m", lambda b: f"{b:g} m")]},
     cozum=r"""Yer çekimi kuvvetinin yaptığı iş, dikey yer değiştirmeye bağlıdır.

- Dikey yer değiştirme (h) = {b} \* sin(45°) = {h:.2f} m

- Yapılan iş (U_g) = W \* h = (mg) \* h

U_g = ({a} \* 9.81) \* {h:.2f} = {W:.0f} \* {h:.2f} ≈ {U:.0f} J\
(Sandık aşağı hareket ettiği için iş pozitiftir.)""")

ekle(no=15, zorluk="kolay",
     params={"a": P(50, "N/m", 25, 150, 25), "c": P(245, "mm", 225, 300, 5)},
     metin="Gerilmemiş uzunluğu 200 mm ve yay sabiti {a} N/m olan bir lastik bant, {c} mm'ye kadar geriliyor. Bantta depolanan elastik potansiyel enerji ne kadardır?",
     hesap=lambda a, c: (lambda s: dict(dl=c - 200, s=s, s2=s * s, half=a / 2, Ve=0.5 * a * s * s))((c - 200) / 1000),
          cevap=("Ve", "J", 4),
     celdirici=lambda v: [2 * v["Ve"],                                                         # 1/2 çarpanı unutuldu
                          0.5 * v["a"] * (v["c"] / 1000)**2,                                   # gerilmemiş boy 200 mm çıkarılmadı
                          0.5 * v["a"] * v["s"],                                               # uzamanın karesi alınmadı
                          0.5 * v["Ve"],                                                       # fazladan 1/2 eklendi
                          3 * v["Ve"]],                                                        # 3 ile çarpıldı
     beklenen={"Ve": 0.050625},
     cozum=r"""Önce yayın ne kadar uzadığı (s) bulunur.\
s = Son uzunluk - İlk uzunluk = {c} mm - 200 mm = {dl:g} mm = {s:g} m\
Elastik potansiyel enerji: Ve = ½ks²\
Ve = ½ \* {a} \* ({s:g})²\
Ve = {half:g} \* {s2:.6g} = {Ve:.3g} J""")

ekle(no=16, zorluk="kolay",
     params={"a": P(400, "Mg", 200, 600, 100), "b": P(10, "m/s", 5, 20, 5)},
     metin="{a} Mg'lık ({kg:,} kg) bir trenin hızı, 100 saniyede düzgün bir şekilde 0'dan {b} m/s'ye çıkıyor. Bu 100 saniye boyunca trene aktarılan toplam iş (kinetik enerji değişimi) ne kadardır?",
     hesap=lambda a, b: dict(kg=a * 1000, half=a * 500, b2=b * b, Uj=a * 500 * b * b, MJ=a * 500 * b * b / 1e6),
          cevap=("MJ", "MJ", 1),
     celdirici=lambda v: [2 * v["MJ"],                                                         # 1/2 çarpanı unutuldu
                          0.5 * v["a"] * v["b"] / 1000,                                        # hızın karesi alınmadı
                          0.5 * v["MJ"],                                                       # fazladan 1/2 eklendi
                          1.5 * v["MJ"],                                                       # 1.5 ile çarpıldı
                          3 * v["MJ"]],                                                        # 3 ile çarpıldı
     beklenen={"MJ": 20},
     cozum=r"""İş-Enerji Prensibi'ne göre yapılan net iş, kinetik enerjideki değişime eşittir.\
ΣU = T₂ - T₁

- T₁ (ilk kinetik enerji) = 0 (durgun halden)

- T₂ (son kinetik enerji) = ½mv₂²

ΣU = ½ \* {kg:,} \* ({b})² - 0\
ΣU = {half:,} \* {b2} = {Uj:,.0f} J = {MJ:g} MJ""")

ekle(no=17, zorluk="kolay",
     params={"a": P(15, "kW", 10, 40, 5), "b": P(10, "m/s", 5, 20, 5)},
     metin="Bir arabanın motoru {a} kW'lık sabit bir güç üretiyor. Araba {b} m/s hıza ulaştığında, motorun tekerleklere uyguladığı itki kuvveti ne kadardır? (Verim ve sürtünme ihmal edilmiştir).",
     hesap=lambda a, b: dict(Pw=a * 1000, F=a * 1000 / b),
          cevap=("F", "N", 0),
     celdirici=lambda v: [v["a"] / v["b"],                                                     # kW Watt'a çevrilmedi
                          0.5 * v["F"],                                                        # 1/2 çarpanı eklendi
                          2.0 * v["F"],                                                        # 2 ile çarpıldı
                          1.5 * v["F"],                                                        # 1.5 ile çarpıldı
                          3.0 * v["F"]],                                                       # 3 ile çarpıldı
     beklenen={"F": 1500},
     kisit=lambda a, b: (a * 1000) % b == 0,
     cozum=r"""P = F \* v formülünden kuvvet çekilir.

- Güç (P) = {a} kW = {Pw:.0f} W

- Hız (v) = {b} m/s

F = P / v = {Pw:.0f} / {b} = {F:.0f} N""")

ekle(no=18, zorluk="kolay",
     params={"a": P(1000, "N", 500, 2000, 500), "b": P(0.5, "m", 0.25, 1, 0.25)},
     metin="Bir top, yaylı bir mekanizmadan fırlatılacaktır. Yayı sıkıştırmak için {a} N'luk bir kuvvet gerekmektedir ve yay {b} m sıkıştırılmıştır. Bu durumda yayın yay sabiti (k) nedir? (F = ks)",
     hesap=lambda a, b: dict(k=a / b),
          cevap=("k", "N/m", 0),
     celdirici=lambda v: [0.5 * v["a"] / v["b"],                                               # 1/2 çarpanı eklendi (potansiyel enerji gibi)
                          1.5 * v["a"] / v["b"],                                               # 1.5 ile çarpıldı
                          2.0 * v["a"] / v["b"],                                               # 2 ile çarpıldı
                          3.0 * v["a"] / v["b"],                                               # 3 ile çarpıldı
                          0.25 * v["a"] / v["b"]],                                             # 4'e bölündü
     beklenen={"k": 2000},
     kisit=lambda a, b: abs(a / b - round(a / b)) < 1e-9 and round(a / b) % 100 == 0,
     cozum=r"""Hooke Yasası'ndan k = F / s bulunur.

- Kuvvet (F) = {a} N

- Sıkışma (s) = {b} m

k = {a} / {b} = {k:.0f} N/m""")

ekle(no=19, zorluk="kolay",
     params={"a": P(300, "N", 100, 500, 100), "b": P(3, "m", 1, 5, 1)},
     metin="{a} N ağırlığındaki A bloğu, iki yayın üzerine düşürülüyor. Blok yaylara çarptıktan sonra en fazla {b} m'lik bir yüksekliğe geri fırlıyor. Bloğun bu yüksekliğe ulaşması için yer çekimine karşı yapılan iş ne kadardır?",
     hesap=lambda a, b: dict(Ug=a * b),
          cevap=("Ug", "J", 0),
     celdirici=lambda v: [v["a"] * 9.81 * v["b"],                                              # ağırlık kütle sanılıp g ile çarpıldı
                          0.5 * v["Ug"],                                                       # 1/2 çarpanı eklendi
                          2 * v["Ug"],                                                         # 2 ile çarpıldı
                          v["a"] / v["b"],                                                     # bölme yapıldı
                          1.5 * v["Ug"]],                                                      # 1.5 ile çarpıldı
     beklenen={"Ug": 900},
     cozum=r"""Yapılan iş, potansiyel enerji değişimine eşittir.

- Yükseklik (h) = {b} m

- Ağırlık (W) = {a} N

U_g = W \* h = {a} \* {b} = {Ug:.0f} J\
(Blok yukarı hareket ettiği için yer çekiminin yaptığı iş negatiftir, ancak bloğun yer çekimine *karşı* yaptığı iş pozitiftir.)""")

ekle(no=20, zorluk="kolay",
     params={"a": P(-1.19, "×10⁹ J", -2.19, -0.49, 0.1), "b": P(0.37, "×10⁹ J", 0.17, 0.77, 0.1)},
     metin="Bir uydu, Dünya'nın kütle çekim potansiyel enerjisi alanında hareket etmektedir. A noktasında potansiyel enerjisi {a}x10⁹ J ve kinetik enerjisi {b}x10⁹ J'dür. Uydunun A noktasındaki toplam mekanik enerjisi nedir?",
     hesap=lambda a, b: dict(E=a + b),
          cevap=("E", "×10⁹ J", 2),
     celdirici=lambda v: [v["b"] - v["a"],                                                     # potansiyel enerji çıkarıldı
                          abs(v["a"]) + v["b"],                                                # potansiyel enerji pozitif alındı
                          float(v["b"]),                                                       # sadece kinetik enerji alındı
                          float(v["a"]),                                                       # sadece potansiyel enerji alındı
                          2 * (v["a"] + v["b"])],                                              # 2 ile çarpıldı
     beklenen={"E": -0.82},
     kisit=lambda a, b: a + b < 0,
     cozum=r"""Toplam mekanik enerji, kinetik ve potansiyel enerjilerin toplamıdır.\
E = T + V\
E = ({b} \* 10⁹ J) + ({a} \* 10⁹ J)\
E = {E:.2f} \* 10⁹ J""")

if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "_out" / "u4"
    sys.exit(1 if calistir(S, out) else 0)
