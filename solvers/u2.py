"""Ünite 2 (Kinematik) sayısal soru solver'ları. Çalıştır: python u2.py

Her soru kendi başına çözülebilir (zincirli sorular parçalandı); sorular bağımsız seed ile üretilir.
"""
import math
from pathlib import Path

import cizimler
from core import P, Soru, calistir

U = 2
g = 9.81
S = []


def ekle(**kw):
    S.append(Soru(unite=U, **kw))


def kok(x):
    return math.sqrt(x)


# ---------------------------------------------------------------- S1-S2
P12 = lambda: {"a": P(3, "", 3, 9, 3), "b": P(2, "", 2, 6, 2), "T": P(3, "s", 2, 5, 1)}

ekle(no=1, zorluk="kolay", params=P12(),
     metin="Bir aracın hızı v(t) = {a}t² + {b}t m/sn fonksiyonu ile ifade edilmiştir. t= {T}sn'de aracın aldığı mesafe nedir?",
     hesap=lambda a, b, T: dict(a3=a / 3, b2=b / 2, x=a / 3 * T ** 3 + b / 2 * T ** 2, T3=T ** 3, T2=T ** 2),
          cevap=("x", "m", 1),
     celdirici=lambda v: [v["a"] * v["T"]**2 + v["b"] * v["T"],                             # integral alınmadı, hız hesaplandı
                          v["a"] * v["T"]**3 + v["b"] * v["T"]**2,                             # integral paydaları unutuldu
                          v["a"] / 2 * v["T"]**2 + v["b"] * v["T"],                             # integral dereceleri artırılmadı
                          v["a"] / 2 * v["T"]**3 + v["b"] / 2 * v["T"]**2,                     # paydalar her ikisi için 2 alındı
                          v["a"] / 3 * v["T"]**2 + v["b"] / 2 * v["T"]],                     # dereceler artırılmadı ama bölündü
     beklenen={"x": 36},
     cozum=r"""Alınan mesafe (x), hız fonksiyonunun (v(t)) zamana (t) göre integralidir. t=0'dan t={T}'e kadar belirli integral alınır.

1.  **İntegral denkleminin kurulması:**\
    x = ∫v(t) dt = ∫₀^{T} ({a}t² + {b}t) dt

2.  **İntegralin alınması:**\
    ∫({a}t² + {b}t) dt = {a3:g}t³ + {b2:g}t²

3.  **Belirli integralin hesaplanması:**\
    x = {a3:g} \* {T}³ + {b2:g} \* {T}² = {a3:g} \* {T3} + {b2:g} \* {T2}\
    x = {x:g} m""")

ekle(no=2, zorluk="kolay", params=P12(),
     metin="Bir aracın hızı v(t) = {a}t² + {b}t m/sn fonksiyonu ile ifade edilmiştir. t= {T}sn'de aracın ivmesi nedir?",
     hesap=lambda a, b, T: dict(a2=2 * a, aT=2 * a * T + b),
          cevap=("aT", "m/s²", 1),
     celdirici=lambda v: [v["a"] * v["T"]**2 + v["b"] * v["T"],                             # türev alınmadı, hız hesaplandı
                          v["a"] * v["T"] + v["b"],                                           # türevdeki 2 çarpanı unutuldu
                          v["a"] / 2 * v["T"]**2 + v["b"] * v["T"],                             # türev yerine integral alındı
                          2 * v["a"] * v["T"],                                                  # sabit b terimi atıldı
                          2.0 * v["a"]],                                                          # T yerine 1 konuldu
     beklenen={"aT": 20},
     cozum=r"""İvme (a), hızın (v) zamana göre türevidir.

1.  **Türev alınması:**\
    a(t) = dv/dt = d/dt ({a}t² + {b}t) = {a2}t + {b}

2.  **Değerin hesaplanması:**\
    a({T}) = {a2}({T}) + {b} = {aT} m/sn²""")

# ---------------------------------------------------------------- S3
ekle(no=3, zorluk="kolay",
     params={"c": P(8, "", 4, 10, 2), "T": P(5, "s", 4, 8, 1)},
     kisit=lambda c, T: T > c / 2,
     metin="Bir parçacığın konumu x(t) = {c}t - t² (t: saniye) fonksiyonu ile temsil ediliyor. {T}. saniyede parçacığın kat ettiği toplam mesafe nedir?",
     hesap=lambda c, T: dict(ty=c / 2, xy=c * c / 4, xT=c * T - T * T, d2=abs(c * T - T * T - c * c / 4),
                             d=c * c / 4 + abs(c * T - T * T - c * c / 4)),
          cevap=("d", "m", 1),
     celdirici=lambda v: [v["c"] * v["T"] - v["T"]**2,                                       # yön değişimi dikkate alınmadı, sadece net konum alındı
                          v["c"]**2 / 4,                                                          # sadece durma anına kadar olan mesafe hesaplandı
                          v["c"]**2 / 4 + (v["c"] * v["T"] - v["T"]**2),                      # geri dönüş mesafesi yerine son konum eklendi
                          v["c"] * v["T"] + v["T"]**2,                                       # denklemde işaret hatası (+ alındı)
                          v["c"] * v["T"]],                                                     # t² terimi ihmal edildi
     beklenen={"d": 17},
     cozum=r"""Parçacığın yön değiştirip değiştirmediğini anlamak için önce hız fonksiyonu bulunur.

1.  **Hız fonksiyonu:** v(t) = dx/dt = {c} - 2t

2.  **Yön değiştirme noktası (v(t)=0):** {c} - 2t = 0 => t = {ty:g} saniye\
    0-{ty:g} sn ve {ty:g}-{T} sn aralıkları ayrı ayrı incelenmelidir.

3.  **Konumlar:**

    - x(0) = 0 m

    - x({ty:g}) = {xy:g} m

    - x({T}) = {xT:g} m

4.  **Kat edilen mesafe:**

    - 0-{ty:g} sn arası: {xy:g} m

    - {ty:g}-{T} sn arası: {d2:g} m

    - Toplam Mesafe = **{d:g} m**""")

# ---------------------------------------------------------------- S4-S7
P45 = lambda: {"k": P(0.5, "", 0.5, 2, 0.5, liste=(0.5, 2)), "t": P(25, "s", 16, 49, 1, liste=(16, 25, 36, 49))}

