"""Ünite 5 (İmpuls-Momentum) sayısal soru solver'ları. Çalıştır: python u5.py"""
import math
from pathlib import Path

from core import P, Soru, calistir

U = 5
g = 9.81
S = []


def ekle(**kw):
    S.append(Soru(unite=U, **kw))


def bin_(x):
    """15000 -> '15.000' (md'deki yazım)."""
    return f"{int(x):,}".replace(",", ".")


def yon(v):
    return "sağa" if v > 0 else "sola"


# ---------------------------------------------------------------- KOLAY
ekle(no=1, zorluk="kolay",
     params={"F": P(200, "N", 100, 400, 50), "t": P(10, "s", 5, 20, 5)},
     metin="Şekildeki yatay düzlemde duran bir taşa {F} N'luk sabit bir kuvvet şekildeki gibi uygulanmaktadır. Kuvvetin {t} saniye boyunca taşa uyguladığı itme (impuls) nedir?",
     hesap=lambda F, t: dict(Fx=F * math.cos(math.radians(45)), I=F * math.cos(math.radians(45)) * t),
          cevap=("I", "N·s", 1),
     celdirici=lambda v: [v["F"] * v["t"],                                                     # cos45 açısı unutuldu
                          v["F"] * math.cos(45) * v["t"],                                      # derece yerine radyan alındı
                          0.5 * v["I"],                                                        # 1/2 çarpanı eklendi
                          2 * v["I"],                                                          # 2 ile çarpıldı
                          v["F"] * math.cos(math.radians(45))],                                # zaman çarpanı unutuldu
     beklenen={"I": 1414.214},
     sekil={"dosya": "S1_1.png", "etiketler": [("F", "200 N", lambda F: f"{F:g} N")]},
     cozum=r"""İmpuls = yatay kuvvet bileşeni × zaman (θ = 45°).\
F_x = {F} cos 45° = {Fx:.3f} N\
I = F_x · t = {Fx:.3f} × {t} = {I:.1f} N·s""")

ekle(no=2, zorluk="kolay",
     params={"m": P(100, "kg", 50, 200, 50), "F": P(200, "N", 100, 400, 50), "t": P(10, "s", 5, 20, 5)},
     metin="Kütlesi {m} kg olan ve sürtünmesiz yatay düzlemde duran bir taşa, yatay bileşeni hareket yönünde olan {F} N'luk net bir kuvvet etki etmektedir. {t} saniye sonra taşın hızı ne olur?",
     hesap=lambda m, F, t: dict(I=F * math.cos(math.radians(45)) * t, v=F * math.cos(math.radians(45)) * t / m),
          cevap=("v", "m/s", 3),
     celdirici=lambda v: [v["F"] * v["t"] / v["m"],                                           # cos45 unutuldu
                          v["F"] * math.cos(math.radians(45)) * v["t"],                        # kütleye bölünmesi unutuldu (itme verildi)
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          2 * v["v"],                                                          # 2 ile çarpıldı
                          v["v"] / 4],                                                         # 4'e bölündü
     beklenen={"v": 14.142},
     sekil={"dosya": "S2_1.png", "etiketler": [("F", "200 N", lambda F: f"{F:g} N")]},
     cozum=r"""İmpuls = momentum değişimi: F_x · Δt = m · Δv\
{F} cos 45° × {t} = {m} · (v_son − 0)\
{I:.3f} = {m} · v_son ⇒ v_son = {v:.3f} m/s""")

ekle(no=3, zorluk="kolay", md_kontrol=False,  # md: m/s^{2} üst simgesi
    
     params={"m": P(2, "kg", 1, 4, 1), "v": P(3, "m/s", 2, 6, 1), "th": P(45, "°", 30, 60, 15)},
     metin="{m} kg kütleli bir blok, sürtünmesiz {th}° eğimli bir yüzeyden yukarı doğru {v} m/s ilk hızla fırlatılıyor. Bloğun durana kadar geçen süreyi hesaplayınız. (g = 9.81 m/s²)",
     hesap=lambda m, v, th: dict(W=m * g * math.sin(math.radians(th)), mv=m * v, t=v / (g * math.sin(math.radians(th)))),
          cevap=("t", "s", 3),
     celdirici=lambda v: [v["v"] / (9.81 * math.tan(math.radians(v["th"]))),                  # sin yerine tan kullanıldı
                          v["v"] / math.sin(math.radians(v["th"])),                           # yer çekimi g unutuldu
                          v["v"] / (10 * math.sin(math.radians(v["th"]))),                     # g=10 kullanıldı
                          v["v"] / 9.81,                                                       # eğim açısı ihmal edildi
                          2 * v["t"]],                                                         # 2 ile çarpıldı
     beklenen={"t": 0.4320},
     cozum=r"""Hareket yönü yukarı pozitif olsun. Aşağı doğru ağırlık bileşeni kuvvet uygular.\
Momentum ilkesi: m·v₁ + Σ∫F dt = m·v₂\
{m}({v}) − ({m} · 9.81 · sin {th}°) · t = 0\
{mv:g} − {W:.2f}t = 0 ⇒ t ≈ {t:.3f} s""")

