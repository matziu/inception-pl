# Glosariusz EN→PL — Inception (polska nomenklatura branżowa KD/SSWiN)

Wersja robocza. Źródło: polska dokumentacja branżowa KD/SSWiN. Legenda źródła: **✅ branż.** = potwierdzone w dokumentacji branżowej; **🟢 wybór użytk.** = wariant zatwierdzony przez użytkownika w pilotażu; **⚠️ std** = standardowa polska nomenklatura branżowa (do potwierdzenia).

Decyzje kręgosłupowe: **Door→Przejście · Area→Strefa · Input/Output→Linia wejściowa/wyjściowa · Credential→Identyfikator**.

Konwencja **Przejście vs drzwi**: obiekt logiczny / stan / odblokowanie → „przejście”; fizyczne otwarcie lub zamknięcie skrzydła → „drzwi”.

## Obiekty główne

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| User | Użytkownik | ✅ branż. |  |
| Area | Strefa | 🟢 wybór użytk. | Decyzja. Pełny termin branżowy: Strefa alarmowa. Zone w Inception = tylko sprzęt/strefa czasowa — brak kolizji |
| Door | Przejście | 🟢 wybór użytk. | Decyzja: fizyczne drzwi/brama wraz z osprzętem |
| Reader | Czytnik | ✅ branż. |  |
| Credential | Identyfikator | 🟢 wybór użytk. | Decyzja. Fizyczny token = Nośnik |
| Card | Karta | ✅ branż. |  |
| Remote Fob | Zdalny pilot | 🟢 wybór użytk. | Pilot RF (bezprzewodowy, z przyciskami). Decyzja: fob→pilot |
| Fob (pilot RF) | Pilot | 🟢 wybór użytk. | np. Fob Template→Szablon pilota, Fobs→Piloty, Fob Serial→Numer seryjny pilota |
| Fob (zbliżeniowy = credential) | Brelok | 🟢 wybór użytk. | TYLKO gdy 'fob' = token zbliżeniowy odczytywany przez czytnik (def. identyfikatora) |
| Input | Linia wejściowa | 🟢 wybór użytk. | Decyzja: forma pełna (krótko: Wejście tylko przy ciasnym UI) |
| Output | Linia wyjściowa | 🟢 wybór użytk. | Decyzja: forma pełna; w komunikatach dynamicznych też pełna |
| Permission | Uprawnienie | ✅ branż. |  |
| Permissions | Uprawnienia (prawa dostępu) | ✅ branż. |  |
| Web Page Profile | Profil dostępu do panelu | 🟢 wybór użytk. | Live review: ujednolicone z 'profil strony internetowej/WWW/webowej' (77 stringów). Spójne z 'Dostęp do panelu zarządzania' |
| Schedule | Harmonogram | ✅ branż. |  |
| Function Key | Klawisz funkcyjny | ✅ branż. | F1-F4, *, # |
| Local Command | Komenda lokalna | ✅ branż. |  |
| Automation | Automatyka | ✅ branż. |  |
| Automation Node | Węzeł automatyki | ✅ branż. |  |
| Door Group | Grupa przejść | ✅ branż. |  |
| Area Group | Grupa stref | ✅ branż. | Analogia do Grupa przejść/węzłów |
| Storage Unit | Jednostka (boks) | ⚠️ std | Do potw.; magazyn samoobsługowy |
| Site | Obiekt (lokalizacja) | ⚠️ std | Cała instalacja |

## Dostęp

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Access | Dostęp | ✅ branż. |  |
| Access Control | Kontrola dostępu | ✅ branż. |  |
| Access Granted | Przyznanie dostępu | ✅ branż. | Stan: Dostęp przyznany |
| Access Denied | Odmowa dostępu | ✅ branż. | Wariant spotykany: Autoryzacja negatywna |
| Request to Exit (REX) | Przycisk wyjścia | ✅ branż. |  |
| Anti-passback | Anti-passback | ✅ branż. | Zostawione z ang. (konwencja branżowa) |
| Occupancy | Obecność | ✅ branż. | Limit obecnych, Kontrola obecnych |
| Occupancy Limit | Limit obecnych | ✅ branż. |  |
| Operator | Operator | ✅ branż. | Obsługa systemu (VISO) |
| Remote / Web Access | Dostęp do panelu zarządzania | 🟢 wybór użytk. | Live review (podmenu w zarządzaniu użytkownikami) |
| Master | Master | ✅ branż. | Bez tłumaczenia |
| Time & Attendance (T&A) | RCP (rejestracja czasu pracy) | ✅ branż. |  |
| Badge (v) | Odczyt karty | 🟢 wybór użytk. | Partia 2; np. „3-krotny odczyt karty” |