ekle(no=4, zorluk="orta", params=P45(),
     metin="Başlangıç hızı sıfır olan bir parçacığın ivmesi a(v) = {k} * v⁻¹ m/sn² fonksiyonu ile temsil ediliyor. {t} saniye sonunda parçacığın hızı ne olur?",
     hesap=lambda k, t: dict(kt=k * t, v2=2 * k * t, v=kok(2 * k * t)),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [v["k"] * v["t"],                                                     # v dv integralindeki 1/2 çarpanı unutuldu
                          2 * v["k"] * v["t"],                                                 # karekök alınmadı
                          math.sqrt(v["k"] * v["t"]),                                           # 2 çarpanı karekök içine alınmadı
                          math.sqrt(2 * v["k"] * v["t"]) / 2,                                   # integral kuralı karıştırıldı
                          2 * math.sqrt(2 * v["k"] * v["t"])],                                 # fazladan 2 ile çarpıldı
     beklenen={"v": 5},
     cozum=r"""a = dv/dt ilişkisi kullanılarak diferansiyel denklem çözülür.

1.  **Diferansiyel denklemi kurma:**\
    a = dv/dt =\> {k} / v = dv/dt\
    v dv = {k} dt

2.  **İntegral alma:**\
    ∫₀ᵛ v dv = ∫₀^{t} {k} dt

3.  **İntegralleri çözme:**

    - Sol taraf: v²/2

    - Sağ taraf: {k} \* {t} = {kt:g}

4.  **Hızı bulma:**\
    v²/2 = {kt:g}\
    v² = {v2:g}\
    v = {v:g} m/sn""")

ekle(no=5, zorluk="orta", params=P45(),
     metin="Bir parçacığın hızı v(x) = {k} * x⁻¹ m/sn (x: konum) fonksiyonu ile temsil ediliyor. Parçacığın t=0 anında x=0 konumunda olduğu varsayılırsa, {t} saniyede ne kadar yer değiştirir?",
     hesap=lambda k, t: dict(kt=k * t, x2=2 * k * t, x=kok(2 * k * t)),
          cevap=("x", "m", 1),
     celdirici=lambda v: [v["k"] * v["t"],                                                     # x dx integralindeki 1/2 çarpanı unutuldu
                          2 * v["k"] * v["t"],                                                 # karekök alınmadı
                          math.sqrt(v["k"] * v["t"]),                                           # 2 çarpanı karekök içine alınmadı
                          0.5 * math.sqrt(2 * v["k"] * v["t"]),                                 # integral kuralı karıştırıldı
                          2 * math.sqrt(2 * v["k"] * v["t"])],                                 # fazladan 2 ile çarpıldı
     beklenen={"x": 5},
     cozum=r"""v = dx/dt ilişkisi kullanılarak diferansiyel denklem çözülür.

1.  **Diferansiyel denklemi kurma:**\
    v = dx/dt =\> {k} / x = dx/dt\
    x dx = {k} dt

2.  **İntegral alma:**\
    ∫₀ˣ x dx = ∫₀^{t} {k} dt

3.  **İntegralleri çözme:**

    - Sol taraf: x²/2

    - Sağ taraf: {k} \* {t} = {kt:g}

4.  **Konumu bulma:**\
    x²/2 = {kt:g}\
    x² = {x2:g}\
    x = {x:g} m""")

P67 = lambda: {"v0": P(4, "m/s", 2, 6, 1), "v1": P(5, "m/s", 5, 8, 1), "k": P(0.5, "", 0.5, 1, 0.5)}

ekle(no=6, zorluk="orta", params=P67(), kisit=lambda v0, v1, k: v1 > v0,
     metin="Başlangıç hızı {v0} m/sn olan bir parçacığın ivmesi a(v) = {k} * v⁻¹ m/sn² ile veriliyor. Parçacık hızını {v1} m/sn'ye kaç saniyede çıkarır?",
     hesap=lambda v0, v1, k: dict(s=(v1 ** 2 - v0 ** 2) / 2, s1=v1 ** 2 / 2, s0=v0 ** 2 / 2, t=(v1 ** 2 - v0 ** 2) / (2 * k)),
          cevap=("t", "s", 1),
     celdirici=lambda v: [(v["v1"] - v["v0"]) / v["k"],                                       # kareler unutuldu
                          (v["v1"]**2 - v["v0"]**2) / v["k"],                                 # 1/2 çarpanı unutuldu
                          (v["v1"]**2 + v["v0"]**2) / (2 * v["k"]),                           # sınırlar toplandı
                          v["v1"]**2 / (2 * v["k"]),                                           # v0 unutuldu
                          (v["v1"] - v["v0"]) / (2 * v["k"])],                               # kareler unutuldu ve fazladan 2'ye bölündü
     beklenen={"t": 9},
     cozum=r"""a = dv/dt ilişkisinden v dv = {k} dt denklemi kurulur.

1.  **İntegral alma (v={v0}'dan v={v1}'e, t=0'dan t'ye):**\
    ∫ v dv = ∫₀ᵗ {k} dt

2.  **İntegralleri çözme:**

    - Sol taraf: [v²/2] = ({v1}²/2) - ({v0}²/2) = {s1:g} - {s0:g} = {s:g}

    - Sağ taraf: {k}t

3.  **Zamanı bulma:**\
    {s:g} = {k}t\
    t = {t:g} saniye""")

ekle(no=7, zorluk="orta",
     params={"x0": P(3, "m", 1, 4, 1), "x1": P(5, "m", 5, 8, 1), "k": P(0.5, "", 0.5, 1, 0.5)},
     kisit=lambda x0, x1, k: x1 > x0,
     metin="Başlangıç konumu {x0} m olan bir parçacığın hızı v(x) = {k} * x⁻¹ m/sn ile veriliyor. Parçacık {x1} m konumuna ne kadar sürede ulaşır?",
     hesap=lambda x0, x1, k: dict(s=(x1 ** 2 - x0 ** 2) / 2, s1=x1 ** 2 / 2, s0=x0 ** 2 / 2, t=(x1 ** 2 - x0 ** 2) / (2 * k)),
          cevap=("t", "s", 1),
     celdirici=lambda v: [(v["x1"] - v["x0"]) / v["k"],                                       # kareler unutuldu
                          (v["x1"]**2 - v["x0"]**2) / v["k"],                                 # 1/2 çarpanı unutuldu
                          (v["x1"]**2 + v["x0"]**2) / (2 * v["k"]),                           # sınırlar toplandı
                          v["x1"]**2 / (2 * v["k"]),                                           # x0 unutuldu
                          (v["x1"] - v["x0"]) / (2 * v["k"])],                               # kareler unutuldu ve fazladan 2'ye bölündü
     beklenen={"t": 16},
     cozum=r"""v = dx/dt ilişkisinden x dx = {k} dt denklemi kurulur.

1.  **İntegral alma (x={x0}'dan x={x1}'e, t=0'dan t'ye):**\
    ∫ x dx = ∫₀ᵗ {k} dt

2.  **İntegralleri çözme:**

    - Sol taraf: [x²/2] = ({x1}²/2) - ({x0}²/2) = {s1:g} - {s0:g} = {s:g}

    - Sağ taraf: {k}t

3.  **Zamanı bulma:**\
    {s:g} = {k}t\
    t = {t:g} saniye""")