ekle(no=4, zorluk="kolay",
     params={"F": P(10, "N", 5, 20, 5), "t1": P(2, "s", 1, 3, 1), "t2": P(4, "s", 4, 6, 1)},
     metin="Bir cisme etki eden kuvvetin zamana bağlı grafiği verilmiştir. Kuvvet 0-{t1} saniye arasında 0'dan {F} N'a doğrusal artmakta, {t1}-{t2} saniye arasında {F} N sabit kalmaktadır. Cisme etki eden toplam itmeyi (impuls) bulunuz.",
     hesap=lambda F, t1, t2: dict(A1=t1 * F / 2, A2=(t2 - t1) * F, I=t1 * F / 2 + (t2 - t1) * F, dt=t2 - t1),
          cevap=("I", "N·s", 1),
     celdirici=lambda v: [v["t2"] * v["F"],                                                   # üçgen alanındaki 1/2 unutuldu
                          float(v["A1"]),                                                      # sadece üçgen alanı alındı
                          float(v["A2"]),                                                      # sadece dikdörtgen alanı alındı
                          v["I"] / 2,                                                          # tüm alan 2'ye bölündü
                          1.5 * v["I"]],                                                       # 1.5 ile çarpıldı
     beklenen={"I": 30},
     cozum=r"""İtme = Kuvvet-Zaman grafiğinin altındaki alan.\
Alan 1 (Üçgen): ({t1} × {F})/2 = {A1:g} N·s\
Alan 2 (Dikdörtgen): ({t2} − {t1}) × {F} = {A2:g} N·s\
Toplam İtme = {A1:g} + {A2:g} = {I:g} N·s""")

ekle(no=5, zorluk="kolay",
     params={"m1": P(15000, "kg", 10000, 20000, 5000), "v1": P(1.5, "m/s", 1, 3, 0.5), "m2": P(12000, "kg", 8000, 16000, 2000)},
     metin="{m1s} kg kütleli bir vagon {v1} m/s hızla giderken, ters yönden gelen {m2s} kg kütleli ve 0.75 m/s hıza sahip başka bir vagonla çarpışıp kenetleniyor. Kenetlendikten sonraki ortak hızları ne olur?",
     hesap=lambda m1, v1, m2: dict(m1s=bin_(m1), m2s=bin_(m2), p1=m1 * v1, p2=m2 * 0.75, mt=m1 + m2,
                                   dp=m1 * v1 - m2 * 0.75, v=(m1 * v1 - m2 * 0.75) / (m1 + m2), yon=yon(m1 * v1 - m2 * 0.75)),
          cevap=("v", "m/s", 3),
     celdirici=lambda v: [(v["m1"] * v["v1"] + v["m2"] * 0.75) / (v["m1"] + v["m2"]),         # zıt yön eksi yerine artı alındı
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          1.5 * v["v"],                                                        # 1.5 ile çarpıldı
                          2.0 * v["v"],                                                        # 2 ile çarpıldı
                          0.25 * v["v"]],                                                      # 4'e bölündü
     beklenen={"v": 0.5},
     cozum=r"""Momentum korunumu: Σmv₁ = Σmv₂\
({m1} · {v1}) + ({m2} · −0.75) = ({m1} + {m2}) · v_ortak\
{p1:g} − {p2:g} = {mt} · v_ortak\
{dp:g} = {mt} · v_ortak ⇒ v_ortak = {v:.3g} m/s ({yon})""")

