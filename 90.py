import requests
from bs4 import BeautifulSoup

page=requests.get("https://allegro.pl/oferta/dell-latitude-e7250-i5-4gb-128gb-ssd-win-10-kamera-9271658105")        # tutaj strona na ktorej szukamy
soup=BeautifulSoup(page.content, 'html.parser')
# print(soup)  # to jest zrodlo strony

nazwa=soup.find(class_="_9a071_1Ux3M _9a071_3nB-- _9a071_1R3g4 _9a071_1S3No")   # tutaj kopiujemy z nazwy
print(nazwa.get_text())


cena=soup.find(class_="_9a071_1Q_68")       # tutaj kopiujemy z ceny
print(cena.get_text())

