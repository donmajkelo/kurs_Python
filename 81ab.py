
class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__kontrakt=kontrakt
        self.__pensja=pensja

    def get_Imie(self):
        return self.__imie
    def get_Nazwisko(self):
        return self.__nazwisko
    def get_Kontrakt(self):
        return self.__kontrakt
    def get_Pensja(self):
        return self.__pensja
    def set_Imie(self, imie):
        self.__imie=imie
    def set_Nazwisko(self, nazwisko):
        self.__nazwisko=nazwisko
    def set_Kontrakt(self, kontrakt):
        self.__kontrakt=kontrakt
    def set_Pensja(self, pensja):
        self.__pensja=pensja

    def __str__(self):
        return f"Imie: {self.get_Imie()} Nazwisko: {self.get_Nazwisko()} Kontrakt: {self.get_Kontrakt()} Pensja: {self.get_Pensja()}"


class PracownikController:           # to jest dział kadr , nie tworzymy tu obiektow - nie kazda klasa sluzy do budowania obiektow

    def __init__(self):
        self.lista_Pracownikow=[]
        # lista_Pracownikow = []

    def dodajPracownika(self, imie, nazwisko, etat="staz", pensja=1000):
        pracownik=Pracownik(imie, nazwisko, etat, pensja)
        self.lista_Pracownikow.append(pracownik)
        print(" Dodano pracownika")


    def pokazPracownika(self):
        for i in self.lista_Pracownikow:
            print(i)

    def usunPracownika(self, nazwisko):
        znaleziono= False  # zmienna flagowa
        for i in self.lista_Pracownikow:
            if(i.get_Nazwisko()==nazwisko):
                self.lista_Pracownikow.remove(i)
                print(" usunieto pracownika")
                znaleziono= True
                break
        if(znaleziono== False):
            print(" Pracownik nie został znaleziony ")

    def zmianaKontrakt(self, nazwisko, pensja):
        znaleziono = False  # zmienna flagowa
        for i in self.lista_Pracownikow:
            if (i.get_Nazwisko() == nazwisko):
                i.set_Kontrakt("etat")
                i.set_Pensja(pensja)
                print(" uaktualniono kontrakt pracownika")
                znaleziono = True
        if (znaleziono == False):
            print(" Pracownik nie został znaleziony ")

    def modyfikujPracownika(self, nowe_Imie, nowe_Nazwisko, nazwisko):
        znaleziono = False  # zmienna flagowa
        for i in self.lista_Pracownikow:
            if (i.get_Nazwisko() == nazwisko):
                # i.remove(get_Nazwisko())
                i.set_Imie(nowe_Imie)
                i.set_Nazwisko(nowe_Nazwisko)
                print(" zmodyfikowano dane pracownika")
                znaleziono = True
        if (znaleziono == False):
            print(" Pracownik nie został znaleziony ")

    def szukaj(self, szukana):
        for i in self.lista_Pracownikow:
            if(i.get_Imie().find(szukana) >= 0 or i.get_Nazwisko().find(szukana) >= 0 ):
                print(i)



class Firma(PracownikController):

    def __init__(self, nazwa_Firmy):
        super().__init__()
        self.nazwa_Firmy=nazwa_Firmy
        self.menu()

    def menu(self):

        while(True):
            print(f" Witaj w firmie {self.nazwa_Firmy}")
            menu=input("D-dodaj pracownika, P-pokaz pracowanika, U- usun pracownika, M-modyfikuj, W-wyszukaj, Z- zmien kontrakt pracowanika").upper()

            if(menu=="D"):
                imie=input(" Podaj imie: ")
                nazwisko=input(" Podaj nazwisko: ")
                etat=input(" Kogo dodajemy E-etat czy S-staz").upper()

                if(etat=="E"):
                    etat = "etat"
                    pensja=int(input("Podaj wysokosc wynagrodzenia"))
                    self.dodajPracownika(imie, nazwisko, etat, pensja)
                elif(etat=="S"):
                    self.dodajPracownika(imie, nazwisko)
            elif(menu=="P"):
                self.pokazPracownika()
            elif(menu=="Z"):
                nazwisko = input(" Podaj nazwisko: ")
                pensja = int(input(" Podaj nowa pensje: "))
                # if (nazwisko != ""):
                self.zmianaKontrakt(nazwisko, pensja)

            elif(menu=="U"):
                nazwisko = input(" Podaj nazwisko: ")
                if(nazwisko!=""):
                    self.usunPracownika(nazwisko)
            elif (menu == "M"):
                nazwisko = input(" Podaj nazwisko do modyfikacji: ")
                nowe_Imie=input(" Podaj nowe imie ")
                nowe_Nazwisko=input(" Podaj nowe nazwisko: ")
                if (nazwisko != ""):
                    self.modyfikujPracownika(nowe_Imie, nowe_Nazwisko, nazwisko)
            elif (menu == "W"):
                szukana = input(" Podaj wartosc szukana: ")
                self.szukaj(szukana)
                # if (nazwisko != ""):
                #     self.usunPracownika(nazwisko)
            elif (menu == "K"):
                print(f" Koniec programu ")
                break
            else:
                print(f" Nierozpoznana opcja menu")

ob1=Firma("Zenek")
# ob1=Pracownik("Zenek",  "Gluch", "staz", 1788)



