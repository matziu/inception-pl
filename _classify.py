# -*- coding: utf-8 -*-
"""Klasyfikuje stringi IRT na obszary funkcjonalne (theme) i poziomy (tier).
Tier 1 = krótkie etykiety/komunikaty (UI użytkownika), Tier 2 = konfiguracja,
Tier 3 = długie opisy pomocy. Zapisuje _plan.csv i drukuje macierz liczności."""
import xml.etree.ElementTree as ET, re, csv

FILES = ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]
rows = []
for fn in FILES:
    for s in ET.parse(fn).getroot().findall("string"):
        rows.append((s.get("name"), fn, s.text or "", s.get("rules") or "", s.get("fullContext") or ""))

HELP = re.compile(r"This (trigger )?condition|If enabled|If disabled|Allows |Specifies |is used to|are used to|\[Configuration|\[System|will be true|This option|When enabled|When this", re.I)

THEMES = [
    ("uzbrajanie/strefy", re.compile(r"\b(arm|armed|arming|disarm|disarmed|area|areas|stay|entry delay|exit delay|siren|alarm|tamper)\b", re.I)),
    ("dostep/przejscia", re.compile(r"\b(door|doors|access|unlock|lock|locked|credential|card|badge|reader|readers|rex|request to exit|forced|held open|lockdown)\b", re.I)),
    ("automatyka/sterowanie", re.compile(r"\b(output|outputs|automation|auxiliary|aux|pulse|trigger|control|controlled)\b", re.I)),
    ("uzytkownicy/uprawnienia", re.compile(r"\b(user|users|permission|permissions|operator|pin|profile|holiday)\b", re.I)),
    ("zdarzenia/raporty", re.compile(r"\b(event|events|review|report|reports|reporting|notification|monitoring|message|messages)\b", re.I)),
    ("harmonogramy/czas", re.compile(r"\b(schedule|schedules|time|date|period|timezone|time zone)\b", re.I)),
    ("windy", re.compile(r"\b(lift|lifts|floor|floors|elevator)\b", re.I)),
    ("komunikacja/sprzet", re.compile(r"\b(lan|ip|network|ntp|dhcp|email|smtp|connection|module|modules|firmware|expander|terminal|wiegand|osdp|serial)\b", re.I)),
]

def theme_of(t):
    for name, rx in THEMES:
        if rx.search(t):
            return name
    return "system/ogolne"

def tier_of(t):
    n = len(t)
    if n > 200 or HELP.search(t):
        return 3
    if n <= 40:
        return 1
    return 2

plan = []
for h, fn, t, rules, fc in rows:
    tt = t.strip()
    if not tt:
        continue
    plan.append((h, fn, len(t), tier_of(t), theme_of(t), rules, fc, t))

with open("_plan.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["hash", "plik", "dlugosc", "tier", "obszar", "rules", "fullContext", "EN"])
    for r in plan:
        w.writerow(r)

# Macierz theme x tier
from collections import defaultdict
m = defaultdict(lambda: [0, 0, 0])
for _, _, _, tier, theme, _, _, _ in plan:
    m[theme][tier - 1] += 1
order = [t[0] for t in THEMES] + ["system/ogolne"]
print("Obszar funkcjonalny            T1(etykiety) T2(konfig) T3(pomoc)  RAZEM")
print("-" * 74)
tot = [0, 0, 0]
for th in order:
    a, b, c = m[th]
    tot[0] += a; tot[1] += b; tot[2] += c
    print(f"{th:30s} {a:8d} {b:9d} {c:9d} {a+b+c:8d}")
print("-" * 74)
print(f"{'RAZEM':30s} {tot[0]:8d} {tot[1]:9d} {tot[2]:9d} {sum(tot):8d}")
