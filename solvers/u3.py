"""Ünite 3 (Kuvvet ve İvme) sayısal soru solver'ları. Çalıştır: python u3.py"""
import math
import sys
from pathlib import Path

from core import P, Soru, calistir

U = 3
g = 9.81
S = []


def ekle(**kw):
    S.append(Soru(unite=U, **kw))


ekle(no=1, zorluk="orta",
     params={"m": P(3000, "kg", 2000, 4000, 500), "v": P(0.2, "m/s", 0.1, 0.5, 0.1), "t": P(0.3, "s", 0.1, 0.5, 0.1)},
     metin="Başlangıçta durmakta olan {m} kg'lık bir döküm parçası, sabit bir ivme ile {t} saniyede {v} m/s'lik bir hıza ulaştırılıyor. Parçanın ivmesi nedir?",
     hesap=lambda m, v, t: dict(a=v / t),
          cevap=("a", "m/s²", 3),
     celdirici=lambda v: [v["v"] * v["t"],                                                     # v·t yapıldı (çarpma)
                          v["v"] / v["t"]**2,                                                 # v/t² yapıldı
                          0.5 * v["v"] / v["t"],                                               # 1/2 çarpanı eklendi
                          2 * v["v"] / v["t"],                                                 # 2 ile çarpıldı
                          0.75 * v["v"] / v["t"]],                                             # katsayı hatası
     beklenen={"a": 0.667},
     cozum=r"""Bu bir kinematik problemidir. Sabit ivmeli hareket denklemlerinden biri kullanılır.\
Verilenler:

- Başlangıç hızı (v₀) = 0 m/s (durgun halden)

- Son hız (v) = {v} m/s

- Süre (t) = {t} s

Kullanılacak denklem: v = v₀ + a\*t\
{v} = 0 + a \* ({t})\
a = {v} / {t}\
a = {a:.3f} m/s²""")

ekle(no=2, zorluk="orta",
     params={"M": P(160, "Mg", 120, 200, 20), "a": P(196200, "N", 180000, 220000, 10000), "b": P(155440, "N", 140000, 160000, 5000)},
     metin="{M} Mg ({kg:,} kg) kütleli bir tren, eğimli bir yolda yukarı doğru hareket etmektedir. Motorun uyguladığı çekiş kuvveti {a:,} N ve eğimden dolayı trene etki eden yer çekimi kuvvetinin bileşeni {b:,} N'dur. Trenin ivmesi nedir? (Sürtünme ihmal edilmiştir).",
     hesap=lambda M, a, b: dict(kg=M * 1000, dF=a - b, acc=(a - b) / (M * 1000)),
          cevap=("acc", "m/s²", 2),
     celdirici=lambda v: [(v["a"] + v["b"]) / (v["M"] * 1000),                                 # kuvvetler çıkarılmak yerine toplandı
                          v["a"] / (v["M"] * 1000),                                           # yer çekimi bileşeni ihmal edildi
                          v["b"] / (v["M"] * 1000),                                           # motor çekiş kuvveti ihmal edildi
                          v["acc"] / 2,                                                       # ivme yarıya bölündü
                          2 * v["acc"]],                                                      # ivme 2 ile çarpıldı
     beklenen={"acc": 0.25475},
     kisit=lambda M, a, b: a > b and 0.05 < (a - b) / (M * 1000) < 1.0,
     cozum=r"""Newton'un İkinci Yasası (ΣF = m\*a) kullanılır.\
Verilenler:

- Kütle (m) = {kg:,} kg

- Çekiş Kuvveti (F_çekiş) = {a:,} N

- Yer çekimi bileşeni (F_g) = {b:,} N (harekete ters yönde)

Yokuş yukarı yönde net kuvvet:\
ΣF = F_çekiş - F_g\
ΣF = {a:,} - {b:,} = {dF:,} N

Şimdi ivmeyi bulalım:\
a = ΣF / m\
a = {dF:,} / {kg:,}\
a ≈ {acc:.2f} m/s²""")

