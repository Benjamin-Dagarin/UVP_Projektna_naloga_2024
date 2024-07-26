# Glavna_datoteka.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import re
import requests
import time
import csv

#############################################################################
# Moduli
import fantazijska_literatura as fl
import spletne_strani as spl

#############################################################################
# Prvi del - Analiza fantazijske literature in zapis v csv

userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
)

linki_desetletja = spl.strani_po_desetletjih()
with open('fantazijska_literatura.csv', 'w', encoding='UTF-8') as dat:
    kljuci = ['Naslov', 'Avtor', 'Leta izida', 'Dolžina', 'Točke', 'Ocena', 'Število bralcev']
    csv_pisec = csv.writer(dat)
    csv_pisec.writerow(kljuci)
    for link in linki_desetletja:
        podatki = fl.desetletje_podatki(link)
        for knjiga in podatki:
            csv_pisec.writerow(knjiga)
        print('konec')
        break

#print(podatki)



