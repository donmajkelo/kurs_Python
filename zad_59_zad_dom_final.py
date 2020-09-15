
def gra():
    import random
    print(f"Gramy w gre: Zgadnij liczbe z przedzialu 1-100. Masz 5 prob ")
    los = random.randint(1, 100)
    lista = []
    while (True):
        zm_pomocnicza = 0
        x = int(input(f"Podaj liczbe: "))
        lista.append(x)
        if(len(lista)==5):
            decyzja=input(f" Przegrales, za duzo prob. Czy chcesz zagrac jeszcze raz? T/N ").upper()
            if(decyzja=="N"):
                print(f" Wybrales N. Konczymy gre. Do zobaczenia ")
                break
            elif(decyzja=="T"):
                los = random.randint(1, 100)
                lista = []
                zm_pomocnicza = 1
            else:
                print(f" Podales wartosci niedopuszczalne. KONIEC")
                break
        if (los == x ):
            decyzja = input(f" Brawo!!!, Zgadles. Czy chcesz zagrac jeszcze raz? T/N ").upper()
            if (decyzja == "N"):
                print(f" Wybrales N. Konczymy gre. Do zobaczenia ")
                break
            elif (decyzja == "T"):
                los = random.randint(1, 100)
                lista = []
                zm_pomocnicza=1
            else:
                print(f" Podales wartosci niedopuszczalne. KONIEC")
                break
        elif (los > x and zm_pomocnicza==0):
            print(f"Za mało. Podaj wieksza liczbe ")
        elif (los < x and zm_pomocnicza==0):
            print(f"Za duzo. Podaj mniejsza liczbe ")

gra()


