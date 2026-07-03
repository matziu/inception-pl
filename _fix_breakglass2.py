# -*- coding: utf-8 -*-
"""Ujednolica 'break glass' w 4 długich opisach pomocy -> KAC Przycisk ewakuacyjny."""
import json
import xml.etree.ElementTree as ET

NEW = {
    "313514FD": " - Konfiguruje linię wejściową jako KAC Przycisk ewakuacyjny. Po wybraniu tej opcji należy powiązać tę linię wejściową z przejściem. KAC Przycisk ewakuacyjny jest często podłączony bezpośrednio do obwodu zasilania drzwi, umożliwiając odblokowanie drzwi w nagłych wypadkach. Powoduje to jednak ominięcie stanu linii wyjściowej zamka, więc nawet jeśli kontroler wskazuje zablokowane przejście, drzwi mogą być faktycznie otwarte. Poprzez podłączenie KAC Przycisku ewakuacyjnego do systemu i powiązanie go z przejściem, przejście zostanie oznaczone jako odblokowane, a przyczyna zostanie zidentyfikowana jako KAC Przycisk ewakuacyjny. Generowane jest również ostrzeżenie z monitem, że KAC Przycisk ewakuacyjny należy naprawić i że przejście nie jest zabezpieczone.",
    "3139387E": " - Konfiguruje linię wejściową jako KAC Przycisk ewakuacyjny i po ustawieniu konieczne będzie powiązanie tej linii wejściowej z przejściem. KAC Przycisk ewakuacyjny jest często podłączony bezpośrednio do obwodu zasilania przejścia, co umożliwia odblokowanie drzwi w nagłej sytuacji. Powoduje to jednak ominięcie stanu linii wyjściowej zamka — nawet jeśli kontroler wskazuje, że przejście jest zablokowane, drzwi można faktycznie otworzyć. Podłączając KAC Przycisk ewakuacyjny do systemu i łącząc go z przejściem, przejście zostanie oznaczone jako odblokowane, a jako przyczyna zostanie wskazany KAC Przycisk ewakuacyjny. Zostanie również wygenerowane ostrzeżenie informujące, że KAC Przycisk ewakuacyjny wymaga naprawy i że przejście nie jest zabezpieczone.",
    "2CADD683": " - Jeśli funkcja linii wejściowej jest ustawiona na funkcję kontroli dostępu, taką jak czujnik otwarcia drzwi, czujnik ryglowy/kontaktowy, REX, REN lub KAC Przycisk ewakuacyjny, należy ustawić opcję powiązanego przejścia. Powiązane przejście służy do określenia, które przejście powinno reagować na informacje z linii wejściowej. Opcja powiązanego przejścia nie jest dostępna, jeśli funkcja linii wejściowej jest ustawiona na czujkę ogólnego przeznaczenia lub przełącznik/przycisk ogólnego przeznaczenia, ponieważ te funkcje nie odnoszą się do kontroli dostępu.",
    "7C969ACD": "Strona przeglądu systemu wyświetla ogólne informacje o systemie Inception. Wszelkie problemy, które mogą uniemożliwiać optymalne działanie systemu, są również wyświetlane i powodują pojawienie się ostrzeżenia lub błędu na pasku powiadomień u góry strony. Wszelkie ostrzeżenia powinny być jak najszybciej usunięte. Mogą one wskazywać na problemy, takie jak moduły lub urządzenia peryferyjne offline lub mające problemy zdrowotne, np. problemy z zasilaniem, lub na to, że ścieżka raportowania alarmów jest offline. Wyświetlane są również inne ostrzeżenia, takie jak linie wejściowe stale zaizolowane lub przejścia, które nie mogą zostać zablokowane z powodu uruchomionego KAC Przycisku ewakuacyjnego.",
}

allh = set()
for f in ["InnerRangeTranslations_1.xml", "InnerRangeTranslations_2.xml", "InnerRangeTranslations_3.xml"]:
    for s in ET.parse(f).getroot().findall("string"):
        allh.add(s.get("name"))
pref2full = {}
for h in allh:
    pref2full.setdefault(h[:8], []).append(h)

zf = json.load(open("batches/batch_zfix.json", encoding="utf-8"))
for pref, plv in NEW.items():
    full = pref2full.get(pref, [])
    if len(full) == 1:
        zf[full[0]] = plv
        print("OK", pref, "->", full[0])
    else:
        print("UWAGA", pref, "dopasowania:", full)
json.dump(zf, open("batches/batch_zfix.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