# ---------------------------------------------------------------- S8-S9
ekle(no=8, zorluk="orta",
     params={"k": P(4, "", 1, 16, 1, liste=(1, 4, 9, 16)), "x": P(2, "m", 1, 4, 1)},
     metin="Başlangıç hızı sıfır olan parçacığın ivmesi a(x) = {k}x m/sn² fonksiyonu ile temsil ediliyor. {x} m yer değiştirince hızı ne olur?",
     hesap=lambda k, x: dict(h=k / 2, L=k / 2 * x * x, v2=k * x * x, v=x * kok(k)),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [0.5 * v["x"] * math.sqrt(v["k"]),                                     # 1/2 çarpanı eklendi
                          v["x"] * math.sqrt(v["k"] / 2),                                       # 2 çarpanı ters tarafa yazıldı
                          math.sqrt(2) * v["x"] * math.sqrt(v["k"]),                             # v²/2'deki 2 unutuldu
                          2 * v["x"] * math.sqrt(v["k"]),                                       # 2 ile çarpıldı
                          3 * v["x"] * math.sqrt(v["k"])],                                     # katsayı hatası
     beklenen={"v": 4},
     cozum=r"""İvme, hız ve konum arasındaki zamandan bağımsız a dx = v dv ilişkisi kullanılır.

1.  **Formülde yerine koyma:**\
    ({k}x) dx = v dv

2.  **İntegral alma (x=0'dan {x}'e, v=0'dan v'ye):**\
    ∫₀^{x} ({k}x) dx = ∫₀ᵛ v dv

3.  **İntegralleri çözme:**

    - Sol taraf: [{h:g}x²] = {h:g}({x})² = {L:g}

    - Sağ taraf: v²/2

4.  **Hızı bulma:**\
    {L:g} = v²/2 =\> v² = {v2:g} =\> v = {v:g} m/sn""")

ekle(no=9, zorluk="orta",
     params={"k": P(4, "", 1, 9, 1, liste=(1, 4, 9)), "v": P(36, "m/s", 12, 48, 12)},
     metin="Başlangıç hızı sıfır olan parçacığın ivmesi a(x) = {k}x m/sn² ile veriliyor. Hızı {v} m/sn olduğunda ne kadar yer değiştirmiştir?",
     hesap=lambda k, v: dict(h=k / 2, R=v * v / 2, x2=v * v / k, x=v / kok(k)),
          cevap=("x", "m", 1),
     celdirici=lambda v: [v["v"]**2 / (2 * v["k"]),                                           # integral kuralı karıştırıldı (x² unutuldu)
                          v["v"]**2 / v["k"],                                                 # karekök alınmadı
                          math.sqrt(v["v"] / v["k"]),                                           # v² yerine v alındı
                          2 * v["v"] / math.sqrt(v["k"]),                                       # fazladan 2 çarpanı
                          0.5 * v["v"] / math.sqrt(v["k"])],                                   # 1/2 çarpanı hatası
     beklenen={"x": 18},
     cozum=r"""a dx = v dv ilişkisi kullanılır.

1.  **İntegral alma (x=0'dan x'e, v=0'dan {v}'ye):**\
    ∫₀ˣ ({k}x) dx = ∫₀^{v} v dv

2.  **İntegralleri çözme:**

    - Sol taraf: [{h:g}x²] = {h:g}x²

    - Sağ taraf: {v}²/2 = {R:g}

3.  **Yer değiştirmeyi bulma:**\
    {h:g}x² = {R:g} =\> x² = {x2:g} =\> x = {x:g} m""")

# ---------------------------------------------------------------- S10-S12  (hava balonu)
P10 = lambda: {"a": P(8, "m/s", 5, 10, 1, liste=(5, 8, 10)), "T": P(2, "s", 1, 3, 1)}


def _balon(a, T):
    x = a * T
    vy = x / 5 * a
    return dict(x=x, vx=a, vy=vy, v=math.hypot(a, vy), th=math.degrees(math.atan2(vy, a)),
                a2=a * a, vy2=vy ** 2, tn=vy / a)


BAL = {"dosya": "S10_1.png", "etiketler": [("x", [178, 338, 232, 360], lambda x: f"{x:g} m")]}   # json'da 'x²' diye etiketli
ekle(no=10, zorluk="orta", params=P10(), hesap=_balon,      cevap=("v", "m/s", 2),
     celdirici=lambda v: [v["vy"],                                                               # bileşke yerine sadece düşey hız
                          v["vx"] + v["vy"],                                                   # skaler toplandı
                          v["vx"]**2 + v["vy"]**2,                                             # karekök alınmadı
                          math.hypot(v["vx"], 2 * v["vy"]),                                     # vy türevinde 2 katı alındı
                          v["vx"]],                                                              # bileşke yerine sadece yatay hız
     beklenen={"v": 26.82},
     metin="Şekildeki hava balonunun yatay konumu x = {a}t (m), yörüngesi ise y = x²/10 ile tanımlanmıştır. t={T} saniye olduğunda bileşke hızın büyüklüğü m/sn cinsinden nedir?",
     sekil=BAL,
     cozum=r"""1.  **Hızın x-Bileşenini (vx) Bulma:**\
    vx = dx/dt = d/dt ({a}t) = {a} m/sn (sabit)

2.  **Hızın y-Bileşenini (vy) Bulma (Zincir Kuralı):**\
    vy = dy/dx \* dx/dt\
    dy/dx = d/dx (x²/10) = x/5\
    vy = (x/5) \* vx = (x/5) \* {a}

3.  **t={T} saniye için:**

    - x({T}) = {a} \* {T} = {x:g} m

    - vx = {a} m/sn

    - vy = {a} \* ({x:g}) / 5 = {vy:g} m/sn

4.  **Bileşke hız:**\
    v = √(vx² + vy²) = √({a}² + {vy:g}²) = √({a2:g} + {vy2:g})\
    v ≈ {v:.2f} m/sn""")

ekle(no=11, zorluk="orta", params=P10(), hesap=_balon,      cevap=("th", "°", 2),
     celdirici=lambda v: [math.radians(v["th"]),                                                 # derece yerine radyan
                          v["th"] / 2,                                                           # yarı açı hatası
                          v["th"] + 15,                                                          # açı kaydırma hatası
                          180 - v["th"],                                                         # bütünler açı alındı
                          math.degrees(math.atan2(v["vy"], 2 * v["vx"]))],                      # tanım paydası 2 katı alındı
     beklenen={"th": 72.65},
     metin="Şekildeki hava balonunun yatay konumu x = {a}t (m), yörüngesi ise y = x²/10 ile tanımlanmıştır. t={T} saniye olduğunda bileşke hızın x ekseni ile yaptığı açı derece cinsinden nedir?",
     sekil=dict(BAL, dosya="S11_1.png"),
     cozum=r"""1.  **Hız Bileşenleri:** vx = {a} m/sn, vy = {vy:g} m/sn

2.  **Açıyı Hesaplama:**\
    tan(θ) = vy / vx = {vy:g} / {a} = {tn:g}\
    θ = arctan({tn:g}) ≈ {th:.2f}°""")

