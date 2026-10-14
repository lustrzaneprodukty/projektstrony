# Raport finalizacji — Lustrzane Produkty

Data: 14.10.2026. Zakres: załączony statyczny frontend; bez publikacji i bez przyszłych integracji.

## Wprowadzone zmiany

- Zachowano nazwę marki Lustrzane Produkty. Dane Puchary i Medale Sp. z o.o., adres, NIP, REGON i KRS wprowadzono w stopce, dokumentach i danych Organization. Wykorzystano e-mail i telefon istniejące w projekcie; nie potwierdzano zewnętrznie obsługi tych kanałów przez spółkę.
- Zredagowano 12 podstron prawnych i informacyjnych. Usunięto publiczne pola do uzupełnienia, statusy robocze i zapowiedzi integracji. Formularze oświadczeń zachowują celowo puste miejsca do wypełnienia przez klienta.
- Regulamin opisuje rzeczywistą ścieżkę zapytania i uzgodnienia oferty e-mail. Rozróżnia odstąpienie bez przyczyny, niezgodność towaru z umową i ewentualną gwarancję. Wyjątek dla personalizacji nie obejmuje automatycznie standardowych wariantów i nie wyłącza reklamacji.
- Ujednolicono zasady uzgadniania projektu w FAQ i dokumentach. Usunięto obietnicę 48 godzin i niepotwierdzoną bezpłatność przygotowania grafiki. Ten opis procesu wymaga faktycznego stosowania przez obsługę.
- Rozbudowano zakładkę bezpieczeństwa i dodano renderer danych GPSR konkretnego wyrobu. Nie przypisano automatycznie spółki jako producenta produktów demonstracyjnych.
- Politykę prywatności i cookies dopasowano do braku backendu, płatności i analityki. Frontend nie zapisuje cookies/localStorage/sessionStorage/IndexedDB. Brak banera odpowiada temu kodowi; nie jest wynikiem audytu hostingu.
- Nie uruchomiono Stripe. Podstawę zapisów i wymagania dla późniejszej integracji umieszczono w niepublicznym pliku TEKSTY-DO-WDROZENIA.md. Publiczna polityka nie przypisuje danych nieaktywnemu operatorowi.
- Zmieniono title, H1 i opis strony głównej zgodnie z rzeczywistą kolekcją voucherów, certyfikatów, wizytówek i dekoracji. Stałe podstrony mają odrębne tytuły i opisy. Nie dodano SEO dla fikcyjnych nagród ani statuetek.
- Usunięto domenę testową, wymuszone noindex dokumentów oraz dane Product demonstracyjnego katalogu. Konfiguracja SITE_URL uruchamia canonical, og:url, obraz OG i sitemap. Organization oraz WebSite nie wymagają fikcyjnej domeny; BreadcrumbList pojawia się po jej ustawieniu.
- Przykładowe ceny zastąpiono widocznym zaproszeniem do wyceny. Źródłowy katalog pozostaje wymienny. Eksport wyszukiwarki ograniczono do czterech publicznych pól, aby przyszłe dane wewnętrzne nie trafiały automatycznie do przeglądarki.
- Naprawiono kontakt w stopce prowadzący wcześniej do tej samej stopki. Dodano przycisk pauzy przewijania opinii i natywne sterowanie filmem oraz zatrzymanie przy ograniczonym ruchu.
- Nie zmieniono pliku CSS, fontów, zdjęć ani filmu. Układ sekcji, klasy, kolory i identyfikacja pozostały. Treści, stopka i nowe kontrolki mogą zmienić lokalną wysokość lub łamanie wierszy.

## Wyniki kontroli

| Kontrola | Wynik |
|---|---|
| Generowanie `python build.py` | poprawne |
| `python verify.py` | 29 stron, 1848 lokalnych odwołań, 0 błędów |
| H1, title, description | po jednym na każdej stronie |
| Lokalne strony, zasoby i kotwice | wszystkie wskazane cele istnieją |
| Powielone identyfikatory HTML | brak |
| JSON-LD | poprawny JSON, bez Product/Offer/ocen demonstracyjnych |
| `node --check` app.js i data.js | poprawna składnia |
| SITE_URL ustawione / puste | canonical i sitemap włączane warunkowo; brak domeny testowej w wersji końcowej |
| GPSR własny / inny producent | poprawne przypisanie; brak danych podmiotu UE przy producencie spoza UE zatrzymuje generowanie |
| Escaping treści GPSR | tekst HTML kodowany |
| Lokalny serwer HTTP | 29 stron dostępnych, kod 200 |
| Porównanie CSS i mediów z ZIP źródłowym | identyczne bajtowo |
| Testy interakcji i zrzuty desktop/mobile | niewykonane: brak zainstalowanej przeglądarki Chromium |

Skan treści HTML/JS i nazw zasobów nie ujawnił jawnych danych dostawców surowców, rachunków bankowych ani kluczy Stripe. Nie otrzymano listy poufnych nazw do porównania. Logotypy marek, realizacje i obrazy wiadomości zachowano; bez potwierdzenia ich pochodzenia nie można kategorycznie wykluczyć informacji poufnych w samych pikselach ani potwierdzić praw do publikacji. Nie wykonano pełnego OCR ani oceny praw do mediów.

## Kwestie wymagające potwierdzenia przed uruchomieniem

