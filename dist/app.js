(()=>{'use strict';
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const normalize=s=>s.toLocaleLowerCase('pl').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ł/g,'l');
let lastFocus=null;
function openDialog(d){lastFocus=document.activeElement;d.showModal();document.body.classList.add('modal-open')}
function closeDialog(d){d.close()}
$$('dialog').forEach(d=>{d.addEventListener('close',()=>{document.body.classList.remove('modal-open');lastFocus?.focus()});d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)closeDialog(d)}});$$('[data-close]',d).forEach(b=>b.addEventListener('click',()=>closeDialog(d)))});
const menu=$('.menu-toggle'),nav=$('#mobile-nav');menu?.addEventListener('click',()=>{const isOpen=menu.getAttribute('aria-expanded')==='true';nav.hidden=isOpen;menu.setAttribute('aria-expanded',String(!isOpen));menu.setAttribute('aria-label',isOpen?'Otwórz menu':'Zamknij menu')});$$('a',nav).forEach(a=>a.addEventListener('click',()=>{nav.hidden=true;menu.setAttribute('aria-expanded','false')}));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!nav.hidden){nav.hidden=true;menu.setAttribute('aria-expanded','false');menu.focus()}});matchMedia('(min-width:901px)').addEventListener('change',e=>{if(e.matches){nav.hidden=true;menu.setAttribute('aria-expanded','false')}});
let ticking=false;window.addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{$('.header').classList.toggle('scrolled',scrollY>15);ticking=false});ticking=true}},{passive:true});
const messages={produkt:['Twoja wizja. Nowe możliwości.','Pracujemy nad kreatorem własnych produktów. Już teraz możesz opowiedzieć nam o swoim pomyśle — sprawdzimy możliwości jego realizacji.'],logo:['Piękny początek Twojej marki.','Bezpłatny kreator logo pojawi się wkrótce. Jeśli potrzebujesz pomocy w przygotowaniu materiałów do produktu, skontaktuj się z nami.'],koszyk:['Twój przyszły koszyk.','Zakupy online pojawią się w przyszłości. Dziś wybierz produkt i wyślij zapytanie — przygotujemy indywidualną ofertę.']};
$$('[data-soon]').forEach(b=>b.addEventListener('click',()=>{const m=messages[b.dataset.soon];$('#soon-title').textContent=m[0];$('#soon-copy').textContent=m[1];openDialog($('#soon-dialog'))}));$('#soon-dialog a').addEventListener('click',()=>closeDialog($('#soon-dialog')));
function searchResults(){const q=normalize($('#global-search').value.trim());const list=CATALOG.filter(p=>normalize(p.name+' '+p.category).includes(q));$('#search-results').innerHTML=list.length?list.map(p=>`<a class="search-result" href="/produkty/${p.slug}/"><img src="${p.image}" alt="" width="55" height="64"><span><strong>${escape(p.name)}</strong><small>${escape(p.category)} · personalizacja</small></span></a>`).join(''):'<p>Nie znaleziono produktu. Spróbuj hasła „voucher” lub „tablica”.</p>'}
$$('[data-search]').forEach(b=>b.addEventListener('click',()=>{searchResults();openDialog($('#search-dialog'));$('#global-search').focus()}));$('#global-search').addEventListener('input',searchResults);
const partner=$('#partner-logos');if(partner)partner.innerHTML=[...PARTNERS].sort((a,b)=>['infini','mmgold','lumiere','carpatee','dives','schulke','clavier'].indexOf(a.name)-['infini','mmgold','lumiere','carpatee','dives','schulke','clavier'].indexOf(b.name)).map(p=>`<img src="${p.image}" alt="${escape(p.name)}" width="130" height="55" loading="lazy">`).join('');
const screens=$('#review-screens');if(screens)screens.innerHTML=REVIEWS.slice(10).map((src,i)=>`<button data-gallery="opinie" data-src="${src}" aria-label="Powiększ oryginalną opinię ${i+11}"><img src="${src}" alt="Oryginalna wiadomość klienta — opinia ${i+11}" loading="lazy" width="700" height="280"><span>Powiększ wiadomość ↗</span></button>`).join('');
// Duplicate only visual cards; keep the original gallery accessible.
const track=$('.reviews-track'),viewport=$('.reviews-viewport'),pause=$('#toggle-reviews');
if(track){
 const originals=[...track.children];
 originals.forEach(card=>{const clone=card.cloneNode(true);clone.removeAttribute('data-gallery');clone.setAttribute('aria-hidden','true');clone.tabIndex=-1;clone.addEventListener('click',()=>card.click());track.append(clone)});
 pause.addEventListener('click',()=>{const stopped=viewport.classList.toggle('is-paused');pause.setAttribute('aria-pressed',String(stopped));pause.textContent=stopped?'Wznów przewijanie':'Wstrzymaj przewijanie'});
}
let gallery=[],galleryIndex=0;function showGallery(){const entry=gallery[galleryIndex];$('#lightbox-image').src=entry.dataset.src;$('#lightbox-image').alt=$('img',entry)?.alt||'Powiększone zdjęcie';$('#lightbox-counter').textContent=`${galleryIndex+1} / ${gallery.length}`;$('#lightbox-prev').hidden=$('#lightbox-next').hidden=gallery.length<2;}
$$('[data-gallery]').forEach(b=>b.addEventListener('click',()=>{gallery=$$('[data-gallery]').filter(x=>x.dataset.gallery===b.dataset.gallery);galleryIndex=gallery.indexOf(b);showGallery();openDialog($('#lightbox'))}));function move(n){galleryIndex=(galleryIndex+n+gallery.length)%gallery.length;showGallery()}$('#lightbox-prev').addEventListener('click',()=>move(-1));$('#lightbox-next').addEventListener('click',()=>move(1));$('#lightbox').addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();move(-1)}if(e.key==='ArrowRight'){e.preventDefault();move(1)}});let startX=null;$('#lightbox-image').addEventListener('touchstart',e=>{startX=e.changedTouches[0].clientX},{passive:true});$('#lightbox-image').addEventListener('touchend',e=>{if(startX!==null){const diff=e.changedTouches[0].clientX-startX;if(Math.abs(diff)>60&&gallery.length>1)move(diff<0?1:-1);startX=null}},{passive:true});
$$('[data-view]').forEach(b=>b.addEventListener('click',()=>{$$('[data-view]').forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b))});$('.main-product-image').classList.toggle('zoomed',b.dataset.view==='detail')}));
$('.inquiry-cta')?.addEventListener('click',e=>{const q=$('#quantity');if(!q.checkValidity()){e.preventDefault();q.reportValidity();return}const name=$('.detail-copy h1').textContent,finish=$('input[name=finish]:checked').value;e.currentTarget.href='mailto:grafiki.beauty@gmail.com?subject='+encodeURIComponent('Zapytanie — '+name)+'&body='+encodeURIComponent('Dzień dobry,\nProszę o wycenę produktu: '+name+'\nWykończenie: '+finish+'\nLiczba sztuk: '+q.value+'\n\nDodatkowe informacje: ')});
$$('.inquiry-form').forEach(form=>{form.addEventListener('submit',e=>{e.preventDefault();const name=form.elements.name,message=form.elements.message;name.setCustomValidity(name.value.trim().length<2?'Wpisz imię (co najmniej 2 znaki).':'');message.setCustomValidity(message.value.trim().length<10?'Napisz przynajmniej 10 znaków o swoim zapytaniu.':'');if(!form.reportValidity())return;const q=$('#quantity');if(q&&!q.checkValidity()){q.reportValidity();return}const data=new FormData(form),finish=$('input[name=finish]:checked')?.value;const text=`Dzień dobry,\n\nChcę zapytać o: ${data.get('product')||'produkt indywidualny'}.\n${finish?'Preferowane wykończenie: '+finish+'\n':''}${q?'Liczba sztuk: '+q.value+'\n':''}\n${data.get('message').trim()}\n\nImię: ${data.get('name').trim()}\nE-mail: ${data.get('email')}\n${data.get('phone')?'Telefon: '+data.get('phone')+'\n':''}`;const subject=`Zapytanie — ${data.get('product')||'Lustrzane Produkty'}`;const mailto='mailto:grafiki.beauty@gmail.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(text);const status=$('.form-status',form);status.hidden=false;status.innerHTML='<strong>Zapytanie jest przygotowane — jeszcze nie zostało wysłane.</strong><p>Jeśli aplikacja pocztowa się nie otworzyła, skopiuj treść i wyślij ją na <a href="mailto:grafiki.beauty@gmail.com">grafiki.beauty@gmail.com</a>.</p><label>Treść zapytania<textarea readonly rows="7"></textarea></label><button type="button" class="small-btn copy-inquiry">Kopiuj treść</button> <a class="retry-mail">Otwórz pocztę ponownie ↗</a><p class="copy-status" role="status"></p>';$('textarea',status).value=text;$('.retry-mail',status).href=mailto;$('.copy-inquiry',status).addEventListener('click',async()=>{try{await navigator.clipboard.writeText(text);$('.copy-status',status).textContent='Skopiowano treść zapytania.'}catch{$('textarea',status).focus();$('textarea',status).select();$('.copy-status',status).textContent='Zaznaczono treść. Skopiuj ją ręcznie.'}});window.location.href=mailto;});$$('input,textarea',form).forEach(input=>input.addEventListener('input',()=>input.setCustomValidity('')))});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver'in window){document.documentElement.classList.add('js-motion');const reveal=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');reveal.unobserve(e.target)}}),{threshold:.08});$$('.reveal').forEach(x=>reveal.observe(x));}
if('IntersectionObserver'in window){const activeObserver=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){$$('.desktop-nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}}),{rootMargin:'-15% 0px -65% 0px'});$$('main section[id]').forEach(s=>activeObserver.observe(s));}

// A single damped light source follows the pointer; no sparkles or particle effects.
const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
const finePointer=matchMedia('(hover: hover) and (pointer: fine)');
$$('[data-tilt-stage], [data-reflection]').forEach(stage=>{
 const object=$('[data-tilt-object]',stage)||stage;
 let x=0,y=0,tx=0,ty=0,light=0,targetLight=0,frame=0;
 function draw(){
  x+=(tx-x)*.13;y+=(ty-y)*.13;light+=(targetLight-light)*.11;
  object.style.setProperty('--rx',(-y*7).toFixed(3)+'deg');
  object.style.setProperty('--ry',(x*10).toFixed(3)+'deg');
  object.style.setProperty('--mx',(50+x*43).toFixed(2)+'%');
  object.style.setProperty('--my',(45+y*40).toFixed(2)+'%');
  object.style.setProperty('--shine',light.toFixed(3));
  if(Math.abs(tx-x)+Math.abs(ty-y)+Math.abs(targetLight-light)>.002){frame=requestAnimationFrame(draw)}else{frame=0}
 }
 function schedule(){if(!frame)frame=requestAnimationFrame(draw)}
 stage.addEventListener('pointermove',e=>{
  if(motionPreference.matches||!finePointer.matches||e.pointerType==='touch')return;
  const r=stage.getBoundingClientRect();
  tx=Math.max(-1,Math.min(1,(e.clientX-r.left)/r.width*2-1));
  ty=Math.max(-1,Math.min(1,(e.clientY-r.top)/r.height*2-1));targetLight=1;schedule();
 },{passive:true});
 stage.addEventListener('pointerleave',()=>{tx=0;ty=0;targetLight=0;schedule()},{passive:true});
 motionPreference.addEventListener('change',()=>{if(motionPreference.matches){cancelAnimationFrame(frame);frame=0;x=y=tx=ty=light=targetLight=0;['--rx','--ry','--mx','--my','--shine'].forEach(k=>object.style.removeProperty(k))}});
});

})();
