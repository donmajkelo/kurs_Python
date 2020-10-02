import pickle

class Kontakt:

    def __init__(self, imie, nazwisko,):
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__telefon=[]

    def get_Imie(self):
        return self.__imie

    def get_Nazwisko(self):
        return self.__nazwisko

    def get_Telefon(self):
        return self.__telefon

    def set_Imie(self, imie):
        self.__imie=imie

    def set_Nazwisko(self, nazwisko):
        self.__nazwisko=nazwisko

    def set_Telefon(self, telefon):
        self.__telefon.append(telefon)

class KoontaktController:

    def __init__(self):
        self.listakontakty=[]

    def dodajKontakt(self, imie, nazwisko):
        kont1 = Kontakt(imie, nazwisko)
        self.listakontakty.append(kont1)
        print(" Dodano kontakt")

    def usunKontakt(self,nazwisko):
        znaleziono = False
        for i in self.listakontakty:
            if (i.get_Nazwisko() == nazwisko):
                self.listakontakty.remove(i)
                print(" Usunieto kontakt")
                znaleziono = True
                break
        if (znaleziono == False):
            print(" Kontakt o tym nzwisku nie istnieje")

    def dodajTelefon(self, nazwisko, telefon):
        znaleziono=False
        for i in self.listakontakty:
            if(i.get_Nazwisko()==nazwisko):
                i.set_Telefon(telefon)
                znaleziono=True
                break
        if(znaleziono==False):
            print(" Kontakt o tym nzwisku nie istnieje")

    def usunTelefon(self):
        pass

    def wyswietlKontakty(self):

        for i in self.listakontakty:
            print(f" Imie: {i.get_Imie()} Nazwisko: {i.get_Nazwisko()}")
            for j in i.get_Telefon():
                print(f" Tel: {j}")
        # if (self.listakontakty: == 0):
        #     print(" Brak kontaktow ")

class App(KoontaktController):

    def __init__(self):
        super().__init__()
# tworzymy try na wypadek braku pliku
        try:
            f=open("86_3.dat", "rb")
            self.ListaKontakty=pickle.load(f)
            f.close()
        except:
            f=open("86_3.dat", "wb")
            pickle.dump([], f)
            f.close()
        finally:
            f = open("86_3.dat", "rb")
            self.ListaKontakty = pickle.load(f)
            f.close()

        self.menu()

    def menu(self):

        while(True):
            menu=input(" 1-Dodaj Kontakt, 2 - usun kontakt, 3 - Dodaj telefon, 4 - usun telefon, 5- wyswitl kontakty, 6 - koniec")

            if(menu=="1"):
                imie = input(" Podaj imie Kontaktu: ")
                nazwisko = input(" Podaj nazwisko Kontaktu: ")
                self.dodajKontakt(imie,nazwisko)
            elif (menu == "2"):
                nazwisko = input(" Podaj nazwisko do usuniecia kontaktu: ")
                self.usunKontakt(nazwisko)
            elif (menu == "3"):
                nazwisko = input(" Podaj nazwisko Kontaktu: ")
                telefon=input(" Podaj nr telefonu: ")
                self.dodajTelefon(nazwisko, telefon)
            elif (menu == "4"):
                nazwisko = input(" Podaj nazwisko do usuniecia kontaktu: ")
                telefon = input(" Podaj nr telefonu do usuniecia: ")
                self.usunKontakt(nazwisko)
            elif (menu == "5"):
                self.wyswietlKontakty()
            elif (menu == "6"):
                f = open("86_3.dat", "wb")
                pickle.dump(self.ListaKontakty, f)
                f.close()
                break
            else:
                print (f" Nierozpoznana opcja menu")

ob=App()