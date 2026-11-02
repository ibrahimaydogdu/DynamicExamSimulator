"""Parametrik soru üretimi için ortak çerçeve.

Her soru bir `Soru` nesnesidir: parametre aralıkları (P), soru metni şablonu, çözüm şablonu
ve `hesap` fonksiyonu. Şekil etiketleri `sekil` ile bağlanır. `dogrula` orijinal değerlerle
şablonu md dosyasıyla karşılaştırır; `uret` rastgele bir varyant üretir.
"""
import json
import random
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "md"
MEDIA = ROOT / "media"
SAYILAR = MEDIA / "sayilar_duzeltilmis.json"
def _font_yolu():
    """Times New Roman varsa o, yoksa matplotlib ile gelen DejaVu Serif (tarayıcıda/Pyodide'de)."""
    for y in (r"C:\Windows\Fonts\times.ttf", "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"):
        if Path(y).exists():
            return y
    import matplotlib
    return str(Path(matplotlib.get_data_path()) / "fonts" / "ttf" / "DejaVuSerif.ttf")


FONT = _font_yolu()
UNITE_ADI = "Dinamik {u}. Ünite Sayısal Sorular"


def norm(x):
    x = round(float(x), 6)
    return int(x) if x == int(x) else x


@dataclass
class P:
    default: float
    birim: str
    lo: float
    hi: float
    step: float
    liste: tuple = ()   # verilirse ızgara yerine bu değerler kullanılır

    def degerler(self):
        if self.liste:
            return [norm(x) for x in self.liste]
        n = int(round((self.hi - self.lo) / self.step))
        return [norm(self.lo + i * self.step) for i in range(n + 1)]


@dataclass
class Soru:
    unite: int
    no: int
    zorluk: str
    params: dict
    metin: str
    cozum: str
    hesap: Callable
    beklenen: dict = field(default_factory=dict)   # varsayılan değerlerde beklenen sonuçlar
    kisit: Optional[Callable] = None                # kisit(**p) -> bool
    sekil: Optional[dict] = None                    # {"dosya": "S5_1.png", "etiketler": [(param, anahtar, fmt)]}
    cevap: Optional[tuple] = None                   # (vals anahtarı, birim, ondalık basamak); None: çoktan seçmeli yapılamaz (sembolik/denklem)
    celdirici: Optional[Callable] = None            # celdirici(vals: dict) -> [değer, ...] tipik hatalı sonuçlar (en az 4)
    md_kontrol: bool = True                         # False: metin md'den bilerek farklı (ör. sembolik soru sayısallaştırıldı)

    @property
    def id(self):
        return f"u{self.unite}_s{self.no}"


def render(s, p):
    vals = {**p, **s.hesap(**p)}
    return s.metin.format(**vals), s.cozum.format(**vals), vals


def varsayilan(s):
    return {k: norm(v.default) for k, v in s.params.items()}


def _sayilar(t):
    return sorted(re.findall(r"\d+(?:[.,]\d+)?", t.replace(",", "")))


def md_metin(unite, no):
    t = (MD / (UNITE_ADI.format(u=unite) + ".md")).read_text(encoding="utf-8")
    m = re.search(rf"(?m)^(?:\*\*|#+ *)Soru {no}\**:?\**[ \t]*(.*)$", t)
    if not m:
        return None
    resim = r"!\[[^\]]*\]\([^)]*\)"
    ilk = re.sub(resim, "", m.group(1)).strip().rstrip("\\").strip()
    if ilk:
        return ilk
    sonra = t[m.end():].strip().split("\n\n")[0]
    return re.sub(resim, "", sonra).strip()


def dogrula(s):
    """Orijinal değerlerle: (1) şablondaki sayılar md metnindekilerle aynı mı, (2) beklenen sonuçlar."""
    hatalar = []
    p = varsayilan(s)
    metin, cozum, vals = render(s, p)
    orj = md_metin(s.unite, s.no)
    if orj is None:
        hatalar.append("md metni bulunamadı")
    elif s.md_kontrol and _sayilar(orj) != _sayilar(metin):
        hatalar.append(f"metin sayıları farklı: md={_sayilar(orj)} şablon={_sayilar(metin)}")
    for k, v in s.beklenen.items():
        if abs(vals[k] - v) > 1e-3 * max(1, abs(v)):
            hatalar.append(f"{k}: hesaplanan {vals[k]} != beklenen {v}")
    if s.kisit and not s.kisit(**p):
        hatalar.append("varsayılan değerler kısıtı sağlamıyor")
    return hatalar


