# LUSTRZANE PRODUKTY — pliki strony

Aktualna wersja z 11 października 2026, zawierająca ostatnie poprawki: nowe złoto, niższy panel odbicia, okrągły emblemat ATELIER BEAUTY, refleksy, białe opinie, zmieniony FAQ i kontakt w stopce.

## Zawartość
- `dist/` — kompletna strona gotowa na hosting: HTML, CSS, JavaScript, zdjęcia WebP i lokalne fonty. Obejmuje stronę główną, 15 stron produktów, prywatność i stronę 404.
- `build.py` — źródłowe szablony HTML i generator stron (Python 3, bez dodatkowych bibliotek).
- `products.json` — katalog produktów.
- `FONT-LICENSE.txt` — licencja fontów.
- `URUCHOM-WINDOWS.bat` / `uruchom-mac-linux.sh` — lokalny podgląd.

## Jak obejrzeć stronę na komputerze
1. Rozpakuj całe archiwum.
2. Zainstaluj Python 3, jeśli nie jest dostępny.
3. Otwórz terminal w folderze z tą instrukcją i wykonaj:

   python -m http.server 8080 --directory dist

   Na macOS/Linux użyj `python3`, jeśli komenda `python` nie działa.
4. Wejdź w przeglądarce na http://localhost:8080
5. Serwer zatrzymasz skrótem Ctrl+C.

Możesz też użyć dołączonego skryptu dla swojego systemu. Nie uruchamiaj strony przez dwuklik pliku HTML — ścieżki zasobów zaczynają się od `/` i wymagają serwera HTTP.

## Jak wgrać stronę na hosting
Wgraj ZAWARTOŚĆ folderu `dist` do głównego katalogu domeny (np. public_html). `index.html` ma znaleźć się bezpośrednio w katalogu głównym, nie w podfolderze dist. Hosting powinien obsługiwać index.html w podkatalogach. Plik `404.html` można ustawić jako stronę błędu 404 w panelu hostingu.

Nie jest potrzebny Node.js, npm, baza danych ani backend. Pliki nie zawierają kont, kluczy dostępu ani konfiguracji prywatnego hostingu.

Przed publikacją pod własną domeną zamień adres `https://lustrzane-produkty.peppyluck4.chatgpt.site` na docelowy adres w `build.py`, a następnie uruchom `python build.py`. Zaktualizuje to adresy canonical, Open Graph, robots.txt i sitemap.xml. Wgranie plików na publiczny hosting udostępni je publicznie — archiwum nie zawiera mechanizmu logowania obecnego podglądu prywatnego.

## Edycja
- Wygląd i animacje: `dist/style.css`.
- Interakcje i formularze: `dist/app.js`.
- Treści sekcji i FAQ: `build.py`, potem `python build.py`.
- Katalog, przykładowe ceny (`price`) i etykiety (`badge`): `products.json`, potem `python build.py`. Generator synchronizuje też wyszukiwarkę w nagłówku.
- Zdjęcia i fonty: `dist/assets/`.

Nie edytuj wygenerowanego HTML, jeśli zamierzasz później uruchamiać generator — nadpisze ręczne zmiany w HTML.

## Zakres działania
Formularz przygotowuje wiadomość do wysłania przez aplikację pocztową użytkownika, nie wysyła wiadomości serwerowo. Koszyk, płatności, konta, kreatory i podgląd personalizacji 3D nie są wdrożone. Obracające się emblematy to prezentacyjne efekty CSS reagujące na kursor. Treść FAQ została wstawiona zgodnie z dostarczonym tekstem właściciela; opis podglądu w FAQ dotyczy planowanej funkcji.

Pliki są gotowe do dalszego rozwijania. Kontrole odnośników i kodu wykonano; wizualne testy we wszystkich docelowych przeglądarkach pozostają do wykonania. Przed rozpoczęciem sprzedaży uzupełnij dane administratora i dokumenty sklepu.

## Ostatnia poprawka efektów
Refleks na obu emblematach działa automatycznie co 6,5 sekundy. Wydzielone maski ograniczają światło do obrysu powierzchni, w tym okrągłego emblematu ATELIER BEAUTY. Ustawienie ograniczonych animacji wyłącza ruch.

## Aktualizacja wyglądu
Usunięto kategorie, wyszukiwanie i sortowanie w sekcji kolekcji, napis nad nagłówkiem oraz formularz po FAQ. Kontakt prowadzi do stopki; formularze konkretnych produktów pozostają dostępne. Białe kapsułki, mniejsze nazwy i ceny są wspólne dla wszystkich kart. Ceny są wyłącznie przykładowe i wymagają zastąpienia prawdziwym cennikiem. Etykiety BESTSELLER również można edytować w products.json.

Opinie przesuwają się powoli; zatrzymują się po najechaniu, ustawieniu fokusu, otwarciu zdjęcia lub użyciu przycisku pauzy. Ograniczenie animacji w systemie wyłącza przewijanie.
