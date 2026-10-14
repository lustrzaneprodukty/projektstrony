"""Opcjonalne dane rzeczywistego katalogu. Nie przypisuje producenta automatycznie."""
from html import escape as esc
OWN_MANUFACTURER = {
    'name': 'Puchary i Medale Sp. z o.o.',
    'address': 'ul. Gagarina 100, 44-268 Jastrzębie-Zdrój, Polska',
    'email': 'grafiki.beauty@gmail.com',
    'nip': '6332240252', 'regon': '383437540', 'krs': '0000787581'
}
def product_safety(product):
    safety = product.get('safety')
    if not safety:
        return '<section class="container"><p class="fine"><a href="/bezpieczenstwo-produktow/">Bezpieczeństwo produktów i kontakt z producentem</a></p></section>'
    manufacturer = OWN_MANUFACTURER if safety.get('ownManufacture') is True else safety.get('manufacturer', {})
    if not all(manufacturer.get(k) for k in ('name','address','email')) or not safety.get('identifier'):
        raise ValueError('Niepełne dane GPSR produktu: '+product['slug'])
    def contact(data):
        return '<p>'+esc(data['name'])+'<br>'+esc(data['address'])+'<br>'+esc(data['email'])+'</p>'
    body='<p>Identyfikator: '+esc(safety['identifier'])+'</p><h3>Producent</h3>'+contact(manufacturer)
    if safety.get('manufacturerOutsideEU') and not safety.get('responsiblePerson'):
        raise ValueError('Wymagany podmiot odpowiedzialny w UE: '+product['slug'])
    if safety.get('responsiblePerson'):
        person=safety['responsiblePerson']
        if not all(person.get(k) for k in ('name','address','email')):raise ValueError('Niepełny kontakt podmiotu odpowiedzialnego')
        body+='<h3>Podmiot odpowiedzialny w UE</h3>'+contact(person)
    if safety.get('intendedUse'):body+='<p>'+esc(safety['intendedUse'])+'</p>'
    for heading,key in [('Bezpieczne użytkowanie','instructions'),('Ostrzeżenia','warnings')]:
        if safety.get(key):body+='<h3>'+heading+'</h3><ul>'+''.join('<li>'+esc(x)+'</li>' for x in safety[key])+'</ul>'
    return '<section class="section container legal"><h2>Informacje o bezpieczeństwie</h2>'+body+'</section>'
