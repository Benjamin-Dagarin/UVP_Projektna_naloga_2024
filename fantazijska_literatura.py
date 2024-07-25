# fantazijska_literatura.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import requests
import re
import time

##############################################################################
# Vzorci

vzorec_01 = re.compile(r'score: ((\d+),(\d+)|(\d+))')
vzorec_strani = re.compile(r'\d+')
vzorec_izid = re.compile(r'\d\d\d\d')
vzorec_desetletje = re.compile(r'\d+')



#############################################################################
def pridobi_tocke(html_knjige):
    span_s_tockami = html_knjige.find(['span'], class_="smallText uitext")
    tocke_niz = span_s_tockami.find('a').string
    zadetek = vzorec_01.search(tocke_niz).group(1)
    return zadetek

def pridobi_avtorja(blok):
    return blok.find('a', class_="authorName").string

def pridobi_naslov(blok):
    nadznacka = blok.find(['a'], class_="bookTitle")
    return nadznacka.find('span').string

def pridobi_izid_strani(html):
    #niz_s_podatki = blok.find(['script'], type="application/ld+json").string
    strani = None
    izid = None
    try:
        odsek = html.find(['div'], class_='BookDetails')
        odsek_s_stranmi = odsek.find(['div'], 
                                     class_="FeaturedDetails").find_all('p')[0]
        tekst = odsek_s_stranmi.string
        strani = (vzorec_strani.findall(tekst))[0]
    except:
        pass
    try:
        znacka_izid = odsek.find(['div'],
                                 class_="FeaturedDetails").find_all('p')[1]
        izid_tekst = znacka_izid.string
        izid = (vzorec_izid.findall(izid_tekst))[0]
    except:
        pass

    if izid != None and strani != None:
        return [int(izid), int(strani)]
    elif izid == None:
        if strani == None:
            return [izid, strani]
        else:
            return [izid, int(strani)]
    else:
        if strani == None:
            return [int(izid), strani]

def obdelava_strani(link):
    podatki = []
    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    )
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')
    tabela = html.find(['table'], class_="tableList js-dataTooltip")
    knjige = tabela.find_all('tr')
    #print(knjige[0])
    i = 0
    for knjiga in knjige:
        print(f'knjiga številka: {i}')
        link_do_knjige = knjiga.find('a')['href']
        #print(f'link_do_knjige: {link_do_knjige}')
        tocke = None
        avtor = None
        naslov = None
        try:
            tocke = pridobi_tocke
        except:
            pass
        try:
            avtor = pridobi_avtorja(knjiga)
        except:
            pass
        try:
            naslov = pridobi_naslov(knjiga)
        except:
            pass
        cel_link = "https://www.goodreads.com" + link_do_knjige
        #print(f'cel link: {cel_link}')
        pridobi_stran_knjiga = requests.get(cel_link,
                                            headers={'User-Agent' : userAgent})
        html_knjiga = BeautifulSoup(pridobi_stran_knjiga.text, 'html.parser',
                                    from_encoding='UTF-8')
        izid_in_strani = pridobi_izid_strani(html_knjiga)
        izid = izid_in_strani[0]
        strani = izid_in_strani[1]
        podatki.append([naslov, avtor, izid, strani, tocke])
        i += 1
    return podatki


#def pridobi_strani(blok):
#    odsek = blok.find(['div'], class_='BookDetails')
#    odsek_z_izidom = odsek.find(['div'], class_="FeaturedDetails")
#    tekst = odsek_s_stranmi.string
#    strani = (vzorec_strani.findall(tekst))[0]
#    return int(strani)


## Ekstrakcija podatkov na spletni strani od knjige
#def pridobi_izid_in_strani(link):
#    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
#            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
#    )
#    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
#    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')


# Ekstrakcija blokov in nato podatkov na ustrezni strani
def desetletje_podatki(link):
    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    )
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')
    desetletje_niz = html.find(['h1'], class_="gr-h1 gr-h1--serif").string
    desetletje = int((vzorec_desetletje.findall(desetletje_niz))[0])
    podatki = []
    trenutni_link = link
    podatki.extend(obdelava_strani(trenutni_link))
    print(podatki)
    i = 2
    while True:
        time.sleep(0.1)
        nova_stran = link + f'.Best_Fantasy_of_the_{desetletje}s?page={i}'
        try:
            podatki.extend(obdelava_strani(nova_stran))
        except:
            break
    
    return podatki

    

    

        

