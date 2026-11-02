"""Pandoc çıktısı sınav docx'ini düzenler (python-docx):
  - SoruMetni paragrafları sola yaslı (iki yana yaslı şıklar bozuk görünüyordu),
  - SoruMetni + hemen ardından gelen SoruSekil -> iki hücreli tablo (metin solda, şekil sağda),
  - ardışık Secenek paragrafları -> kutulu tek satırlık (gerekirse 3'lü satırlı) şık tablosu.
"""
import copy
import re

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

METIN_IN, SEKIL_IN = 1.65, 2.0      # sütun genişliği ~3.7 in
KUTU_TOPLAM_IN = 3.6
OGRENCI_NO = "202_0801___"            # 11 hane; rakam yazılı hane otomatik doldurulur ve işaretlenir, _ boş
BALON_FONT, BOS, DOLU = "Aptos Light", "○", "●"
KUTU_UZUN = 12                      # harf dahil bu uzunluktan uzun şıklar 3 sütunda dizilir


def _metin(el):
    """Paragraf düz metni (lxml itertext bu sınıflarda metni tekrarlıyor)."""
    return "".join(el.xpath(".//w:t/text()"))


def _stil(el):
    v = el.xpath("./w:pPr/w:pStyle/@w:val")
    return v[0] if v else None


def _ppr(p):
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = OxmlElement("w:pPr")
        p.insert(0, ppr)
    return ppr


def _hiza(p, deger):
    ppr = _ppr(p)
    for j in ppr.findall(qn("w:jc")):
        ppr.remove(j)
    j = OxmlElement("w:jc")
    j.set(qn("w:val"), deger)
    ppr.append(j)


def _aralik(p, once=0, sonra=0):
    ppr = _ppr(p)
    for s in ppr.findall(qn("w:spacing")):
        ppr.remove(s)
    s = OxmlElement("w:spacing")
    s.set(qn("w:before"), str(once))
    s.set(qn("w:after"), str(sonra))
    ppr.append(s)


def _ayirici():
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0")
    sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), "60")
    sp.set(qn("w:lineRule"), "exact")
    ppr.append(sp)
    p.append(ppr)
    return p


def _tablo(kap, satir, sutun, genislikler, kenarlik, yan=40):
    """kap: Document ya da hücre. tblPr alt öğeleri şema sırasında eklenir (Word katı sıra ister)."""
    t = kap.add_table(satir, sutun)
    tblpr = t._tbl.tblPr
    look = tblpr.find(qn("w:tblLook"))
    ekle = (lambda e: look.addprevious(e)) if look is not None else tblpr.append
    mar = OxmlElement("w:tblCellMar")
    for yon, w in (("left", yan), ("right", yan), ("top", 20), ("bottom", 20)):
        e = OxmlElement(f"w:{yon}")
        e.set(qn("w:w"), str(w))
        e.set(qn("w:type"), "dxa")
        mar.append(e)
    if kenarlik:
        b = OxmlElement("w:tblBorders")
        for yon in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{yon}")
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), "4")
            e.set(qn("w:space"), "0")
            e.set(qn("w:color"), "000000")
            b.append(e)
        ekle(b)
    ekle(mar)
    t.autofit = False
    for r in t.rows:
        for c, w in zip(r.cells, genislikler):
            c.width = Inches(w)
    return t


def _hucreye(hucre, ogeler):
    ilk = hucre.paragraphs[0]._p
    for o in ogeler:
        ilk.addprevious(o)
    hucre._tc.remove(ilk)


def _yukseklik(satir, in_):
    trpr = satir._tr.get_or_add_trPr()
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(in_ * 1440)))
    h.set(qn("w:hRule"), "atLeast")
    trpr.append(h)


def _yaz(hucre, metin, kalin=False, hiza="left", pt=9.5, font=None):
    p = hucre.paragraphs[0]
    p.alignment = {"left": 0, "center": 1, "right": 2}[hiza]
    p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(0)
    r = p.add_run(metin)
    r.bold = kalin
    r.font.size = Pt(pt)
    if font:
        r.font.name = font


def _ic_tablo(hucre, satir, sutun, genislikler, kenarlik=True, yan=40, ilk_sil=True):
    """Hücre içine kenarlıklı tablo koyar (hücrenin baştaki boş paragrafı silinir, sondaki küçültülür)."""
    t = _tablo(hucre, satir, sutun, genislikler, kenarlik, yan)
    if ilk_sil:
        hucre._tc.remove(hucre.paragraphs[0]._p)
    son = hucre.paragraphs[-1]._p
    ppr = _ppr(son)
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0")
    sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), "20")
    sp.set(qn("w:lineRule"), "exact")
    ppr.append(sp)
    return t


