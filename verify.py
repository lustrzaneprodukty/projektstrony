"""Kontrola wygenerowanego frontendu: python verify.py."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.titles=0;self.desc=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.titles+=1
  if tag=='meta' and a.get('name')=='description':self.desc+=1
  for key in ('href','src','poster','data-src'):
   if a.get(key):self.links.append(a[key])
root=Path('dist');pages={p:Page(p.read_text()) for p in root.rglob('*.html')};errors=[];links=0
for path,page in pages.items():
 text=path.read_text()
 if (page.h1,page.titles,page.desc)!=(1,1,1):errors.append(f'{path}: H1/title/description')
 if len(page.ids)!=len(set(page.ids)):errors.append(f'{path}: duplicate id')
 if re.search(r'UZUPEŁNIJ|TODO|wkrótce|przykładowa|peppyluck4',text,re.I):errors.append(f'{path}: draft content')
 if '/dane-sprzedawcy/' not in text or '/dostawa-i-platnosci/' not in text:errors.append(f'{path}: legal navigation')
 for raw in page.links:
  u=urlsplit(raw)
  if u.scheme or u.netloc:continue
  target=root/unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path) if u.path else path
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{path}: missing {raw}')
  elif u.fragment and target in pages and unquote(u.fragment)not in pages[target].ids:errors.append(f'{path}: anchor {raw}')
  links+=1
 for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
  graph=json.loads(block)['@graph']
  if any(n['@type']in ['Product','Offer','AggregateRating'] for n in graph):errors.append(f'{path}: demo schema')
print(json.dumps({'pages':len(pages),'localReferences':links,'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
