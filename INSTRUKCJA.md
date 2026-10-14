# Lustrzane Produkty — frontend, 14.10.2026

Pełny projekt obejmuje źródła, zasoby i wygenerowany katalog `dist/` (29 stron HTML). Szczegóły zmian, testów i ograniczeń: `dokumentacja/RAPORT-FINALIZACJI.md`.

## Podgląd i edycja

W katalogu projektu uruchom `python -m http.server 8080 --directory dist` i otwórz http://localhost:8080. Nie otwieraj HTML przez dwuklik. W macOS/Linux polecenie może nazywać się `python3`.

- `build.py`: sekcje, FAQ, szablony stron i stopka.
- `legal_content.py`: treści prawne i informacyjne.
- `seo_legal.py`: metadane, dane strukturalne, mapa strony i zbiorcze dokumenty.
- `product_content.py`: renderowanie danych GPSR.
- `products.json`: wymienny katalog demonstracyjny.
- `dist/style.css`, `dist/app.js`, `dist/assets/`: style, interakcje i media; generator ich nie odtwarza z osobnego katalogu źródłowego. Zachowaj cały projekt.

Po zmianach uruchom `python build.py`, następnie `python verify.py`. Generator nadpisuje HTML oraz aktualizuje `dist/data.js`. Python nie potrzebuje dodatkowych bibliotek. Nie publikuj katalogu źródłowego ani dokumentacji technicznej; hosting otrzymuje wyłącznie zawartość `dist/`.

## Domena

Domyślnie nie ma canonical, og:url ani sitemap z niepotwierdzonym adresem. Aby je wygenerować, ustaw zmienną środowiskową `SITE_URL` na potwierdzony adres HTTPS domeny, bez końcowej ścieżki, i uruchom generator. Nie wpisuj adresu testowego do źródeł.

Sitemap obejmuje stronę główną, stałe podstrony oraz tylko produkty z `published: true`. Bez domeny `robots.txt` dopuszcza indeksowanie, bez wpisu Sitemap. Tylko strona błędu 404 ma noindex. Hosting musi sam zwracać kod HTTP 404 dla nieistniejących tras.

## Zakres funkcji

Katalog, wyszukiwarka, galeria, dialogi informacyjne i linki e-mail działają bez backendu. Kod formularza przygotowuje wiadomość lokalnie; nie wysyła jej sam. Aktualne szablony nie wyświetlają formularza zapytania — główną drogą kontaktu jest e-mail. Nie ma aktywnych kont, checkoutu, Stripe, konfiguratora 3D ani przesyłania plików do serwera.

Przed rozpoczęciem sprzedaży należy zamknąć kwestie wskazane w raporcie. Dokumenty opisują znany zakres działania; nie stanowią potwierdzenia audytu procesów spółki ani infrastruktury produkcyjnej.
