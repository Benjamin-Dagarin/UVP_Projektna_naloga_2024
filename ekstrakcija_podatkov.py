# fantazijska_literatura.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import requests
import re
import time

##############################################################################
# Vzorci

vzorec_tocke = re.compile(r'score: ((\d+),(\d+)|(\d+))')
vzorec_strani = re.compile(r'\d+')
vzorec_izid = re.compile(r'\d{4,4}')
vzorec_desetletje = re.compile(r'\d+')
vzorec_ocena = re.compile(r'\d\.\d{2,2}')
vzorec_skrajsan = (r'(\d{0,3},\d{3,3},\d{3,3})|(\d{0,3},\d{3,3})|(\d{0,3})'
                     + r' ratings')
vzorec_st_bralcev = re.compile(vzorec_skrajsan)

#############################################################################
# Funkcije, namenjene ekstarhiranju posameznih podatkov o knjigah

def izlusci_bralce(vnos):
    """Ko v funkciji 'pridobi_oceno_st_bralcev' pridobivamo število bralcev,
       ta vrača sezname seznamov, ki vsebujejo prazne nize in pa število 
       bralcev.
       
       S to funkcijo želimo iz seznama možnih rezultatov pridobiti tisti 
       podseznam, ki vsebuje število bralcev, nato pa iz njega še število 
       bralcev samo.
    """
    seznam = vnos
    for el in seznam:
        if el.count('') == len(el):
            seznam.remove(el)
    seznam = list(seznam)
    for el in seznam[0]:
        if el != '':
            return el
    return None

def pridobi_tocke(blok_knjige):
    """Pridobimo število točk, ki jih je prejela posamezna knjiga.

       Ker je v številu za ločevanje števk uporabljena vejica, jo
       moramo odstraniti.
    """
    span_s_tockami = blok_knjige.find(['span'], class_="smallText uitext")
    tocke_niz = span_s_tockami.find('a').string
    zadetek = str(vzorec_tocke.search(tocke_niz).group(1))
    if ',' in zadetek:
        novi_zadetek = zadetek.replace(',', '')
        return int(novi_zadetek)
    
    return int(zadetek)

def pridobi_avtorja(blok_knjige):
    return blok_knjige.find(['a'], class_="authorName").string

def pridobi_naslov(blok_knjige):
    nadznacka = blok_knjige.find(['a'], class_="bookTitle")
    return nadznacka.find('span').string

def pridobi_izid_strani(html_knjige):
    strani = None
    izid = None
    try:
        odsek = html_knjige.find(['div'], class_='BookDetails')
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
        return [int(izid), strani]

def pridobi_oceno_st_bralcev(blok_knjige):
    znacka = blok_knjige.find(['span'], class_ = "minirating")
    iskani_blok = str(znacka)
    ocena = None
    bralci = None
    st_bralcev = None

    try:
        ocena = vzorec_ocena.findall(iskani_blok)[0]
    except:
        pass
    try:
        bralci = (vzorec_st_bralcev.findall(iskani_blok))
    except:
        pass
    try:
        st_bralcev = izlusci_bralce(bralci)
    except:
        pass
    try:    
        if "," in st_bralcev:
            st_bralcev = st_bralcev.replace(',', "") # Odstrani vejice v številu
    except:
        pass

    if ocena != None and st_bralcev != None:
        return [float(ocena), int(st_bralcev)]
    elif ocena == None:
        if st_bralcev == None:
            return [ocena, st_bralcev]
        else:
            return [ocena, int(st_bralcev)]
    else:
        return [float(ocena), st_bralcev]

#############################################################################
# Luščenje podatkov s spletne strani pri posameznem desetletju

def obdelava_strani(link):
    """Prejme link spletne strani in iz nje izlušči vse podatke o posameznih
       knjigah.

       Če podatka ni (mogoče pridobiti), mu pripiše vrednost 'None'.
    """

    podatki = []
    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
                 ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    )
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')
    tabela = html.find(['table'], class_="tableList js-dataTooltip")
    knjige = tabela.find_all('tr')
    for knjiga in knjige:
        link_do_knjige = knjiga.find('a')['href']
        tocke = None
        avtor = None
        naslov = None
        try:
            tocke = pridobi_tocke(knjiga)
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
        pridobi_stran_knjiga = requests.get(cel_link,
                                            headers={'User-Agent' : userAgent})
        html_knjiga = BeautifulSoup(pridobi_stran_knjiga.text, 'html.parser',
                                    from_encoding='UTF-8')
        izid_in_strani = pridobi_izid_strani(html_knjiga)
        izid = izid_in_strani[0]
        strani = izid_in_strani[1]
        ocena_in_bralci = pridobi_oceno_st_bralcev(knjiga)
        ocena = ocena_in_bralci[0]
        st_bralcev = ocena_in_bralci[1]
        podatki.append([naslov, avtor, izid, strani, tocke, ocena, st_bralcev])

    return podatki

##############################################################################
# Ekstrakcija blokov in nato podatkov na ustrezni strani posameznega
# desetletja

def desetletje_podatki(link):
    """S prve spletne strani od posameznega desetletja, ki ji priprada 'link'
       v argumentu funkcije, ekstrahira vse podatke o knjigah, nato pa gre na
       naslednje strani posameznega desetletja.
    """

    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    )
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')
    desetletje_niz = html.find(['h1'], class_="gr-h1 gr-h1--serif").string
    desetletje = int((vzorec_desetletje.findall(desetletje_niz))[0])  # Iskanje oznake desetletja, da jo lahko potem vstavim v link za naslednje strani po desetletjih
    podatki = []
    trenutni_link = link
    podatki.extend(obdelava_strani(trenutni_link))
    i = 2
    while True:
        time.sleep(0.1)  # Varovalka, da spletna stran ne začne zavračati requestov
        nova_stran = link + f'.Best_Fantasy_of_the_{desetletje}s?page={i}'
        try:
            podatki.extend(obdelava_strani(nova_stran))
        except:
            break
        else:
            i += 1
    
    return podatki

    

    

        

