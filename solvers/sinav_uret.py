"""Vize sınavı üretici (Ünite 2-5): sözel test + sayısal test + boşluk doldurmalı, cevap anahtarı.

Varsayılan yapı (15 sorunun 14'ü; 15. soru klasik, elle eklenir):
    4 sözel çoktan seçmeli, 5 sayısal çoktan seçmeli, 5 boşluk doldurmalı (hata payı %5, %5-%10 arası yarım puan)

Kullanım (solvers/ içinden):
    python sinav_uret.py --grup A,B --seed 1 --ad vize
    python sinav_uret.py --sozel 1,2,1 --secmeli 2,2,1 --bosluk 1,2,2     # kolay,orta,zor sayıları
Çıktı: ../sinavlar/<ad>/ altında sinav_<grup>.md/.docx, cevap_anahtari_<grup>.md/.docx, sekil_<grup>/
Her grup aynı soruları farklı sayılarla ve farklı şık sırasıyla alır (sözel: B grubunda şıklar karıştırılır).
"""
import argparse
import math
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

import sozel
import u2, u3, u4, u5
from PIL import Image
from core import MD, UNITE_ADI, render, uret

ROOT = Path(__file__).resolve().parent.parent
STIL = ROOT / "stil"
HAVUZ = {2: u2, 3: u3, 4: u4, 5: u5}
ZORLUK = {"kolay": 0, "orta": 1, "zor": 2}
HARF = "abcde"
SEKIL_EN, SEKIL_BOY = 1.95, 2.3  # şekil kutusu (in); metinle yan yana konur

# Aynı senaryoyu paylaşan sayısal sorulardan sınavda en fazla biri seçilir.
AILELER = [
    (2, {1, 2}), (2, {4, 5}), (2, {6, 7}), (2, {8, 9}), (2, {10, 11, 12}), (2, {13, 14, 15}), (2, {16, 17}), (2, {18, 19}),
    (5, {1, 2}), (5, {8, 9}), (5, {18, 21, 26}),
]
CARPANLAR = [0.5, 2, 1.5, 0.75, 1.25, 0.8, 1.2, 0.6, 1.8, 2.5, 0.4, 1 / math.sqrt(2), math.sqrt(2), 0.9, 1.1]
SIKLI_KARISTIRMA_YASAK = re.compile(r"yukarıdaki|hepsi|hiçbiri|tümü|her ikisi", re.I)


def aile(s):
    for u, kume in AILELER:
        if s.unite == u and s.no in kume:
            return (u, min(kume))
    return (s.unite, s.no)


def sayisal_havuz(birimler, taslak):
    out = []
    for u in birimler:
        for s in HAVUZ[u].S:
            if s.cevap is None:
                if not (taslak and len(s.beklenen) == 1):
                    continue
                s.cevap = (next(iter(s.beklenen)), "", 3)
            out.append(s)
    return out


def zorluk_f(s):
    return s["zorluk"] if isinstance(s, dict) else s.zorluk


def sec(havuz, sayilar, rnd, unite_f, aile_f=None, yasak=(), sayac=None):
    """Zorluk başına istenen sayıda soru seçer; her seferinde o ana kadar en az soru seçilmiş üniteden alır
    (ünite dengesi), aynı aileden ikinci soruyu almaz."""
    sayac = {} if sayac is None else sayac
    secilen, aileler = [], set(yasak)
    for zor, n in sayilar.items():
        aday = [s for s in havuz if zorluk_f(s) == zor]
        rnd.shuffle(aday)
        for _ in range(n):
            gecerli = [s for s in aday if aile_f is None or aile_f(s) not in aileler]
            if not gecerli:
                print(f"UYARI: {zor} için {n} soru istendi, daha az bulundu", file=sys.stderr)
                break
            en_az = min(sayac.get(unite_f(s), 0) for s in gecerli)
            s = rnd.choice([s for s in gecerli if sayac.get(unite_f(s), 0) == en_az])
            aday.remove(s)
            secilen.append(s)
            sayac[unite_f(s)] = sayac.get(unite_f(s), 0) + 1
            if aile_f:
                aileler.add(aile_f(s))
    return secilen, aileler


