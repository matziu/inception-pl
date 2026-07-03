# -*- coding: utf-8 -*-
"""Naprawia uszkodzone batch_s*.json (niezaescapowane cudzysłowy) parserem liniowym,
porównuje odzyskane klucze ze slice i wskazuje porcje do ponownego uruchomienia."""
import json, re, glob, os

HASH = re.compile(r'^\s*"([0-9A-Fa-f]{32})"\s*:\s*(.*)$')

def loose_parse(path):
    out = {}
    for ln in open(path, encoding="utf-8").read().split("\n"):
        m = HASH.match(ln)
        if not m:
            continue
        h = m.group(1)
        v = m.group(2).strip()
        # usuń pojedynczy trailing przecinek
        if v.endswith(","):
            v = v[:-1].rstrip()
        # zdejmij otaczające cudzysłowy; wnętrze traktuj dosłownie
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            inner = v[1:-1]
        else:
            inner = v.strip('"')
        inner = inner.replace('\\"', '"').replace('\\\\', '\\')
        out[h] = inner
    return out

rerun = []
for i in range(1, 34):
    sid = f"{i:02d}"
    bf = f"batches/batch_s{sid}.json"
    sf = f"slices/slice_{sid}.json"
    slice_keys = set(json.load(open(sf, encoding="utf-8")).keys())
    if not os.path.exists(bf):
        print(f"slice {sid}: BRAK pliku -> rerun ({len(slice_keys)} wpisów)")
        rerun.append(sid)
        continue
    try:
        d = json.load(open(bf, encoding="utf-8"))
        status = "OK (strict)"
    except Exception:
        d = loose_parse(bf)
        # zapisz naprawiony, czysty JSON
        json.dump(d, open(bf, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        status = "NAPRAWIONY"
    miss = slice_keys - set(d.keys())
    extra = set(d.keys()) - slice_keys
    flag = ""
    if miss:
        flag = f" -> BRAKUJE {len(miss)} kluczy, rerun"
        rerun.append(sid)
    if status != "OK (strict)" or miss or extra:
        print(f"slice {sid}: {status} | odzyskano {len(d)}/{len(slice_keys)}" +
              (f" | nadmiar {len(extra)}" if extra else "") + flag)

print("\nPorcje do ponownego uruchomienia:", rerun if rerun else "BRAK")
