# -*- coding: utf-8 -*-
"""Buduje pakiet importowy `Polish 7.2.1.8507.irlanguage` (ZIP: description.xml + IntegritiTranslations_1.xml).
Szablon: pack_template/ (eksport z oficjalnego narzędzia InRange z 2026-06-23 — zachowuje kolejność,
zahashowane grupy unique= i 3 stringi spoza zestawu tłumaczonego). Podmieniane są WYŁĄCZNIE treści
<string>...</string> wg hasha, wartościami z batches/*.json (ostatni batch wygrywa — jak w _build_PL.py)."""
import re, json, glob, zipfile

PACK_NAME = "Polish 7.2.1.8507.irlanguage"

trans = {}
for bf in sorted(glob.glob("batches/*.json")):
    with open(bf, encoding="utf-8") as f:
        trans.update(json.load(f))
print(f"Wczytano {len(trans)} tłumaczeń.")

def esc(s):  # jak w _build_PL.py: tylko & < >
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

STR_RE = re.compile(r'(<string\b[^>]*>)(.*?)(</string>)', re.S)
NAME_RE = re.compile(r'name="([0-9A-Fa-f]{32})"')

raw = open("pack_template/IntegritiTranslations_1.xml", encoding="utf-8", newline="").read()
applied, untouched = 0, []
def repl(m):
    global applied
    nm = NAME_RE.search(m.group(1))
    if nm and nm.group(1).upper() in trans:
        applied += 1
        return m.group(1) + esc(trans[nm.group(1).upper()]) + m.group(3)
    untouched.append(nm.group(1) if nm else "?")
    return m.group(0)
out = STR_RE.sub(repl, raw)

desc = open("pack_template/description.xml", encoding="utf-8", newline="").read()
with zipfile.ZipFile(PACK_NAME, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("description.xml", desc)
    z.writestr("IntegritiTranslations_1.xml", out)

total = len(STR_RE.findall(raw))
print(f"Podmieniono {applied}/{total} stringów; bez zmian (spoza zestawu): {len(untouched)}")
for h in untouched[:10]:
    print("  szablonowy:", h)
print(f"Zapisano: {PACK_NAME}")