ekle(no=6, zorluk="kolay",
     params={"mA": P(2000, "kg", 1000, 3000, 500), "vA": P(2, "m/s", 1, 4, 1), "vB": P(4, "m/s", 2, 6, 1)},
     metin="A aracı {mA} kg kütleli ve sağa doğru {vA} m/s hızla, B aracı 1500 kg kütleli ve sola doğru {vB} m/s hızla hareket etmektedir. Kafa kafaya çarpışıp kenetlenirlerse çarpışma sonrası hız ne olur?",
     hesap=lambda mA, vA, vB: dict(pA=mA * vA, pB=1500 * vB, dp=mA * vA - 1500 * vB, mt=mA + 1500,
                                   v=(mA * vA - 1500 * vB) / (mA + 1500), yon=yon(mA * vA - 1500 * vB)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [(v["mA"] * v["vA"] + 1500 * v["vB"]) / (v["mA"] + 1500),           # zıt yön eksi yerine artı alındı
                          -float(v["v"]),                                                      # yön hatası (ters işaret)
                          (v["mA"] * v["vA"] - 1500 * v["vB"]) / v["mA"],                     # paydada B kütlesi unutuldu
                          2 * v["v"],                                                          # 2 ile çarpıldı
                          0.5 * v["v"]],                                                       # 1/2 çarpanı eklendi
     beklenen={"v": -0.5714},
     cozum=r"""Σmv₁ = Σmv₂ (sağ yön pozitif)\
({mA} · {vA}) + (1500 · −{vB}) = ({mA} + 1500) · v_ortak\
{pA:g} − {pB:g} = {mt} · v_ortak\
{dp:g} = {mt} · v_ortak ⇒ v_ortak = {v:.2f} m/s ({yon})""")

ekle(no=7, zorluk="kolay",
     params={"v": P(500, "m/s", 300, 700, 100), "m": P(0.002, "kg", 0.001, 0.005, 0.001), "dt": P(0.001, "s", 0.001, 0.004, 0.001)},
     metin="{v} m/s namlu çıkış hızına sahip {m} kg'lık bir mermi {dt} saniye içinde namludan çıkmaktadır. Mermiye etki eden ortalama kuvveti bulunuz.",
     hesap=lambda v, m, dt: dict(mv=m * v, F=m * v / dt),
          cevap=("F", "N", 0),
     celdirici=lambda v: [v["m"] * v["v"] * v["dt"],                                          # dt ile bölmek yerine çarpıldı
                          v["m"] * v["v"],                                                     # süreye bölünmedi (momentum değişimi)
                          0.5 * v["F"],                                                        # 1/2 çarpanı eklendi
                          2.0 * v["F"],                                                        # 2 ile çarpıldı
                          1.5 * v["F"]],                                                       # 1.5 ile çarpıldı
     beklenen={"F": 1000},
     cozum=r"""F_ort · Δt = m · Δv\
F_ort · {dt} = {m} · ({v} − 0)\
F_ort = {mv:g}/{dt} = {F:.0f} N""")

# ---------------------------------------------------------------- ORTA
ekle(no=8, zorluk="orta",
     params={"mc": P(75, "kg", 60, 90, 15), "ma": P(50, "kg", 40, 60, 10), "vr": P(3, "m/s", 2, 4, 1)},
     metin="Sürtünmesiz ray üzerinde duran {ma} kg kütleli A aracı üzerindeki {mc} kg kütleli çocuk, araca göre {vr} m/s bağıl hızla yatay olarak atlıyor. Çocuğun yere göre hızı nedir?",
     hesap=lambda mc, ma, vr: dict(mt=mc + ma, va=-mc * vr / (mc + ma), vc=ma * vr / (mc + ma), nmcvr=mc * vr),
          cevap=("vc", "m/s", 2),
     celdirici=lambda v: [v["mc"] * v["vr"] / (v["mc"] + v["ma"]),                            # çocuğun hızı yerine araba hızı hesaplandı
                          float(v["vr"]),                                                      # bağıl hız doğrudan yer hızı sanıldı
                          v["vr"] - v["vc"],                                                   # bağıl hızdan çıkarıldı
                          0.5 * v["vc"],                                                       # 1/2 çarpanı eklendi
                          2 * v["vc"]],                                                        # 2 ile çarpıldı
     beklenen={"vc": 1.2, "va": -1.8},
     cozum=r"""Momentum korunumu: 0 = m_c · v_c + m_a · v_a\
Bağıl hız: v_c = v_a + v_c/a ⇒ v_c = v_a + {vr}\
0 = {mc}(v_a + {vr}) + {ma}v_a ⇒ {mt}v_a = −{nmcvr:g} ⇒ v_a = {va:.3g} m/s\
v_c = {va:.3g} + {vr} = {vc:.3g} m/s""")

ekle(no=9, zorluk="orta",
     params={"mc": P(75, "kg", 60, 90, 15), "ma": P(50, "kg", 40, 60, 10), "vr": P(3, "m/s", 2, 4, 1)},
     metin="Sürtünmesiz ray üzerinde duran {ma} kg kütleli A aracı üzerindeki {mc} kg kütleli çocuk, araca göre {vr} m/s bağıl hızla yatay olarak atlıyor. Çocuk atladıktan hemen sonra A aracının hızı (büyüklük olarak) nedir?",
     hesap=lambda mc, ma, vr: dict(mt=mc + ma, va=-mc * vr / (mc + ma), vaa=mc * vr / (mc + ma), nmcvr=mc * vr),
          cevap=("vaa", "m/s", 2),
     celdirici=lambda v: [v["ma"] * v["vr"] / (v["mc"] + v["ma"]),                            # araba yerine çocuğun hızı hesaplandı
                          float(v["vr"]),                                                      # bağıl hız doğrudan araba hızı sanıldı
                          2 * v["vaa"],                                                        # 2 ile çarpıldı
                          0.5 * v["vaa"],                                                      # 1/2 çarpanı eklendi
                          1.5 * v["vaa"]],                                                     # 1.5 ile çarpıldı
     beklenen={"vaa": 1.8},
     cozum=r"""Momentum korunumu: 0 = m_c · v_c + m_a · v_a\
Bağıl hız: v_c = v_a + v_c/a ⇒ v_c = v_a + {vr}\
0 = {mc}(v_a + {vr}) + {ma}v_a ⇒ {mt}v_a = −{nmcvr:g} ⇒ v_a = {va:.3g} m/s\
Büyüklük: |v_a| = {vaa:.3g} m/s""")

ekle(no=10, zorluk="orta",
     params={"t": P(80, "s", 40, 120, 20), "vk": P(40, "km/h", 20, 60, 10)},
     metin="50 tonluk bir lokomotif ve her biri 30 tonluk 3 vagon duruştan harekete geçiyor. Trenin {t} saniyede {vk} km/h ({v:.2f} m/s) hıza ulaşması için lokomotifin tekerleklerine etki eden **ortalama** çekiş kuvveti (F) ne olmalıdır? (Sürtünmeleri ihmal ediniz).",
     hesap=lambda t, vk: dict(v=round(vk / 3.6, 2), mt=140000, F=140000 * round(vk / 3.6, 2) / t, Fkn=140000 * round(vk / 3.6, 2) / t / 1000),
          cevap=("F", "N", 0),
     celdirici=lambda v: [140000 * v["vk"] / v["t"],                                          # km/h m/s'ye çevrilmedi
                          50000 * v["v"] / v["t"],                                             # sadece lokomotif kütlesi alındı (vagonlar unutuldu)
                          90000 * v["v"] / v["t"],                                             # sadece vagon kütlesi alındı (lokomotif unutuldu)
                          0.5 * v["F"],                                                        # 1/2 çarpanı eklendi
                          2.0 * v["F"]],                                                       # 2 ile çarpıldı
     beklenen={"F": 19442.5},
     sekil={"dosya": "S10_1.png", "etiketler": [("F", "F = 30 kN", lambda F: "F")]},
     cozum=r"""Toplam kütle = 50 + 3(30) = 140 ton = 140.000 kg\
F · Δt = m · Δv\
F · {t} = 140.000 · {v:.2f}\
F = {F:.0f} N ≈ {Fkn:.1f} kN""")

ekle(no=11, zorluk="orta",
     params={"mA": P(2500, "kg", 2000, 3000, 500), "mB": P(1250, "kg", 1000, 1500, 250), "vr": P(2, "m/s", 1, 4, 1)},
     metin="{mA} kg'lık bir cip (A), {mB} kg'lık bir arabayı (B) vinç halatı kendine göre {vr} m/s hızla çekmektedir. Çarpıştıkları andaki hızlarını momentum korunumu ile ilişkilendiriniz (Başlangıçta duruyorlar, sürtünmeyi ihmal ediniz).",
     hesap=lambda mA, mB, vr: dict(k=mA / mB, vA=vr * mB / (mA + mB), vB=-vr * mA / (mA + mB), r3=1 + mA / mB),
          cevap=None,  # test dışı: birden çok bağımsız sonuç isteyenler (vA ve vB)
     beklenen={"vA": 0.6667, "vB": -1.3333},
     cozum=r"""Momentum korunumu: m_A·v_A + m_B·v_B = 0\
{mA}v_A + {mB}v_B = 0 ⇒ v_B = −{k:g}v_A\
Bağıl hız: v_A/B = v_A − v_B = {vr} (halat sarma hızı)\
v_A − (−{k:g}v_A) = {vr} ⇒ {r3:g}v_A = {vr} ⇒ v_A = {vA:.2f} m/s, v_B = {vB:.2f} m/s""")

ekle(no=12, zorluk="orta",
     params={"mm": P(0.1, "kg", 0.05, 0.2, 0.05), "v": P(900, "m/s", 600, 1000, 100)},
     metin="300 kg'lık bir araba üzerindeki 75 kg'lık bir adam, {mm} kg'lık bir mermiyi arabaya göre {v} m/s hızla yatay olarak ateşliyor. Ateşleme sonrası arabanın hızı ne olur? (Başlangıçta duruyorlar, sürtünmeyi ihmal ediniz).",
     hesap=lambda mm, v: dict(mv=mm * v, mt=375 + mm, va=-mm * v / (375 + mm)),
          cevap=("va", "m/s", 2),
     celdirici=lambda v: [-v["mm"] * v["v"] / 300,                                            # adamın kütlesi (75 kg) unutuldu
                          abs(v["va"]),                                                        # geri tepme yönü pozitif alındı
                          2 * v["va"],                                                         # 2 ile çarpıldı
                          0.5 * v["va"],                                                       # 1/2 çarpanı eklendi
                          1.5 * v["va"]],                                                      # 1.5 ile çarpıldı
     beklenen={"va": -0.24},
     cozum=r"""Sistem momentumu korunur (başlangıçta 0).\
0 = m_mermi·v_mermi + (m_adam + m_araba)·v_araba\
v_mermi = v_araba + {v}\
0 = {mm}(v_araba + {v}) + 375v_araba\
{mt:g}v_araba = −{mv:g} ⇒ v_araba ≈ {va:.2f} m/s""")

ekle(no=13, zorluk="orta",
     params={"ms": P(70, "kg", 50, 90, 10), "mb": P(8, "kg", 4, 12, 2), "vr": P(2, "m/s", 1, 4, 1)},
     metin="Buz pateni yapan {ms} kg kütleli bir sporcu, elindeki {mb} kg'lık bir bloğu kendisine göre {vr} m/s hızla yatay olarak fırlatıyor. Başlangıçta duran sporcunun fırlatma sonrası hızı ne olur?",
     hesap=lambda ms, mb, vr: dict(mt=ms + mb, mbv=mb * vr, vs=-mb * vr / (ms + mb)),
          cevap=("vs", "m/s", 3),
     celdirici=lambda v: [abs(v["vs"]),                                                       # geri tepme yönü pozitif alındı
                          -v["mb"] * v["vr"] / v["ms"],                                       # paydada blok kütlesi eklenmedi
                          2 * v["vs"],                                                         # 2 ile çarpıldı
                          0.5 * v["vs"],                                                       # 1/2 çarpanı eklendi
                          1.5 * v["vs"]],                                                      # 1.5 ile çarpıldı
     beklenen={"vs": -0.2051},
     cozum=r"""0 = m_blok·v_blok + m_sporcu·v_sporcu\
v_blok = v_sporcu + {vr} (bağıl hız)\
0 = {mb}(v_sporcu + {vr}) + {ms}v_sporcu\
{mt}v_sporcu = −{mbv:g} ⇒ v_sporcu = {vs:.3f} m/s""")

ekle(no=14, zorluk="orta",
     params={"vA": P(6, "m/s", 4, 10, 2), "e": P(0.6, "", 0.2, 0.8, 0.2), "mB": P(5, "kg", 2, 6, 1)},
     metin="0.5 kg kütleli A topu {vA} m/s hızla sağa giderken, durmakta olan {mB} kg kütleli B bloğuna çarpıyor. Geri dönme (Restitüsyon) katsayısı e = {e} ise çarpışmadan hemen sonra B'nin hızı ne olur? e = (v_B2 − v_A2)/(v_A1 − v_B1)",
     hesap=lambda vA, e, mB: dict(p=0.5 * vA, ev=e * vA, hv=0.5 * e * vA, mt=0.5 + mB,
                                  vB=0.5 * vA * (1 + e) / (0.5 + mB)),
          cevap=("vB", "m/s", 2),
     celdirici=lambda v: [0.5 * v["vA"] * v["e"] / (0.5 + v["mB"]),                           # (1+e) yerine e kullanıldı
                          0.5 * v["vA"] / (0.5 + v["mB"]),                                     # (1+e) unutuldu (e=0 sanıldı)
                          0.5 * v["vA"] * (1 + v["e"]) / v["mB"],                             # paydada topun kütlesi eklenmedi
                          2 * v["vB"],                                                         # 2 ile çarpıldı
                          0.5 * v["vB"]],                                                      # 1/2 çarpanı eklendi
     beklenen={"vB": 0.8727},
     cozum=r"""Momentum korunumu: 0.5({vA}) + 0 = 0.5v_A2 + {mB}v_B2 ⇒ {p:g} = 0.5v_A2 + {mB}v_B2 …(1)\
Restitüsyon: {e} = (v_B2 − v_A2)/{vA} ⇒ v_A2 = v_B2 − {ev:g} …(2)\
(2)→(1): {p:g} = 0.5(v_B2 − {ev:g}) + {mB}v_B2 ⇒ {p:g} + {hv:g} = {mt:g}v_B2\
v_B2 ≈ {vB:.2f} m/s""")

ekle(no=15, zorluk="orta",
     params={"m1": P(5000, "kg", 4000, 6000, 1000), "v1": P(30, "km/h", 20, 40, 10), "v2": P(10, "km/h", 5, 15, 5)},
     metin="{m1} kg'lık kamyon {v1} km/h hızla giderken, aynı yönde {v2} km/h hızla giden 2000 kg'lık araca arkadan çarpıyor. Çarpışma sonrası araçlar kenetlenirse (plastik çarpışma), ortak hız ne olur?",
     hesap=lambda m1, v1, v2: dict(u1=round(v1 / 3.6, 2), u2=round(v2 / 3.6, 2), mt=m1 + 2000,
                                   p1=m1 * round(v1 / 3.6, 2), p2=2000 * round(v2 / 3.6, 2),
                                   pt=m1 * round(v1 / 3.6, 2) + 2000 * round(v2 / 3.6, 2),
                                   v=(m1 * round(v1 / 3.6, 2) + 2000 * round(v2 / 3.6, 2)) / (m1 + 2000),
                                   vk=3.6 * (m1 * round(v1 / 3.6, 2) + 2000 * round(v2 / 3.6, 2)) / (m1 + 2000)),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [(v["m1"] * v["v1"] + 2000 * v["v2"]) / (v["m1"] + 2000),           # km/h m/s'ye çevrilmedi
                          (v["m1"] * v["u1"] - 2000 * v["u2"]) / (v["m1"] + 2000),           # aynı yön eksi alındı
                          (v["u1"] + v["u2"]) / 2,                                            # kütleler hesaba katılmadan ortalama alındı
                          2 * v["v"],                                                          # 2 ile çarpıldı
                          0.5 * v["v"]],                                                       # 1/2 çarpanı eklendi
     beklenen={"v": 6.7443},
     cozum=r"""{v1} km/h = {u1:.2f} m/s, {v2} km/h = {u2:.2f} m/s\
Σmv₁ = Σmv₂\
{m1}({u1:.2f}) + 2000({u2:.2f}) = ({mt})v_ortak\
{p1:.0f} + {p2:.0f} = {pt:.0f} = {mt}v_ortak\
v_ortak ≈ {v:.2f} m/s ({vk:.1f} km/h)""")

ekle(no=16, zorluk="orta",
     params={"mA": P(10, "kg", 6, 12, 2), "vA": P(2, "m/s", 1, 4, 1), "t": P(3, "s", 2, 5, 1)},
     metin="{mA} kg'lık A silindiri aşağı doğru {vA} m/s hızla hareket ederken, ipe bağlı 8 kg'lık B silindiri yukarı doğru hareket etmektedir. {t} saniye sonraki hızları bulmak için kullanılacak temel impuls-momentum denklemini (A cismi için) yazınız. (İp gerilmesi T).",
     hesap=lambda mA, vA, t: dict(mv=mA * vA, W=mA * g * t, T3=t),
          cevap=None,  # test dışı: denklem veya sembolik cevaplı (impuls-momentum denklemi)
     beklenen={"W": 294.3},
     sekil={"dosya": "S16_1.png", "etiketler": [("mA", [141, 216, 179, 241], lambda m: f"{m:g} kg"),   # json'da A/B etiketleri yer değiştirmiş
                                                 ("mA", [24, 252, 64, 274], lambda m: "8 kg")]},
     cozum=r"""A cismi için (aşağı yön pozitif):\
m_A·v_A1 + Σ∫F dt = m_A·v_A2\
{mA}({vA}) + ({mA} · 9.81 · {t}) − (T · {t}) = {mA}v_A2\
{mv:g} + {W:.1f} − {t}T = {mA}v_A2""")

ekle(no=17, zorluk="orta",
     params={"mA": P(10, "kg", 5, 20, 5), "mB": P(50, "kg", 30, 70, 10), "t": P(2, "s", 1, 4, 1)},
     metin="Makaralı sistemde A bloğu {mA} kg, B bloğu {mB} kg'dır. Sistem serbest bırakıldıktan {t} saniye sonra B bloğunun hızı ne olur? (İp gerilmesini ve ivmeyi sabit varsayınız, basit dinamik de kullanılabilir ancak impuls ile çözünüz).",
     kisit=lambda mA, mB, t: mB > mA,
     hesap=lambda mA, mB, t: dict(dm=mB - mA, mt=mB + mA, a=(mB - mA) * g / (mB + mA), v=(mB - mA) * g / (mB + mA) * t),
          cevap=("v", "m/s", 2),
     celdirici=lambda v: [(v["mB"] - v["mA"]) * 9.81 * v["t"] / v["mB"],                     # paydada A kütlesi eklenmedi
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          2.0 * v["v"],                                                        # 2 ile çarpıldı
                          3.0 * v["v"],                                                        # 3 ile çarpıldı
                          0.25 * v["v"]],                                                      # 4'e bölündü
     beklenen={"a": 6.54, "v": 13.08},
     sekil={"dosya": "S17_1.png", "etiketler": [("mB", [249, 219, 303, 243], lambda m: f"{m:g} kg"),
                                                 ("mA", [90, 220, 137, 242], lambda m: f"{m:g} kg")]},
     cozum=r"""Sistem ivmesi\
a = (m_B − m_A)g/(m_B + m_A) = ({dm} · 9.81)/{mt} = {a:.2f} m/s²\
v = v₀ + a·t = 0 + {a:.2f} · {t} = {v:.2f} m/s""")

ekle(no=18, zorluk="orta", md_kontrol=False,  # md: r_{1}, r_{2} alt simgeleri
    
     params={"v1": P(5, "m/s", 3, 8, 1), "r1": P(1.5, "m", 1, 2, 0.5), "r2": P(1.2, "m", 0.6, 1.2, 0.3)},
     metin="Şekildeki sistemde elastik ip ucundaki 3 kg'lık disk yatay düzlemde dönmektedir. r₁ = {r1} m'de teğetsel hız {v1} m/s ise, ip kısaltılıp r₂ = {r2} m olduğunda diskin hızı ne olur?",
     kisit=lambda v1, r1, r2: r2 < r1,
     hesap=lambda v1, r1, r2: dict(H=3 * v1 * r1, c=3 * r2, v2=v1 * r1 / r2),
          cevap=("v2", "m/s", 2),
     celdirici=lambda v: [v["v1"] * v["r2"] / v["r1"],                                        # yarıçap oranı ters çevrildi (r2/r1)
                          v["v1"] * (v["r1"] / v["r2"])**2,                                   # yarıçap oranının karesi alındı
                          0.5 * v["v2"],                                                       # 1/2 çarpanı eklendi
                          2 * v["v2"],                                                         # 2 ile çarpıldı
                          1.5 * v["v2"]],                                                      # 1.5 ile çarpıldı
     beklenen={"v2": 6.25},
     sekil={"dosya": "S18_1.png", "etiketler": [("v1", "v = 5 m/s", lambda v: f"v = {v:g} m/s")]},
     cozum=r"""Açısal momentum korunumu: H₁ = H₂ ⇒ m·v₁·r₁ = m·v₂·r₂\
3 · {v1} · {r1} = 3 · v₂ · {r2}\
{H:g} = {c:g}v₂ ⇒ v₂ = {v2:.2f} m/s""")

ekle(no=19, zorluk="orta",
     params={"mA": P(2, "kg", 1, 4, 1), "vA": P(4, "m/s", 2, 6, 2), "e": P(0.8, "", 0.4, 0.8, 0.2)},
     metin="{mA} kg'lık bir top, ipe asılı 20 kg'lık duran bir bloğa {vA} m/s hızla çarpıyor. Restitüsyon katsayısı e = {e}. Çarpışmadan hemen sonra bloğun hızı nedir?",
     hesap=lambda mA, vA, e: dict(p=mA * vA, ev=e * vA, mt=mA + 20, vB=mA * vA * (1 + e) / (mA + 20), s=(1 + e) * vA),
          cevap=("vB", "m/s", 2),
     celdirici=lambda v: [v["mA"] * v["vA"] * v["e"] / (v["mA"] + 20),                        # (1+e) yerine e kullanıldı
                          v["mA"] * v["vA"] / (v["mA"] + 20),                                 # (1+e) unutuldu
                          v["mA"] * v["vA"] * (1 + v["e"]) / 20,                              # paydada top kütlesi eklenmedi
                          2 * v["vB"],                                                         # 2 ile çarpıldı
                          0.5 * v["vB"]],                                                      # 1/2 çarpanı eklendi
     beklenen={"vB": 0.6545},
     sekil={"dosya": "S19_1.png", "etiketler": [("vA", "4 m/s", lambda v: f"{v:g} m/s")]},
     cozum=r"""Momentum: {mA}({vA}) + 0 = {mA}v_A2 + 20v_B2 ⇒ {p:g} = {mA}v_A2 + 20v_B2\
Restitüsyon: {e} = (v_B2 − v_A2)/{vA} ⇒ {ev:g} = v_B2 − v_A2\
Birinci denklem ile ({mA} × ikinci denklem) toplanırsa: {p:g} + {mA} · {ev:g} = {mt}v_B2\
v_B2 ≈ {vB:.2f} m/s""")

ekle(no=20, zorluk="orta",
     params={"m": P(1500, "kg", 900, 2700, 450)},
     metin="{m} kg'lık bir roket kızağına etki eden itki kuvvetinin zamana göre değişimi şekilde (kN cinsinden) verilmiştir. Kızağın t = 2.5 s'deki hızı nedir? (Başlangıç hızı 0, sürtünme ihmal edilecektir.)",
     hesap=lambda m: dict(I=135000, v=135000 / m),
          cevap=("v", "m/s", 1),
     celdirici=lambda v: [135 / v["m"],                                                        # kN N'a çevrilmedi
                          2.0 * v["v"],                                                        # 2 ile çarpıldı
                          0.5 * v["v"],                                                        # 1/2 çarpanı eklendi
                          1.5 * v["v"],                                                        # 1.5 ile çarpıldı
                          0.25 * v["v"]],                                                      # 4'e bölündü
     beklenen={"v": 90},
     cozum=r"""İtme, kuvvet-zaman grafiğinin altında kalan alandır. Grafik 0.5 s genişliğinde 5 basamaktan oluşur: 30, 60, 90, 60 ve 30 kN.\
I = 0.5 · (30 + 60 + 90 + 60 + 30) = 135 kN·s = 135000 N·s\
I = m·Δv ⇒ 135000 = {m} · v_son\
v_son = {v:.4g} m/s""")

ekle(no=21, zorluk="orta",
     params={"v1": P(5, "m/s", 3, 7, 1), "r1": P(0.5, "m", 0.5, 1, 0.25), "r2": P(0.25, "m", 0.25, 0.5, 0.25)},
     metin="2 kg'lık top, {r1} m yarıçaplı dairesel yolda {v1} m/s hızla dönmektedir. Topa teğetsel bir kuvvet etki etmemektedir. İp çekilerek yarıçap {r2} m'ye düşürülürse yeni hız ne olur?",
     kisit=lambda v1, r1, r2: r2 < r1,
     hesap=lambda v1, r1, r2: dict(H=v1 * r1, v2=v1 * r1 / r2),
          cevap=("v2", "m/s", 1),
     celdirici=lambda v: [v["v1"] * v["r2"] / v["r1"],                                        # yarıçap oranı ters çevrildi
                          v["v1"] * (v["r1"] / v["r2"])**2,                                   # yarıçap oranının karesi alındı
                          2.0 * v["v2"],                                                       # 2 ile çarpıldı
                          0.5 * v["v2"],                                                       # 1/2 çarpanı eklendi
                          1.5 * v["v2"]],                                                      # 1.5 ile çarpıldı
     beklenen={"v2": 10},
     cozum=r"""Açısal momentum korunumu: m·v₁·r₁ = m·v₂·r₂\
{v1} · {r1} = v₂ · {r2}\
{H:g} = {r2}v₂ ⇒ v₂ = {v2:g} m/s""")

# ---------------------------------------------------------------- ZOR
c45 = math.cos(math.radians(45))
s45 = math.sin(math.radians(45))
c30 = math.cos(math.radians(30))
s30 = math.sin(math.radians(30))


def _s22(v0):
    k = 1.5 * s45 / (2.5 * s30)         # v_B = k v_A (dikey denge)
    vA = 4 * v0 / (-1.5 * c45 + 2.5 * k * c30)
    return dict(P0=4 * v0, k=k, a1=1.5 * c45, a2=2.5 * c30, net=-1.5 * c45 + 2.5 * k * c30, vA=vA, vB=k * vA)


ekle(no=22, zorluk="zor",
     params={"v0": P(20, "m/s", 10, 30, 10)},
     metin="4 kg'lık bir mermi yatayda {v0} m/s hızla giderken havada patlayarak iki parçaya ayrılıyor: A parçası (1.5 kg) ve B parçası (2.5 kg). A parçası yatayla 45 derece yukarı sola doğru B parçası yatayla 30 derece aşağı sağa doğru fırlıyor. A parçasının hızını bulunuz.",
     hesap=_s22,
          cevap=("vA", "m/s", 0),
     celdirici=lambda v: [4 * v["v0"] / (2.5 - 1.5),                                          # açı bileşenleri unutuldu
                          float(v["vB"]),                                                      # B parçasının hızı verildi
                          2.0 * v["vA"],                                                       # 2 ile çarpıldı
                          0.5 * v["vA"],                                                       # 1/2 çarpanı eklendi
                          float(v["v0"])],                                                     # başlangıç hızı verildi
     beklenen={"vA": 103.03},
     sekil={"dosya": "S22_1.png", "etiketler": [("v0", "20 m/s", lambda v: f"{v:g} m/s")]},
     cozum=r"""Dikey momentum korunumu: 0 = m_A(v_A sin 45°) − m_B(v_B sin 30°)\
1.5·v_A/√2 − 2.5·v_B/2 = 0 ⇒ v_B = {k:.4f}v_A …(1)\
Yatay momentum korunumu: 4({v0}) = −1.5(v_A cos 45°) + 2.5(v_B cos 30°)\
{P0:g} = −{a1:.3f}v_A + {a2:.3f}v_B …(2)\
(1)→(2): {net:.3f}v_A = {P0:g} ⇒ v_A ≈ {vA:.0f} m/s""")

ekle(no=23, zorluk="zor",
     params={"mc": P(300, "kg", 200, 400, 100), "h": P(0.5, "m", 0.5, 2, 0.5), "e": P(0.1, "", 0.1, 0.3, 0.1)},
     metin="800 kg'lık bir kazık (pile), {mc} kg'lık bir çekiç ile {h} m yükseklikten vurularak kuma çakılıyor. Çarpışma plastik değil, e = {e}. Çekiç kazığa çarptığında kazığın ilk hızı ne olur?",
     hesap=lambda mc, h, e: dict(vc1=math.sqrt(2 * g * h), vp=mc * math.sqrt(2 * g * h) * (1 + e) / (mc + 800),
                                 pc=mc * round(math.sqrt(2 * g * h), 2), ev=e * round(math.sqrt(2 * g * h), 2), mt=mc + 800),
          cevap=("vp", "m/s", 2),
     celdirici=lambda v: [v["mc"] * v["vc1"] * v["e"] / (v["mc"] + 800),                      # (1+e) yerine e kullanıldı
                          v["mc"] * v["vc1"] / (v["mc"] + 800),                               # (1+e) unutuldu
                          v["mc"] * v["vc1"] * (1 + v["e"]) / 800,                            # paydada çekiç kütlesi eklenmedi
                          2 * v["vp"],                                                         # 2 ile çarpıldı
                          0.5 * v["vp"]],                                                      # 1/2 çarpanı eklendi
     beklenen={"vp": 0.9387},
     sekil={"dosya": "S23_1.png", "etiketler": [("h", "0.5 m", lambda h: f"{h:g} m")]},
     cozum=r"""Çekiç hızı: v_c1 = √(2 · 9.81 · {h}) ≈ {vc1:.2f} m/s\
Momentum: {mc}({vc1:.2f}) + 0 = {mc}v_c2 + 800v_p2 …(1)\
Restitüsyon: {e} = (v_p2 − v_c2)/{vc1:.2f} ⇒ v_c2 = v_p2 − {ev:.3f} …(2)\
(2)→(1) ve çözümle: v_p2 ≈ {vp:.2f} m/s""")

ekle(no=24, zorluk="zor",
     params={"v": P(5, "m/s", 3, 8, 1), "e": P(0.8, "", 0.4, 0.8, 0.2)},
     metin="0.4 kg'lık A bilardo topu {v} m/s hızla duran B topuna çarpıyor. Çarpışma merkezi değil, eğik çarpışmadır. Çarpışma düzleminin normali ile A'nın geliş doğrultusu arasında 30 derece açı vardır. e = {e}. B topunun çarpışma sonrası hızı nedir? (B topu normal doğrultusunda hareket eder).",
     hesap=lambda v, e: dict(vt=v * s30, vn=v * c30, vB=(1 + e) / 2 * v * c30, vAn=(1 - e) / 2 * v * c30),
          cevap=("vB", "m/s", 3),
     celdirici=lambda v: [(1 + v["e"]) / 2 * v["v"] * math.sin(math.radians(30)),            # cos30 yerine sin30 kullanıldı
                          v["v"] * math.cos(math.radians(30)),                                # restitüsyon (1+e)/2 faktörü unutuldu
                          v["e"] / 2 * v["v"] * math.cos(math.radians(30)),                   # (1+e) yerine e kullanıldı
                          2 * v["vB"],                                                         # 2 ile çarpıldı
                          0.5 * v["vB"]],                                                      # 1/2 çarpanı eklendi
     beklenen={"vB": 3.8971},
     sekil={"dosya": "S24_1.png", "etiketler": [("v", "(v_A)_1 = 5 m/s", lambda v: f"(v_A)_1 = {v:g} m/s")]},
     cozum=r"""Teğetsel momentum korunur: v_At2 = v_At1 = {v} sin 30° = {vt:g} m/s\
Normal momentum (eşit kütleler): m({v} cos 30°) = m·v_An2 + m·v_Bn2\
Restitüsyon (normal eksen): {e} = (v_Bn2 − v_An2)/({v} cos 30°)\
İkisi çözülürse: v_Bn2 = (1 + e)/2 · {v} cos 30° = {vB:.3f} m/s""")

ekle(no=25, zorluk="zor",
     params={"m": P(3, "kg", 2, 6, 1), "v": P(20, "m/s", 10, 30, 5), "rho": P(10, "m", 5, 15, 5)},
     metin="{m} kg kütleli bir top eğri bir yoldan aşağı kayarak B noktasına geliyor. B noktasındaki eğrilik yarıçapı {rho} m'dir. Topun hızı {v} m/s ise ve B noktası eğrilik merkezine (O) göre yatay konumdaysa, topun O noktasına göre açısal momentumu nedir?",
     hesap=lambda m, v, rho: dict(H=m * v * rho),
          cevap=("H", "kg·m²/s", 0),
     celdirici=lambda v: [float(v["v"] * v["rho"]),                                           # kütle m unutuldu (v·r)
                          float(v["m"] * v["v"]),                                              # yarıçap rho unutuldu (çizgisel momentum)
                          v["m"] * v["v"] / v["rho"],                                         # m·v/rho yapıldı
                          2.0 * v["H"],                                                        # 2 ile çarpıldı
                          0.5 * v["H"]],                                                       # 1/2 çarpanı eklendi
     beklenen={"H": 600},
     cozum=r"""H_O = m · v · r (hız vektörü yarıçap vektörüne diktir)\
H_O = {m} kg · {v} m/s · {rho} m = {H:g} kg·m²/s""")

ekle(no=26, zorluk="zor",
     params={"v1": P(10, "m/s", 5, 15, 5), "r1": P(3, "m", 3, 6, 1), "r2": P(2, "m", 1, 2, 1)},
     metin="Bir lunapark aracı r = {r1} m yarıçaplı yörüngede {v1} m/s hızla dönerken, kol içeri doğru çekilerek yarıçap saniyede 1 m/s hızla kısaltılıyor. Yarıçap {r2} m olduğunda aracın teğetsel hızı ne olur?",
     kisit=lambda v1, r1, r2: r2 < r1,
     hesap=lambda v1, r1, r2: dict(H=v1 * r1, v2=v1 * r1 / r2),
          cevap=("v2", "m/s", 1),
     celdirici=lambda v: [v["v1"] * v["r2"] / v["r1"],                                        # yarıçap oranı ters çevrildi
                          v["v1"] * (v["r1"] / v["r2"])**2,                                   # yarıçap oranının karesi alındı
                          2.0 * v["v2"],                                                       # 2 ile çarpıldı
                          0.5 * v["v2"],                                                       # 1/2 çarpanı eklendi
                          1.5 * v["v2"]],                                                      # 1.5 ile çarpıldı
     beklenen={"v2": 15},
     cozum=r"""Merkezi kuvvet moment oluşturmaz, açısal momentum korunur.\
m·v₁·r₁ = m·v₂·r₂\
{v1} · {r1} = v₂ · {r2} ⇒ v₂ = {v2:g} m/s""")


if __name__ == "__main__":
    calistir(S, Path(__file__).parent / "_out" / "u5")
