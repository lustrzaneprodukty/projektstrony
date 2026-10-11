# Dokumenty i wdrożenie sklepu — 11.10.2026

Przygotowano rozbudowaną wersję redakcyjną dla sklepu sprzedającego fizyczne produkty lustrzane, również personalizowane. Nie jest to potwierdzenie pełnej zgodności uruchomionego sklepu ani indywidualna opinia prawna. Ostateczna ocena zależy od danych przedsiębiorcy, modelu sprzedaży, produktów, umów z dostawcami i działającej technologii. Przed startem zalecana jest kontrola prawna gotowej konfiguracji, zwłaszcza powierzenia danych, wyjątków od odstąpienia i zmian ustawowych z 2026 r.

## Co jest gotowe

12 podstron z rozbudowanymi zasadami: regulamin, dostawa i płatności, zwroty i reklamacje, prywatność, skrót RODO, cookies, personalizacja i pliki, zasady opinii, bezpieczeństwo produktów, dostępność, dane sprzedawcy, oraz formularze. Podstrony są połączone w stopce i mają spisy treści. Jest zbiorczy plik HTML do przeglądania i wydruku. Źródłem wszystkich treści jest `legal_content.py`.

To projekt docelowych warunków, a nie oświadczenie, że koszyk, płatności, panel zgód albo elektroniczne odstąpienie już działają. W obecnej wersji pozostaje formularz mailto. Dokumenty mają oznaczenie wersji roboczej i noindex do chwili uzupełnienia. Nie publikuj pustych danych jako regulaminu czynnego sklepu.

## Dane wymagane od właściciela

| Zakres | Co ustalić |
|---|---|
| Sprzedawca | Pełna firma, forma prawna, adres, NIP, CEIDG / KRS, sąd i kapitał, jeśli dotyczy; domena; data wejścia w życie |
| Kontakt | Adres korespondencyjny, zwrotów i reklamacji, telefon, e-mail, godziny obsługi; potwierdzić użycie adresu Gmail |
| Płatność | Metody, operator i pełna firma, numer konta, termin; nie wpisywać BLIK / kart, dopóki nie ma integracji |
| Dostawa | Kraje, przewoźnicy, usługi, ceny brutto, progi, gabaryty, odbiór osobisty i koszt zwrotu gabarytów |
| Produkcja | Termin pierwszego projektu, produkcji i transportu; zakres poprawek; wymagania plików |
| Dane | Dostawcy i umowy powierzenia, role, państwa transferów, zabezpieczenia; logi, pliki produkcyjne i backup — rzeczywiste okresy |
| RODO | Czy jest IOD; brak automatycznego obowiązku jego powołania tylko z powodu prowadzenia sklepu |
| Opinie | Dowody pochodzenia, weryfikacji, zgód na publikację; korzyści dla autorów i zasady wyboru |
| GPSR | Producent, odpowiedzialny podmiot UE, identyfikatory, ocena ryzyka, instrukcje i etykiety dla każdego produktu |
| Dostępność | Status mikroprzedsiębiorcy, zakres PAD, wynik audytu i opis faktycznej zgodności |

Nie da się prawdziwie uzupełnić tych danych samą analizą internetu. Oznaczenia `[UZUPEŁNIJ: ...]` wskazują konkretny brak; nie są zastępstwem wykonania obowiązku. Przeszukaj je w `legal_content.py` i uzupełnij, a następnie uruchom `python build.py`.

## Proponowane zasady operacyjne do przyjęcia

Przyjęto model bez obowiązkowego konta, płatność z góry w ciągu 7 dni, odpowiedź na ofertę klienta w ciągu 2 dni roboczych, zawarcie umowy przez wyraźny e-mail akceptacji, brak milczącego zatwierdzania projektu, brak automatycznego przepadku zaliczki, koszt zwykłego zwrotu po stronie kupującego oraz koszty reklamacji po stronie sprzedawcy. To proponowane zobowiązania sklepu, a nie uniwersalne ustawowe terminy. Jeśli wybierzesz inny model, trzeba spójnie zmienić dokumenty i działanie sklepu.

