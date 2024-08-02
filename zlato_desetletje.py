# zlato_desetletje.py

##############################################################################
# Knjižnice

import pandas as pd
from operator import itemgetter

##############################################################################
# Ekstrakcija linkov do spletnih strani po desetletjih

def mesto_v_tabeli(df, ime_stolpca):
        """Funkcija, namenjena razvrščanju desetletij po kategorijah. 
        
        Vsakemu desetletju pripišemo število točk v posamezni kategoriji.
        """

        desetletja = [1900 + i*10 for i in range(2,13)]
        pari = []
        for desetl in desetletja:
            try:
                pari.append([df.loc[desetl,ime_stolpca], desetl])
            except:
                pari.append([-1, desetl])
        sortiranje_po_mestih = sorted(pari, key=itemgetter(0,1))
        pari_desetletje_mesto = []
        for i in range(len(sortiranje_po_mestih)):
            pari_desetletje_mesto.append([sortiranje_po_mestih[i][1], i])
        pari_desetletje_mesto.sort(key=itemgetter(0))
        mesta = list(map(lambda x: int(x[1]), pari_desetletje_mesto))

        return mesta

    