ekle(no=12, zorluk="orta", params=P10(), hesap=_balon,      cevap=("vy", "m/s", 1),
     celdirici=lambda v: [v["x"] / 5,                                                            # dx/dt zincir kuralı çarpanı unutuldu
                          2 * v["vy"],                                                           # türevde fazladan 2 çarpanı
                          v["vy"] / 2,                                                           # zincir kuralı yarım alındı
                          v["vy"] / 3,                                                           # katsayı hatası
                          3 * v["vy"]],                                                          # katsayı hatası
     beklenen={"vy": 25.6},
     metin="Şekildeki hava balonunun yatay konumu x = {a}t (m), yörüngesi ise y = x²/10 ile tanımlanmıştır. t={T} saniye olduğunda balonun düşey hızı (v_y) ne kadardır?",
     sekil=dict(BAL, dosya="S12_1.png"),
     cozum=r"""1.  **t={T} anındaki x konumu:** x({T}) = {a} \* {T} = {x:g} m

2.  **vy denklemi:** vy = (x/5) \* {a}

3.  **Değeri yerine koyma:** vy = {x:g} \* {a} / 5 = **{vy:g} m/sn**""")

# ---------------------------------------------------------------- S13-S14  (çuval)
P13 = lambda: {"v": P(12, "m/s", 8, 16, 2), "h": P(6, "m", 2, 8, 2)}


def _cuval(v, h):
    t = round(math.sqrt(2 * h / g), 2)
    return dict(t2=h / (g / 2), t=t, R=v * t, h2=g / 2)


ekle(no=13, zorluk="orta", params=P13(), hesap=_cuval,      cevap=("t", "s", 2),
     celdirici=lambda v: [math.sqrt(v["h"] / 9.81),                                             # ½gt² formülündeki 2 çarpanı unutuldu
                          2 * v["h"] / 9.81,                                                     # karekök alınması unutuldu
                          math.sqrt(2 * v["h"] / 10),                                             # g=10 alındı
                          v["h"] / v["v"],                                                     # düşey yükseklik yatay hıza bölündü
                          2 * v["t"]],                                                           # serbest düşme süresi 2 ile çarpıldı
     beklenen={"t": 1.11},
     metin="Şekilde gösterilen bir çuval, {v} m/s yatay hızla {h} m yükseklikteki bir rampadan kaymaktadır. Çuvalın yere çarpması için gereken süre nedir? (g = 9.81 m/sn²)",
     sekil={"dosya": "S13_1.png", "etiketler": [("v", [148, 93, 215, 119], lambda v: f"{v:g} m/s"),
                                                   ("h", [40, 232, 76, 252], lambda h: f"{h:g} m")]},
     cozum=r"""Düşme süresi sadece dikey hareketle ilgilidir. Yatay hız süreyi etkilemez.\
h = v_y₀\*t + ½gt²

- Başlangıç dikey hız (v_y₀) = 0

- Yükseklik (h) = {h} m\
  {h} = 0 \* t + ½ \* (9.81) \* t²\
  {h} = 4.905 \* t²\
  t² = {h} / 4.905 ≈ {t2:.4f}\
  t ≈ {t:.2f} saniye""")

ekle(no=14, zorluk="orta", params=P13(), hesap=_cuval,      cevap=("R", "m", 2),
     celdirici=lambda v: [v["v"] * math.sqrt(v["h"] / 9.81),                                   # uçuş süresinde 2 çarpanı unutuldu
                          v["v"] * (2 * v["h"] / 9.81),                                         # sürede karekök unutuldu
                          v["v"] * math.sqrt(2 * v["h"] / 10),                                 # g=10 alındı
                          v["t"],                                                                # yatay hızla çarpılmadı
                          0.5 * v["v"] * v["t"]],                                               # ½ çarpanı hatası
     beklenen={"R": 13.32},
     metin="Şekilde gösterilen bir çuval, {v} m/s yatay hızla {h} m yükseklikteki bir rampadan kaymaktadır. Çuvalın yatayda kat ettiği mesafe (R) nedir? (g = 9.81 m/sn²)",
     sekil={"dosya": "S14_1.png", "etiketler": [("v", [148, 93, 215, 119], lambda v: f"{v:g} m/s"),
                                                   ("h", [40, 232, 76, 252], lambda h: f"{h:g} m")]},
     cozum=r"""Önce düşme süresi dikey hareketten bulunur: {h} = ½ \* 9.81 \* t² =\> t ≈ {t:.2f} sn.\
Yatay hareket sabit hızlıdır: R = vx \* t

- Yatay hız (vx) = {v} m/sn

- Uçuş süresi (t) ≈ {t:.2f} sn\
  R = {v} \* {t:.2f} ≈ {R:.2f} metre""")

# ---------------------------------------------------------------- S15  (şekil sorunlu)
ekle(no=15, zorluk="orta",
     params={"h": P(3, "m", 1, 5, 1)},
     metin="{h} m yükseklikteki bir rampadan 30° açıyla fırlatılan bir motosiklet 2 sn sonra yere düşüyor. Rampadan ayrılma hızı (v_A) nedir? (g = 10 m/sn²)",
     hesap=lambda h: dict(c=20 - h, v=(20 - h)),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [(20 - v["h"]) / math.sqrt(3),                                          # sin30 yerine cos30 kullanıldı
                          40 - v["h"],                                                           # ½gt²'deki ½ unutuldu
                          19.62 - v["h"],                                                        # g=10 yerine g=9.81 kullanıldı
                          20 + v["h"],                                                           # h çıkarılmak yerine eklendi
                          0.5 * 10 * 2**2 / 2 - v["h"] / 2],                                      # denklem çarpan hatası
     beklenen={"v": 17},
     sekil={"dosya": "S15_1.png", "cizim": cizimler.s15},
     cozum=r"""Dikey hareket denklemi kullanılır.\
y = y₀ + (v_A \* sinα) \* t - ½gt²

- y = 0 (son konum)

- y₀ = {h} m (ilk konum)

- α = 30°

- t = 2 sn\
  0 = {h} + (v_A \* sin30°) \* 2 - ½ \* 10 \* 2²\
  0 = {h} + v_A - 20\
  v_A = {v:g} m/sn""")

# ---------------------------------------------------------------- S16-S17  (buz patencisi)
P16 = lambda: {"a": P(1, "m/s²", 1, 3, 1), "v0": P(6, "m/s", 4, 8, 2), "T": P(4, "s", 2, 5, 1), "r": P(20, "m", 10, 50, 10)}

ekle(no=16, zorluk="orta", params=P16(),
     metin="P noktasında hızı {v0}m/sn olan bir buz patencisi, hızını sabit {a} m/sn² ivmeyle artırıyor. {T} saniye sonra ivmenin teğetsel bileşeni ne olur?",
     hesap=lambda a, v0, T, r: dict(at=a),
          cevap=("at", "m/s²", 1),
     celdirici=lambda v: [(v["v0"] + v["a"] * v["T"])**2 / v["r"],                         # teğetsel ivme yerine normal ivme hesaplandı
                          v["v0"] + v["a"] * v["T"],                                         # ivme yerine hız hesaplandı
                          math.hypot(v["a"], (v["v0"] + v["a"] * v["T"])**2 / v["r"]),      # toplam ivme hesaplandı
                          v["a"] * v["T"],                                                     # ivme zamanla çarpıldı
                          v["v0"] / v["T"]],                                                   # v0 / T yapıldı
     beklenen={"at": 1},
     cozum=r"""Teğetsel ivme (at), hızın büyüklüğündeki değişim oranıdır. Soruda bu değerin hareket boyunca sabit ve {a} m/sn² olduğu doğrudan verilmiştir. Dolayısıyla {T} saniye sonra da teğetsel ivme **{at} m/sn²**'dir.""")