def _etiket(img, kutu, metin):
    x1, y1, x2, y2 = kutu
    px = img.load()
    W, H = img.size
    pad = 2
    halka = [px[min(W - 1, x), max(0, min(H - 1, y))]
             for x in range(max(0, x1 - pad), min(W, x2 + pad), 2) for y in (y1 - pad, y2 + pad)]
    halka += [px[max(0, min(W - 1, x)), y]
              for y in range(max(0, y1), min(H, y2), 2) for x in (x1 - pad, x2 + pad)]
    renk = tuple(sorted(c[i] for c in halka)[len(halka) // 2] for i in range(3))
    d = ImageDraw.Draw(img)
    d.rectangle([x1 - 1, y1 - 1, x2 + 1, y2 + 1], fill=renk)
    pt = (y2 - y1) + 2
    while pt > 7:
        w = d.textlength(metin, font=ImageFont.truetype(FONT, pt))
        if w <= (x2 - x1) + 3:
            break
        pt -= 1
    f = ImageFont.truetype(FONT, pt)
    w = d.textlength(metin, font=f)
    d.text(((x1 + x2 - w) / 2, (y1 + y2) / 2), metin, font=f, fill=(0, 0, 0), anchor="lm")


def _kutu(unite, dosya, anahtar):
    """Tek kutu için list, '*metin' ile aynı metne sahip tüm kutular için list-of-list döner."""
    if isinstance(anahtar, (list, tuple)):
        return list(anahtar)
    if anahtar.startswith("*"):
        d = json.loads(SAYILAR.read_text(encoding="utf-8"))[UNITE_ADI.format(u=unite)][dosya]
        return [t["kutu"] for t in d["tespitler"] if t.get("kutu") and t.get("gercek_metin") == anahtar[1:]]
    d = json.loads(SAYILAR.read_text(encoding="utf-8"))[UNITE_ADI.format(u=unite)][dosya]
    for t in d["tespitler"]:
        if t.get("kutu") and t.get("gercek_metin") == anahtar:
            return t["kutu"]
    raise KeyError(f"{dosya}: '{anahtar}' kutusu bulunamadı")


def sekil_uret(s, vals, cikis):
    if s.sekil.get("cizim"):
        s.sekil["cizim"](vals, cikis)
        return
    img = Image.open(MEDIA / UNITE_ADI.format(u=s.unite) / s.sekil["dosya"]).convert("RGB")
    for param, anahtar, fmt in s.sekil.get("etiketler", []):
        k = _kutu(s.unite, s.sekil["dosya"], anahtar)
        for kutu in (k if isinstance(anahtar, str) and anahtar.startswith("*") else [k]):
            _etiket(img, kutu, fmt(vals[param]))
    img.save(cikis)


def uret(s, seed, cikis_dir=None):
    rnd = random.Random(seed)
    izgara = {k: v.degerler() for k, v in s.params.items()}
    for _ in range(500):
        p = {k: rnd.choice(v) for k, v in izgara.items()}
        if not s.kisit or s.kisit(**p):
            break
    else:
        raise RuntimeError(f"{s.id}: kısıtı sağlayan değer bulunamadı")
    metin, cozum, vals = render(s, p)
    sonuc = {"id": s.id, "seed": seed, "params": p, "metin": metin, "cozum": cozum}
    if cikis_dir and s.sekil and (s.sekil.get("etiketler") or s.sekil.get("cizim")):
        cikis_dir = Path(cikis_dir)
        cikis_dir.mkdir(parents=True, exist_ok=True)
        yol = cikis_dir / f"{s.id}_{seed}.png"
        sekil_uret(s, vals, yol)
        sonuc["sekil"] = str(yol)
    return sonuc


def calistir(sorular, cikis_dir):
    sys.stdout.reconfigure(encoding="utf-8")
    kotu = 0
    for s in sorular:
        h = dogrula(s)
        print(("OK   " if not h else "HATA ") + s.id, *h)
        kotu += bool(h)
        if not h:
            for seed in (1, 2):
                uret(s, seed, cikis_dir)
    print(f"{len(sorular) - kotu}/{len(sorular)} soru doğrulandı")
    return kotu
