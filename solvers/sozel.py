"""Sözel çoktan seçmeli soruları md dosyalarından ayıklar ve zorluk tablosunu okur (Ünite 2-5).

parse(unite) -> [{"unite", "no", "metin", "siklar": [5 metin], "dogru": 0-4, "zorluk"}]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "md"
ZORLUK_MD = ROOT / "zorluk_tablosu.md"
HARFLER = "ABCDE"


def _aralik(s):
    out = set()
    for p in re.split(r"[,\s]+", s.strip()):
        if not p:
            continue
        m = re.fullmatch(r"(\d+)[–-](\d+)", p)
        if m:
            out |= set(range(int(m.group(1)), int(m.group(2)) + 1))
        elif p.isdigit():
            out.add(int(p))
    return out


def zorluklar():
    """{unite: {no: 'kolay'|'orta'|'zor'}} (zorluk_tablosu.md 'Sözel Sorular' bölümü)."""
    t = ZORLUK_MD.read_text(encoding="utf-8")
    t = t[t.index("## Sözel Sorular"):]
    t = t.split("## Notlar")[0]
    out = {}
    for m in re.finditer(r"(?m)^\|\s*(\d+)\s*\(\d+\)\s*\|(.*)\|\s*$", t):
        k, o, z = [c.strip() for c in m.group(2).split("|")]
        out[int(m.group(1))] = {n: d for d, kume in (("kolay", k), ("orta", o), ("zor", z)) for n in _aralik(kume)}
    return out


def _temizle(s):
    s = s.replace("**", "")
    s = re.sub(r"\\\s*$", "", s.strip(), flags=re.M).strip()
    return "  \n".join(l.strip() for l in s.split("\n") if l.strip())


def _siklar(blok):
    return [m.group(2).strip() for m in re.finditer(r"(?m)^- ([A-E])\) (.*)$", blok)]


def parse(unite):
    t = (MD / f"Dinamik {unite}. Ünite Sözel Sorular.md").read_text(encoding="utf-8")
    sorular = []
    if unite == 5:
        parcalar = re.split(r"(?m)^\*\*Soru (\d+)\*\*\s*$", t)
        for i in range(1, len(parcalar), 2):
            no, blok = int(parcalar[i]), parcalar[i + 1]
            m = re.search(r"\*\*Doğru Cevap:\s*([A-E])\*\*", blok)
            ilk = blok.index("- A)") if "- A)" in blok else None
            if not m or ilk is None:
                continue
            sorular.append(dict(no=no, metin=_temizle(blok[:ilk]), siklar=_siklar(blok), dogru=HARFLER.index(m.group(1))))
    else:
        govde, _, anahtar = t.partition("**Cevap Anahtarı**")
        cevap = {int(n): h for n, h in re.findall(r"(?m)^\s*(\d+)\.\s+\*\*([A-E])\)\*\*", anahtar)}
        parcalar = re.split(r"(?m)^\*\*(\d+)\.\s", govde)
        for i in range(1, len(parcalar), 2):
            no, blok = int(parcalar[i]), parcalar[i + 1]
            ilk = blok.index("- A)")
            sorular.append(dict(no=no, metin=_temizle(blok[:ilk]), siklar=_siklar(blok), dogru=HARFLER.index(cevap[no])))
    z = zorluklar().get(unite, {})
    for s in sorular:
        s["unite"] = unite
        s["zorluk"] = z.get(s["no"], "orta")
    return sorular


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for u in (2, 3, 4, 5):
        qs = parse(u)
        kotu = [s["no"] for s in qs if len(s["siklar"]) != 5]
        print(f"Ü{u}: {len(qs)} soru, 5 şıksız: {kotu}, zorluk: " +
              ", ".join(f"{d}={sum(s['zorluk'] == d for s in qs)}" for d in ("kolay", "orta", "zor")))
    s = parse(2)[12]
    print(s["no"], s["metin"], s["siklar"], "doğru:", HARFLER[s["dogru"]])
