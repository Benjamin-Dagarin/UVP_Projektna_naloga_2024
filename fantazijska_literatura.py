# fantazijska_literatura.py

##############################################################################
# Knjižnice

from bs4 import BeautifulSoup
import re

##############################################################################
# Vzorci

vzorec_tabela = re.compile(r'class="tableList js-dataTooltip"')
vzorec_id = re.compile('<div id="all_votes">')
#############################################################################
# Ekstrakcija blokov na ustrezni strani

def bloki(bs_dat):
    return bs_dat.find_all('table')[0]

