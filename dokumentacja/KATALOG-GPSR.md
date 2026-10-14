# Katalog i informacje GPSR

Obecnych 15 produktów nie oznaczono jako rzeczywisty katalog sprzedażowy. Pola cenowe w źródle zachowano do wymiany katalogu; przykładowych kwot nie pokazuje się klientom. Wyszukiwarka otrzymuje tylko name, slug, category i image. Nie eksportuj całych rekordów magazynowych, danych dostawców, cen zakupu ani dokumentacji technicznej do `dist/`.

Dotychczasowe pola produktu pozostają bez zmian. Można dodać pola variants, images, model3d, seo, personalization i structuredData; ich integracja pozostaje osobnym zadaniem. Nie są automatycznie renderowane ani eksportowane. `published: true` dodaje produkt do sitemap po ustawieniu domeny; ustawiaj je dopiero po weryfikacji rzeczywistej oferty.

Renderer `product_safety()` obsługuje opcjonalny obiekt `safety`:

| Pole | Znaczenie |
|---|---|
| ownManufacture | Tylko wartość true przypisuje spółkę jako rzeczywistego producenta |
| manufacturer | Dla pozostałych: name, address, email |
| identifier | Potwierdzony typ lub inny identyfikator wyrobu |
| manufacturerOutsideEU | true wymaga responsiblePerson |
| responsiblePerson | name, address, email podmiotu odpowiedzialnego w UE |
| intendedUse | Przeznaczenie konkretnego wyrobu |
| instructions | Tablica instrukcji po polsku |
| warnings | Tablica ostrzeżeń wynikających z oceny ryzyka |

Brak obiektu safety nie przypisuje fikcyjnego producenta; wyświetla odnośnik do ogólnej informacji. Niepełne wymagane dane w dodanym obiekcie przerywają generowanie. Sam odnośnik nie wystarcza do uruchomienia rzeczywistej oferty objętej art. 19 GPSR. Przed sprzedażą każdy produkt musi mieć zweryfikowaną identyfikację, zdjęcie, producenta, wymagane kontakty oraz właściwe informacje bezpieczeństwa. Zdjęcie już jest w szablonie produktu.

Nie dodano danych Product, Offer ani ocen dla demonstracyjnego katalogu. Model danych nie zastępuje oceny ryzyka, dokumentacji technicznej, oznakowania, instrukcji i obsługi zgłoszeń. Dostawcy surowców mogą pozostać w dokumentacji wewnętrznej; wymaganych danych producenta lub podmiotu odpowiedzialnego nie wolno ukrywać.
