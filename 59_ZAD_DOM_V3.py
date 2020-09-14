import random

print(f"Gramy w gre: Zgadnij liczbe z przedzialu 1-100. Masz 5 prob ")

def gra():
    los = random.randint(1, 10)
    lista = []
    while (True):
        x = int(input(f"Podaj liczbe: "))
        lista.append(x)
        if(len(lista)==5):
            decyzja=input(f" Przegrales, za duzo prob. Czy chcesz zagrac jeszcze raz? T/N ").upper()
            return decyzja
        if (los == x):
            decyzja = input(f" Brawo!!!, Zgadles. Czy chcesz zagrac jeszcze raz? T/N ").upper()
            return decyzja
        elif (los > x):
            print(f"Za mało. Podaj wieksza liczbe ")
        elif (los < x):
            print(f"Za duzo. Podaj mniejsza liczbe ")

while(True):
    if(gra()=='N'):
        print(f" Wybrales N. Konczymy gre. Do zobaczenia ")
        break
    elif(gra()=='T'):
        gra()
    else:
        print(f" Podales wartosci niedopuszczalne. KONIEC")
        break