def _kenar(hucre, yonler=("top", "left", "bottom", "right")):
    tcpr = hucre._tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for yon in yonler:
        e = OxmlElement(f"w:{yon}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "6")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        b.append(e)
    tcpr.append(b)


def _siyah(hucre):
    """Kayıt (köşe) işareti: siyah dolgulu, çok küçük paragraflı hücre."""
    tcpr = hucre._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), "000000")
    tcpr.append(sh)
    ppr = _ppr(hucre.paragraphs[0]._p)
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0")
    sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), "20")
    sp.set(qn("w:lineRule"), "exact")
    ppr.append(sp)


def _sabit(satir, in_):
    trpr = satir._tr.get_or_add_trPr()
    for e in trpr.findall(qn("w:trHeight")):
        trpr.remove(e)
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(in_ * 1440)))
    h.set(qn("w:hRule"), "exact")
    trpr.append(h)


def _sol_panel(hucre, grup):
    """Sınav grubu (A-D balonları; öğrencinin grubu dolu) + Öğrenci No (11 kutu; sabit hanelerin rakamı yazılı ve
    balonu dolu) + 0-9 balon sütunları. Hücre kenar boşlukları 0 -> balonlar büyük."""
    n = len(OGRENCI_NO)
    t = _ic_tablo(hucre, 15, n + 1, [3.4 / (n + 1)] * (n + 1), False, yan=0)
    t.cell(0, 0).merge(t.cell(0, n))
    _yaz(t.cell(0, 0), "Sınav grubu", True, "center", 9)
    for k, h in enumerate("ABCD"):
        _yaz(t.cell(1, k), h, False, "center", 8.5)
        _yaz(t.cell(2, k), DOLU if h == grup else BOS, False, "center", 9.5, BALON_FONT)
    t.cell(3, 0).merge(t.cell(3, 5))
    _yaz(t.cell(3, 0), "Öğrenci No", True, "center", 9)
    for k, ch in enumerate(OGRENCI_NO):
        _kenar(t.cell(4, 1 + k))
        _yaz(t.cell(4, 1 + k), ch if ch.isdigit() else "", False, "center", 9.5)
    for d in range(10):
        _yaz(t.cell(5 + d, 0), str(d), False, "center", 8.5)
        for k, ch in enumerate(OGRENCI_NO):
            _yaz(t.cell(5 + d, 1 + k), DOLU if ch == str(d) else BOS, False, "center", 9.5, BALON_FONT)
    for i, r in enumerate(t.rows):
        _yukseklik(r, 0.2 if i == 4 else 0.176)
    return t


def _sag_panel(hucre, n, birimler):
    """Test soruları (1..n) için A-E balonları (başlık tek), altında boşluk doldurma cevap kutuları."""
    t = _ic_tablo(hucre, 2 + n, 6, [0.35] + [0.5] * 5, False, yan=0)
    t.cell(0, 0).merge(t.cell(0, 5))
    _yaz(t.cell(0, 0), "Dinamik – Test", True, "center", 9)
    for k, h in enumerate("ABCDE"):
        _yaz(t.cell(1, 1 + k), h, False, "center", 8.5)
    for q in range(1, n + 1):
        _yaz(t.cell(1 + q, 0), str(q), False, "center", 9)
        for k in range(5):
            _yaz(t.cell(1 + q, 1 + k), BOS, False, "center", 9.5, BALON_FONT)
    for row in t.rows:
        _yukseklik(row, 0.19)
    m = len(birimler)
    kutu = _ic_tablo(hucre, 2, m, [3.4 / m] * m, True, yan=0, ilk_sil=False)
    for k, b in enumerate(birimler):
        _yaz(kutu.cell(0, k), str(n + k + 1), True, "center", 10)
        _yaz(kutu.cell(1, k), b, False, "right", 9)
    _yukseklik(kutu.rows[1], 0.4)
    return t


