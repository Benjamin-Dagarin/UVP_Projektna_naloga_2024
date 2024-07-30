import pandas as pd
from operator import itemgetter
import random
#nek_slovar = {'Oseba':['Janez Novak', 'Miha Kovač'], 'Starost':[45, 76]}
#
#zlate_tocke = {
#    'Desetletje': [1900 + i*10 for i in range(2,13)],
#    'Delež':[],
#    'Kvaliteta':[],
#    'Število bralcev':[],
#    'Število avtorjev':[],
#}
#
#testna_tabela = pd.DataFrame(
#    {
#    'Desetletje': [1900 + i*10 for i in range(2,13)],
#    'Število knjig':[random.randint(1, 100000) for _ in range(2,13)],
#})
#testna_tabela.set_index('Desetletje', drop=True, inplace=True)
#print(testna_tabela)

#tabela = pd.DataFrame(nek_slovar)
#print(tabela)

# Pandas deluje tudi v navadni pythonski skripti!

#class ZlatoDesetletje:
#
#    @staticmethod
#    def mesto_v_tabeli(df, ime_stolpca):
#        desetletja = [1900 + i*10 for i in range(2,13)]
#        print(type(df.index))
#        print(list(df.index))
#        #print(type(desetletja))
#        #print(len(desetletja))
#        pari = []
#
#        #print(st_desetletij)
#        for desetl in desetletja:
#            print('A')
#            print(desetl)
#            #print(df.iloc[i, 0])
#            print('B')
#            pari.append([df.loc[desetl,ime_stolpca], desetl])
#            #print(pari)
#        print('C')
#        sortiranje_po_mestih = sorted(pari, key=itemgetter(0,1))
#        pari_desetletje_mesto = []
#        for i in range(len(desetletja)):
#            print(('D', i))
#            pari_desetletje_mesto.append([sortiranje_po_mestih[i][1], i])
#        #print(pari_desetletje_mesto)
#        print('E')
#        pari_desetletje_mesto.sort(key=itemgetter(0))
#        #print(pari_desetletje_mesto)
#        print('F')
#        mesta = list(map(lambda x: x[1], pari_desetletje_mesto))
#        print('G')
#        return mesta


def mesto_v_tabeli(df, ime_stolpca):
        desetletja = [1900 + i*10 for i in range(2,13)]
        print(type(df.index))
        print(list(df.index))
        #print(type(desetletja))
        #print(len(desetletja))
        pari = []

        #print(st_desetletij)
        for desetl in desetletja:
            print('A')
            print(desetl)
            #print(df.iloc[i, 0])
            print('B')
            try:
                pari.append([df.loc[desetl,ime_stolpca], desetl])
            except:
                pari.append([-1, desetl])
        print('C')
        print(pari)
        sortiranje_po_mestih = sorted(pari, key=itemgetter(0,1))
        print(sortiranje_po_mestih)
        pari_desetletje_mesto = []
        for i in range(len(sortiranje_po_mestih)):
            print(('D', i))
            pari_desetletje_mesto.append([sortiranje_po_mestih[i][1], i])
        print(pari_desetletje_mesto)
        print('E')
        pari_desetletje_mesto.sort(key=itemgetter(0))
        print(pari_desetletje_mesto)
        print('F')
        mesta = list(map(lambda x: int(x[1]), pari_desetletje_mesto))
        print('G')
        print(mesta)
        return mesta



