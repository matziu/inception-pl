# BRIEF TŁUMACZA — Inception EN→PL (kontrola dostępu, polska nomenklatura branżowa)

Tłumaczysz interfejs WWW systemu kontroli dostępu **Inner Range Inception** na **profesjonalny polski**, zgodny z polską nomenklaturą branżową KD/SSWiN.

## ZASADY TWARDE (krytyczne — złamanie psuje import)
1. Klucze JSON = 32-znakowe hashe. KOPIUJ JE DOKŁADNIE z pliku slice. Nie zmieniaj, nie dodawaj, nie usuwaj kluczy.
2. Przetłumacz KAŻDY wpis ze slice. Wynik ma mieć tyle samo kluczy co wejście.
3. Placeholdery `{0}` `{1}` `{2}` … zostaw bez zmian (te same numery), wstawione w sensownym miejscu zdania.
4. Znaczniki HTML (`<i>…</i>`, `<b>`, `<p>`, `<ul>`, `<li>`, `<br>`) zostaw — tłumacz tekst MIĘDZY nimi. Nie usuwaj ani nie dodawaj znaczników.
5. Zachowaj wiodące/końcowe spacje oraz interpunkcję (np. `"Tekst:"` zostaje z dwukropkiem; `" fragment "` zostaje ze spacjami).
6. NIE TŁUMACZ (zostaw 1:1): PIN, OSDP, Wiegand, SIFER, LAN, IP, NTP, DHCP, GMT, SMTP, DNS, URL, REST, API, RFID, NFC, MIFARE, Bluetooth, Master, anti-passback, DUIM, oraz nazwy modeli/produktów (np. „Elite X", „Mini Expander" — nazwy własne sprzętu) i kody.
7. Jednostki i wartości zostaw (np. `[s]`, `[Ohm]`, `V`, `mA`, liczby, adresy).
8. Stosuj GLOSARIUSZ poniżej DOKŁADNIE i KONSEKWENTNIE. Pełna lista także w pliku `glosariusz_inception_PL.csv` (separator `;`) — możesz go przeczytać.

## GLOSARIUSZ (stosuj dokładnie)
Obiekty: User→Użytkownik · Area→Strefa · Door→Przejście · Reader→Czytnik · Credential→Identyfikator · Card→Karta · Fob→Brelok · Input→Linia wejściowa · Output→Linia wyjściowa · Permission→Uprawnienie · Permissions→Uprawnienia · Schedule→Harmonogram · Function Key→Klawisz funkcyjny · Local Command→Komenda lokalna · Automation Node→Węzeł automatyki · Door Group→Grupa przejść · Lift→Winda · Floor→Piętro · Terminal→Terminal · Module→Moduł · Expander→Ekspander · Controller→Kontroler · Storage Unit→Jednostka (boks) · Site→Obiekt.