1. **Spółka i kontakt:** sąd rejestrowy i kapitał zakładowy uzupełniono w aktualizacji opisanej poniżej. Potwierdzić obsługę istniejącego e-maila i telefonu także jako kontaktu producenta. Potwierdzić adres logistyczny zwrotów; nie ustanowiono fikcyjnego oddzielnego magazynu.
2. **RODO i hosting:** dostawcy, role, umowy powierzenia, kraje przetwarzania i konkretne podstawy transferów, rzeczywiste kryteria/okresy logów i kopii, status IOD, legalna publikacja opinii i realizacji. Opis transferów jest ogólny z powodu braku umów; nie jest kompletną informacją o ustalonym transferze. Przed zbieraniem danych w środowisku produkcyjnym należy go skonkretyzować.
3. **Produkty:** rzeczywisty katalog, ceny, warianty, identyfikacja, producent każdego wyrobu, ocena ryzyka i wynikające z niej ostrzeżenia, oznakowanie i instrukcje. Ogólna strona GPSR nie wystarcza do legalnego wystawienia każdej oferty. Dokumentacja materiałowa pozostaje wewnętrzna, a obowiązkowe dane producenta i podmiotu UE pozostają publiczne.
4. **Sprzedaż i Stripe:** checkout, moment zawarcia umowy, wybrane metody i właściwy podmiot Stripe, dane przekazywane operatorowi, zwroty, trwały nośnik i aktualne wymagania funkcji odstąpienia. Szczegóły w TEKSTY-DO-WDROZENIA.md. Nie wykonano integracji.
5. **Dostawy:** przewoźnika i ceny potwierdzono i opublikowano w aktualizacji poniżej. Do ustalenia pozostają konkretne kraje dostaw zagranicznych, terminy, zasady odbioru zwrotów oraz szacunki kosztów zwrotu towarów, których nie da się odesłać zwykłą pocztą. Informacje muszą być przekazane przed umową, nie dopiero po reklamacji lub odstąpieniu.
6. **Domena i dalsze funkcje:** potwierdzona domena, konfigurator 3D, kreator logo, studio projektowania, rzeczywiste dane Product i sitemap, testy indeksowania. Nie uruchomiono Search Console.
7. **Weryfikacja końcowa:** testy wizualne i klawiaturą na komputerze i telefonie, działanie aplikacji pocztowej, audyt cookies na rzeczywistym hostingu, ocena zastosowania wymagań dostępności i całej ścieżki zakupu. Dokumenty nie są deklaracją pełnej zgodności prawnej ani certyfikatem GPSR.

## Źródła i zakres weryfikacji prawnej

Sprawdzono oficjalne źródła 14.10.2026. Ochronę konsumenta i treść GPSR oparto na dostępnych przepisach i objaśnieniach, bez deklarowania zgodności nieznanych procesów operacyjnych.

- UOKiK: https://prawakonsumenta.uokik.gov.pl/reklamacja/niezgodnosc/
- UOKiK — wyjątki: https://prawakonsumenta.uokik.gov.pl/prawo-odstapienia-od-umowy/wylaczenia-prawa-do-odstapienia/
- UOKiK — skutki odstąpienia: https://prawakonsumenta.uokik.gov.pl/prawo-odstapienia-od-umowy/skutek/
- Dziennik Ustaw — tekst jednolity ustawy o prawach konsumenta: https://dziennikustaw.gov.pl/DU/2026/1244 (sprawdzono wpis publikacyjny; pełna treść przez użyty czytnik nie była dostępna).
- EUR-Lex — rozporządzenie 2023/988, w szczególności art. 9 i 19: https://eur-lex.europa.eu/eli/reg/2023/988/oj/eng
- EUR-Lex wskazuje wersję skonsolidowaną 29.05.2026: https://eur-lex.europa.eu/eli/reg/2023/988/2026-05-29/eng . Odczyt tej wersji został zablokowany przez weryfikację przeglądarki; nie potwierdzono pełnego zakresu zmian z 2026 r. Dostępny był tekst pierwotny i informacja o wersji aktualnej. Konieczna końcowa kontrola tekstu skonsolidowanego przed sprzedażą.
- UODO — kryteria retencji: https://uodo.gov.pl/pl/676/4260
- UODO — tekst RODO: https://uodo.gov.pl/pl/file/1460

Brakujące dane i powyższe ograniczenia nie zostały zamaskowane fikcyjnymi informacjami w publicznych dokumentach.

## Aktualizacja danych spółki i wysyłki — 14.10.2026, po przekazaniu danych

- Na podstawie zrzutu użytkownika uzupełniono kapitał zakładowy 5 000,00 zł. Pozostałe numery i adres są zgodne z przekazanymi wcześniej danymi.
- Sąd: Sąd Rejonowy w Gliwicach, X Wydział Gospodarczy Krajowego Rejestru Sądowego. Dwie bazy wskazują zgodne dane: https://www.bizraport.pl/krs/0000787581/puchary-i-medale-spolka-z-ograniczona-odpowiedzialnoscia oraz https://analizafirm.pl/firma/0000787581/puchary-i-medale . Bezpośredni odczyt API Ministerstwa Sprawiedliwości nie był dostępny; nie przedstawiamy tej kontroli jako pobrania urzędowego odpisu KRS.
- Stopka na wszystkich stronach zawiera komplet podanych danych identyfikacyjnych, sąd, kapitał i zwięzły cennik dostaw z odnośnikiem do warunków. Nazwa marki pozostała bez zmian.
- Dostawy wyłącznie InPost: Paczkomat w Polsce 14,99 PLN, kurier w Polsce 17,99 PLN, przesyłka międzynarodowa 99,00 PLN. Cennik konsumencki przedstawiono jako brutto. Zaktualizowano regulamin, stronę dostaw i informację o odbiorcy danych w polityce prywatności.
- Nie dopisano krajów ani gwarantowanych terminów bez potwierdzenia. Dostępność zagranicznego doręczenia jest potwierdzana przed zawarciem umowy.
- Nadal brak aktywnego checkoutu i Stripe, zgodnie z ustalonym zakresem. Uzupełnienie stopki nie uruchamia sprzedaży ani integracji przewoźnika.
