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
        self.kontakty=[]

    def dodajKontakt(self, imie, nazwisko):
        kont1 = Kontakt(imie, nazwisko)
        self.kontakty.append(kont1)
        print(" Dodano kontakt")

    def usunKontakt(self):
        pass

    def dodajTelefon(self):
        pass

    def usunTelefon(self):
        pass

    def wyswietlKontakty(self):
        pass


class App(KoontaktController):

    def __init__(self):
        super().__init__()
# tworzymy try na wypadek braku pliku
        try:
            f=open("86_3.dat", "rb")
            self.kontakty=pickle.load(f)
            f.close()
        except:
            f=open("86_3.dat", "wb")
            pickle.dump([], f)
            f.close()
        finally:
            f = open("86_3.dat", "rb")
            self.kontakty = pickle.load(f)
            f.close()

        self.menu()

    def menu(self):

        while(True):
            menu=input(" 1-Dodaj Kontakt, 2 - usun kontakt, 3 - Dodaj telefon, 4 - usun telefon, 5- wyswitl kontakty, 6 - koniec")

            if(menu==1):
                imie = input(" Podaj imie Kontaktu: ")
                nazwisko = input(" Podaj nazwisko Kontaktu: ")
                self.dodajKontakt(imie,nazwisko)
            elif (menu == 2):
                pass
            elif (menu == 3):
                pass
            elif (menu == 4):
                pass
            elif (menu == 5):
                pass
            elif (menu == 6):
                f = open("86_3.dat", "wb")
                pickle.dump(self.kontakty, f)
                f.close()
                break
            else:
                print (f" Nierozpoznana opcja menu")

ob=App()