# -*- coding: utf-8 -*-
"""Obejście błędu eksportu PDF Inception: usuwa znaki diakrytyczne i nie-ASCII
ze stringów komunikatów zdarzeń (grupy unique=...), zachowując sens.
Wynik nadpisuje finalne PL w batches/batch_zzascii.json (sortuje się ostatni -> wygrywa).
Łatwo odwracalne: usuń batch_zzascii.json i przebuduj."""
import glob, json, re, unicodedata, itertools
import xml.etree.ElementTree as ET

# Grupy zdarzeń do objęcia obejściem (na razie tylko komunikaty zdarzeń):
GROUPS = ["Message"]

rules = {}
for f in ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]:
    for s in ET.parse(f).getroot().findall("string"):
        rules[s.get("name")] = s.get("rules") or ""

pl = {}
for f in sorted(glob.glob("batches/*.json")):
    if f.endswith("batch_zzascii.json"):
        continue  # nie czytaj własnego outputu
    try:
        pl.update(json.load(open(f, encoding="utf-8")))
    except Exception:
        pass

MAP = str.maketrans({
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
    'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z',
    '—': '-', '–': '-', '„': '"', '”': '"', '“': '"', '’': "'", '‘': "'", '…': '...', ' ': ' ',
})

def asciify(s):
    s = s.translate(MAP)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return s

def in_groups(r):
    return any(re.search(r"\bunique=" + g + r"\b", r) for g in GROUPS)

overrides = {}
already = 0
for h, v in pl.items():
    if in_groups(rules.get(h, "")):
        a = asciify(v)
        if a != v:
            overrides[h] = a
        else:
            already += 1

json.dump(overrides, open("batches/batch_zzascii.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"Grupy {GROUPS}: zdiakrytyzowanych (zmienionych): {len(overrides)} | już ASCII: {already}")
print("Przyklady:")
for h in itertools.islice(overrides, 8):
    print(f"  {pl[h][:60]!r}\n   -> {overrides[h][:60]!r}")