## Alarm i uzbrojenie

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Arm | Uzbrojenie / uzbroić | ✅ branż. |  |
| Disarm | Rozbrojenie / rozbroić | ✅ branż. |  |
| Armed | Uzbrojona | ✅ branż. | O strefie (r. żeński) |
| Disarmed | Rozbrojona | ✅ branż. |  |
| Arming | Uzbrajanie | ✅ branż. |  |
| Auto-Arm | Automatyczne uzbrojenie | 🟢 wybór użytk. | Partia 1 (nie „Auto-uzbrojenie”) |
| Clear Alarm | Skasuj alarm | 🟢 wybór użytk. | Partia 1 |
| Cancel Siren | Wycisz sygnalizator | 🟢 wybór użytk. | Partia 1 |
| Perimeter Arm | Uzbrojenie zewnętrzne | 🟢 wybór użytk. | Partia 2 (nie „obwodowe”) |
| Walk Test | Test obchodowy | 🟢 wybór użytk. | Partia 2 |
| Isolate / Isolated | Izolować / Zaizolowana | 🟢 wybór użytk. | Partia 2; perf. „zaizolować”; zdarz.: „Użytkownik {0} zaizolował linię wejściową {1}” |
| Detector | Czujka | 🟢 wybór użytk. | Partia 2 |
| Audio / Audible Alarm | Alarm dźwiękowy / akustyczny | ⚠️ std | Audio=dźwiękowy, Audible=akustyczny |
| Cabinet (Tamper) | Obudowa (sabotaż obudowy) | ⚠️ std | Partia 2 |
| Alarm | Alarm | ✅ branż. |  |
| Tamper | Sabotaż | ✅ branż. | Alarm sabotażowy |
| Siren | Sygnalizator (akustyczny) | 🟢 wybór użytk. | Pilotaż: zatwierdzone zamiast „Syrena” |
| Entry Delay | Opóźnienie na wejście | 🟢 wybór użytk. | Pilotaż (zamiast „Czas na wejście”) |
| Exit Delay | Opóźnienie na wyjście | 🟢 wybór użytk. | Pilotaż (zamiast „Czas na wyjście”) |

## Zdarzenia i monitorowanie

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Feedback | Sygnalizacja zwrotna | ⚠️ std | Reakcja czytnika (LED/buzzer) |
| Event | Zdarzenie | ✅ branż. |  |
| Review | Rejestr zdarzeń | 🟢 wybór użytk. | Pilotaż |
| Notification | Powiadomienie | ⚠️ std |  |
| Monitoring | Monitorowanie (dozór) | ✅ branż. |  |
| Monitoring Station | Stacja monitorowania | 🟢 wybór użytk. | Pilotaż |
| Report | Raport | ⚠️ std |  |
| Message | Komunikat | ⚠️ std |  |
| Warning | Ostrzeżenie | ⚠️ std |  |

## Logika i automatyka

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| State | Stan | ✅ branż. |  |
| Module/System Health | Stan modułu / systemu | 🟢 wybór użytk. | Live review: 'health'→'stan' (NIE 'zdrowie'). 'health issues'→'problemy ze stanem' |
| Input Sealed / Unsealed | Normalny / Wyzwolony | 🟢 wybór użytk. | Konwencja branżowa (stan normalny / wyzwolenie wejścia). Sealed≠drzwi Closed (='Zamknięte'). Ujednolicono 28 str. (był chaos: uszczelniony/zapieczętowany/'niespokojne linie') |
| States Entered | Wykryte stany | 🟢 wybór użytk. | Test sprzętu — stany, w jakie wchodziły wejścia (było błędnie 'Wejścia w stan') |
| Normal | Stan normalny | ✅ branż. |  |
| Active | Aktywny / wyzwolony | ✅ branż. | Branżowo: wyzwolenie linii |
| Trigger (v) | wyzwalać | ✅ branż. |  |
| Trigger (n) | Wyzwolenie | ✅ branż. |  |
| Trigger Condition | Warunek wyzwalający | ⚠️ std | Pojęcie z Inception |
| Condition | Warunek | ⚠️ std |  |
| Action | Akcja | ✅ branż. |  |
| Pulse | Impuls (chwilowy) | ⚠️ std |  |