ekle(no=3, zorluk="kolay",
     params={"m": P(10, "kg", 5, 20, 5)},
     metin="30°'lik eğik düzlem üzerinde duran {m} kg'lık A bloğuna etki eden normal kuvvet ne kadardır? (g = 9.81 m/s²)",
     hesap=lambda m: dict(W=m * g, N=m * g * 0.866),
          cevap=("N", "N", 2),
     celdirici=lambda v: [v["m"] * 9.81 * 0.5,                                                # cos30 yerine sin30 kullanıldı
                          v["m"] * 9.81,                                                      # eğim ihmal edildi (mg alındı)
                          v["m"] * 10 * 0.866,                                                # g=10 kullanıldı
                          v["m"] * 9.81 / 0.866,                                              # cos30'a bölündü
                          v["m"] * 9.81 * math.tan(math.radians(30))],                        # tan30 kullanıldı
     beklenen={"N": 84.96},
     cozum=r"""Normal kuvvet, yüzeye dik olan kuvvetlerin dengesinden bulunur. Serbest cisim diyagramında, ağırlığın (mg) yüzeye dik bileşeni normal kuvvete eşittir.\
Verilenler:

- Kütle (m) = {m} kg

- Eğim açısı (θ) = 30°

- Yer çekimi ivmesi (g) = 9.81 m/s²

N = mg \* cos(θ)\
N = {m} \* 9.81 \* cos(30°)\
N = {W:.1f} \* 0.866\
N = {N:.2f} N""")

ekle(no=4, zorluk="kolay",
     params={"W": P(100, "N", 50, 200, 50)},
     metin="30°'lik eğik düzlemde sabit hızla aşağı kayan {W} N ağırlığındaki bir bloğa etki eden kinetik sürtünme kuvveti ne kadardır?",
     hesap=lambda W: dict(Fs=W * 0.5),
          cevap=("Fs", "N", 1),
     celdirici=lambda v: [v["W"] * math.cos(math.radians(30)),                                # sin30 yerine cos30 kullanıldı
                          float(v["W"]),                                                      # toplam ağırlık alındı
                          0.25 * v["W"],                                                      # 1/4 katsayısı kullanıldı
                          v["W"] * math.tan(math.radians(30)),                                # tan30 kullanıldı
                          0.75 * v["W"]],                                                     # katsayı hatası
     beklenen={"Fs": 50},
     cozum=r"""Blok "sabit hızla" hareket ettiği için ivme sıfırdır (a=0). Bu, net kuvvetin de sıfır olduğu anlamına gelir (ΣF=0). Eğim boyunca aşağı yönde hareket olduğundan, sürtünme kuvveti yukarı yöndedir.\
Ağırlığın eğime paralel bileşeni:\
W_paralel = W \* sin(θ) = {W} \* sin(30°) = {W} \* 0.5 = {Fs:g} N\
Net kuvvetin sıfır olması için sürtünme kuvveti bu kuvvete eşit olmalıdır:\
F_sürtünme = W_paralel = {Fs:g} N""")

ekle(no=5, zorluk="orta",
     params={"F": P(2, "kN", 1, 4, 1)},
     metin="Bir römorkör, her biri {F} kN'luk su direncine maruz kalan üç özdeş barcı sabit hızla çekmektedir. Sadece son barç düşünüldüğünde, ikinci ve üçüncü barç arasındaki kablodaki gerilme kuvveti nedir?",
     hesap=lambda F: dict(T=F),
          cevap=("T", "kN", 1),
     celdirici=lambda v: [3.0 * v["F"],                                                       # 3 barcın toplam direnci alındı
                          2.0 * v["F"],                                                       # 2 barcın direnci alındı
                          v["F"] / 3,                                                         # 3'e bölündü
                          v["F"] / 2,                                                         # 2'ye bölündü
                          4.0 * v["F"]],                                                      # 4 ile çarpıldı
     beklenen={"T": 2},
     sekil={"dosya": "S5_1.png", "etiketler": [("F", "*2 kN", lambda F: f"{F:g} kN")]},
     cozum=r"""Sistem "sabit hızla" hareket ettiğinden, her bir parçası için net kuvvet sıfırdır. Sadece üçüncü (en sondaki) barç için serbest cisim diyagramı çizilirse:

- İleri yönde kablo gerilmesi (T)

- Geri yönde su direnci (F_direnç = {F} kN)\
  Net kuvvetin sıfır olması için:\
  ΣF = T - F_direnç = 0\
  T = F_direnç = {T:g} kN""")

