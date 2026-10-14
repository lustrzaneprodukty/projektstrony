"""Wywoływany przez build.py. SITE_URL ustaw dopiero po potwierdzeniu domeny."""
import os
from urllib.parse import urlsplit
from legal_content import DOCS
BASE=os.environ.get('SITE_URL','').strip().rstrip('/')
if BASE:
    parsed=urlsplit(BASE)
    if parsed.scheme!='https' or not parsed.hostname or parsed.path or parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError('SITE_URL musi być adresem HTTPS domeny bez ścieżki, danych logowania, zapytania i fragmentu')
links=''.join(f'<a href="/{slug}/">{esc(data["title"])}</a>' for slug,data in DOCS.items())
for slug,data in DOCS.items():
    title=data['title']
    toc='<nav class="legal-toc" aria-label="Spis treści">'+''.join(f'<a href="#punkt-{i}">{esc(h)}</a>' for i,(h,t) in enumerate(data['sections'],1))+'</nav>'
    content=''.join(f'<section id="punkt-{i}" class="legal-section"><h2>{esc(h)}</h2>{t}</section>' for i,(h,t) in enumerate(data['sections'],1))
    body='<article class="section container legal legal-document"><p class="eyebrow">PRZEJRZYSTE ZASADY</p><h1>'+esc(title)+'</h1><p class="legal-lead">'+esc(data['intro'])+'</p><p class="legal-version">Wersja dokumentu: 14.10.2026</p>'+toc+content+'<nav class="legal-related" aria-label="Dokumenty sklepu">'+links+'</nav></article>'
    d=P/slug;d.mkdir(exist_ok=True);(d/'index.html').write_text(shell(title+' — Lustrzane Produkty',data['intro'],body,'/'+slug+'/'))
for file in P.rglob('*.html'):
    s=file.read_text()
    s=s.replace('<div class="container footer-bottom">','<nav class="container footer-documents" aria-label="Informacje sklepu">'+links+'</nav><div class="container footer-bottom">')
    relative=file.relative_to(P).as_posix();path='/' if relative=='index.html' else '/'+relative.removesuffix('index.html')
    missing=file.name=='404.html'
    meta='<meta name="robots" content="'+('noindex, follow' if missing else 'index, follow, max-image-preview:large')+'"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="Lustrzane Produkty">'
    graph=[{'@type':'Organization','name':'Lustrzane Produkty','legalName':'Puchary i Medale Sp. z o.o.','taxID':'6332240252','identifier':[{'@type':'PropertyValue','propertyID':'REGON','value':'383437540'},{'@type':'PropertyValue','propertyID':'KRS','value':'0000787581'}],'email':'grafiki.beauty@gmail.com','telephone':'+48883242299','address':{'@type':'PostalAddress','streetAddress':'ul. Gagarina 100','postalCode':'44-268','addressLocality':'Jastrzębie-Zdrój','addressCountry':'PL'}},{'@type':'WebSite','name':'Lustrzane Produkty','inLanguage':'pl-PL'}]
    if BASE and not missing:
        meta+='<link rel="canonical" href="'+esc(BASE+path)+'"><meta property="og:url" content="'+esc(BASE+path)+'"><meta property="og:image" content="'+esc(BASE+'/assets/campaign.webp')+'"><meta property="og:image:alt" content="Personalizowane produkty lustrzane"><meta name="twitter:card" content="summary_large_image">'
        for node,kind in zip(graph,['organization','website']):node.update({'@id':BASE+'/#'+kind,'url':BASE+'/'})
        if path!='/':
            label=html.unescape(re.search(r'<h1>(.*?)</h1>',s).group(1))
            graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Strona główna','item':BASE+'/'},{'@type':'ListItem','position':2,'name':label,'item':BASE+path}]})
    if not missing:meta+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')+'</script>'
    if path=='/':meta+='<link rel="preload" as="image" href="/assets/hero.webp" fetchpriority="high">'
    file.write_text(s.replace('</head>',meta+'</head>'))
# Demonstracyjne produkty nie trafiają do sitemap ani danych Product/Offer.
urls=['/']+['/'+slug+'/' for slug in DOCS]+['/produkty/'+p['slug']+'/' for p in products if p.get('published') is True]
if BASE:
    (P/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(BASE+u)+'</loc></url>' for u in urls)+'</urlset>')
else:(P/'sitemap.xml').unlink(missing_ok=True)
(P/'robots.txt').write_text('User-agent: *\nAllow: /\n'+('Sitemap: '+BASE+'/sitemap.xml\n' if BASE else ''))
all_docs=''
for slug,data in DOCS.items():
    content=''.join('<h3>'+esc(h)+'</h3>'+t for h,t in data['sections'])
    content=re.sub(r'id="([^"]+)"',lambda m:'id="'+slug+'-'+m.group(1)+'"',content)
    all_docs+='<article id="'+slug+'"><h2>'+esc(data['title'])+'</h2><p>'+esc(data['intro'])+'</p>'+content+'</article>'
all_docs=re.sub(r'href="/([^/]+)/#([^"]+)"',lambda m:'href="#'+m.group(1)+'-'+m.group(2)+'"',all_docs)
all_docs=re.sub(r'href="/([^/]+)/"',lambda m:'href="#'+m.group(1)+'"',all_docs)
Path('dokumentacja').mkdir(exist_ok=True)
Path('dokumentacja/Dokumenty-sklepu.html').write_text('<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dokumenty sklepu — Lustrzane Produkty</title><style>body{max-width:940px;margin:40px auto;padding:24px;font:16px/1.7 system-ui;color:#24231f}article{margin-top:48px}table{border-collapse:collapse}th,td{border:1px solid #ccc;padding:10px;text-align:left}a{color:#72541e}@media print{article{break-before:page}body{font-size:10pt}}</style></head><body><h1>Lustrzane Produkty — dokumenty sklepu</h1><p>Wersja 14.10.2026</p>'+all_docs+'</body></html>')
