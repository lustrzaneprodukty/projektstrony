# Stripe i checkout — dokumentacja wdrożeniowa, poza stroną publiczną

Stripe jest planowany, ale nie został uruchomiony. Publiczne dokumenty prawidłowo informują, że strona nie pobiera płatności i nie przekazuje danych operatorowi płatności. Nie publikujemy danych rachunku, metod płatności ani logotypów. Nie dodano kodu Stripe, SDK, kluczy ani żądań sieciowych do operatora.

## Podstawa regulaminowa po uruchomieniu

Po potwierdzeniu podmiotu obsługującego konto i konfiguracji można włączyć do regulaminu następującą zasadę:

„Płatności elektroniczne obsługiwane są za pośrednictwem Stripe. Dostępne dla danego zamówienia sposoby zapłaty są wskazane przed jego złożeniem. Przed zatwierdzeniem płatności Klient widzi kwotę i walutę transakcji. Odrzucenie lub przerwanie płatności nie stanowi potwierdzenia jej wykonania. Reklamacje dotyczące zakupu można kierować do Sprzedawcy; procedura operatora nie ogranicza ustawowych praw Klienta wobec Sprzedawcy. Zwroty płatności następują zgodnie z zasadami odstąpienia i reklamacji, co do zasady tą samą metodą, chyba że Klient wyraźnie zgodzi się na inną, bez kosztów.”

Tego tekstu nie włączono do publicznego regulaminu, ponieważ sugerowałby aktywną usługę. Przed publikacją dopisać potwierdzoną pełną nazwę właściwego podmiotu Stripe i rzeczywisty termin płatności. Nie zakładać dostępności kart, BLIK ani portfeli.

## Polityka prywatności po integracji

Opisać faktyczne kategorie przekazywanych danych (np. identyfikator zamówienia, kwota, waluta, dane kontaktowe — wyłącznie po sprawdzeniu integracji), cel realizacji płatności, właściwe podstawy, rolę prawną operatora, okresy lub kryteria przechowywania, transfery i zabezpieczenia oraz odnośnik do właściwej informacji Stripe. Nie wpisywać, że sklep nie ma dostępu do danych karty, dopóki wybrana architektura tego nie potwierdzi.

## Warunki uruchomienia

- Uzgodnić moment zawarcia umowy, moment pobrania środków i obsługę braku płatności. Zaktualizować publiczne zasady zamówienia, dziś oparte na zapytaniu e-mail.
- Przed zamówieniem pokazać pełną cenę, cechy i personalizację, dostawę, termin oraz prawo odstąpienia albo rzeczywisty ustawowy wyjątek.
- Przycisk końcowy: „Zamówienie z obowiązkiem zapłaty”. Akceptacja regulaminu odrębna od dobrowolnych zgód.
- Potwierdzenie umowy i właściwą wersję dokumentów dostarczyć na trwałym nośniku. Sprawdzić aktualny obowiązek elektronicznej funkcji odstąpienia dla wdrażanej ścieżki.
- Zweryfikować podpis webhooka i idempotencję, źródło cen po stronie serwera, stany płatności, ponowienia, odrzucenie, zwroty i brak podwójnego zamówienia. Sam powrót z płatności nie potwierdza zapłaty.
- Przeprowadzić testy Stripe w trybie testowym, dopiero potem wdrożenie produkcyjne w odrębnym etapie.
- Sprawdzić rzeczywiste cookies i połączenia sieciowe. Jeśli pojawią się opcjonalne technologie, wdrożyć zgodę z blokadą przed zgodą, odmową i równie łatwym wycofaniem.
