"""Simülatör için docs/paket.zip üretir (Pyodide'de açılır): çözücüler, md, Ünite 2-5 sayısal şekilleri, şablon.

Çalıştır: python solvers/web_paketle.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEDEF = ROOT / "docs" / "paket.zip"
PY = ["core.py", "cizimler.py", "sozel.py", "sinav_uret.py", "sim.py", "u2.py", "u3.py", "u4.py", "u5.py"]


def main():
    dosyalar = [(ROOT / "solvers" / f, f"solvers/{f}") for f in PY]
    dosyalar += [(ROOT / "zorluk_tablosu.md", "zorluk_tablosu.md"), (ROOT / "stil" / "sinav_sablonu.md", "stil/sinav_sablonu.md"),
                 (ROOT / "media" / "sayilar_duzeltilmis.json", "media/sayilar_duzeltilmis.json")]
    for u in (2, 3, 4, 5):
        for tur in ("Sözel", "Sayısal"):
            p = ROOT / "md" / f"Dinamik {u}. Ünite {tur} Sorular.md"
            dosyalar.append((p, f"md/{p.name}"))
        for p in sorted((ROOT / "media" / f"Dinamik {u}. Ünite Sayısal Sorular").glob("*")):
            dosyalar.append((p, f"media/{p.parent.name}/{p.name}"))
    HEDEF.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(HEDEF, "w", zipfile.ZIP_DEFLATED) as z:
        for yol, ad in dosyalar:
            z.write(yol, ad)
    print(f"{len(dosyalar)} dosya, {HEDEF.stat().st_size / 1e6:.1f} MB -> {HEDEF}")


if __name__ == "__main__":
    main()
