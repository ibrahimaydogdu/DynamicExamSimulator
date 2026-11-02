"""Tarayıcı (Pyodide) sınav simülatörü için tek bir deneme sınavını JSON olarak üretir.

sinav_json(seed, grup) -> JSON metni. Seçim/şık/plan mantığı sinav_uret.py ile aynıdır; çıktı docx yerine
soru metinleri, şekiller (base64 PNG), şıklar, doğru cevaplar ve çözümlerdir. Cevap denetimi sayfada (JS) yapılır.
"""
import base64
import json
import random
import tempfile
from pathlib import Path

import sozel
from core import render
from sinav_uret import (EK_FORMUL, STIL, ZORLUK, aile, aralik_metni, formul_tablosu, fmt, say3, sayisal_havuz, sec,
                        siklar, sozel_siklar, varyant)

GRUPLAR = "ABCD"
TAM, YARIM, MUTLAK, ESIK = 5, 10, 0.001, 0.01


def _resim(yol):
    if not yol:
        return None
    return "data:image/png;base64," + base64.b64encode(Path(yol).read_bytes()).decode()


def sinav(seed, grup="A", sozel_say="1,2,1", secmeli="2,2,1", bosluk="1,2,2", birimler=(2, 3, 4, 5)):
    gi = GRUPLAR.index(grup)
    rnd = random.Random(seed)
    soz, _ = sec([q for u in birimler for q in sozel.parse(u)], say3(sozel_say), rnd, lambda q: q["unite"], sayac={})
    soz.sort(key=lambda q: (q["unite"], ZORLUK[q["zorluk"]], q["no"]))
    havuz = sayisal_havuz(birimler, False)
    sayac = {}
    mc, aileler = sec([s for s in havuz if s.celdirici is not None], say3(secmeli), rnd, lambda s: s.unite, aile, sayac=sayac)
    mc.sort(key=lambda s: (s.unite, ZORLUK[s.zorluk], s.no))
    bos, _ = sec([s for s in havuz if s not in mc], say3(bosluk), rnd, lambda s: s.unite, aile, yasak=aileler, sayac=sayac)
    bos.sort(key=lambda s: (s.unite, ZORLUK[s.zorluk], s.no))

    def plan(anahtar, ilk=None):
        r = random.Random(f"{seed}-plan-{anahtar}")
        sira = [x for x in range(5) if x != ilk]
        r.shuffle(sira)
        sira = ([ilk] if ilk is not None else []) + sira
        return [sira[g % 5] for g in range(len(GRUPLAR))]

    grnd = random.Random(f"{seed}-{grup}")
    sd = Path(tempfile.mkdtemp())
    out = {"seed": seed, "grup": grup, "sorular": []}
    n = 0
    for q in soz:
        n += 1
        metinler, dogru = sozel_siklar(q, gi > 0, grnd, plan(f"s{q['unite']}-{q['no']}", q["dogru"])[gi])
        out["sorular"].append(dict(n=n, tur="sozel", kaynak=f"Ü{q['unite']}-S{q['no']}", zorluk=q["zorluk"],
                                   metin=q["metin"], siklar=metinler, dogru=dogru))
    for s in mc:
        n += 1
        sonuc, vals, img = varyant(s, seed * 1000 + n + 17 * gi, sd, n, [])
        ak, birim, ond = s.cevap
        ozel = [float(x) for x in s.celdirici(vals)]
        metinler, dogru = siklar(vals[ak], birim, ond, grnd, ozel, plan(s.id)[gi])
        out["sorular"].append(dict(n=n, tur="secmeli", kaynak=s.id, zorluk=s.zorluk, metin=sonuc["metin"].strip(),
                                   resim=_resim(img), siklar=metinler, dogru=dogru, cozum=sonuc["cozum"].strip()))
    for s in bos:
        n += 1
        sonuc, vals, img = varyant(s, seed * 1000 + n + 17 * gi, sd, n, [])
        ak, birim, ond = s.cevap
        d = vals[ak]
        out["sorular"].append(dict(n=n, tur="bosluk", kaynak=s.id, zorluk=s.zorluk, metin=sonuc["metin"].strip(),
                                   resim=_resim(img), birim=birim, deger=d, cevap=f"{fmt(d, ond)} {birim}".strip(),
                                   aralik=aralik_metni(d, TAM, YARIM, ond, MUTLAK, ESIK), cozum=sonuc["cozum"].strip()))
    out["kriter"] = dict(tam=TAM, yarim=YARIM, mutlak=MUTLAK, esik=ESIK)
    out["formul"] = formul_tablosu()
    return json.dumps(out, ensure_ascii=False)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    d = json.loads(sinav(int(sys.argv[1]) if len(sys.argv) > 1 else 5001, sys.argv[2] if len(sys.argv) > 2 else "B"))
    for q in d["sorular"]:
        print(q["n"], q["kaynak"], q["tur"], q.get("dogru", q.get("cevap")), "resim" if q.get("resim") else "")