Wyjątek dla personalizacji trzeba przypisać do konkretnego produktu i procesu. Nie wyłączać zwrotu wyłącznie dlatego, że rzecz wyprodukowano dopiero po zamówieniu lub wybrano standardowy rozmiar. Nie przenosić wyjątku na reklamację. Nie oferowano tu osobnej sprzedaży plików, abonamentu, konta ani newslettera — ich późniejsze dodanie wymaga odpowiednich warunków, a nie automatycznego zastosowania wyjątku dla towaru fizycznego.

## Warunki uruchomienia procesu zakupowego

1. Każda oferta: prawdziwa cena brutto, materiał, wymiary, ilość, zawartość, personalizacja, termin, informacje bezpieczeństwa i producent. Usunąć „ceny przykładowe” dopiero po zastąpieniu cen rzeczywistymi. Sprawdzić prawdziwość oznaczeń BESTSELLER i zapewnień o podglądzie 3D.
2. Koszyk: dostawa i koszt całkowity przed zakupem; korekta danych; oddzielne, niezaznaczone zgody; regulamin możliwy do zapisania; informacja o odstąpieniu / wyjątku przy danym towarze. Przycisk „Zamówienie z obowiązkiem zapłaty”.
3. E-mail: potwierdzenie umowy z niezmienną kopią regulaminu i pouczenia, ceną i specyfikacją. Sam link do zmiennej strony to za mało. Rozróżnić potwierdzenie wpływu od przyjęcia oferty. Zapisać wersję zaakceptowanego projektu.
4. Zwroty i reklamacje: rzeczywiście obsługiwany e-mail i adres, terminy, dowód doręczenia odpowiedzi, organizacja bezpłatnego odbioru reklamowanego towaru. Nie żądać zdjęć ani paragonu jako warunku.
5. Funkcja odstąpienia online: zaplanować dostępny przycisk, identyfikację umowy bez przymusowego zakładania konta, podsumowanie i „Potwierdź odstąpienie od umowy”, skuteczną wysyłkę oraz niezwłoczne potwierdzenie na trwałym nośniku z treścią, datą i godziną. Plik formularza i mailto nie są taką funkcją. Zakres dotyczy umów, dla których prawo istnieje. Nie blokować reklamacji produktu personalizowanego.
6. Cookies: audyt rzeczywistej domeny i wszystkich integracji; test przed zgodą, po odmowie, po selekcji i po cofnięciu. Bez opcjonalnego śledzenia nie dodawać pozornego banera. Gdy jest śledzenie — panel musi blokować narzędzia przed zgodą, a nie tylko zasłaniać stronę.
7. Dostępność: sprawdzić klawiaturę, fokus, etykiety, kontrast, powiększenie, czytnik ekranu, błędy formularzy, płatność i alternatywę dla wizualnego konfiguratora. Jeśli PAD obowiązuje, uzupełnić obowiązkową informację o spełnieniu wymagań i obsługę skarg.
8. Promocje: historia cen i najniższa cena z 30 dni, wyliczenia rabatów, prawdziwe komunikaty o dostępności; nie tworzyć fikcyjnego pośpiechu. Ustawowych praw nie reklamować jako wyjątkowej korzyści sklepu.
9. Opinie: powiązanie z rzeczywistym zamówieniem, jeśli deklarowana jest weryfikacja; opis selekcji, ujawnienie zachęt, anonimizacja i podstawa publikacji. Przed publicznym wdrożeniem usunąć lub wyjaśnić materiały, których pochodzenia nie można udokumentować.
10. Dokumenty: usunąć baner roboczy, zatwierdzić datę i wersję; zdjąć noindex podstron prawnych tylko po uzupełnieniu; ustawić SITE_URL dla prawdziwej domeny. Zachować poprzednie wersje dla starych zamówień.

