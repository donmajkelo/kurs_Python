
pracownicy=[]

class Pracownik:

    def __init__(self, imie, nazwisko, email, telefon):
        self.imie=imie
        self.nazwisko=nazwisko
        self.email=email
        self.telefon=telefon

    def __str__(self):
        return f" Imie: {self.imie}, Nazwisko: {self.nazwisko}, email: {self.email}, telefon: {self.telefon}"

while(True):
    menu=input(" D -dodaj, P=pokaz, U- usun, Z - Zmiana, K- Koniec").upper()
    if(menu=='D'):
        imie= input(" Podaj imie: ")
        nazwisko = input(" Podaj nazwisko: ")
        email = input(" Podaj email: ")
        telefon = input(" Podaj telefon: ")
        pracownik=Pracownik(imie, nazwisko, email, telefon)
        pracownicy.append(pracownik)

    elif (menu == 'P'):
          for x in pracownicy:              # dajemy foreach    tutaj trafiaja obiekty z listy pracownicy
            print(x)
    elif (menu == 'U'):
        nazwisko = input(" Podaj nazwisko pracownika do usuniecia: ")
        for o in pracownicy:            # na zmienną "o" trafiaja obiekty !!!
            if(o.nazwisko == nazwisko):     # wyszukujemy nazwisko z obiektu i porownujemy z podanym nazwiskiem
                pracownicy.remove(o)
                break
        # pracownicy.remove(pracownicy[nazwisko])
    elif (menu == 'Z'):
        nazwisko = input(" Podaj nazwisko w ktory dokonamy zmian: ")

        if(nazwisko==""):
            print (f" Nie podales zadnego nazwiska ")
        else:
            nowe_imie = input(" Podaj nowe imie: ")
            nowe_nazwisko = input(" Podaj nowe nazwisko: ")
            nowy_email = input(" Podaj nowy email: ")
            nowy_telefon = input(" Podaj nowy telefon: ")

            for n in pracownicy:
                if (n.nazwisko == nazwisko):

                    if (nowe_imie!=""):
                        n.imie=nowe_imie
                    if (nowe_nazwisko != ""):
                        n.nazwisko = nowe_nazwisko
                    if (nowy_email != ""):
                        n.email = nowy_email
                    if (nowy_telefon != ""):
                        n.telefon = nowy_telefon
                    break

    elif (menu == 'K'):
        break
    else:
        print (f" Nierozpoznana opcja MENU ")








