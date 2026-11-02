"""Ünite 6 Soru 1 - kayan çubuk (ani dönme merkezi). Pilot solver.

Parametreler: a = çubuk boyu L [m], b = A ucu hızı v_A [m/s]. theta sabit (30°),
çünkü şekildeki çubuk açısı değişirse çizim yanıltıcı olur.
"""
import json, math, random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "media" / "Dinamik 6. Ünite Sayısal Sorular" / "S1_1.png"
JSON = ROOT / "media" / "sayilar_duzeltilmis.json"
THETA = 30.0
PARAMS = {"a": (1.0, 2.5, 0.5), "b": (2.0, 6.0, 1.0)}  # (min, max, adım)

METIN = ("Şekildeki çubuk duvara ve yere dayalı olarak kaymaktadır. A ucu sağa doğru "
         "$v_{{A}} = {b}$ m/s hızla hareket etmektedir. $\theta = 30^{{\circ}}$ olduğu anda "
         "çubuğun açısal hızı ($\omega$) kaç rad/s'dir? (Çubuk boyu $L = {a}$m)")


def coz(a, b):
    r_a = a * math.sin(math.radians(THETA))
    omega = b / r_a
    r_b = a * math.cos(math.radians(THETA))
    return {"r_a": r_a, "omega": omega, "r_b": r_b, "v_b": omega * r_b}


def cozum_metni(a, b):
    s = coz(a, b)
    return (f"IC yöntemiyle: $r_{{A/IC}} = L \cdot \sin(30^{{\circ}}) = {a} \cdot 0.5 = {s['r_a']:.2f}$ m\n\n"
            f"$\omega = v_{{A}}/r_{{A/IC}} = {b}/{s['r_a']:.2f} = {s['omega']:.2f}$ rad/s.")


def _etiket(img, kutu, metin, font_pt):
    """Kutuyu çevresindeki ortanca renkle boyayıp yeni metni ortalar."""
    x1, y1, x2, y2 = kutu
    pad = 4
    halka = [img.getpixel((x, y)) for x in range(x1 - pad, x2 + pad, 3) for y in (y1 - pad, y2 + pad)]
    halka += [img.getpixel((x, y)) for y in range(y1, y2, 3) for x in (x1 - pad, x2 + pad)]
    renk = tuple(sorted(c[i] for c in halka)[len(halka) // 2] for i in range(3))
    d = ImageDraw.Draw(img)
    d.rectangle([x1, y1, x2, y2], fill=renk)
    f = ImageFont.truetype("C:/Windows/Fonts/times.ttf", font_pt)
    w = d.textlength(metin, font=f)
    d.text(((x1 + x2 - w) / 2, (y1 + y2) / 2), metin, font=f, fill=(5, 5, 5), anchor="lm")


def sekil(a, b, cikis):
    tespit = json.load(open(JSON, encoding="utf-8"))["Dinamik 6. Ünite Sayısal Sorular"]["S1_1.png"]["tespitler"]
    kutu = {t["gercek_metin"]: t["kutu"] for t in tespit if t.get("kutu")}
    img = Image.open(IMG).convert("RGB")
    _etiket(img, kutu["1.5 m"], f"{a:g} m", 34)
    _etiket(img, kutu["v_A = 3 m/s"], f"= {b:g} m/s", 34)
    img.save(cikis)


def uret(seed, cikis_dir):
    rnd = random.Random(seed)
    p = {k: round(rnd.randrange(0, int(round((hi - lo) / st)) + 1) * st + lo, 3) for k, (lo, hi, st) in PARAMS.items()}
    a, b = p["a"], p["b"]
    cikis_dir = Path(cikis_dir); cikis_dir.mkdir(parents=True, exist_ok=True)
    sekil(a, b, cikis_dir / f"u6_s1_{seed}.png")
    return {"metin": METIN.format(a=f"{a:g}", b=f"{b:g}"), "cozum": cozum_metni(a, b), "params": p}


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    o = coz(1.5, 3)  # orijinal değerlerle doğrulama (md: omega = 4 rad/s, v_B = 5.2 m/s)
    assert abs(o["omega"] - 4) < 1e-9 and abs(o["v_b"] - 5.196) < 1e-3, o
    print("Orijinal değer testi geçti: ω =", o["omega"], "rad/s, v_B =", round(o["v_b"], 2))
    out = ROOT / "solvers" / "_out"
    for s in (1, 2, 3):
        r = uret(s, out); print(r["params"], "->", r["cozum"].splitlines()[-1])
