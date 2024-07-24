# Glavna_datoteka.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import re
import requests
import time
import fantazijska_literatura as fl

#############################################################################
#############################################################################
# Prvi del - Analiza fantazijske literature

podatki = []

desetletja = [(1900 + 10*i) for i in range(3, 10)] + [2000, 2010, 2020]
userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
)


for i in range(1000, 150000):
    print(i)
    time.sleep(0.1)
    zacetek_spletne_strani = None
    spletna_stran_i = f'https://www.goodreads.com/list/show/{i}'
    try:
        zacetek_spletne_strani = requests.get(spletna_stran_i, 
                                              headers = {'User-Agent' : userAgent})
    except:
        continue
    else:
        html = BeautifulSoup(zacetek_spletne_strani.text, 'html.parser', from_encoding='UTF-8')
        odseki_kode = fl.bloki(html)
        print(odseki_kode)
        break

