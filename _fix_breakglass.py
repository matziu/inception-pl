# -*- coding: utf-8 -*-
"""Ujednolica 'break glass' -> 'KAC Przycisk ewakuacyjny' w widocznych stringach.
Dopasowuje po dokładnym EN, nadpisuje w batch_zfix.json. (Czujka stłuczenia szkła pominięta.)"""
import json
import xml.etree.ElementTree as ET

EN2PL = {
    "Breakglass": "KAC Przycisk ewakuacyjny",
    "Opened (unsecured), Unlocked (Breakglass Broken, Battery Low)":
        "Otwarte (niezabezpieczone), Odblokowane (KAC Przycisk ewakuacyjny uruchomiony, niski poziom baterii)",
    "Opened (unsecured), Unlocked (Breakglass Broken)":
        "Otwarte (niezabezpieczone), Odblokowane (KAC Przycisk ewakuacyjny uruchomiony)",
    "Unlocked (Breakglass Broken, Battery Low)":
        "Odblokowane (KAC Przycisk ewakuacyjny uruchomiony, niski poziom baterii)",
    "Unlocked (Breakglass Broken)":
        "Odblokowane (KAC Przycisk ewakuacyjny uruchomiony)",
    "Doors with Broken Emergency Breakglass":
        "Przejścia z uruchomionym KAC Przyciskiem ewakuacyjnym",
    "The following {0} doors have broken emergency breakglasses. Until they are replaced/reset, the door can not be locked.":
        "Następujące {0} przejść ma uruchomione KAC Przyciski ewakuacyjne. Do czasu ich wymiany/resetu przejścia nie mogą zostać zablokowane.",
    # zdarzenia (unique=Message -> zostaną zdiakrytyzowane przez _asciify_events.py)
    "Door Breakglass Broken": "Uruchomiono KAC Przycisk ewakuacyjny przejścia",
    "Door Breakglass Restored": "Przywrócono KAC Przycisk ewakuacyjny przejścia",
}

en2hash = {}
for f in ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]:
    for s in ET.parse(f).getroot().findall("string"):
        en2hash[(s.text or "")] = s.get("name")

zf = json.load(open("batches/batch_zfix.json", encoding="utf-8"))
applied = []
missing = []
for en, plv in EN2PL.items():
    h = en2hash.get(en)
    if h:
        zf[h] = plv
        applied.append((h, en))
    else:
        missing.append(en)
json.dump(zf, open("batches/batch_zfix.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"Zastosowano: {len(applied)}")
for h, en in applied:
    print(f"  {h[:8]}  {en[:50]!r}")
if missing:
    print("NIE ZNALEZIONO (EN):", missing)