ekle(no=17, zorluk="orta", params=P16(),
     metin="P noktasında hızı {v0}m/sn olan bir buz patencisi, hızını sabit {a} m/sn² ivmeyle artırıyor. {T} saniye sonra ivmenin normal bileşeni (an) nedir? (r={r}m)",
     hesap=lambda a, v0, T, r: dict(v=v0 + a * T, an=(v0 + a * T) ** 2 / r, v2=(v0 + a * T) ** 2),
          cevap=("an", "m/s²", 1),
     celdirici=lambda v: [v["v0"]**2 / v["r"],                                                 # son hız yerine ilk hız v0 kullanıldı
                          (v["v0"] + v["a"] * v["T"]) / v["r"],                             # hızın karesi alınmadı
                          (v["v0"] + v["a"] * v["T"])**2,                                     # yarıçapa bölünmesi unutuldu
                          float(v["a"]),                                                         # normal ivme yerine teğetsel ivme alındı
                          (v["v0"] + v["a"] * v["T"])**2 / (v["r"] / 2)],                   # yarıçap yarım alındı
     beklenen={"an": 5},
     cozum=r"""Normal ivme an = v²/r formülü ile bulunur. Önce {T} saniye sonraki hız bulunmalıdır.

1.  **{T} Saniye Sonraki Hızı Hesaplama:**\
    v = v₀ + at \* t = {v0} + ({a} \* {T}) = {v:g} m/sn

2.  **Normal İvmenin Hesaplanması:**\
    an = v²/r = {v:g}² / {r} = {v2:g} / {r} = {an:.3g} m/sn²""")

# ---------------------------------------------------------------- S18-S19  (kayakçı)
P18 = lambda: {"at": P(2, "m/s²", 1, 4, 1), "an": P(1.27, "m/s²", 1, 2, 0.5)}

ekle(no=18, zorluk="orta", params=P18(),
     metin="Parabolik bir yörüngede kayan bir kayakçının hızı 6 m/sn ve hızının artış oranı (teğetsel ivme) {at} m/sn²'dir. O andaki normal ivmesi {an} m/sn² ise, bileşke ivmenin büyüklüğü nedir?",
     hesap=lambda at, an: dict(a=math.hypot(at, an), at2=at * at, an2=round(an * an, 2), s=at * at + round(an * an, 2),
                               ar=math.sqrt(at * at + round(an * an, 2))),
          cevap=("ar", "m/s²", 2),
     celdirici=lambda v: [v["at"] + v["an"],                                                   # skaler toplandı
                          (v["at"] + v["an"]) / 2,                                             # ortalama ivme alındı
                          2 * v["ar"],                                                           # 2 ile çarpıldı
                          0.5 * v["ar"],                                                         # yarıya bölündü
                          float(v["at"])],                                                       # sadece teğetsel alındı
     beklenen={"ar": 2.37},
     sekil=None,
     cozum=r"""Bileşke ivme, teğetsel ve normal bileşenlerin vektörel toplamıdır.\
a = √(at² + an²)

- at = {at} m/sn²

- an = {an} m/sn²\
  a = √({at}² + {an}²) = √({at2:g} + {an2:g}) = √{s:.3g} ≈ {ar:.2f} m/sn²""")


def _kayakci(at, an):
    ax = at * math.cos(math.radians(225)) + an * math.cos(math.radians(135))
    ay = at * math.sin(math.radians(225)) + an * math.sin(math.radians(135))
    phi = math.degrees(math.atan2(ay, ax)) % 360
    return dict(atx=at * math.cos(math.radians(225)), aty=at * math.sin(math.radians(225)),
                anx=an * math.cos(math.radians(135)), any_=an * math.sin(math.radians(135)),
                ax=ax, ay=ay, phi=phi, ref=abs(phi - 180))


ekle(no=19, zorluk="zor", params=P18(),
     metin="Parabolik bir yörüngede kayan bir kayakçının hızının artış oranı (teğetsel ivme) {at} m/sn², normal ivmesi {an} m/sn²'dir. Bileşke ivme vektörünün x ekseni ile yaptığı açı nedir? (Kayakçının bulunduğu noktadaki eğim açısı 45°'dir.)",
     hesap=_kayakci,      cevap=("phi", "°", 1),
     celdirici=lambda v: [(v["phi"] + 45) % 360,                                                # açıya eğim eklendi
                          (v["phi"] - 45) % 360,                                                # eğim açısı çıkarıldı
                          v["phi"] / 2,                                                          # yarı açı hatası
                          (v["phi"] + 90) % 360,                                                # 90 derece dik eksen hatası
                          (v["phi"] + 180) % 360],                                               # zıt yön alındı
     beklenen={"phi": 192.5},
     cozum=r"""İvme bileşenlerini x-y koordinatlarına dönüştürmek gerekir.

1.  **Eksenleri Tanımlama:** Teğet yönü, pozitif x-ekseniyle 225° açı yapar. Normal yönü ise buna dik ve eğrilik merkezine doğru, yani 135° açı yapar.

2.  **Teğetsel İvmenin Bileşenleri:**

    - a_tx = at \* cos(225°) = {at} \* (-√2/2) ≈ {atx:.3f} m/sn²

    - a_ty = at \* sin(225°) ≈ {aty:.3f} m/sn²

3.  **Normal İvmenin Bileşenleri:**

    - a_nx = an \* cos(135°) = {an} \* (-√2/2) ≈ {anx:.3f} m/sn²

    - a_ny = an \* sin(135°) = {an} \* (√2/2) ≈ {any_:.3f} m/sn²

4.  **Bileşke İvmenin Bileşenleri:**

    - ax = {ax:.3f} m/sn²

    - ay = {ay:.3f} m/sn²

5.  **Açının Hesaplanması:**\
    φ = atan2(ay, ax) ≈ {phi:.1f}° (pozitif x-ekseninden ölçülen)""")

