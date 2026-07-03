# -*- coding: utf-8 -*-
"""Tworzy slices/slice_NN.json (hash->EN) z nieprzetłumaczonych stringów, w kolejności tier->obszar."""
import csv, json, os, math, glob

done = set()
for b in glob.glob("batches/*.json"):
    try:
        done |= set(json.load(open(b, encoding="utf-8")).keys())
    except Exception:
        pass

rows = []
with open("_plan.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        if r["hash"] in done:
            continue
        rows.append((int(r["tier"]), r["obszar"], r["hash"], r["EN"]))

themeorder = {t: i for i, t in enumerate([
    "uzbrajanie/strefy", "dostep/przejscia", "automatyka/sterowanie",
    "uzytkownicy/uprawnienia", "zdarzenia/raporty", "harmonogramy/czas",
    "windy", "komunikacja/sprzet", "system/ogolne"])}
rows.sort(key=lambda x: (x[0], themeorder.get(x[1], 99), x[2]))

# wyczyść stare slices
os.makedirs("slices", exist_ok=True)
for old in glob.glob("slices/slice_*.json"):
    os.remove(old)

SIZE = 250
n = math.ceil(len(rows) / SIZE)
for i in range(n):
    chunk = rows[i*SIZE:(i+1)*SIZE]
    d = {h: en for (_, _, h, en) in chunk}
    json.dump(d, open(f"slices/slice_{i+1:02d}.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)
print(f"Pozostalo do tlumaczenia: {len(rows)}")
print(f"Utworzono slices: {n} (po max {SIZE})")
