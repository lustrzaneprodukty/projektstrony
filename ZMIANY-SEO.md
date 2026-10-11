# Aktualizacja strony

Zmieniono hasła w sekcji własnego produktu, wyrównano etykiety, usunięto strzałki z kart, zmniejszono poświatę i dodano złoty gradient w sekcji o marce. Galerie produktów mają jednolite pole 4:5, białe tło i zaokrąglone rogi; zdjęcia są pokazywane w całości. Usunięto sekcje formularza i „Stworzony dla Twojej marki” z podstron produktów. Przycisk zapytania otwiera e-mail z produktem, wykończeniem i liczbą sztuk.

## SEO
Każda karta ma tytuł, opis, canonical, Open Graph, Twitter Card, dane Product i BreadcrumbList. Dodano Organization, WebSite oraz sitemap.xml i robots.txt. Ceny przykładowe nie są publikowane w danych strukturalnych jako oferty. Nie dodano fikcyjnych ocen ani informacji o firmie.

Adres bazowy zachowano z istniejącego projektu. Przy zmianie domeny przebuduj z SITE_URL ustawionym na pełny docelowy adres, np. w macOS/Linux:

    SITE_URL=https://twoja-domena.pl python3 build.py

Na Windows PowerShell:

    $env:SITE_URL="https://twoja-domena.pl"
    python build.py

Po wdrożeniu zgłoś sitemap.xml w Google Search Console. Samo przygotowanie SEO nie oznacza gwarancji indeksacji ani pozycji.

## Dokumenty do uzupełnienia
Regulamin, polityka prywatności, cookies, dostawa i płatności, zwroty i reklamacje, dane sprzedawcy. Treści edytuje się w seo_legal.py, następnie uruchamia build.py. Są to szablony z polami DO UZUPEŁNIENIA, nie gotowe dokumenty prawne. Mają noindex i są pominięte w sitemapie do czasu uzupełnienia. Po uzupełnieniu należy zmienić warunek draft w seo_legal.py.

Przed uruchomieniem sprzedaży należy uzupełnić rzeczywiste ceny brutto, dane firmy, zasady obsługi, pełne dokumenty oraz informacje o producentach i bezpieczeństwie produktów odpowiednie dla asortymentu. Trzeba także zweryfikować zastosowanie wymogów dostępności, mechanizmów zakupowych i cookies na docelowym hostingu. Obecnie koszyk i płatności nie działają; strona pozostaje katalogiem z zapytaniami.

Podstawa zakresu informacji:
https://prawakonsumenta.uokik.gov.pl/prawo-do-informacji/sprzedaz-poza-lokalem-i-na-odleglosc/
https://uokik.gov.pl/public/omnibus-i-obowiazki-informacyjne-w-e-commerce-kolejne-dzialania-i-zarzuty-prezesa-uokik
https://uokik.gov.pl/public/bezpieczenstwo-produktow-obowiazki-przedsiebiorcow

## Kontrola
Sprawdzono budowanie, składnię JavaScript, dane JSON-LD i lokalne ścieżki zasobów. Podgląd w przeglądarce nie został zweryfikowany w tym środowisku z powodu niedostępności Chromium.

Do hostingu wgrywa się zawartość dist. Pełna paczka zawiera również źródła do kolejnych edycji.

## Dodatkowe poprawki
Złoty gradient w nagłówkach „w praktyce”, „do zachwytu” i „Zaprojektuj je za darmo”. Podpis „PEŁNA PERSONALIZACJA”. Zmniejszono odstęp między opiniami i FAQ. Usunięto stronę zasad publikowania opinii i jej odnośniki. Pasek dokumentów wyśrodkowano.