## Zmiany prawne z 2026 r. — punkty do kontroli przed startem

Weryfikacja źródeł: 11.10.2026. Odczytano oficjalny tekst jednolity ustawy o prawach konsumenta Dz.U. 2026 poz. 1244, stan na 2.09.2026. Zawiera m.in. art. 7aa ust. 2 o dobrowolnym oświadczeniu przedsiębiorcy co do zawodowego charakteru umowy. Nie utożsamiać daty publikacji tekstu jednolitego z uchwaleniem zupełnie nowej ustawy.

Dyrektywa (UE) 2023/2673 przewiduje funkcję odstąpienia przez interfejs i termin stosowania środków krajowych od 19.06.2026. Oficjalna karta UC82 opisuje ją jako element projektu; w tej analizie nie potwierdzono ogłoszenia ostatecznej polskiej implementacji funkcji. Nie twierdzimy więc, że sam termin dyrektywy dowodzi obowiązywania konkretnej polskiej sankcji. Dla przyszłego sklepu należy funkcję zaprojektować i sprawdzić aktualny stan wdrożenia w dniu uruchomienia, szczególnie przy sprzedaży do innych krajów.

Dyrektywa (UE) 2024/825 i rozporządzenie wykonawcze (UE) 2025/1960: Komisja wskazuje stosowanie rozwiązań od 27.09.2026. Dotyczą m.in. komunikowania ustawowej odpowiedzialności za zgodność, oznaczenia dodatkowej gwarancji trwałości i twierdzeń środowiskowych. Przed startem pobrać oficjalną polską wersję ujednoliconego komunikatu i zastosować zgodnie z właściwymi przepisami oraz sprawdzić polską implementację UC111. Nie tworzyć własnego znaku GARAN i nie sugerować dodatkowej gwarancji producenta, której nie udzielono. Ten pakiet nie wdraża oficjalnej grafiki ani nie potwierdza zakończenia krajowej implementacji. Nie używać haseł „ekologiczny”, „zero wpływu”, „neutralny klimatycznie” czy certyfikatów bez podstaw.

Platforma ODR została zamknięta 20.07.2025. Nie dodawać starego obowiązkowego linku do niej. Nadal potrzebna jest prawidłowa informacja o ADR i odpowiedź na trwałym nośniku po nierozwiązanej reklamacji.

## RODO — wdrożenie wewnętrzne

Dokument na stronie nie zastępuje inwentaryzacji danych, analizy podstaw, rejestru czynności tam, gdzie wymagany (regularne przetwarzanie nie staje się „sporadyczne” tylko z powodu małej firmy), upoważnień, umów powierzenia, kontroli dostępu, aktualizacji, MFA i kopii zapasowych. Ustalić procedurę praw osób oraz naruszeń, z oceną obowiązku zgłoszenia do UODO w ciągu 72 godzin od stwierdzenia i zawiadomienia osób przy wysokim ryzyku. Prowadzić rejestr naruszeń także gdy nie wymagają zgłoszenia. Ocenić, czy potrzebne są IOD lub DPIA — nie deklarować obowiązku ani zwolnienia bez analizy.

Dane kursantów do certyfikatów mogą być powierzeniem, a nie zwykłym zakupem z danymi zamawiającego. Przed ich otrzymaniem ustalić role i podpisać art. 28 RODO, obejmując przedmiot i czas, charakter i cel, rodzaje danych i kategorie osób; udokumentowane polecenia; poufność; bezpieczeństwo; dalszych procesorów i uprawnienie do sprzeciwu; pomoc w prawach i art. 32–36; incydenty; usunięcie / zwrot i kopie; informacje i audyty; powiadomienie o poleceniu naruszającym prawo. Nie używać pustego wzoru bez wpisania faktycznych podwykonawców i środków bezpieczeństwa. Administrator musi ocenić obowiązek informacyjny wobec osób na certyfikatach.

