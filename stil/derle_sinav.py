#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
İNM 203 Dinamik - Sınav Dokümanı Pandoc Derleyicisi
Bu betik, hazırlanan Markdown sınav sorularını 'VizeSınavıA.docx' şablonuna
(2 sütunlu, Times New Roman, dar kenar boşluklu, üniversite üstbilgili) tam uyumlu DOCX dosyasına dönüştürür.

Kullanım:
    python derle_sinav.py <girdi.md> [-o <cikti.docx>] [--grup A] [--tarih "13.11.2025"]
"""

import os
import sys
import argparse
import subprocess
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DOC = os.path.join(ROOT_DIR, "sinav_stili_referans.docx")

def derle(girdi_md, cikti_docx=None, grup=None, tarih=None):
    if not os.path.exists(girdi_md):
        print(f"Hata: Girdi dosyası bulunamadı: {girdi_md}")
        sys.exit(1)
        
    if not os.path.exists(REF_DOC):
        print(f"Hata: Referans şablonu bulunamadı: {REF_DOC}")
        sys.exit(1)

    if not shutil.which("pandoc"):
        print("Hata: Sistemde 'pandoc' komutu bulunamadı! Lütfen Pandoc'un kurulu ve PATH'e ekli olduğundan emin olun.")
        sys.exit(1)

    if not cikti_docx:
        base, _ = os.path.splitext(girdi_md)
        cikti_docx = f"{base}.docx"

    cmd = [
        "pandoc",
        girdi_md,
        "-o",
        cikti_docx,
        f"--reference-doc={REF_DOC}",
        "--wrap=none"
    ]

    print(f"Derleniyor: {os.path.basename(girdi_md)} -> {os.path.basename(cikti_docx)}")
    res = subprocess.run(cmd, capture_output=True)
    
    if res.returncode == 0:
        print(f"BAŞARILI: Sınav dokümanı üretildi -> {cikti_docx}")
    else:
        err_msg = res.stderr.decode('cp1254', errors='ignore')
        print(f"HATA: Pandoc derlemesi başarısız oldu:\n{err_msg}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Markdown sınav dosyalarını VizeSınavıA formatında DOCX'e dönüştürür.")
    parser.add_argument("girdi", help="Girdi Markdown dosyası (örn: sinav_sablonu.md)")
    parser.add_argument("-o", "--cikti", help="Çıktı DOCX dosyası (varsayılan: <girdi_adı>.docx)")
    args = parser.parse_args()

    derle(args.girdi, args.cikti)
