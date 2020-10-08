import requests
from bs4 import BeautifulSoup
#
# page=requests.get("https://allegro.pl/kategoria/laptopy-dell-77917?bmatch=baseline-product-cl-eyesa2-engag-dict45-ele-1-4-0717")        # tutaj strona na ktorej szukamy
# soup=BeautifulSoup(page.content, 'html.parser')
# # print(soup)  # to jest zrodlo strony
#
# # nazwa=soup.find_all(class_="_115at")
# nazwa=soup.find_all(class_="_1s2v1 _dsf2b _1rj80")
# print(nazwa.get_text())
#
#
# cena=soup.find_all(class_="_mitvy _3e3a8_39EPX")
# print(cena.get_text())

#
# page=requests.get("https://allegro.pl/kategoria/laptopy-dell-77917?bmatch=baseline-product-cl-eyesa2-engag-dict45-ele-1-4-0717")        # tutaj strona na ktorej szukamy
# soup=BeautifulSoup(page.content, 'html.parser')
# listanazw=soup

import requests
from bs4 import BeautifulSoup

# page = requests.get("https://allegro.pl/oferta/mata-korkowa-spokey-savasana-joga-fitness-korek-9625526948?bi_m=mpage&")
# soup = BeautifulSoup(page.content, 'html.parser')
# nazwa = soup.find(class_="_9a071_1Ux3M _9a071_3nB-- _9a071_1R3g4 _9a071_1S3No")
# print(nazwa.get_text())
#
# cena = soup.find(class_="_1svub _lf05o _9a071_2MEB_")
# print(cena.get_text())

# V1
# page = requests.get("https://allegro.pl/kategoria/trening-fitness-maty-110136?bmatch=baseline-product-eyesa2-engag-dict45-spo-1-5-0717")
# soup = BeautifulSoup(page.content, 'html.parser')
# listaNazw = soup.find_all(class_="_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY")
# listaCena = soup.find_all(class_="msa3_z4 _9c44d_2K6FN")
# for i in range(len(listaCena)):
#     print(listaNazw[i].get_text(), listaCena[i].get_text())


# # V2
page = requests.get("https://allegro.pl/kategoria/trening-fitness-maty-110136?bmatch=baseline-product-eyesa2-engag-dict45-spo-1-5-0717")
soup = BeautifulSoup(page.content, 'html.parser')
linki = soup.find_all(class_="_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY")
for i in linki:
    link = i['href']

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    nazwa = soup.find(class_="_9a071_1Ux3M _9a071_3nB-- _9a071_1R3g4 _9a071_1S3No")
    print(nazwa.get_text())

    cena = soup.find(class_="_1svub _lf05o _9a071_2MEB_")
    print(cena.get_text())


