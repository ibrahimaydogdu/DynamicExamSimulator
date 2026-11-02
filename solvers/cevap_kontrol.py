"""Her sorunun `cevap` ve `celdirici` tanımını varsayılan değerlerde ve 5 rastgele varyantta kontrol eder.
Çalıştır: python cevap_kontrol.py
"""
import sys
import random
import u2, u3, u4, u5
from core import render, varsayilan, uret

sys.stdout.reconfigure(encoding="utf-8")

def fmt(v, ond):
    s = f"{v:.{ond}f}"
    return "0" if float(s) == 0 and v == 0 else s

hatalar = 0
eksik = 0
toplam = 0

for m in (u2, u3, u4, u5):
    for s in m.S:
        toplam += 1
        if s.cevap is None:
            print(f"{s.id:8} --  (test dışı)")
            eksik += 1
            continue
        
        anahtar, birim, ond = s.cevap
        hata_list = []
        
        # 1. Varsayılan değer kontrolü
        p_def = varsayilan(s)
        _, _, vals_def = render(s, p_def)
        
        if anahtar not in vals_def:
            hata_list.append(f"anahtar '{anahtar}' vals içinde yok!")
        else:
            dogru_val = vals_def[anahtar]
            dogru_fmt = fmt(dogru_val, ond)
            
            if s.celdirici is None:
                hata_list.append("celdirici tanımlanmamış!")
            else:
                try:
                    c_def = [float(x) for x in s.celdirici(vals_def)]
                    if len(c_def) < 4:
                        hata_list.append(f"çeldirici sayısı < 4 ({len(c_def)})")
                    c_fmts = [fmt(x, ond) for x in c_def]
                    if dogru_fmt in c_fmts:
                        hata_list.append(f"çeldirici doğru cevaba eşit ({dogru_fmt})")
                    if len(set(c_fmts)) < 4:
                        hata_list.append(f"çeldiriciler basamakta ayırt edilemiyor (benzersiz fmt < 4: {c_fmts})")
                except Exception as e:
                    hata_list.append(f"varsayılan celdirici hatası: {e}")
        
        # 2. 5 rastgele varyant kontrolü
        for seed in (101, 202, 303, 404, 505):
            try:
                res = uret(s, seed)
                _, _, vals_var = render(s, res["params"])
                if anahtar not in vals_var:
                    hata_list.append(f"varyant (seed={seed}) anahtar '{anahtar}' yok!")
                    break
                v_ans = vals_var[anahtar]
                v_fmt = fmt(v_ans, ond)
                if s.celdirici:
                    c_vals = [float(x) for x in s.celdirici(vals_var)]
                    if len(c_vals) < 4:
                        hata_list.append(f"varyant (seed={seed}) çeldirici sayısı < 4")
                        break
                    c_var_fmts = [fmt(x, ond) for x in c_vals]
                    if v_fmt in c_var_fmts:
                        hata_list.append(f"varyant (seed={seed}) çeldirici doğru cevaba eşit: {v_fmt} in {c_var_fmts}")
                        break
                    if len(set(c_var_fmts)) < 4:
                        hata_list.append(f"varyant (seed={seed}) benzersiz çeldirici < 4: {c_var_fmts}")
                        break
            except Exception as e:
                hata_list.append(f"varyant (seed={seed}) hata: {e}")
                break
        
        # Çıktı formatı
        if hata_list:
            hatalar += 1
            print(f"!! {s.id:8} {anahtar:6} = {vals_def.get(anahtar, 0):.{ond}f} {birim:7} HATA: {'; '.join(hata_list)}")
        else:
            c_str = ", ".join(fmt(x, ond) for x in s.celdirici(vals_def)) if s.celdirici else ""
            print(f"   {s.id:8} {anahtar:6} = {vals_def[anahtar]:.{ond}f} {birim:7} [çeldiriciler: {c_str}]")

print("-" * 60)
print(f"Toplam soru: {toplam}, Test dışı: {eksik}, Hatalı: {hatalar}, Başarılı: {toplam - eksik - hatalar}")