## Przejście i osprzęt

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Lock | Zamek | ✅ branż. |  |
| Electric Strike | Elektrozaczep | ✅ branż. |  |
| Magnetic Lock | Zwora (elektromagnetyczna) | ✅ branż. |  |
| Unlock | Odblokowanie / odblokować | ✅ branż. |  |
| Locked | Zablokowane | ✅ branż. |  |
| Unlocked | Odblokowane | ✅ branż. |  |
| Door Contact / Position | Czujnik otwarcia drzwi | ✅ branż. |  |
| Break Glass / Breakglass | KAC Przycisk ewakuacyjny | 🟢 wybór użytk. | Decyzja: brak jednolitego standardu, KAC=konwencja branżowa. 'Broken'→'uruchomiony'. UWAGA: glass-break DETECTOR = 'czujka stłuczenia szkła' (inne urządzenie!) |
| Forced Door | Siłowe otwarcie drzwi | 🟢 wybór użytk. | Pilotaż: stan „siłowego otwarcia” |
| Door Held Open | Drzwi przytrzymane otwarte | 🟢 wybór użytk. | Pilotaż |
| Held Open Too Long | Zbyt długie otwarcie drzwi | ⚠️ std | Faza „zbyt długiego otwarcia” |

## Windy

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Lift | Winda | ✅ branż. |  |
| Floor | Piętro | ✅ branż. |  |
| Lift Car | Kabina windy | ⚠️ std |  |

## Czas

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Time | Czas | ✅ branż. |  |
| Date | Data | ✅ branż. |  |
| Time Period | Przedział czasowy | ⚠️ std |  |
| Time Zone | Strefa czasowa | ⚠️ std | Nie mylić z Area |
| Daylight Saving | Czas letni | ⚠️ std |  |
| Holiday | Święto / dzień wolny | ⚠️ std |  |

## Sprzęt i moduły

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Controller | Kontroler | ✅ branż. |  |
| Module | Moduł | ✅ branż. |  |
| Expander | Ekspander | ✅ branż. |  |
| Terminal | Terminal | ✅ branż. | Terminal dostępu |
| Keypad | Klawiatura | ✅ branż. |  |
| Firmware | Firmware | ✅ branż. | Spotykane też: oprogramowanie firmowe |
| Serial Number | Numer seryjny | ⚠️ std |  |
| Encryption Key | Klucz szyfrujący | ✅ branż. | Spotykane też: klucz komunikacyjny |

## Interfejs (UI)

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| Save | Zapisz | ✅ branż. |  |
| Cancel | Anuluj | ⚠️ std |  |
| Delete | Usuń | ⚠️ std |  |
| Add | Dodaj | ⚠️ std |  |
| Edit | Edytuj | ⚠️ std |  |
| Configure | Konfiguruj | ✅ branż. | Konfiguracja |
| Settings | Ustawienia | ✅ branż. |  |
| Options | Opcje | ✅ branż. |  |
| Enabled | Włączone | 🟢 wybór użytk. | Pilotaż (wariant „załączona” odrzucony) |
| Disabled | Wyłączone | 🟢 wybór użytk. | Pilotaż |
| Default | Domyślny | ✅ branż. |  |
| Select | Wybierz | ✅ branż. |  |
| Back | Wstecz | ⚠️ std |  |
| Next | Dalej | ⚠️ std |  |

## Bez tłumaczenia

| EN (Inception) | PL (kanoniczne) | Źródło | Uwagi |
|---|---|---|---|
| PIN | PIN | ✅ branż. |  |
| OSDP | OSDP | ✅ branż. |  |
| Wiegand | Wiegand | ✅ branż. |  |
| REST API | REST API | ⚠️ std |  |
| LAN / IP / NTP / DHCP | LAN / IP / NTP / DHCP | ✅ branż. |  |

