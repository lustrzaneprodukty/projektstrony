import os
BASE=os.environ.get('SITE_URL','https://lustrzane-produkty.peppyluck4.chatgpt.site').rstrip('/')
docs={
'regulamin':('Regulamin sklepu',{'Sprzedawca':'Nazwa, forma prawna, NIP, rejestr, adres siedziby i kontakt.','Zamówienia':'Sposób składania zamówień, moment zawarcia umowy, akceptacja projektu, personalizacja, poprawianie błędów, potwierdzenie umowy.','Warunki sprzedaży':'Ceny brutto, podatki, płatności, dodatkowe koszty, realizacja i dostawa.','Prawa klienta':'Reklamacje, odstąpienie, wyjątki, wzór formularza i pozasądowe rozwiązywanie sporów.','Usługi elektroniczne':'Zakres usług, wymagania techniczne, zakaz treści bezprawnych, reklamacje usług i zasady zmian regulaminu.'}),
'prywatnosc':('Polityka prywatności',{'Administrator':'Pełna nazwa i adres, kontakt w sprawach danych oraz inspektor, jeśli dotyczy.','Cele i podstawy':'Cele, podstawy prawne, zakres danych, obowiązek podania i skutki odmowy.','Odbiorcy danych':'Hosting, poczta, księgowość, przewoźnicy i płatności; okresy przechowywania, transfery poza EOG i zabezpieczenia.','Prawa osób':'Dostęp, sprostowanie, usunięcie, ograniczenie, przenoszenie, sprzeciw, cofnięcie zgody, skarga do Prezesa UODO, profilowanie i automatyczne decyzje.'}),
'cookies':('Polityka cookies',{'Stan obecny':'Frontend nie instaluje własnych cookies analitycznych ani reklamowych. Hosting wymaga osobnej weryfikacji.','Wykaz technologii':'Dostawcy, nazwy, cele i czas działania cookies docelowego hostingu. Po dodaniu opcjonalnej analityki lub reklamy wymagane będzie zarządzanie zgodą przed ich uruchomieniem i możliwość wycofania zgody.'}),
'dostawa-i-platnosci':('Dostawa i płatności',{'Płatności':'Metody, operatorzy, waluta, terminy zapłaty.','Dostawa':'Przewoźnicy, obszar, koszty brutto, odbiór osobisty.','Terminy':'Czas projektu, akceptacji, produkcji i transportu.'}),
'zwroty-i-reklamacje':('Zwroty i reklamacje',{'Odstąpienie':'Zasady, terminy, adres zwrotów, koszt odesłania, zwrot płatności i wzór formularza.','Personalizacja':'Zakres wyjątków od odstąpienia dla towarów wykonanych według specyfikacji klienta lub dla jego zindywidualizowanych potrzeb. Personalizacja nie wyłącza odpowiedzialności za niezgodność towaru z umową.','Reklamacje':'Adres i e-mail, sposób zgłoszenia, procedura, terminy odpowiedzi, uprawnienia klienta.','Spory':'Właściwe podmioty ADR i zasady udziału przedsiębiorcy.'}),
'dane-sprzedawcy':('Dane sprzedawcy',{'Firma':'Pełna nazwa, forma prawna, NIP, CEIDG lub KRS i pozostałe wymagane dane rejestrowe.','Adres':'Siedziba, korespondencja, reklamacje i zwroty.','Kontakt':'Potwierdzenie kontaktu marki: grafiki.beauty@gmail.com, +48 883 242 299; godziny obsługi.'}),
'zasady-opinii':('Zasady publikowania opinii',{'Pochodzenie i weryfikacja':'Sposób pozyskiwania i weryfikacji czy autor kupił lub używał produktu, dobór opinii, moderacja, zgody na publikację i ewentualne wynagrodzenie.'})}
docs.pop('zasady-opinii', None)
obsolete=P/'zasady-opinii/index.html'
if obsolete.exists(): obsolete.unlink()
links=''.join(f'<a href="/{slug}/">{esc(title)}</a>' for slug,(title,_) in docs.items())
for slug,(title,sections) in docs.items():
 body='<section class="section container legal"><p class="eyebrow">INFORMACJE DLA KLIENTÓW</p><h1>'+title+'</h1><p class="legal-status">Dokument w przygotowaniu. Dane i pełna treść zostaną uzupełnione przed uruchomieniem sklepu internetowego.</p><nav aria-label="Dokumenty sklepu">'+links+'</nav>'+''.join('<h2>'+h+'</h2><p>'+t+' <strong>[DO UZUPEŁNIENIA]</strong></p>' for h,t in sections.items())+'</section>'
 d=P/slug;d.mkdir(exist_ok=True);(d/'index.html').write_text(shell(title+' — Lustrzane Produkty',title+' i informacje dla klientów.',body,'/'+slug+'/'))
for file in P.rglob('*.html'):
 s=file.read_text().replace('https://lustrzane-produkty.peppyluck4.chatgpt.site',BASE)
 s=s.replace('<div class="container footer-bottom">','<nav class="container footer-documents" aria-label="Informacje sklepu">'+links+'</nav><div class="container footer-bottom">')
 relative=file.relative_to(P).as_posix();path='/' if relative=='index.html' else '/'+relative.removesuffix('index.html')
 draft=path.strip('/') in docs or file.name=='404.html'
 title=re.search(r'<title>(.*?)</title>',s).group(1);desc=re.search(r'name="description" content="(.*?)"',s).group(1)
 product=next((x for x in products if path=='/produkty/'+x['slug']+'/'),None)
 img=BASE+(product['image'] if product else '/assets/campaign.webp')
 s=re.sub(r'<meta property="og:image"[^>]+>',f'<meta property="og:image" content="{img}">',s)
 meta=f'<meta name="robots" content="{"noindex, follow" if draft else "index, follow, max-image-preview:large"}"><meta property="og:url" content="{BASE+path}"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="Lustrzane Produkty"><meta property="og:image:alt" content="{esc(product["name"] if product else "Produkty lustrzane")}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{img}">'
 graph=[{'@type':'Organization','@id':BASE+'/#organization','name':'Lustrzane Produkty','url':BASE+'/'},{'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'Lustrzane Produkty','inLanguage':'pl-PL'}]
 if product:graph += [{'@type':'Product','name':product['name'],'description':product['description'],'image':[img],'url':BASE+path,'category':product['category']},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Strona główna','item':BASE+'/'},{'@type':'ListItem','position':2,'name':product['name'],'item':BASE+path}]}]
 if not draft:meta+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')+'</script>'
 file.write_text(s.replace('</head>',meta+'</head>'))
urls=['/']+['/produkty/'+p['slug']+'/' for p in products]
(P/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(BASE+u)+'</loc></url>' for u in urls)+'</urlset>')
(P/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