# ---------------------------------------------------------------- S20-S21
ekle(no=20, zorluk="orta",
     params={"r": P(10, "m", 5, 20, 5), "w": P(0.1, "rad/s", 0.1, 0.5, 0.1, liste=(0.1, 0.2, 0.5))},
     metin="r={r}m (sabit) yarıçaplı bir yörüngede dönen bir sepetin açısal konumu θ = {w}t rad'dır. t=1sn'de sepetin bileşke hızı nedir?",
     hesap=lambda r, w: dict(vt=r * w, v=r * w),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [v["r"] * v["w"]**2,                                                 # normal ivme hesaplandı
                          v["r"] / v["w"],                                                     # r/ω yapıldı
                          v["w"] / v["r"],                                                     # ω/r yapıldı
                          2 * v["r"] * v["w"],                                                 # 2 ile çarpıldı
                          0.5 * v["r"] * v["w"]],                                               # 1/2 çarpanı eklendi
     beklenen={"v": 1},
     cozum=r"""1.  **Radyal Hız (v_r):** Yarıçap sabit olduğundan ṙ = 0. Dolayısıyla v_r = 0.

2.  **Enine Hız (v_θ):**

    - Açısal hız: θ̇ = d/dt({w}t) = {w} rad/sn (sabit)

    - v_θ = r \* θ̇ = {r} \* {w} = {vt:g} m/sn

3.  **Bileşke Hız:**\
    v = √(v_r² + v_θ²) = √(0² + {vt:g}²) = {v:g} m/sn""")

ekle(no=21, zorluk="orta",
     params={"k1": P(100, "mm", 50, 200, 50), "k2": P(1, "", 1, 3, 1)},
     metin="Bir mekanizmada B bileziğinin radyal konumu r = {k1}t² (mm) ve açısal konumu θ = {k2s}t³ (rad) olarak verilmiştir. t=1 saniye anında bileziğin bileşke hızı nedir?",
     hesap=lambda k1, k2: dict(k2s="" if k2 == 1 else k2, rd=2 * k1, wd=3 * k2, vth=k1 * 3 * k2, v=math.hypot(2 * k1, k1 * 3 * k2),
                               rd2=(2 * k1) ** 2, vth2=(k1 * 3 * k2) ** 2, s=(2 * k1) ** 2 + (k1 * 3 * k2) ** 2),
          cevap=("v", "mm/s", 2),
     celdirici=lambda v: [2 * v["k1"] + 3 * v["k1"] * v["k2"],                               # skaler toplandı
                          math.hypot(v["k1"], v["k1"] * v["k2"]),                             # türev katsayıları unutuldu
                          (2 * v["k1"])**2 + (3 * v["k1"] * v["k2"])**2,                     # karekök alınmadı
                          2.0 * v["k1"],                                                         # sadece radyal hız
                          3.0 * v["k1"] * v["k2"]],                                             # sadece enine hız
     beklenen={"v": 360.56},
     cozum=r"""1.  **Gerekli Değerleri t=1 için bulma:**

    - r(1) = {k1}(1)² = {k1} mm

    - ṙ = dr/dt = {rd}t =\> ṙ(1) = {rd} mm/sn

    - θ̇ = dθ/dt = {wd}t² =\> θ̇(1) = {wd} rad/sn

2.  **Hız Bileşenlerini Hesaplama:**

    - Radyal hız: v_r = ṙ = {rd} mm/sn

    - Enine hız: v_θ = r \* θ̇ = {k1} \* {wd} = {vth:g} mm/sn

3.  **Bileşke Hızı Bulma:**\
    v = √(v_r² + v_θ²) = √({rd}² + {vth:g}²) = √{s:g}\
    v ≈ {v:.2f} mm/sn""")

# ---------------------------------------------------------------- S22-S25  (makaralar)
ekle(no=22, zorluk="orta",
     params={"vM": P(10, "m/s", 6, 15, 3)},
     metin="Şekildeki makara sisteminde, motor (M) halatı {vM} m/s sabit hızla kendine doğru çekmektedir. Silindir A'nın hızı nedir ve hangi yöndedir?",
     hesap=lambda vM: dict(vA=vM / 3),
          cevap=("vA", "m/s", 2),
     celdirici=lambda v: [3.0 * v["vM"],                                                         # 3 ile çarpıldı
                          v["vM"] / 2,                                                           # 2 ip sayıldı
                          v["vM"] / 4,                                                           # 4 ip sayıldı
                          float(v["vM"]),                                                        # mekanik avantaj ihmal edildi
                          2 * v["vM"] / 3],                                                      # 2/3 oranı alındı
     beklenen={"vA": 3.333},
     cozum=r"""1.  **İp Uzunluğu Denklemi:** Referans (datum) olarak üst sabit makaraların seviyesini alalım. Silindirin konumu s_A, motorun çektiği ipin ucu s_M olsun. Silindire bağlı 3 adet dikey ip segmenti vardır.\
    L = 3s_A + s_M

2.  **Zamana Göre Türev Alma:**\
    dL/dt = 3(ds_A/dt) + (ds_M/dt)\
    0 = 3v_A + v_M

3.  **Hızı Hesaplama:** Motor ipi kendine doğru çektiği için s_M artar, yani v_M = +{vM} m/s.\
    0 = 3v_A + {vM}\
    v_A = -{vM}/3 ≈ -{vA:.2f} m/sn\
    Negatif işaret, s_A mesafesinin azaldığını, yani silindirin **yukarı doğru** hareket ettiğini gösterir. Hızı **{vA:.2f} m/sn**'dir.""")

ekle(no=23, zorluk="zor",
     params={"k": P(0.2, "m/s³", 0.1, 0.4, 0.1), "h": P(4, "m", 2, 8, 2)},
     metin="A ve B motorları kabloları a = {k}t m/s² ivmesiyle çekiyor. Başlangıçta durgun olan yükün h = {h} m yükselmesi ne kadar zaman alır?",
     hesap=lambda k, h: dict(kk=0.75 * k, kv=0.75 * k / 2, kh=0.75 * k / 6, t3=h / (0.75 * k / 6), t=(h / (0.75 * k / 6)) ** (1 / 3)),
          cevap=("t", "s", 2),
     celdirici=lambda v: [(6 * v["h"] / v["k"]) ** (1 / 3),                                     # 3/4 makara oranı unutuldu
                          math.sqrt(2 * v["h"] / (0.75 * v["k"])),                             # ivme sabit varsayıldı
                          (6 * v["h"] / (v["k"] * 4 / 3)) ** (1 / 3),                           # 4/3 ters oran kullanıldı
                          v["h"] / (0.75 * v["k"] / 6),                                       # küpkök alınmadı
                          0.5 * v["t"]],                                                         # katsayı hatası
     beklenen={"t": 5.43},
     cozum=r"""1.  **Kinematik İlişkiyi Kurma:** İp uzunluğundan 4v_yük = 3v_motor bulunur. Bu ivmeler için de geçerlidir: a_yük = (3/4)a_motor.

2.  **Yükün İvmesi:** a_yük = (3/4) \* ({k}t) = {kk:g}t m/s²

3.  **İvmeden Hıza, Hızdan Konuma Geçiş (İntegral):**

    - v_yük(t) = ∫({kk:g}t) dt = {kv:g}t²

    - h(t) = ∫({kv:g}t²) dt = {kh:g}t³

4.  **Zamanı Bulma:**\
    {h} = {kh:g}t³\
    t³ = {h} / {kh:g} = {t3:.4g}\
    t = ({t3:.4g})^(1/3) ≈ {t:.2f} saniye""")

