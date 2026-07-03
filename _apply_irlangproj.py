# -*- coding: utf-8 -*-
"""Nakłada tłumaczenia z podanych batchy na PL/*.irlangproj (podmiana treści <TranslationEntry> wg hasha).
Użycie: python _apply_irlangproj.py [batches/plik1.json ...]  (domyślnie batch_zzz-anuluj.json)"""
import re, json, sys, glob

batch_files = sys.argv[1:] or ["batches/batch_zzz-anuluj.json"]
proj = glob.glob("PL/*.irlangproj")[0]

trans = {}
for bf in batch_files:
    with open(bf, encoding="utf-8") as f:
        trans.update(json.load(f))

def esc(s):  # jak w _build_PL.py: tylko & < >
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

raw = open(proj, encoding="utf-8").read()
ENTRY_RE = re.compile(r'(<TranslationEntry\b[^>]*name="([0-9A-Fa-f]{32})"[^>]*>)(.*?)(</TranslationEntry>)', re.S)
applied = []
def repl(m):
    h = m.group(2).upper()
    if h in trans:
        applied.append(h)
        return m.group(1) + esc(trans[h]) + m.group(4)
    return m.group(0)
out = ENTRY_RE.sub(repl, raw)
open(proj, "w", encoding="utf-8", newline="").write(out)
print(f"{proj}: podmieniono {len(applied)}/{len(trans)} wpisów.")
missing = set(k.upper() for k in trans) - set(applied)
for h in sorted(missing):
    print("  BRAK:", h)
