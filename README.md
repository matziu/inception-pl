# Inception PL — polskie tłumaczenie interfejsu Inner Range Inception

Polski pakiet językowy (`.irlanguage`) dla kontrolera **Inner Range Inception**, firmware **7.2.1.8507**. Przetłumaczone **8327/8327 stringów** interfejsu WWW (100% zestawu do tłumaczenia).

## Import na kontroler

1. Pobierz `Polish-7.2.1.8507-vX.Y.Z.irlanguage` z zakładki **Releases**.
2. W Inception wgraj pakiet językowy (sekcja System / ustawienia języka) i wybierz język **Polish**.
3. Odśwież przeglądarkę z pominięciem cache (**Ctrl+F5**) — część stringów (`translateForJs`) trafia do bundli JS i potrafi zostać w starej wersji.

## Struktura repozytorium

| Ścieżka | Rola |
|---|---|
| `batches/*.json` | **Źródło prawdy tłumaczeń** (hash → tekst PL). Nakładane alfabetycznie, ostatni wygrywa. Poprawki dodawać jako `batch_z*.json`. |
| `_build_PL.py` | Buduje `PL/InnerRangeTranslations_1-3.xml` + kontrole jakości (pokrycie, placeholdery `{n}`, znaczniki, kolizje `unique=`). |
| `_pack_irlanguage.py` | Buduje pakiet importowy `Polish 7.2.1.8507.irlanguage` na bazie `pack_template/`. |
| `_apply_irlangproj.py` | Nanosi batch na `PL/*.irlangproj` (projekt oficjalnego narzędzia InRange; trzyma pełną polszczyznę, także tam gdzie build daje ASCII). |
| `pack_template/` | Eksport z oficjalnego narzędzia InRange (23.06.2026) — wzorzec kolejności stringów i zahashowanych grup `unique=`. Podmieniamy w nim wyłącznie treści `<string>`. |
| `_extracted/` | Zawartość oryginalnego szablonu `.irlanguagetemplate`: stringi EN + plik kontekstowy (pomoc). |
| `InnerRangeTranslations_1-3.xml` (korzeń) | Oryginały EN — wejście buildu. **Nie edytować.** |
| `glosariusz_inception_PL.md` / `.csv` | Glosariusz terminologii (polska nomenklatura branżowa KD/SSWiN). |
| `slices/`, `_plan.csv`, `_AGENT_BRIEF.md` | Potok tłumaczenia wspomaganego agentami (materiał historyczny). |

## Proces poprawek i wydania

1. Poprawka → wpisy w nowym `batches/batch_z*.json` (uwaga: hash obecny w pliku późniejszym alfabetycznie nadpisuje wcześniejszy; komunikaty zdarzeń patrz „Konwencje").
2. `python _build_PL.py` — wynik musi być: pokrycie 100%, 0 kolizji, 0 błędów placeholderów.
3. `python _pack_irlanguage.py` — świeży pakiet `.irlanguage`.
4. `python _apply_irlangproj.py batches/batch_zNOWY.json` — synchronizacja projektu InRange.
5. Wpis w `CHANGELOG.md` → commit → tag `vX.Y.Z` → release na GitHubie z pakietem w załączniku.

## Konwencje

- **Komunikaty zdarzeń** (grupa `rules="unique=Message"`) są celowo **bez polskich znaków** (`batch_zzascii.json`) — obejście błędu eksportu PDF w firmware Inception (litery rozjeżdżają się przy znakach spoza ASCII; zgłoszone do Inner Range). Poprawka ich treści = edycja wpisu w `batch_zzascii.json` (ASCII), nie w późniejszym batchu. Po naprawie firmware: usunąć ten batch i przebudować.
- **Terminologia**: patrz glosariusz. Decyzje kręgosłupowe: Door→Przejście, Area→Strefa, Input/Output→Linia wejściowa/wyjściowa, Credential→Identyfikator, Review→Rejestr zdarzeń, Sealed/Unsealed→Normalny/Wyzwolony, Forgive (anti-passback)→Anuluj naruszenia.
- **Nie zmieniać nigdy**: hashy `name=`, placeholderów `{0}`, atrybutów `translateForJs`/`rules`/`notes`, unikalności w grupach `unique=`.

## Prawa

Angielskie stringi źródłowe i format plików są własnością **Inner Range** — repozytorium jest prywatne; nie publikować bez zgody producenta. Zewnętrzne materiały referencyjne użyte przy budowie glosariusza nie wchodzą w skład repozytorium.
