# -*- coding: utf-8 -*-
import json, glob, random
import xml.etree.ElementTree as ET

SRC = ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]
PLF = ["PL/" + f for f in SRC]

en = {}
for f in SRC:
    for s in ET.parse(f).getroot().findall("string"):
        en[s.get("name")] = s.text or ""
valid = set(en)

# 1) usuń klucze spoza EN z batchy (kosmetyka -> unknown=0)
removed = 0
for bf in glob.glob("batches/*.json"):
    d = json.load(open(bf, encoding="utf-8"))
    bad = [k for k in d if k not in valid]
    if bad:
        for k in bad:
            del d[k]
        json.dump(d, open(bf, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        removed += len(bad)
print("Usuniete nieznane klucze z batchy:", removed)

# 2) poprawnosc PL XML + zachowanie atrybutow
for f in PLF:
    root = ET.parse(f).getroot()  # wyjatek = zle sformulowany XML
    ss = root.findall("string")
    tfj = sum(1 for s in ss if s.get("translateForJs") is not None)
    fc = sum(1 for s in ss if s.get("fullContext") is not None)
    print(f"{f}: {len(ss)} stringow | translateForJs:{tfj} | fullContext:{fc} | XML OK")

# 3) PL identyczne z EN (oczekiwane: akronimy/liczby/nazwy)
pl = {}
for f in PLF:
    for s in ET.parse(f).getroot().findall("string"):
        pl[s.get("name")] = s.text or ""
same = [(h, v) for h, v in pl.items() if v == en.get(h, "") and v.strip()]
print(f"\nPL identyczne z EN: {len(same)} (oczekiwane: PIN/OSDP/akronimy/liczby/nazwy modeli)")
print("Przyklady:", [v for _, v in same[:18]])

# 4) probka EN -> PL
random.seed(11)
samp = random.sample(list(pl.keys()), 14)
print("\n=== PROBKA EN -> PL ===")
for h in samp:
    print("EN:", en[h][:90])
    print("PL:", pl[h][:90])
    print()
