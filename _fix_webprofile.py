# -*- coding: utf-8 -*-
"""Ujednolica 'Web Page Profile' -> 'Profil dostępu do panelu' (zachowuje odmianę słowa 'profil')."""
import json, glob, re
import xml.etree.ElementTree as ET

pl = {}
for f in sorted(glob.glob("batches/*.json")):
    if f.endswith("batch_zzascii.json"):
        continue
    try:
        pl.update(json.load(open(f, encoding="utf-8")))
    except Exception:
        pass

# P1: profil + (strony/stron ...) + internetow/webow/WWW
P1 = re.compile(r'(profil\w*)\s+stron\w*\s+(?:internetow\w+|webow\w+|WWW)', re.IGNORECASE)
# P2: profil + internetow/webow/WWW/uprawnień internetowych (bez 'strony')
P2 = re.compile(r'(profil\w*)\s+(?:uprawnień\s+internetow\w+|internetow\w+|webow\w+|WWW)', re.IGNORECASE)

def fix(s):
    s = P1.sub(lambda m: m.group(1) + " dostępu do panelu", s)
    s = P2.sub(lambda m: m.group(1) + " dostępu do panelu", s)
    return s

zf = json.load(open("batches/batch_zfix.json", encoding="utf-8"))
changed = 0
for h, v in pl.items():
    nv = fix(v)
    if nv != v:
        zf[h] = nv
        changed += 1
json.dump(zf, open("batches/batch_zfix.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Zmieniono web-profile stringow:", changed)
