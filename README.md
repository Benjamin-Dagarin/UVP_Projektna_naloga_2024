# Analiza fantazijskih knjig

V sledeči projektni nalogi, ki sem jo spisal v okviru predmeta Uvod v programiranje, vam bom predstavil analizo izbora fantazijskih knjig, ki sem ga pridobil s spletne strani <https://www.goodreads.com/>. Pri tem sem za delo uporabil programski jezik python.

Najprej sem v datoteki `spletne_strani.py` sestavil funkcijo, ki je iz izhodiščne spletne strani izluščila url-je do spletnih strani fantazijskih knjig, razvščenih po desetletjih. To funkcijo sem potem uvozil v osrednjo datoteko `Glavna_datoteka.py`, kjer sem z zanko `for` iteriral po url-jih. Vanjo sem uvozil tudi funkcije iz `ekstrakcija_podatkov.py`, ki sem jih uporabil za pridobivanje podatkov o knjigah s prej omenjenih spletnih strani. Podatke sem s pomočjo `Glavna_datoteka.py` zapisal v dokumentu csv `podatki_fantazijske_knjige.csv`, ki sem jih uvozil v zvezek `Analiza_fantazijskih_knjig.ipynb`, kjer sem jih analiziral in ustrezno interpretiral.

V prvem delu sem sestavil lestvice najboljših 10 iz vsake kategorije, tj. najkakovostnejše in najbolj brane knjige ter podobno za avtorje. V drugem delu sem raziskoval trende v žanru, predvsem kvaliteto, število bralcev, število avtorjev ter število knjig v odvisnosti od desetletja izida književnega dela, prav tako tudi odvisnost kvalitete od dolžine in branosti od dolžine.

V zadnjem, tretjem delu sem poskusil določiti t.i. "zlato dobo" fantazijskega žanra, torej desetletje, ki je bilo s stališča fantazijske zvrsti najboljše. Pri tem za točkovanje uporabil funkcijo, ki sem jo napisal v `zlato_desetletje.py`.

Ugotovitve sem zbral na koncu posameznih delov, nekaj uvidov v prihodnost tudi v Zaključku. Upam, da bodo rezultati pomagali vsem ljubiteljem fantazijskih knjig pri odločitvi, katero knjigo prebrati najprej.

*Benjamin Dagarin*