def _baslik(doc, p, kod):
    """'BASLIK|grup|n_test|birim1|birim2...' -> sayfa başı (tam genişlik): ad/imza satırı, köşe işaretli optik form
    (solda sınav grubu + öğrenci no, sağda test balonları ve boşluk doldurma kutuları); ardından iki sütunlu düzene
    geçiş."""
    _, grup, n, *birimler = [x.strip() for x in kod.split("|")]
    n = int(n)
    bilgi = _tablo(doc, 1, 6, (1.0, 2.7, 0.6, 1.3, 0.6, 1.3), True)
    for k, (a, b) in enumerate((("Adı Soyadı:", None), ("İmza:", None), ("Grup:", grup))):
        _yaz(bilgi.cell(0, 2 * k), a, True)
        if b:
            _yaz(bilgi.cell(0, 2 * k + 1), b, True, "left", 11)
    _yukseklik(bilgi.rows[0], 0.3)

    # optik form: 5 sütun (köşe işaretleri 0.2 in), 5 satır; içerik panelleri 1-3. satırlarda birleşik
    dis = _tablo(doc, 5, 5, (0.2, 3.45, 0.2, 3.45, 0.2), False)
    for r, h in zip(dis.rows, (0.2, 1.45, 0.2, 1.45, 0.2)):
        _yukseklik(r, h)
    for r in (0, 4):
        for c in (0, 2, 4):
            _siyah(dis.cell(r, c))
        _sabit(dis.rows[r], 0.2)
    for c in (0, 4):
        _siyah(dis.cell(2, c))
    _sabit(dis.rows[2], 0.2)
    sol = dis.cell(1, 1).merge(dis.cell(3, 1))
    sag = dis.cell(1, 3).merge(dis.cell(3, 3))
    _sol_panel(sol, grup)
    _sag_panel(sag, n, birimler)

    # tam genişlikli bölümü bitir: öncekiler 1 sütun, sonraki bölüm (belgenin son bölümü) 2 sütun
    son = doc.sections[-1]._sectPr
    ilk = copy.deepcopy(son)
    for c in ilk.findall(qn("w:cols")):
        ilk.remove(c)
    cols = OxmlElement("w:cols")
    cols.set(qn("w:num"), "1")
    cols.set(qn("w:space"), "144")
    ilk.append(cols)
    kes = OxmlElement("w:p")
    kes_ppr = OxmlElement("w:pPr")
    kes_ppr.append(ilk)
    kes.append(kes_ppr)
    tip = OxmlElement("w:type")
    tip.set(qn("w:val"), "continuous")
    for e in son.findall(qn("w:type")):
        son.remove(e)
    son.insert(0, tip)

    for oge in (bilgi._tbl, _ayirici(), dis._tbl, kes):
        p.addprevious(oge)
    p.getparent().remove(p)


def duzenle(yol, tarih=None):
    doc = Document(str(yol))
    body = doc.element.body
    cocuklar = list(body.iterchildren())
    i = 0
    while i < len(cocuklar):
        el = cocuklar[i]
        st = _stil(el) if el.tag == qn("w:p") else None
        if st == "Isaret":
            _baslik(doc, el, _metin(el).strip())
            i += 1
            continue
        if st == "SoruMetni":
            j = i
            while j < len(cocuklar) and cocuklar[j].tag == qn("w:p") and _stil(cocuklar[j]) == "SoruMetni":
                _hiza(cocuklar[j], "left")
                j += 1
            # ardışık soruları ayır: yalnızca son sorunun paragrafları şekille eşleşir
            i = max(k for k in range(i, j) if re.match(r"\d+\.\s", _metin(cocuklar[k])) or k == i)
            el = cocuklar[i]
            metin = cocuklar[i:j]
            if j < len(cocuklar) and cocuklar[j].tag == qn("w:p") and _stil(cocuklar[j]) == "SoruSekil":
                t = _tablo(doc, 1, 2, (METIN_IN, SEKIL_IN), False)
                el.addprevious(t._tbl)
                sekil = cocuklar[j]
                _hiza(sekil, "center")
                _aralik(sekil)
                _hucreye(t.cell(0, 0), metin)
                _hucreye(t.cell(0, 1), [sekil])
                t._tbl.addnext(_ayirici())
                i = j + 1
            else:
                i = j
            continue
        if st == "Secenek":
            j = i
            while j < len(cocuklar) and cocuklar[j].tag == qn("w:p") and _stil(cocuklar[j]) == "Secenek":
                j += 1
            sec = cocuklar[i:j]
            uzun = max(len(_metin(p)) for p in sec)
            sutun = len(sec) if uzun <= KUTU_UZUN else 3
            satir = -(-len(sec) // sutun)
            t = _tablo(doc, satir, sutun, [KUTU_TOPLAM_IN / sutun] * sutun, True)
            sec[0].addprevious(t._tbl)
            for k, p in enumerate(sec):
                h = t.cell(k // sutun, k % sutun)
                _hiza(p, "left")
                _aralik(p)
                for r in p.iter(qn("w:r")):
                    rpr = r.find(qn("w:rPr"))
                    if rpr is None:
                        rpr = OxmlElement("w:rPr")
                        r.insert(0, rpr)
                    sz = OxmlElement("w:sz")
                    sz.set(qn("w:val"), "19")
                    rpr.append(sz)
                _hucreye(h, [p])
            # boş kalan hücrelerde varsayılan boş paragraf kalır
            t._tbl.addnext(_ayirici())
            i = j
            continue
        i += 1
    if tarih:
        for p in doc.sections[0].header.paragraphs:
            if "Vize sınavı" in p.text and tarih not in p.text:
                son = p.runs[-1]
                yeni = copy.deepcopy(son._r)
                son._r.addnext(yeni)
                for tt in yeni.findall(qn("w:t")):
                    tt.text = ", " + tarih
                    tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    doc.save(str(yol))