def md_sekiller(unite, no):
    """md'de sorunun görselleri (soru bloğu içindeki tüm resimler)."""
    t = (MD / (UNITE_ADI.format(u=unite) + ".md")).read_text(encoding="utf-8")
    basliklar = list(re.finditer(r"(?m)^(?:\*\*|#+ *)Soru (\d+)", t))
    for i, m in enumerate(basliklar):
        if int(m.group(1)) == no:
            blok = t[m.start(): basliklar[i + 1].start() if i + 1 < len(basliklar) else len(t)]
            return re.findall(r"!\[[^\]]*\]\(([^)]*)\)", blok)
    return []


def fmt(v, ond):
    s = f"{v:.{ond}f}"
    return "0" if float(s) == 0 and v == 0 else s


def siklar(deger, birim, ond, rnd, ozel=(), hedef=None):
    """5 şık: doğru + 4 çeldirici (önce soruya özel); artan sırada. hedef: doğru şıkkın artan sıradaki yeri (0-4);
    yeterli çeldirici yoksa önceliğe göre ilk 4 alınır. (şık metinleri, doğru indeks)"""
    gor = lambda v: f"{fmt(v, ond)} {birim}".strip()
    genel = [deger * c for c in CARPANLAR] + ([-deger] if deger > 0 else [])
    rnd.shuffle(genel)
    sirali = list(ozel) + [v for v in genel if not (deger > 0 and v < 0)] + [v for v in genel if deger > 0 and v < 0]
    aday, gorulen = [], {gor(deger)}
    for v in sirali:
        k = gor(v)
        if k not in gorulen and float(fmt(v, ond)) != float(fmt(deger, ond)):
            gorulen.add(k)
            aday.append(v)
    if len(aday) < 4:
        raise RuntimeError(f"şık üretilemedi: {deger} {birim}")
    secilen = aday[:4]
    if hedef is not None:
        alt = [v for v in aday if v < deger][:hedef]
        ust = [v for v in aday if v > deger][:4 - hedef]
        if len(alt) == hedef and len(ust) == 4 - hedef:
            secilen = alt + ust
    tum = {gor(deger): deger, **{gor(v): v for v in secilen}}
    metinler = [k for k, _ in sorted(tum.items(), key=lambda kv: kv[1])]
    return metinler, metinler.index(gor(deger))


def varyant(s, seed, sekil_dir, etiket, onceki):
    for ek in range(60):                       # önceki gruplardan farklı parametre ve farklı cevap
        sonuc = uret(s, seed + 100003 * ek, sekil_dir)
        _, _, vals = render(s, sonuc["params"])
        if (sonuc["params"], round(vals[s.cevap[0]], 6)) not in onceki and                 all(round(vals[s.cevap[0]], 6) != k for _, k in onceki):
            break
    onceki.append((sonuc["params"], round(vals[s.cevap[0]], 6)))
    img = Path(sonuc["sekil"]) if sonuc.get("sekil") else None
    if img is None:
        olan = md_sekiller(s.unite, s.no)
        if olan:
            img = (MD / olan[0]).resolve()
    hedef = None
    if img and img.exists():
        hedef = sekil_dir / f"q{etiket:02d}.png"
        shutil.copy(img, hedef)
        with Image.open(hedef) as im:        # 2x LANCZOS: küçük şekil Word'de/baskıda daha net görünür
            im.convert("RGB").resize((im.width * 2, im.height * 2), Image.LANCZOS).save(hedef, dpi=(300, 300))
        if img.parent == sekil_dir and img != hedef:
            img.unlink()
    return sonuc, vals, hedef


def div(stil, icerik):
    return f'::: {{custom-style="{stil}"}}\n{icerik.rstrip()}\n:::\n'


def sekil_md(grup, img, en=SEKIL_EN, boy=SEKIL_BOY):
    """Şekli en x boy (in) kutusuna oranını koruyarak sığdırır."""
    w, h = Image.open(img).size
    k = min(en / w, boy / h)
    return div("SoruSekil", f"![](sekil_{grup}/{img.name}){{width={w * k:.2f}in height={h * k:.2f}in}}")


