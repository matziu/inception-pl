# -*- coding: utf-8 -*-
"""'health' modułów/systemu: zamienia 'zdrowie/zdrowotny' -> 'stan' w PL, z zachowaniem gramatyki."""
import json, glob
import xml.etree.ElementTree as ET

pl = {}
for f in sorted(glob.glob("batches/*.json")):
    if f.endswith("batch_zzascii.json"):
        continue
    try:
        pl.update(json.load(open(f, encoding="utf-8")))
    except Exception:
        pass

# kolejność: specyficzne frazy najpierw, katch-alle na końcu
REPL = [
    ("stanu zdrowia", "stanu"),
    ("stanem zdrowia", "stanem"),
    ("stanie zdrowia", "stanie"),
    ("ze zdrowiem", "ze stanem"),
    ("problemy zdrowotne", "problemy ze stanem"),
    ("problemów zdrowotnych", "problemów ze stanem"),
    ("problemach zdrowotnych", "problemach ze stanem"),
    ("problemu zdrowotnego", "problemu ze stanem"),
    ("problem zdrowotny", "problem ze stanem"),
    ("zdarzeń zdrowotnych", "zdarzeń dotyczących stanu"),
    # katch-alle (po specyficznych):
    ("zdrowotnych", "dotyczących stanu"),
    ("zdrowotnego", "dotyczącego stanu"),
    ("zdrowotnym", "dotyczącym stanu"),
    ("zdrowotne", "dotyczące stanu"),
    ("zdrowotny", "dotyczący stanu"),
    ("zdrowia", "stanu"),
    ("zdrowiem", "stanem"),
]

def cap(s):
    return s[:1].upper() + s[1:] if s else s

zf = json.load(open("batches/batch_zfix.json", encoding="utf-8"))
changed = 0
for h, v in pl.items():
    if "zdrow" not in v.lower():
        continue
    nv = v
    for a, b in REPL:
        nv = nv.replace(a, b)
        nv = nv.replace(cap(a), cap(b))
    if nv != v:
        zf[h] = nv
        changed += 1
json.dump(zf, open("batches/batch_zfix.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Zmieniono health-stringow:", changed)
