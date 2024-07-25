# Glavna_datoteka.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import re
import requests
import time

#############################################################################
# Moduli
import fantazijska_literatura as fl
import spletne_strani as spl

#############################################################################
# Prvi del - Analiza fantazijske literature

podatki = []

userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
)

linki_desetletja = spl.strani_po_desetletjih()
for link in linki_desetletja:
    podatki.extend(fl.desetletje_podatki(link))
    break

print(podatki)



