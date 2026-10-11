import os
from legal_content import DOCS
BASE=os.environ.get('SITE_URL','https://lustrzane-produkty.peppyluck4.chatgpt.site').rstrip('/')
docs=DOCS
links=''.join(f'<a href="/{slug}/">{esc(data["title"])}</a>' for slug,data in docs.items())
status='<aside class="legal-status"><strong>Wersja do uruchomienia sklepu.</strong> Dokumenty zawierają przygotowane zasady docelowej sprzedaży. Pola oznaczone „UZUPEŁNIJ” wymagają danych Sprzedawcy lub potwierdzenia warunków operacyjnych. Koszyk i płatności nie są jeszcze uruchomione.</aside>'
for slug,data in docs.items():
 title=data['title']
 toc='<nav class="legal-toc" aria-label="Spis treści">'+''.join(f'<a href="#punkt-{i}">{esc(h)}</a>' for i,(h,t) in enumerate(data['sections'],1))+'</nav>'
 content=''.join(f'<section id="punkt-{i}" class="legal-section"><h2>{esc(h)}</h2>{t}</section>' for i,(h,t) in enumerate(data['sections'],1))
 body='<article class="section container legal legal-document"><p class="eyebrow">PRZEJRZYSTE ZASADY</p><h1>'+esc(title)+'</h1><p class="legal-lead">'+esc(data['intro'])+'</p>'+status+'<p class="legal-version">Opracowanie: 11.10.2026 · wersja redakcyjna 1.0</p>'+toc+content+'<nav class="legal-related" aria-label="Dokumenty sklepu">'+links+'</nav></article>'
 d=P/slug;d.mkdir(exist_ok=True);(d/'index.html').write_text(shell(title+', Lustrzane Produkty',data['intro'],body,'/'+slug+'/'))
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

# Zbiorcza, samodzielna wersja do przeglądania i wydruku; poza katalogiem hostingu.
print_style='''body{max-width:940px;margin:50px auto;padding:0 24px;color:#24231f;font:16px/1.75 system-ui,sans-serif}h1{font-size:38px;line-height:1.15}h2{font-size:30px;line-height:1.25;margin-top:55px}h3{font-size:21px;line-height:1.4;margin-top:32px}a{color:#72541e}li{margin-bottom:9px}.legal-status{padding:20px;background:#faf4e5;border:1px solid #d6c498}.legal-table-wrap{overflow-x:auto}table{border-collapse:collapse;font-size:13px;width:100%;min-width:550px}td,th{padding:12px;border:1px solid #ccc;vertical-align:top;text-align:left}th{background:#f5f1e8}.legal-form{border:1px solid #ccc;padding:20px}.document{border-top:1px solid #c8b994;margin-top:50px}@media print{body{margin:0;max-width:none;font-size:10pt}h1{font-size:25pt}h2{font-size:21pt}h3{font-size:14pt;break-after:avoid}.document{break-before:page;border:0}.legal-table-wrap{overflow:visible}table{min-width:0;font-size:9pt}tr{break-inside:avoid}a{color:#000}}'''
all_docs=''
for slug,data in DOCS.items():
 content=''.join('<h3>'+esc(h)+'</h3>'+t for h,t in data['sections'])
 content=re.sub(r'id="([^"]+)"',lambda m:'id="'+slug+'-'+m.group(1)+'"',content)
 all_docs+='<article class="document" id="'+slug+'"><h2>'+esc(data['title'])+'</h2><p>'+esc(data['intro'])+'</p>'+content+'</article>'
# Wersja zbiorcza używa lokalnych odnośników, a nie nieistniejących ścieżek serwera.
all_docs=re.sub(r'href="/([^/]+)/#([^"]+)"',lambda m:'href="#'+m.group(1)+'-'+m.group(2)+'"',all_docs)
all_docs=re.sub(r'href="/([^/]+)/"',lambda m:'href="#'+m.group(1)+'"',all_docs)
Path('dokumentacja').mkdir(exist_ok=True)
Path('dokumentacja/Dokumenty-sklepu.html').write_text('<!doctype html><html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dokumenty sklepu, Lustrzane Produkty</title><style>'+print_style+'</style><body><h1>Lustrzane Produkty<br>Dokumenty sklepu</h1><p>Wersja redakcyjna 1.0 · 11.10.2026</p>'+status+'<p>Przygotowano dla sprzedaży produktów fizycznych, w tym personalizowanych. Przed uruchomieniem wymagane są uzupełnienie danych, dopasowanie do rzeczywistych procesów oraz końcowy przegląd prawny. Instrukcja i źródła: PRZED-URUCHOMIENIEM.md.</p><nav><ol>'+''.join('<li><a href="#'+slug+'">'+esc(data['title'])+'</a></li>' for slug,data in DOCS.items())+'</ol></nav>'+all_docs+'</body></html>')