ekle(no=6, zorluk="kolay",
     params={"m": P(3500, "kg", 2000, 5000, 500), "a": P(4, "m/s²", 2, 6, 1)},
     metin="Bir vinç, {m} kg'lık bir motoru {a} m/s²'lik sabit bir ivme ile yukarı doğru kaldırmaktadır. Motoru tutan dikey kablodaki gerilme kuvveti nedir? (g = 9.81 m/s²)",
     hesap=lambda m, a: dict(ag=a + g, T=m * (a + g)),
          cevap=("T", "N", 0),
     celdirici=lambda v: [v["m"] * (9.81 - v["a"]),                                           # ivme çıkarıldı (aşağı yönlü varsayıldı)
                          v["m"] * 9.81,                                                      # ivme ihmal edildi (sadece mg)
                          v["m"] * v["a"],                                                    # yer çekimi ihmal edildi (sadece ma)
                          v["m"] * (v["a"] + 10),                                             # g=10 kullanıldı
                          2 * v["T"]],                                                        # 2 katı alındı
     beklenen={"T": 48335},
     cozum=r"""Newton'un İkinci Yasası (ΣF = m\*a) dikey yönde uygulanır.\
Verilenler:

- Kütle (m) = {m} kg

- İvme (a) = {a} m/s² (yukarı yönlü)\
  Yukarı yönde net kuvvet:\
  ΣF_y = T - mg\
  T - mg = m\*a\
  T = m\*a + mg = m \* (a + g)\
  T = {m} \* ({a} + 9.81)\
  T = {m} \* {ag:.2f}\
  T = {T:,.0f} N""")

