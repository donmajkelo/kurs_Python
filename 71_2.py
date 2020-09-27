
class Koszyk:

    def __init__(self):
        self.zakupy={}              # to jest słownik w koszyku

    def dodaj_produkt(self, produkt, ilosc):
        if(produkt in self.zakupy):                  # sprawdzamy czy produkt istnieje
            ile_obecnie=self.zakupy[produkt]
            self.zakupy[produkt]=ile_obecnie+ilosc
        else:                                          # w przeciwnym razie wybieramy ilosc produktu
            self.zakupy[produkt]=ilosc

    def odejmij_produkt(self, produkt, ilosc):
        if (produkt in self.zakupy):                    # sprawdzamy czy produkt istnieje
            ile_obecnie = self.zakupy[produkt]
            if(ile_obecnie > ilosc):
                self.zakupy[produkt] = ile_obecnie - ilosc
            elif (ile_obecnie == ilosc):
                del self.zakupy[produkt]
            else:
                print(" Niepoprawna ilosc ")
        else:                                        # w przeciwnym razie wybieramy ilosc produktu
            print(f" Brak produktu w koszyku ")
            # self.zakupy[produkt] = ilosc

koszyk= Koszyk()
sklep= {"chleb": 2.50, "sok": 3.20, "woda": 1.30, "piwo": 5.20}
suma=0
razem=0

while (True):
    menu=input(" D -dodaj do koszyka, u -usun z koszyka,  P=pokaz koszyk, K- koniec").upper()

    if(menu=='D'):
        print(sklep)
        produkt=input(" Podaj nazwe produktu, ktory chcesz kupic ")
        if (produkt in sklep):

            ilosc = int(input(" Podaj ilosc produktu, ktory chcesz kupic "))

            koszyk.dodaj_produkt(produkt,ilosc)
        else:
            print(f' Produktu nie ma w sklepie')

    elif (menu == 'U'):
        produkt = input(" Podaj nazwe produktu, ktory chcesz usunac ")
        ilosc = int(input(" Podaj ilosc produktu, ktory chcesz usunac "))

        koszyk.odejmij_produkt(produkt, ilosc)

    elif (menu == 'P'):
        for x in koszyk.zakupy:         # petla dla zakupow w koszyku
            # print(f" {koszyk.zakupy} ")
            print({x}, {koszyk.zakupy[x]})

    elif(menu=="K"):

        # for i in koszyk.zakupy:
        #     suma+=koszyk.zakupy[i]*sklep[i]
        #     razem+=suma
        #     print(f" {i}, {koszyk.zakupy[i]}, cena: {suma}  ")
        # print(f" Razem do zapłaty: {razem}")
        # break

        for i in koszyk.zakupy:
            suma += koszyk.zakupy[i] * sklep[i]

            print(f" {i} : {koszyk.zakupy[i]} : {sklep[i]} : {koszyk.zakupy[i]*sklep[i]}  ")
        print(f" Razem do zapłaty: {suma} zł")
        break

    else:
     print (f" Nierozpoznana opcja MENU ")