P24 = lambda: {"vA": P(2, "m/s", 2, 6, 2), "vB": P(4, "m/s", 2, 10, 2)}
ekle(no=24, zorluk="orta", params=P24(),
     metin="A motoru kabloyu {vA} m/s, B motoru ise {vB} m/s hızla çekiyorsa, yükün merkezinin hızı nedir?",
     hesap=lambda vA, vB: dict(sol=vA / 2, sag=vB / 2, v=(vA / 2 + vB / 2) / 2),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [(v["vA"] + v["vB"]) / 2,                                             # makara oranı (1/2) unutuldu
                          float(v["vA"] + v["vB"]),                                            # hızlar doğrudan toplandı
                          (v["vA"] + v["vB"]) / 8,                                             # fazladan 2'ye bölündü
                          3 * (v["vA"] + v["vB"]) / 4,                                         # katsayı hatası
                          (v["vA"] + v["vB"]) / 6],                                            # katsayı hatası
     beklenen={"v": 1.5},
     sekil={"dosya": "S24_1.png", "etiketler": [("vA", [122, 2, 168, 22], lambda v: f"v_A = {v:g} m/s"),
                                                   ("vB", [282, 2, 328, 22], lambda v: f"v_B = {v:g} m/s")]},
     cozum=r"""Yük rijit bir cisim gibi davranır. Sol tarafının hızı A motoruna, sağ tarafının hızı B motoruna bağlıdır.

1.  **Sol Tarafın Hızı:** v_sol = v_A / 2 = {vA} / 2 = {sol:g} m/s (yukarı)

2.  **Sağ Tarafın Hızı:** v_sağ = v_B / 2 = {vB} / 2 = {sag:g} m/s (yukarı)

3.  **Merkezin Hızı:** Yükün merkezinin hızı, uç noktaların hızlarının aritmetik ortalamasıdır.\
    v_yük = (v_sol + v_sağ) / 2 = ({sol:g} + {sag:g}) / 2 = {v:g} m/s (yukarı)""")


def _s25(c, aD, d0):
    A, B = c / 24, aD / 2
    u = (-B + math.sqrt(B * B + 4 * A * d0)) / (2 * A)
    return dict(A=A, B=B, C=c / 2, u=u, t=math.sqrt(u), q=B * B + 4 * A * d0)


ekle(no=25, zorluk="zor",
     params={"c": P(3, "", 2, 6, 1), "aD": P(5, "m/s²", 3, 7, 1), "d0": P(3, "m", 2, 6, 1)},
     metin="C motoru kabloyu a_C = {c}t² ivmesiyle, D motoru ise a_D = {aD} m/s² ivmesiyle çekiyor. Başlangıçta aralarında {d0} m olan A ve B bloklarının d=0 konumunda buluşması ne kadar sürer?",
     hesap=_s25,      cevap=("t", "s", 2),
     celdirici=lambda v: [v["u"],                                                                # karekök alınmadı (u = t²)
                          v["d0"] / v["aD"],                                                   # sabit hız varsayıldı
                          math.sqrt(2 * v["d0"] / v["aD"]),                                     # A bloğu ihmal edildi
                          2 * v["t"],                                                            # 2 ile çarpıldı
                          0.5 * v["t"]],                                                         # 1/2 çarpanı hatası
     beklenen={"t": 1.066},
     sekil={"dosya": "S25_1.png", "cizim": cizimler.s25},   # orijinal şekil metinle eşleşmiyordu; şematik çizim
     cozum=r"""1.  **Blokların İvmeleri:**

    - Blok A: a_A = a_C / 2 = {C:g}t² (sağa, pozitif yön)

    - Blok B: a_B = a_D = {aD} m/s² (sola, negatif yön, a_B = -{aD})

2.  **Konum Denklemleri (İki kez integral):**

    - Blok A: x_A(t) = {A:.4g}t⁴

    - Blok B: x_B(t) = {d0} - {B:g}t²

3.  **Konumları Eşitleme:**\
    {A:.4g}t⁴ + {B:g}t² - {d0} = 0\
    u = t² değişken değiştirmesi ile {A:.4g}u² + {B:g}u - {d0} = 0. Pozitif kök u ≈ {u:.3f}\
    t = √u ≈ {t:.2f} saniye""")

# ---------------------------------------------------------------- S26-S30
ekle(no=26, zorluk="kolay",
     params={"vA": P(4, "m/s", 2, 8, 2), "vB": P(3, "m/s", 2, 6, 1)},
     metin="Batıya {vA} m/sn hızla giden bir araba, doğuya {vB} m/sn hızla giden başka bir arabayı nasıl görür?",
     hesap=lambda vA, vB: dict(vr=vB + vA),
          cevap=("vr", "m/s", 1),
     celdirici=lambda v: [abs(v["vB"] - v["vA"]),                                              # zıt yönler toplanmak yerine çıkarıldı
                          math.hypot(v["vA"], v["vB"]),                                         # dik vektörler gibi toplandı
                          (v["vA"] + v["vB"]) / 2,                                             # ortalama hız alındı
                          2 * (v["vA"] + v["vB"]),                                             # 2 ile çarpıldı
                          1.5 * (v["vA"] + v["vB"])],                                          # katsayı hatası
     beklenen={"vr": 7},
     cozum=r"""Bu bir bağıl hız problemidir. Gözlemci (batıya giden) ve gözlenen (doğuya giden) belirlenir. Doğu yönü (+) olsun.\
v_bağıl = v_gözlenen - v_gözlemci\
v_bağıl = (+{vB}) - (-{vA}) = +{vr} m/sn\
Sonuç pozitif olduğu için, batıya giden araba diğer arabayı **doğuya doğru {vr} m/sn hızla** gidiyormuş gibi görür.""")

ekle(no=27, zorluk="kolay",
     params={"u": P(100, "km/h", 60, 120, 20)},
     metin="A uçağı batıya {a} km/h, B uçağı ise kuzeye {b} km/h hızla uçmaktadır. A'nın B'ye göre hızının büyüklüğü nedir?",
     hesap=lambda u: dict(a=4 * u, b=3 * u, a2=(4 * u) ** 2, b2=(3 * u) ** 2, s=(4 * u) ** 2 + (3 * u) ** 2, v=5 * u),
          cevap=("v", "km/h", 0),
     celdirici=lambda v: [7.0 * v["u"],                                                         # skaler toplandı (4u + 3u)
                          1.0 * v["u"],                                                         # skaler çıkarıldı (4u - 3u)
                          25.0 * v["u"],                                                        # karekök alınmadı
                          3.5 * v["u"],                                                         # ortalama alındı
                          10.0 * v["u"]],                                                        # 2 ile çarpıldı
     beklenen={"v": 500},
     cozum=r"""Bu iki boyutlu bir bağıl hız problemidir. Doğu (+i), Kuzey (+j) olsun.

- v_A = -{a}i

- v_B = +{b}j\
  "A'nın B'ye göre hızı" v_A/B demektir.\
  v_A/B = v_A - v_B = -{a}i - {b}j\
  Büyüklüğü: |v_A/B| = √(({a})² + ({b})²) = √({a2:g} + {b2:g}) = √{s:g} = {v:g} km/h""")