# Sınavda gerekmeyen (Ü6-8 ve benzeri) ek formüller: öğrencinin doğru formülü seçmesini sınar. Satırlar tabloya dağıtılır.
EK_FORMUL = [
    r"| $\omega = \dot{\theta}, \quad \alpha = \dot{\omega}$ | $v_B = v_A + \omega \times r_{B/A}$ |",
    r"| $T = \frac{1}{2} I_G \omega^2$ | $\Sigma M_G = I_G\,\alpha$ |",
    r"| $\omega_n = \sqrt{k/m}, \quad f = \frac{\omega_n}{2\pi}$ | $a_B = a_A + \alpha \times r_{B/A} - \omega^2 r_{B/A}$ |",
    r"| $H_O = r \times m v, \quad \Sigma M_O = \dot{H}_O$ | $e = \frac{v_B' - v_A'}{v_A - v_B}$ |",
]


def formul_tablosu():
    t = (STIL / "sinav_sablonu.md").read_text(encoding="utf-8")
    satirlar = t[t.index("### Formüller"):].strip().split("\n")
    bas, govde = satirlar[:4], satirlar[4:]          # başlık, boş satır, tablo başlığı ve ayırıcı
    for k, ek in enumerate(EK_FORMUL):
        govde.insert(2 + 3 * k + k, ek)
    return "\n".join(bas + govde) + "\n"


def aralik_metni(deger, tam, yarim, ond, mutlak=0.001, esik=0.01):
    """Boşluk doldurmalı için kabul aralıkları: göreli hata payı (%); |cevap| < esik ise mutlak hata
    (tam puan ±mutlak, yarım puan ±2·mutlak)."""
    if abs(deger) < esik:
        o = max(ond, 4)
        t1, t2, y1, y2 = deger - mutlak, deger + mutlak, deger - 2 * mutlak, deger + 2 * mutlak
        return (f"mutlak hata: tam puan: {fmt(t1, o)} – {fmt(t2, o)}; yarım puan: {fmt(y1, o)} – {fmt(t1, o)} "
                f"veya {fmt(t2, o)} – {fmt(y2, o)}")
    o = ond + 1
    t1, t2 = sorted((deger * (1 - tam / 100), deger * (1 + tam / 100)))
    y1, y2 = sorted((deger * (1 - yarim / 100), deger * (1 + yarim / 100)))
    return f"tam puan: {fmt(t1, o)} – {fmt(t2, o)}; yarım puan: {fmt(y1, o)} – {fmt(t1, o)} veya {fmt(t2, o)} – {fmt(y2, o)}"


def sozel_siklar(s, karistir, rnd, hedef=None):
    """Sözel şıklar; karistir ise (ve 'yukarıdakilerin hepsi' türü şık yoksa) karıştırılır, hedef verilirse doğru
    şık o sıraya konur."""
    metin = list(s["siklar"])
    dogru = s["dogru"]
    if karistir and not any(SIKLI_KARISTIRMA_YASAK.search(x) for x in metin):
        diger = [i for i in range(5) if i != s["dogru"]]
        rnd.shuffle(diger)
        hedef = rnd.randrange(5) if hedef is None else hedef
        idx = diger[:hedef] + [s["dogru"]] + diger[hedef:]
        metin = [s["siklar"][i] for i in idx]
        dogru = hedef
    return metin, dogru


def say3(s):
    k, o, z = (int(x) for x in s.split(","))
    return {"kolay": k, "orta": o, "zor": z}