ekle(no=7, zorluk="orta",
     params={"rho": P(200, "m", 100, 400, 100), "an": P(4.25, "m/s²", 2, 6, 1)},
     metin="Dikey düzlemde hareket eden 50 kg'lık bir merminin yörüngesinin eğrilik yarıçapı {rho} m'dir. Şekildeki konumda (eğim 30°) mermiye etki eden normal ivme {an} m/s² olduğuna göre, merminin hızı nedir?",
     hesap=lambda rho, an: dict(v2=an * rho, v=math.sqrt(an * rho)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [v["an"] * v["rho"],                                                 # karekök alınmadı (v² hesaplandı)
                          math.sqrt(v["an"] * v["rho"] * math.cos(math.radians(30))),         # eğim açısı cos30 ile çarpıldı
                          math.sqrt(v["rho"] / v["an"]),                                      # rho / an yapıldı
                          2 * math.sqrt(v["an"] * v["rho"]),                                  # fazladan 2 ile çarpıldı
                          0.5 * math.sqrt(v["an"] * v["rho"])],                               # 1/2 çarpanı eklendi
     beklenen={"v": 29.15},
     cozum=r"""Normal ivme formülü a_n = v²/ρ kullanılır.\
Verilenler:

- Normal ivme (a_n) = {an} m/s²

- Eğrilik yarıçapı (ρ) = {rho} m\
  Formülden hızı (v) çekelim:\
  v² = a_n \* ρ\
  v = √(a_n \* ρ)\
  v = √({an} \* {rho})\
  v = √{v2:g}\
  v ≈ {v:.2f} m/s""")

ekle(no=8, zorluk="orta",
     params={},
     metin="Dikey düzlemde hareket eden bir mermiye sadece yer çekimi kuvveti etki etmektedir. Yörüngesinin teğetinin yatayla 30° açı yaptığı bir anda, merminin teğetsel ivmesi nedir? (g = 9.81 m/s²)",
     hesap=lambda: dict(at=-g * 0.5),
          cevap=("at", "m/s²", 3),
     celdirici=lambda v: [-9.81 * math.cos(math.radians(30)),                                 # sin30 yerine cos30 kullanıldı
                          9.81 * 0.5,                                                         # işaret pozitif alındı
                          -10 * 0.5,                                                          # g=10 kullanıldı
                          -9.81,                                                              # açı ihmal edildi (-g alındı)
                          -9.81 * math.tan(math.radians(30))],                                # tan30 kullanıldı
     beklenen={"at": -4.905},
     cozum=r"""Teğetsel ivme, net kuvvetin hareket yönündeki (teğet) bileşeninden kaynaklanır. Tek kuvvet olan yer çekimi (mg) düşey aşağı yönlüdür. Bu kuvvetin teğet bileşeni bulunur.\
ΣF_t = m \* a_t\
-mg \* sin(30°) = m \* a_t\
a_t = -g \* sin(30°)\
a_t = -9.81 \* 0.5\
a_t = {at:.3f} m/s² (Negatif işaret hızın azaldığını gösterir)""")

ekle(no=9, zorluk="kolay",
     params={"rho": P(100, "m", 50, 200, 50), "v": P(20, "m/s", 10, 30, 5)},
     metin="{rho} m yarıçaplı dairesel bir pistte hareket eden bir aracın hızı {v} m/s'dir. Aracın merkezcil (normal) ivmesi nedir?",
     hesap=lambda rho, v: dict(v2=v * v, an=v * v / rho),
          cevap=("an", "m/s²", 1),
     celdirici=lambda v: [v["v"] / v["rho"],                                                  # hızın karesi alınmadı (v/rho)
                          float(v["v"]**2),                                                   # yarıçapa bölünmedi
                          2 * v["v"]**2 / v["rho"],                                           # 2 ile çarpıldı
                          0.5 * v["v"]**2 / v["rho"],                                         # 1/2 çarpanı eklendi
                          3 * v["v"]**2 / v["rho"]],                                          # 3 ile çarpıldı
     beklenen={"an": 4},
     cozum=r"""Merkezcil ivme (normal ivme) formülü a_n = v²/ρ kullanılır.\
Verilenler:

- Hız (v) = {v} m/s

- Yarıçap (ρ) = {rho} m\
  a_n = ({v})² / {rho}\
  a_n = {v2} / {rho}\
  a_n = {an:g} m/s²""")

ekle(no=10, zorluk="orta",
     params={"m": P(30, "kg", 20, 50, 10), "v": P(4, "m/s", 2, 6, 1), "r": P(4, "m", 2, 6, 1)},
     metin="{r} metre uzunluğundaki bir ipe bağlı {m} kg'lık bir top, en alt noktasından {v} m/s hızla geçiyor. Bu anda ipteki gerilme kuvveti ne kadardır? (g = 9.81 m/s²)",
     hesap=lambda m, v, r: dict(mg=m * g, v2r=v * v / r, ma=m * v * v / r, T=m * g + m * v * v / r),
          cevap=("T", "N", 1),
     celdirici=lambda v: [v["m"] * 9.81 - v["m"] * v["v"]**2 / v["r"],                        # merkezcil kuvvet çıkarıldı
                          v["m"] * v["v"]**2 / v["r"],                                        # yer çekimi ihmal edildi
                          v["m"] * 9.81,                                                      # merkezcil kuvvet ihmal edildi
                          v["m"] * 10 + v["m"] * v["v"]**2 / v["r"],                          # g=10 kullanıldı
                          v["m"] * 9.81 + v["v"]**2 / v["r"]],                                # merkezcil kuvvette kütle unutuldu
     beklenen={"T": 414.3},
     sekil={"dosya": "S10_1.png", "etiketler": [("r", "4 m", lambda r: f"{r:g} m")]},
     cozum=r"""En alt noktada, normal ivme yukarı doğrudur. Net kuvvet denklemi dikey yönde yazılır.\
ΣF_n = m \* a_n\
T - mg = m \* (v²/r)\
T = mg + m \* (v²/r)\
Verilenler:

- Kütle (m) = {m} kg

- Hız (v) = {v} m/s

- Yarıçap (r) = {r} m\
  T = ({m} \* 9.81) + {m} \* ({v}² / {r})\
  T = {mg:.1f} + {m} \* ({v2r:g})\
  T = {mg:.1f} + {ma:.1f}\
  T = {T:.1f} N""")

ekle(no=11, zorluk="orta", md_kontrol=False,
     params={"r": P(100, "m", 50, 200, 50)},
     metin="Bir araba dikey bir tepenin zirvesinden (yarıçap r = {r} m) geçmektedir. Arabanın yolla temasını kaybetmemesi için sahip olabileceği maksimum hız nedir? (g = 9.81 m/s²)",
     hesap=lambda r: dict(gr=g * r, v=math.sqrt(g * r)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [9.81 * v["r"],                                                      # karekök alınmadı (v² hesaplandı)
                          math.sqrt(10 * v["r"]),                                             # g=10 kullanıldı
                          math.sqrt(2 * 9.81 * v["r"]),                                       # 2gr formülü ile karıştırıldı
                          0.5 * math.sqrt(9.81 * v["r"]),                                     # 1/2 çarpanı eklendi
                          2 * math.sqrt(9.81 * v["r"])],                                      # 2 ile çarpıldı
     beklenen={"v": 31.32},
     cozum=r"""Yolla temasın tam kesilme anında, yüzeyin normal kuvveti (N) sıfır olur. Bu durumda, merkezcil kuvveti sağlayan tek kuvvet ağırlıktır (mg).\
ΣF_n = m \* a_n\
mg = m \* (v_max² / r)\
g = v_max² / r\
v_max² = gr = 9.81 \* {r} = {gr:.1f}\
v_max = √(gr) = {v:.2f} m/s""")

ekle(no=12, zorluk="orta",
     params={"r": P(0.6, "m", 0.3, 1.2, 0.3), "w": P(2, "rad/s", 1, 5, 1)},
     metin="Yatay düzlemde dönen bir çubuğa takılı 0.5 kg'lık bir bilezik, merkezden {r} m uzaktadır. Çubuğun açısal hızı {w} rad/s ise, bileziğe etki eden merkezcil ivme (radyal ivme) nedir?",
     hesap=lambda r, w: dict(w2=w * w, ar=-r * w * w, mag=r * w * w),
          cevap=("mag", "m/s²", 2),
     celdirici=lambda v: [v["r"] * v["w"],                                                    # hız hesaplandı (r·ω)
                          float(v["w"]**2),                                                   # yarıçap r unutuldu
                          v["r"] / v["w"]**2,                                                 # r / ω² yapıldı
                          2 * v["r"] * v["w"]**2,                                             # 2 ile çarpıldı
                          0.5 * v["r"] * v["w"]**2],                                          # 1/2 çarpanı eklendi
     beklenen={"mag": 2.4},
     sekil={"dosya": "S12_1.png", "etiketler": [("r", "0.6 m", lambda r: f"{r:g} m")]},
     cozum=r"""Kutupsal koordinatlarda radyal ivme formülü a_r = r̈ - rθ̇² dir. Bilezik sabit bir konumda (r={r} m) olduğu için ṙ ve r̈ sıfırdır.

Verilenler:

- r = {r} m

- Açısal hız (θ̇) = {w} rad/s\
  a_r = 0 - ({r}) \* ({w})²\
  a_r = -{r} \* {w2}\
  a_r = {ar:.2f} m/s²\
  Büyüklüğü {mag:.2f} m/s²'dir ve merkeze doğrudur.""")

ekle(no=13, zorluk="orta",
     params={"v": P(15, "m/s", 10, 30, 5), "s": P(10, "m", 5, 20, 5)},
     metin="2 Mg'luk (2000 kg) bir kamyon {v} m/s hızla giderken fren yaparak {s} metrede duruyor. Kamyonun yavaşlama ivmesinin büyüklüğü nedir?",
     hesap=lambda v, s: dict(v2=v * v, a2=2 * s, a=-v * v / (2 * s), amag=v * v / (2 * s)),
          cevap=("amag", "m/s²", 2),
     celdirici=lambda v: [v["v"]**2 / v["s"],                                                 # 2a·s formülündeki 2 unutuldu
                          v["v"] / (2 * v["s"]),                                              # hızın karesi alınmadı
                          v["v"] / v["s"],                                                    # kare alınmadı ve 2 unutuldu
                          3 * v["v"]**2 / (2 * v["s"]),                                       # katsayı hatası
                          0.5 * v["v"]**2 / (2 * v["s"])],                                    # fazladan 2'ye bölündü
     beklenen={"amag": 11.25},
     cozum=r"""Zamandan bağımsız kinematik denklemi kullanılır: v² = v₀² + 2a(s - s₀)\
Verilenler:

- Başlangıç hızı (v₀) = {v} m/s

- Son hız (v) = 0 m/s (duruyor)

- Mesafe (s - s₀) = {s} m\
  0² = {v}² + 2 \* a \* {s}\
  0 = {v2} + {a2}a\
  -{v2} = {a2}a\
  a = -{v2} / {a2} = {a:.2f} m/s²\
  İvmenin büyüklüğü {amag:.2f} m/s²'dir.""")

ekle(no=14, zorluk="zor",
     params={"W": P(300, "N", 200, 600, 100), "F": P(150, "N", 100, 300, 50)},
     metin="A bloğu {W} N ağırlığındadır. Şekildeki makara sisteminde kordona {F} N'luk bir kuvvet uygulanıyor. A bloğuna etki eden net kuvvet nedir? (Makara ağırlıkları ihmal edilmiştir).",
     hesap=lambda W, F: dict(Fup=4 * F, net=4 * F - W),
          cevap=("net", "N", 1),
     celdirici=lambda v: [(4 * v["F"] - v["W"]) * 0.5,                                        # 2'ye bölündü
                          (4 * v["F"] - v["W"]) * 1.5,                                        # katsayı hatası
                          (4 * v["F"] - v["W"]) * 2.0,                                        # 2 ile çarpıldı
                          (4 * v["F"] - v["W"]) * 2.5,                                        # katsayı hatası
                          4.0 * v["F"]],                                                      # ağırlık çıkarılması unutuldu
     beklenen={"net": 300},
     kisit=lambda W, F: 4 * F > W,
     cozum=r"""Uygulanan {F} N'luk kuvvet, kordon boyunca her yerde aynı gerilmeyi oluşturur (T = {F} N). Şekilde {F} N'luk kuvvet iki makara aşamasında ikiye katlanarak A bloğunu çeken kablolar üzerinde toplam 4F = 4 \* {F} = {Fup} N'luk yukarı yönlü kuvvet oluşturur. A bloğunun ağırlığı {W} N'dur.\
ΣF = F_yukarı - W_aşağı = {Fup} - {W} = {net} N (yukarı)""")

ekle(no=15, zorluk="zor", params={},
     metin="Şekildeki A arabasının üzerinde duran B bloğu sürtünmesiz yüzeyden aşağı kaymaktadır. B bloğunun kütlesi 'm' ise, B bloğuna arabanın yüzeyi tarafından uygulanan normal kuvvet (N_B) nedir? (Açı θ)",
     hesap=lambda: dict(),
          cevap=None,  # test dışı: denklem veya sembolik cevaplı (N_B = mg * cos(θ))
     cozum=r"""B bloğunun serbest cisim diyagramı çizilir. Yüzeye dik doğrultuda ivme olmadığı varsayılır (kayma hareketi yüzeye paraleldir). Bu doğrultudaki kuvvetler dengededir.\
ΣF_dik = 0\
N_B - mg \* cos(θ) = 0\
N_B = mg \* cos(θ)""")

ekle(no=16, zorluk="orta",
     params={"m": P(500, "kg", 300, 800, 100), "F": P(6000, "N", 5000, 9000, 1000)},
     metin="{m} kg'lık bir balona {F} N'luk bir kaldırma kuvveti etki ediyor. Balonun başlangıçtaki (hava direnci yokken) yukarı yönlü ivmesi nedir? (g = 9.81 m/s²)",
     hesap=lambda m, F: dict(W=m * g, dF=F - m * g, a=(F - m * g) / m),
          cevap=("a", "m/s²", 2),
     celdirici=lambda v: [v["F"] / v["m"],                                                    # yer çekimi kuvveti ihmal edildi
                          (v["F"] - v["m"] * 10) / v["m"],                                    # g=10 kullanıldı
                          (v["F"] + v["m"] * 9.81) / v["m"],                                  # ağırlık çıkarılmak yerine toplandı
                          2 * (v["F"] - v["m"] * 9.81) / v["m"],                              # 2 ile çarpıldı
                          0.5 * (v["F"] - v["m"] * 9.81) / v["m"]],                           # 1/2 çarpanı eklendi
     beklenen={"a": 2.19},
     kisit=lambda m, F: F > m * g,
     sekil={"dosya": "S16_1.png", "etiketler": [("F", [104, 116, 164, 131], lambda F: f"F = {F / 1000:g} kN")]},
     cozum=r"""Newton'un İkinci Yasası (ΣF = m\*a) dikey yönde uygulanır.\
Verilenler:

- Kütle (m) = {m} kg

- Kaldırma kuvveti (F_kaldırma) = {F} N\
  ΣF_y = F_kaldırma - mg\
  ΣF_y = {F} - ({m} \* 9.81)\
  ΣF_y = {F} - {W:.0f} = {dF:.0f} N\
  a = ΣF_y / m = {dF:.0f} / {m}\
  a = {a:.2f} m/s²""")

ekle(no=17, zorluk="orta",
     params={"m": P(0.2, "kg", 0.1, 0.5, 0.1), "v": P(0.5, "m/s", 0.5, 2, 0.5)},
     metin="{m} kg'lık bir blok, pürüzsüz bir koni yüzeyinde 0.120 m'lik bir yarıçapta {v} m/s'lik sabit bir hızla dönmektedir. Bloğa etki eden net merkezcil kuvvet ne kadardır?",
     hesap=lambda m, v: dict(v2=v * v, an=v * v / 0.12, F=m * v * v / 0.12),
          cevap=("F", "N", 3),
     celdirici=lambda v: [v["v"]**2 / 0.12,                                                   # kütle unutuldu (ivme verildi)
                          2 * v["m"] * v["v"]**2 / 0.12,                                      # 2 ile çarpıldı
                          0.5 * v["m"] * v["v"]**2 / 0.12,                                    # 1/2 çarpanı eklendi
                          v["m"] * v["v"]**2 * 0.12,                                          # r'ye bölünmek yerine r ile çarpıldı
                          3 * v["m"] * v["v"]**2 / 0.12],                                     # 3 ile çarpıldı
     beklenen={"F": 0.41667},
     cozum=r"""Net merkezcil kuvvet F_n = m \* a_n = m \* (v²/r) formülüyle bulunur.\
Verilenler:

- Kütle (m) = {m} kg

- Hız (v) = {v} m/s

- Yarıçap (r) = 0.120 m\
  F_n = {m} \* ({v}² / 0.120)\
  F_n = {m} \* ({v2:g} / 0.120)\
  F_n = {m} \* {an:.4f}\
  F_n ≈ {F:.3f} N""")

ekle(no=18, zorluk="kolay",
     params={"v": P(97, "m/s", 60, 120, 10), "r": P(3000, "m", 2000, 5000, 1000)},
     metin="5000 kg'lık bir uçak, {r} m yarıçaplı yatay bir dairesel yörüngede {v} m/s'lik sabit bir hızla uçmaktadır. Uçağın maruz kaldığı merkezcil ivme nedir?",
     hesap=lambda v, r: dict(v2=v * v, an=v * v / r),
          cevap=("an", "m/s²", 2),
     celdirici=lambda v: [v["v"] / v["r"],                                                    # hızın karesi alınmadı (v/r)
                          2 * v["v"]**2 / v["r"],                                             # 2 ile çarpıldı
                          0.5 * v["v"]**2 / v["r"],                                           # 1/2 çarpanı eklendi
                          v["v"]**2 / (2 * v["r"]),                                           # fazladan 2'ye bölündü
                          3 * v["v"]**2 / v["r"]],                                            # 3 ile çarpıldı
     beklenen={"an": 3.136},
     cozum=r"""Merkezcil ivme a_n = v²/r formülüyle bulunur.\
Verilenler:

- Hız (v) = {v} m/s

- Yarıçap (r) = {r} m\
  a_n = {v}² / {r}\
  a_n = {v2} / {r}\
  a_n ≈ {an:.2f} m/s²""")

ekle(no=19, zorluk="orta",
     params={"mu": P(0.3, "", 0.2, 0.4, 0.05), "N": P(664, "N", 500, 800, 50)},
     metin="80 kg'lık bir sandık, yatayla 20°'lik açı yapan bir zincirle çekilmektedir. Kinetik sürtünme katsayısı μk = {mu} olarak verilmiştir. Sandık hareket halindeyken yüzeyin normal kuvveti {N} N ise, sürtünme kuvveti ne kadardır?",
     hesap=lambda mu, N: dict(Fs=mu * N),
          cevap=("Fs", "N", 1),
     celdirici=lambda v: [v["mu"] * v["N"] * math.cos(math.radians(20)),                      # cos20 ile çarpıldı
                          80 * 9.81 * v["mu"],                                                # N yerine doğrudan sandık ağırlığı alındı
                          v["N"] / v["mu"],                                                   # mu'ye bölündü
                          2 * v["mu"] * v["N"],                                               # 2 ile çarpıldı
                          0.5 * v["mu"] * v["N"]],                                            # 1/2 çarpanı eklendi
     beklenen={"Fs": 199.2},
     sekil={"dosya": "S19_1.png", "etiketler": []},
     cozum=r"""Kinetik sürtünme kuvveti F_s = μ_k \* N formülüyle bulunur.\
Verilenler:

- Kinetik sürtünme katsayısı (μ_k) = {mu}

- Normal kuvvet (N) = {N} N\
  F_s = {mu} \* {N}\
  F_s = {Fs:.1f} N""")

ekle(no=20, zorluk="zor",
     params={"mA": P(25, "kg", 15, 35, 5), "mC": P(10, "kg", 5, 20, 5)},
     metin="Şekildeki sistemde A bloğu ({mA} kg) pürüzsüz eğik düzlemde, C bloğu ({mC} kg) ise sürtünmeli yatay düzlemde hareket etmektedir. C bloğuna etki eden normal kuvvet ne kadardır? (g = 9.81 m/s²)",
     hesap=lambda mA, mC: dict(N=mC * g),
          cevap=("N", "N", 1),
     celdirici=lambda v: [(v["mA"] + v["mC"]) * 9.81,                                         # kütleler toplandı
                          v["mA"] * 9.81,                                                     # C yerine A kütlesi alındı
                          v["mC"] * 10,                                                       # g=10 kullanıldı
                          0.5 * v["mC"] * 9.81,                                               # 1/2 çarpanı eklendi
                          2 * v["mC"] * 9.81],                                                # 2 ile çarpıldı
     beklenen={"N": 98.1},
     sekil={"dosya": "S20_1.png", "etiketler": [("mA", "25 kg", lambda m: f"{m:g} kg"), ("mC", "10 kg", lambda m: f"{m:g} kg")]},
     cozum=r"""Sadece C bloğunun dikey kuvvet dengesine bakılır. C bloğu yatay hareket ettiği için dikey ivmesi sıfırdır.\
ΣF_y = 0\
N_C - m_C\*g = 0\
N_C = m_C \* g\
N_C = {mC} \* 9.81\
N_C = {N:.1f} N""")

if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "_out" / "u3"
    sys.exit(1 if calistir(S, out) else 0)