ekle(no=28, zorluk="orta",
     params={"v1": P(16, "m/s", 10, 20, 2), "v2": P(21, "m/s", 18, 24, 2), "v3": P(24, "m/s", 24, 30, 2)},
     kisit=lambda v1, v2, v3: v1 < v2 < v3,
     metin="Bir trenin hızı şekildeki v-t grafiği ile verilmiştir. 60 saniye boyunca kat ettiği toplam mesafeyi bulunuz. (Grafikte t=0'da v=0, t=20'de v={v1}, t=40'da v={v2}, t=60'da v={v3}, noktalar arası geçişler doğru olacak)",
     hesap=lambda v1, v2, v3: dict(s1=v1 * 10, s2=(v1 + v2) * 10, s3=(v2 + v3) * 10, d=v1 * 10 + (v1 + v2) * 10 + (v2 + v3) * 10,
                                   t1=v1, t2=v1 + v2, t3=v2 + v3),
          cevap=("d", "m", 0),
     celdirici=lambda v: [20 * (v["v1"] + v["v2"] + v["v3"]),                               # yamuk alanı yerine dikdörtgen alanı
                          30 * v["v3"],                                                          # tek üçgen varsayıldı
                          10 * (v["v1"] + v["v2"] + v["v3"]),                               # ortalama hız hatası
                          v["d"] - 5 * v["v1"],                                                # ilk ivmelenme üçgeni unutuldu
                          v["d"] / 2],                                                           # 2'ye bölme hatası
     beklenen={"d": 980},
     cozum=r"""Toplam mesafe, v-t grafiğinin altındaki alana eşittir. Alanı trapezlere bölerek hesaplayabiliriz.

- Alan 1 (0-20s): ½ \* (0 + {v1}) \* 20 = {s1:g} m

- Alan 2 (20-40s): ½ \* ({v1} + {v2}) \* (40-20) = ½ \* {t2:g} \* 20 = {s2:g} m

- Alan 3 (40-60s): ½ \* ({v2} + {v3}) \* (60-40) = ½ \* {t3:g} \* 20 = {s3:g} m\
  Toplam Mesafe = {s1:g} + {s2:g} + {s3:g} = **{d:g} m**""")


def _s29(v, x0):
    y = math.sqrt(4 * x0)
    d1 = 2 / y
    d2 = -4 / y ** 3
    rho = (1 + d1 ** 2) ** 1.5 / abs(d2)
    return dict(y=y, d1=d1, d2=d2, rho=rho, v2=v * v, a=v * v / rho, c4=4 * x0)


ekle(no=29, zorluk="zor",
     params={"v": P(4, "m/s", 2, 6, 2), "x0": P(4, "m", 1, 9, 1, liste=(1, 4, 9))},
     metin="y² = 4x parabolik yolu üzerinde hareket eden bir parçacığın hızı sabit {v} m/s'dir. Parçacık x={x0} m konumundayken ivmesinin büyüklüğü nedir?",
     hesap=_s29,      cevap=("a", "m/s²", 3),
     celdirici=lambda v: [v["v"] / v["rho"],                                                   # v² yerine v alındı
                          float(v["rho"]),                                                       # ivme yerine eğrilik yarıçapı verildi
                          v["v"]**2 / ((1 + v["d1"]**2)**1.5),                                 # formüldeki payda unutuldu
                          v["v"]**2 * v["rho"] / 100,                                         # bölme yerine çarpma yapıldı
                          v["a"] / 2],                                                           # 2'ye bölündü
     beklenen={"a": 0.716},
     cozum=r"""Sabit hız, teğetsel ivmenin sıfır olduğu (at = 0) anlamına gelir. İvme, sadece normal bileşenden oluşur: a = an = v²/ρ.

1.  **Eğrilik Yarıçapını (ρ) Bulma:**

    - dy/dx: 2y(dy/dx) = 4 =\> dy/dx = 2/y

    - d²y/dx²: = -4/y³

    - x={x0} iken y=√(4\*{x0}) = {y:g}.

    - dy/dx = 2/{y:g} = {d1:.3g}

    - d²y/dx² = -4/{y:g}³ = {d2:.4g}

    - ρ = [1 + (dy/dx)²]^(3/2) / |d²y/dx²| ≈ {rho:.2f} m

2.  **İvmeyi Bulma:**\
    a = an = v²/ρ = {v}² / {rho:.2f} ≈ {a:.3f} m/s²""")

ekle(no=30, zorluk="zor",
     params={"c1": P(12, "", 6, 18, 6), "c2": P(3, "", 3, 9, 3), "s0": P(15, "m", 5, 25, 5)},
     metin="Bir parçacığın ivmesi a = ({c1}t - {c2}t¹/²) m/s²'dir. t=0'da parçacık durgun ve konumu s={s0} m ise, t=4 saniyedeki konumunu bulunuz.",
     hesap=lambda c1, c2, s0: dict(p1=c1 / 2, p2=2 * c2 / 3, q1=c1 / 6, q2=4 * c2 / 15,
                                   s=c1 / 6 * 4 ** 3 - 4 * c2 / 15 * 4 ** 2.5 + s0,
                                   w1=c1 / 6 * 64, w2=4 * c2 / 15 * 32),
          cevap=("s", "m", 1),
     celdirici=lambda v: [v["s"] - v["s0"],                                                   # s0 eklenmedi
                          (v["c1"] / 2 * 4**2 - 2 * v["c2"] / 3 * 4**1.5) + v["s0"],         # bir kez integral alındı
                          (v["c1"] * 4**3 - v["c2"] * 4**2.5) + v["s0"],                     # integral paydaları unutuldu
                          (v["c1"] / 6 * 64 + 4 * v["c2"] / 15 * 32) + v["s0"],             # ikinci terim toplandı
                          (v["c1"] * 4 - v["c2"] * math.sqrt(4)) + v["s0"]],                  # integral alınmadan a(4) hesaplandı
     beklenen={"s": 117.4},
     cozum=r"""1.  **Hız Fonksiyonunu Bulma (İntegral):**\
    v(t) = ∫a dt = ∫({c1}t - {c2}t¹/²) dt = {p1:g}t² - {p2:g}t³/² + C₁\
    v(0)=0 olduğundan C₁=0.

2.  **Konum Fonksiyonunu Bulma (İntegral):**\
    s(t) = ∫v dt = {q1:g}t³ - {q2:g}t⁵/² + C₂\
    s(0)={s0} olduğundan C₂={s0}. Yani s(t) = {q1:g}t³ - {q2:g}t⁵/² + {s0}.

3.  **t=4 için Konumu Hesaplama:**\
    s(4) = {q1:g}(4)³ - {q2:g}(4)⁵/² + {s0}\
    s(4) = {w1:g} - {w2:g} + {s0} = {s:.1f} m""")


if __name__ == "__main__":
    calistir(S, Path(__file__).parent / "_out" / "u2")
