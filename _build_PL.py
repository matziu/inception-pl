# -*- coding: utf-8 -*-
"""Build plików PL: oryginalne IRT (raw) + tłumaczenia z batches/*.json -> PL/*.xml.
Podmienia TYLKO treść <string>...</string> wg hasha; reszta pliku bajt w bajt.
Kontrole: pokrycie, nieznane hashe, placeholdery {n}, znaczniki HTML, unikalność (rules=unique=...)."""
import xml.etree.ElementTree as ET, re, json, os, glob, html
from collections import defaultdict

FILES = ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]
os.makedirs("PL", exist_ok=True)
os.makedirs("batches", exist_ok=True)

# 1) wczytaj tłumaczenia
trans = {}
dups = []
for bf in sorted(glob.glob("batches/*.json")):
    with open(bf, encoding="utf-8") as f:
        d = json.load(f)
    for k, v in d.items():
        if k in trans and trans[k] != v:
            dups.append((k, bf))
        trans[k] = v
print(f"Wczytano {len(trans)} tłumaczeń z {len(glob.glob('batches/*.json'))} plików batch.")
if dups:
    print(f"  UWAGA: {len(dups)} hashy zdublowanych w batchach (użyto ostatniego).")

def esc(s):  # escape treści XML (tylko & < >)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

STR_RE = re.compile(r'(<string\b[^>]*>)(.*?)(</string>)', re.S)
NAME_RE = re.compile(r'name="([0-9A-Fa-f]{32})"')

# 2) referencja EN (ET) do kontroli
en = {}
en_rules = {}
for fn in FILES:
    for s in ET.parse(fn).getroot().findall("string"):
        en[s.get("name")] = s.text or ""
        en_rules[s.get("name")] = s.get("rules") or ""

# 3) podmiana w raw i zapis
applied = 0
def repl(m):
    global applied
    head, inner, tail = m.group(1), m.group(2), m.group(3)
    nm = NAME_RE.search(head)
    if not nm:
        return m.group(0)
    h = nm.group(1).upper()
    if h in trans:
        applied += 1
        return head + esc(trans[h]) + tail
    return m.group(0)

per_file = {}
for fn in FILES:
    raw = open(fn, encoding="utf-8").read()
    before = applied
    out = STR_RE.sub(repl, raw)
    per_file[fn] = applied - before
    open(os.path.join("PL", fn), "w", encoding="utf-8", newline="").write(out)

# 4) kontrole jakości
unknown = [h for h in trans if h.upper() not in {k.upper() for k in en}]
ph_re = re.compile(r"\{\d+\}")
ph_bad = []
tag_re = re.compile(r"</?[a-zA-Z][^>]*>")
tag_bad = []
for h, pl in trans.items():
    e = en.get(h, "")
    if sorted(ph_re.findall(e)) != sorted(ph_re.findall(pl)):
        ph_bad.append((h, ph_re.findall(e), ph_re.findall(pl)))
    # HTML w EN jest jako &lt;..&gt; -> po dekodzie
    e_tags = sorted(tag_re.findall(html.unescape(e)))
    pl_tags = sorted(tag_re.findall(pl))
    if e_tags != pl_tags:
        tag_bad.append((h, e_tags, pl_tags))

uniq = defaultdict(lambda: defaultdict(list))
for h, pl in trans.items():
    r = en_rules.get(h, "")
    mu = re.search(r"unique=(\w+)", r)
    if mu:
        uniq[mu.group(1)][pl].append(h)
uniq_bad = []
for grp, vals in uniq.items():
    for val, hs in vals.items():
        if len(hs) > 1:
            uniq_bad.append((grp, val, hs))

total = len(en)
print(f"\nPokrycie: {applied}/{total} ({100*applied/total:.1f}%)")
for fn in FILES:
    print(f"  {fn}: {per_file[fn]}")
print(f"\nKONTROLE:")
print(f"  Nieznane hashe w batchach: {len(unknown)}")
print(f"  Niezgodność placeholderów {{n}}: {len(ph_bad)}")
for h, e, p in ph_bad[:10]:
    print(f"     {h}: EN{e} != PL{p}")
print(f"  Niezgodność znaczników HTML: {len(tag_bad)}")
for h, e, p in tag_bad[:10]:
    print(f"     {h}: EN{e} != PL{p}")
print(f"  Kolizje unikalności (unique=): {len(uniq_bad)}")
for grp, val, hs in uniq_bad[:10]:
    print(f"     [{grp}] '{val}' x{len(hs)}")