Dostęp: Access→Dostęp · Access Control→Kontrola dostępu · Access Granted→Przyznanie dostępu · Access Denied→Odmowa dostępu · Request to Exit / REX→Przycisk wyjścia · Occupancy→Obecność · Occupancy Limit→Limit obecnych · Time & Attendance / T&A→RCP · Operator→Operator · Badge (czynność)→odczyt karty (np. „3-krotny odczyt karty").

Alarm/uzbrojenie: Arm→Uzbrój (przycisk) / Uzbrojenie (rzecz.) · Disarm→Rozbrój / Rozbrojenie · Armed→Uzbrojona · Disarmed→Rozbrojona · Arming→Uzbrajanie · Alarm→Alarm · Tamper→Sabotaż · Siren→Sygnalizator · Entry Delay→Opóźnienie na wejście · Exit Delay→Opóźnienie na wyjście · Auto-Arm→Automatyczne uzbrojenie · Perimeter Arm→Uzbrojenie zewnętrzne · Stay Arm→Uzbrojenie w obecności · Full Arm→Pełne uzbrojenie · Part(ial) Arm→Częściowe uzbrojenie · Night Arm→Nocne uzbrojenie · Walk Test→Test obchodowy · Isolate→izolować/zaizolować · Isolated→Zaizolowana · Detector→Czujka · Clear Alarm→Skasuj alarm · Cancel Siren→Wycisz sygnalizator · Audio Alarm→Alarm dźwiękowy · Audible Alarm→Alarm akustyczny · Cabinet (tamper)→obudowa.

Logika/automatyka: State→Stan · Trigger→Wyzwolenie (rzecz.) / wyzwalać (czas.) · Trigger Condition→Warunek wyzwalający · Condition→Warunek · Action→Akcja · Pulse→Impuls.

Przejście/osprzęt: Lock→Zamek · Electric Strike→Elektrozaczep · Magnetic Lock→Zwora · Unlock→Odblokuj / Odblokowanie · Locked→Zablokowane · Unlocked→Odblokowane · Door Contact / Position→Czujnik otwarcia drzwi · Forced→Siłowe otwarcie (stan „siłowego otwarcia") · Door Held Open→Drzwi przytrzymane otwarte · Held Open Too Long→Zbyt długie otwarcie drzwi.

Zdarzenia/monitorowanie: Event→Zdarzenie · Review→Rejestr zdarzeń · Notification→Powiadomienie · Monitoring→Monitorowanie · Monitoring Station→Stacja monitorowania · Report→Raport · Message→Komunikat · Warning→Ostrzeżenie · Feedback→Sygnalizacja zwrotna.

Czas: Time→Czas · Date→Data · Time Period→Przedział czasowy · Time Zone→Strefa czasowa · Daylight Saving→Czas letni · Holiday→Święto / dzień wolny.

Sprzęt: Firmware→Firmware (oprogr. firmowe) · Serial Number→Numer seryjny · Encryption Key→Klucz szyfrujący · Keypad→Klawiatura.

UI: Save→Zapisz · Cancel→Anuluj · Delete→Usuń · Add→Dodaj · Edit→Edytuj · Configure→Konfiguruj · Settings→Ustawienia · Options→Opcje · Enabled→Włączone · Disabled→Wyłączone · Default→Domyślny · Select→Wybierz · Back→Wstecz · Next→Dalej · Yes/No→Tak/Nie · Save Changes→Zapisz zmiany.

## KONWENCJE
- **Przejście vs drzwi:** obiekt logiczny / stan / odblokowanie → „przejście"; fizyczne otwarcie/zamknięcie skrzydła → „drzwi" (np. „gdy drzwi zostaną otwarte… przejście przechodzi w stan…").
- **Przyciski akcji = tryb rozkazujący:** „Uzbrój", „Rozbrój", „Odblokuj", „Steruj…", „Zapisz", „Usuń".
- **Strefa to rodzaj żeński:** „Strefa uzbrojona/rozbrojona/gotowa".
- **Komunikaty zdarzeń (audyt)** = czas przeszły z użytkownikiem: „Użytkownik {0} zaizolował linię wejściową {1}", „Użytkownik {0} rozbroił strefę {1}".
- Pełna forma „Linia wejściowa/wyjściowa" — nie skracaj nawet w komunikatach.
- Ton: rzeczowy, techniczny, profesjonalny (instrukcja dla instalatora i użytkownika).
- Nawigacja w `[…]` (np. `[Configuration > Access Control]`) — tłumacz nazwy pozycji menu (Configuration→Konfiguracja, Access Control→Kontrola dostępu), zachowując strukturę `[… > …]`.

## FORMAT WYJŚCIA
Zapisz plik wskazany w zadaniu (np. `batches/batch_s07.json`) w UTF-8 jako poprawny obiekt JSON:
`{ "HASH32": "tłumaczenie PL", "HASH32": "tłumaczenie PL", ... }`
Tylko JSON (bez komentarzy, bez ```), klucze dokładnie jak w slice, wszystkie wpisy przetłumaczone.
