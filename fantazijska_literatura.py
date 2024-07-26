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
vzorec_izid = re.compile(r'\d\d\d\d')
vzorec_desetletje = re.compile(r'\d+')
vzorec_ocena = re.compile(r'\d\.\d{2,2}')
vzorec_skrajsan = (r'(\d{0,3},\d{3,3},\d{3,3})|(\d{0,3},\d\d\d)|(\d{0,3})'
                     + r' ratings')


vzorec_st_bralcev = re.compile(vzorec_skrajsan)



#############################################################################
def izlusci_bralce(vnos):
    seznam = vnos
    for el in seznam:
        if el.count('') == len(el):
            seznam.remove(el)
    print(seznam)
    seznam = list(seznam)
    for el in seznam[0]:
        if el != '':
            return el
    return None

def pridobi_tocke(html_knjige):
    span_s_tockami = html_knjige.find(['span'], class_="smallText uitext")
    #print(span_s_tockami)
    tocke_niz = span_s_tockami.find('a').string
    #print(tocke_niz)
    zadetek = vzorec_tocke.search(tocke_niz).group(1)
    if ',' in str(zadetek):
        novi_zadetek = zadetek.replace(',', '')
        #print(novi_zadetek)
        return int(novi_zadetek)
    return int(zadetek)

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
        #print(f'odsek: {odsek}')
        odsek_s_stranmi = odsek.find(['div'], 
                                     class_="FeaturedDetails").find_all('p')[0]
        #print(f'odsek_s_stranmi: {odsek_s_stranmi}')
        tekst = odsek_s_stranmi.string
        #print(f'tekst: {tekst}')
        strani = (vzorec_strani.findall(tekst))[0]
        #print(f'strani: {strani}')
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
        #print([int(izid), int(strani)])
        return [int(izid), int(strani)]
    elif izid == None:
        if strani == None:
            #print([izid, strani])
            return [izid, strani]
        else:
            #print([izid, int(strani)])
            return [izid, int(strani)]
    else:
        #print([int(izid), strani])
        return [int(izid), strani]

def ocena_in_st_bralcev(knjiga):
    print(knjiga)
    print(' ')
    print(knjiga.find(['span'], class_ = "minirating"))
    print(' ')
    znacka = knjiga.find(['span'], class_ = "minirating")
    iskani_niz = str(znacka)
    print(iskani_niz)
    print(' ')
    ocena = None
    bralci = None

    try:
        ocena = vzorec_ocena.findall(iskani_niz)[0]
    except:
        pass
    try:
        bralci = (vzorec_st_bralcev.findall(iskani_niz))
    except:
        pass

    print(bralci)
    st_bralcev = izlusci_bralce(bralci)
    print(st_bralcev)
    try:    
        if "," in st_bralcev:
            st_bralcev = st_bralcev.replace(',', "")
    except:
        pass

    print(st_bralcev)

    if ocena != None and st_bralcev != None:
        #print([int(izid), int(strani)])
        return [float(ocena), int(st_bralcev)]
    elif ocena == None:
        if st_bralcev == None:
            #print([izid, strani])
            return [ocena, st_bralcev]
        else:
            #print([izid, int(strani)])
            return [ocena, int(st_bralcev)]
    else:
        #print([int(izid), strani])
        return [float(ocena), st_bralcev]


def obdelava_strani(link):
    print(link)
    podatki = []
    userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
            ' (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    )
    pridobi_stran = requests.get(link, headers = {'User-Agent' : userAgent})
    html = BeautifulSoup(pridobi_stran.text, 'html.parser', from_encoding='UTF-8')
    tabela = html.find(['table'], class_="tableList js-dataTooltip")
    knjige = tabela.find_all('tr')
    #print(knjige[0])
    i = 1
    for knjiga in knjige:
        print(f'knjiga številka: {i}')
        print(' ')
        link_do_knjige = knjiga.find('a')['href']
        #print(f'link_do_knjige: {link_do_knjige}')
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
        #print(f'cel link: {cel_link}')
        pridobi_stran_knjiga = requests.get(cel_link,
                                            headers={'User-Agent' : userAgent})
        html_knjiga = BeautifulSoup(pridobi_stran_knjiga.text, 'html.parser',
                                    from_encoding='UTF-8')
        izid_in_strani = pridobi_izid_strani(html_knjiga)
        izid = izid_in_strani[0]
        strani = izid_in_strani[1]
        ocena_in_bralci = ocena_in_st_bralcev(knjiga)
        ocena = ocena_in_bralci[0]
        st_bralcev = ocena_in_bralci[1]
        print([naslov, avtor, izid, strani, tocke, ocena, st_bralcev])
        print(' ')
        print(' ')
        print(' ')
        podatki.append([naslov, avtor, izid, strani, tocke, ocena, st_bralcev])
        i += 1
    return podatki

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
    #print(podatki)
    i = 2
    while True:
        #print(i)
        time.sleep(0.1)
        nova_stran = link + f'.Best_Fantasy_of_the_{desetletje}s?page={i}'
        try:
            podatki.extend(obdelava_strani(nova_stran))
        except:
            break
        finally:
            break
    
    return podatki

    

    

        

