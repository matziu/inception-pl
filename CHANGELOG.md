# Changelog

Wszystkie istotne zmiany polskiego pakietu językowego Inception. Format wg [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/); wersje `vMAJOR.MINOR.PATCH` dotyczą tłumaczenia (wersję firmware wskazuje nazwa pakietu).

## [Unreleased]

## [0.1.1] — 2026-07-03

### Zmienione
- „Guided Tours" ujednolicone na **„Samouczki"** (4 stringi). Było niespójnie: nagłówek panelu głównego „Wycieczki z przewodnikiem", a opcja profilu i teksty pomocy „przewodniki". Teraz: nagłówek „Samouczki", opcja „Pokaż skróty samouczków". Trasy PTZ kamer (osobne znaczenie „tour") pozostają bez zmian jako „trasa PTZ".

## [0.1.0] — 2026-07-03

Pierwsze wydanie na GitHubie: pełne tłumaczenie interfejsu WWW (8327/8327 stringów), build czysty (0 kolizji `unique=`, 0 błędów placeholderów `{n}`).

### Fundament (czerwiec 2026)
- Tłumaczenie całego zestawu na bazie glosariusza opartego na polskiej nomenklaturze branżowej KD/SSWiN; rejestr techniczny, przyciski w trybie rozkazującym.
- Decyzje kręgosłupowe: Door→**Przejście**, Area→**Strefa**, Input/Output→**Linia wejściowa/wyjściowa**, Credential→**Identyfikator**, Review→**Rejestr zdarzeń**, Siren→**Sygnalizator**.
- Potok odtwarzalny: `batches/*.json` → `_build_PL.py` → `PL/*.xml` → `_pack_irlanguage.py` → `.irlanguage`.

### Poprawki po przeglądzie na żywo (21–23.06.2026)
- „Scheduling"→„Harmonogramy"; fob→„pilot" (59 stringów; wyjątek: „brelok" zbliżeniowy); Break Glass→„KAC Przycisk ewakuacyjny"; „Remote / Web Access"→„Dostęp do panelu zarządzania"; „Web Page Profile"→„Profil dostępu do panelu" (77 stringów); module/system health→„stan" (24); Valid/Invalid (zachowanie wyjścia przejścia)→„Przyznano/Odrzucono dostęp".
- Stany linii wejściowych: Sealed/Unsealed→**„Normalny/Wyzwolony"** (konwencja branżowa) — ujednolicone w stanach, komunikatach i opisach pomocy (wcześniej mieszanka „zapieczętowane/odpieczętowane/niezabezpieczone").

### Poprawki 03.07.2026
- Rodzina **„Forgive" (anti-passback) → „anuluj naruszenia"** — 35 stringów; wcześniej niespójna mieszanka „przebacz/wybacz/zwolnij" (w jednym dialogu naraz). Blokady logowania: „znieś blokadę" (spójnie z „Blokada zniesiona"). Stany użytkownika: Forgiven→„Wyjątek anti-passback", Violated and Forgiven→„Naruszenie anti-passback anulowane".
- Naprawione przy okazji: nieprzetłumaczone „amnesty"→„amnestia"; „lift login lockouts" tłumaczone jako „blokady logowania **do windy**" (lift = czasownik „znieść") — poprawione; literówka „zostaną zablokowany"; powtórzenie „dla każdego użytkownika… lub dla każdego użytkownika" w pomocy Widoku użytkowników.

### Znane obejścia
- Komunikaty zdarzeń (grupa `unique=Message`, 442 stringi) celowo **bez polskich diakrytyków** — obejście błędu eksportu PDF w firmware Inception (zgłoszony do Inner Range). Odwracalne: usunąć `batches/batch_zzascii.json` i przebudować.