def uret_sinav(args):
    birimler = [int(x) for x in args.birimler.split(",")]
    gruplar = [g.strip() for g in args.grup.split(",")]
    rnd = random.Random(args.seed)

    # --- soru seçimi (tüm gruplar için ortak) ---
    sayac_soz, sayac_say = {}, {}
    sozel_havuz = [q for u in birimler for q in sozel.parse(u)]
    soz, _ = sec(sozel_havuz, say3(args.sozel), rnd, lambda q: q["unite"], sayac=sayac_soz)
    soz.sort(key=lambda q: (q["unite"], ZORLUK[q["zorluk"]], q["no"]))

    havuz = sayisal_havuz(birimler, args.taslak)
    mc_havuz = [s for s in havuz if s.celdirici is not None or args.taslak]
    mc, aileler = sec(mc_havuz, say3(args.secmeli), rnd, lambda s: s.unite, aile, sayac=sayac_say)
    mc.sort(key=lambda s: (s.unite, ZORLUK[s.zorluk], s.no))
    kalan = [s for s in havuz if s not in mc]
    bos, _ = sec(kalan, say3(args.bosluk), rnd, lambda s: s.unite, aile, yasak=aileler, sayac=sayac_say)
    bos.sort(key=lambda s: (s.unite, ZORLUK[s.zorluk], s.no))

    cikis = ROOT / "sinavlar" / args.ad
    cikis.mkdir(parents=True, exist_ok=True)
    onceki = {s.id: [] for s in mc + bos}

    def plan(anahtar, ilk=None):
        """Gruplar için doğru şık sırası: her soruda gruplar farklı sıra alır (ilk verilirse A grubu o sırada kalır)."""
        r = random.Random(f"{args.seed}-plan-{anahtar}")
        sira = [x for x in range(5) if x != ilk]
        r.shuffle(sira)
        sira = ([ilk] if ilk is not None else []) + sira
        return [sira[g % 5] for g in range(len(gruplar))]
    plan_soz = {(q["unite"], q["no"]): plan(f"s{q['unite']}-{q['no']}", q["dogru"]) for q in soz}
    plan_mc = {s.id: plan(s.id) for s in mc}
    ozet = []
    for gi, grup in enumerate(gruplar):
        sd = cikis / f"sekil_{grup}"
        sd.mkdir(parents=True, exist_ok=True)
        grnd = random.Random(f"{args.seed}-{grup}")
        birimler_bos = "|".join(s.cevap[1] for s in bos)
        sorular = [div("Isaret", f"BASLIK|{grup}|{len(soz) + len(mc)}|{birimler_bos}")]
        anahtar, cozumler = [], []
        n = 0

        for q in soz:
            n += 1
            metinler, dogru = sozel_siklar(q, gi > 0, grnd, plan_soz[(q["unite"], q["no"])][gi])
            sorular.append(div("SoruMetni", f"**{n}.** {q['metin']}  \n" + "".join(f"{HARF[i]}) {m}  \n" for i, m in enumerate(metinler))))
            anahtar.append((n, f"sözel Ü{q['unite']}-S{q['no']}", q["zorluk"], f"{HARF[dogru]}) {metinler[dogru]}"))
        for s in mc:
            n += 1
            sonuc, vals, img = varyant(s, args.seed * 1000 + n + 17 * gi, sd, n, onceki[s.id])
            ak, birim, ond = s.cevap
            ozel = [float(x) for x in s.celdirici(vals)] if s.celdirici else []
            metinler, dogru = siklar(vals[ak], birim, ond, grnd, ozel, plan_mc[s.id][gi])
            sorular.append(div("SoruMetni", f"**{n}.** {sonuc['metin'].strip()}"))
            if img:
                sorular.append(sekil_md(grup, img))
            sorular.extend(div("Secenek", f"{HARF[i]}\\) {m}") for i, m in enumerate(metinler))
            anahtar.append((n, s.id, s.zorluk, f"{HARF[dogru]}) {metinler[dogru]}"))
            cozumler.append(f"**{n}. ({s.id}, {s.zorluk}) — Doğru şık: {HARF[dogru]}) {metinler[dogru]}**\n\n{sonuc['cozum'].strip()}\n")
        for s in bos:
            n += 1
            sonuc, vals, img = varyant(s, args.seed * 1000 + n + 17 * gi, sd, n, onceki[s.id])
            ak, birim, ond = s.cevap
            d = vals[ak]
            sorular.append(div("SoruMetni", f"**{n}.** {sonuc['metin'].strip()}"))
            if img:
                sorular.append(sekil_md(grup, img))
            aralik = aralik_metni(d, args.tam, args.yarim, ond, args.mutlak)
            anahtar.append((n, s.id, s.zorluk, f"{fmt(d, ond)} {birim}".strip() + f" ({aralik})"))
            cozumler.append(f"**{n}. ({s.id}, {s.zorluk}) — Cevap: {fmt(d, ond)} {birim}**  \n({aralik})\n\n{sonuc['cozum'].strip()}\n")
        sorular.append(formul_tablosu())
        md = cikis / f"sinav_{grup}.md"
        md.write_text("\n".join(sorular), encoding="utf-8")
        satirlar = ["| No | Soru | Zorluk | Cevap |", "| :-: | :-- | :-- | :-- |"]
        satirlar += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in anahtar]
        ca = cikis / f"cevap_anahtari_{grup}.md"
        ca.write_text(f"**GRUP {grup} — CEVAP ANAHTARI**\n\n"
                      f"Boşluk doldurmalı sorular: ±%{args.tam:g} içinde tam puan, %{args.tam:g}–%{args.yarim:g} arasında yarım puan. "
                      f"|Cevap| < 0.01 ise mutlak hata: ±{args.mutlak:g} tam puan, ±{2 * args.mutlak:g} yarım puan.\n\n"
                      + "\n".join(satirlar) + "\n\n---\n\n" + "\n\n".join(cozumler), encoding="utf-8")
        for dosya in (md, ca):
            docx = dosya.with_suffix(".docx")
            r = subprocess.run(["pandoc", str(dosya), "-o", str(docx), f"--reference-doc={STIL / 'sinav_stili_referans.docx'}",
                                "--wrap=none", f"--resource-path={cikis}"], capture_output=True)
            if r.returncode == 0 and dosya == md:
                from docx_duzen import duzenle
                duzenle(docx, args.tarih)
            print(("OK  " if r.returncode == 0 else "HATA"), docx.name, r.stderr.decode("utf-8", "ignore")[:300])
        ozet.append((grup, anahtar))
    ns = len(soz) + len(mc)
    for g, a in ozet:
        print(f"GRUP {g}: " + " ".join(f"{no}{c[0]}" for no, _, _, c in a[:ns]) + "  | boşluk: " +
              ", ".join(c.split(' (')[0] for _, _, _, c in a[ns:]))
    print("Sözel:", ", ".join(f"Ü{q['unite']}S{q['no']}({q['zorluk']})" for q in soz))
    print("Sayısal test:", ", ".join(f"{s.id}({s.zorluk})" for s in mc))
    print("Boşluk doldurma:", ", ".join(f"{s.id}({s.zorluk})" for s in bos))
    print("Çıktı:", cikis)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--grup", default="A,B")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--sozel", default="1,2,1", help="sözel test: kolay,orta,zor (varsayılan toplam 4)")
    ap.add_argument("--secmeli", default="2,2,1", help="sayısal test: kolay,orta,zor (toplam 5)")
    ap.add_argument("--bosluk", default="1,2,2", help="boşluk doldurmalı: kolay,orta,zor (toplam 5)")
    ap.add_argument("--tam", type=float, default=5, help="tam puan hata payı, %")
    ap.add_argument("--yarim", type=float, default=10, help="yarım puan üst sınırı, %")
    ap.add_argument("--mutlak", type=float, default=0.001, help="|cevap| < 0.01 ise mutlak hata payı (tam puan)")
    ap.add_argument("--birimler", default="2,3,4,5")
    ap.add_argument("--ad", default="vize_taslak")
    ap.add_argument("--tarih", default="__.__.2026", help="üstbilgideki sınav tarihi (örn. 13.11.2026)")
    ap.add_argument("--taslak", action="store_true", help="cevap/çeldirici tanımı olmayan tek-sonuçlu soruları beklenen anahtarıyla kullan (test)")
    uret_sinav(ap.parse_args())
