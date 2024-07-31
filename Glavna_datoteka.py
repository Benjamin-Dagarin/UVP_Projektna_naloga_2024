# Glavna_datoteka.py

##############################################################################
# Knjižnice

import csv

#############################################################################
# Moduli

import ekstrakcija_podatkov as ep
import spletne_strani as spl

#############################################################################
# Pridobivanje podatkov o knjigah in njihov zapis v csv

linki_desetletja = spl.strani_po_desetletjih()
with open('podatki_fantazijske_knjige.csv', 'w', encoding='UTF-8') as dat:
    kljuci = ['Naslov', 'Avtor', 'Leto izida', 'Dolžina',
              'Točke', 'Ocena', 'Število bralcev']
    csv_pisec = csv.writer(dat)
    csv_pisec.writerow(kljuci)
    for link in linki_desetletja:
        podatki = ep.desetletje_podatki(link)  # Ekstrakcija podatkov za desetletje
        for knjiga in podatki:
            csv_pisec.writerow(knjiga)