## Produkty, podatki i opakowania

GPSR wymaga nie tylko strony: identyfikowalność produktu i partii, analiza ryzyka, dokumentacja techniczna producenta (co do zasady 10 lat), oznakowanie, instrukcje, rejestr zgłoszeń i procedura zdarzeń/odzyskania. Potwierdzić rolę producenta dla wyrobu wprowadzanego pod własną marką. Nie zastępować oceny ryzyka ogólnym ostrzeżeniem „nie dla dzieci”. Ocenić materiały, powłoki, krawędzie i mocowania. Dla produktów podlegających odrębnym regulacjom zbadać je osobno; nie nanosić CE bez właściwej podstawy.

Z księgowością ustalić status VAT, kasę fiskalną i ewentualne zwolnienia, fakturowanie / KSeF według aktualnego harmonogramu i statusu nabywcy. Zweryfikować BDO i obowiązki wprowadzającego produkty w opakowaniach, ewidencję i sprawozdawczość. Przy sprzedaży zagranicznej ocenić VAT/OSS, lokalne obowiązki opakowaniowe, język i ochronę konsumenta. To obowiązki zależne od modelu działalności, których nie załatwia tekst regulaminu.

## Źródła oficjalne

- Ustawa o prawach konsumenta, tekst jednolity 2026: https://eli.gov.pl/eli/DU/2026/1244/ogl (szczególnie art. 7a, 7aa, 12–21, 27–38, 43a–43g).
- UOKiK — reklamacje: https://prawakonsumenta.uokik.gov.pl/reklamacja/niezgodnosc/
- UOKiK — wyjątki od odstąpienia: https://prawakonsumenta.uokik.gov.pl/prawo-odstapienia-od-umowy/wylaczenia-prawa-do-odstapienia/
- RODO — tekst udostępniony przez UODO: https://www.uodo.gov.pl/pl/404/539 (art. 5–6, 12–22, 24–36, 44–49).
- Prawo komunikacji elektronicznej: https://eli.gov.pl/eli/DU/2024/1221/ogl/pol (art. 398–399; stosować z późniejszymi zmianami).
- Polski Akt o Dostępności: https://eli.gov.pl/eli/DU/2024/731/ogl oraz wyjaśnienia: https://www.gov.pl/web/dostepnosc-cyfrowa/polski-akt-o-dostepnosci--uslugi-handlu-elektronicznego
- UOKiK — GPSR pytania i odpowiedzi: https://www.uokik.gov.pl/public/bezpieczenstwo-produktow-pytania-i-odpowiedzi
- ADR: https://polubowne.uokik.gov.pl/
- KPRM — projekt po likwidacji ODR: https://www.gov.pl/web/premier/projekt-ustawy-o-zmianie-ustawy-o-pozasadowym-rozwiazywaniu-sporow-konsumenckich-oraz-niektorych-innych-ustaw2
- UC82: https://www.gov.pl/web/premier/projekt-ustawy-o-kredycie-konsumenckim-oraz-o-zmianie-ustawy-o-prawach-konsumenta
- Dyrektywa 2023/2673: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=oj%3AL_202302673
- Komisja Europejska — komunikat i gwarancja trwałości: https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/sustainable-consumption_en
- Rozporządzenie 2025/1960: https://eur-lex.europa.eu/eli/reg_impl/2025/1960/oj
- UC111: https://www.gov.pl/web/premier/projekt-ustawy-o-zmianie-ustawy-o-przeciwdzialaniu-nieuczciwym-praktykom-rynkowym-oraz-ustawy-o-prawach-konsumenta

Źródła urzędowe były podstawą redakcji; nie kopiowano regulaminu innego sklepu. Nie udało się potwierdzić wszystkich etapów implementacji zmian 2026 r.; wskazano je osobno zamiast przedstawiać projekt jako ustawę. Ostateczny przegląd powinien odnosić się do daty faktycznego startu.
