# spletne_strani.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import requests
from user_agent import userAgent

##############################################################################
# Ekstrakcija linkov do spletnih strani po desetletjih

def strani_po_desetletjih():
    """Iz spletne strani, ki jo lahko najdemo na url-ju, shranjenim pod
       spremenljivko 'link', izluščimo url-je vseh spletnih strani, ki ustrezajo
       podameznim desetletjem.
    """
    link = "https://www.goodreads.com/list/show/79774.Best_Fantasy_of_the_30s"
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser',
                         from_encoding='UTF-8')
    znacka_z_linki = html.find(['div'],
                               class_="u-paddingBottomMedium mediumText")
    podznacke = znacka_z_linki.find_all('a')
    linki = []
    for i in range(4, 14):
        linki.append((podznacke[i])['href'])
        
    return linki



    