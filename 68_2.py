
lista_studentow=[]

class Student:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
        self.oceny=[]

    def dodaj_ocene(self,ocena):
        self.oceny.append(ocena)

    def wypisz_ocene(self):
        for i in self.oceny:
            print (f" Oceny to: {i} " )
        print()

    def policz_srednia(self):
        suma=0
        for o in self.oceny:
            suma += o

        srednia = suma/ len(self.oceny)
        print(f" Srednia {srednia}")

    def __str__(self):
        return f" Imie: {self.imie}, Nazwisko: {self.nazwisko}"

while(True):
   menu=input(" D -dodaj sudenta, u -usun studenta, L - lista studentow, O - dodaj ocene studentowi, w - wypisz ocene studenta, s -srednia ocen studenta, K- koniec,  P=pokaz").upper()
   if(menu=='D'):
        imie= input(" Podaj imie: ")
        nazwisko = input(" Podaj nazwisko: ")
        student1=Student(imie, nazwisko)
        lista_studentow.append(student1)

   elif (menu == 'L'):
          for x in lista_studentow:              # dajemy foreach    tutaj trafiaja obiekty z listy lista_studentow
            print(x)
   elif (menu == 'U'):
        nazwisko = input(" Podaj nazwisko studenta do usuniecia: ")
        for o in lista_studentow:            # na zmienną "o" trafiaja obiekty !!!
           if(o.nazwisko == nazwisko):     # wyszukujemy nazwisko z obiektu i porownujemy z podanym nazwiskiem
               lista_studentow.remove(o)
               break

   elif (menu == 'O'):
       nazwisko = input(" Podaj nazwisko studenta: ")
       ocena = int(input(" Podaj ocene: "))
       for x in lista_studentow:
            if(x.nazwisko==nazwisko):
                x.dodaj_ocene(ocena)
                print (f" Dodano {ocena} studentowi {nazwisko}")

   elif (menu == 'W'):
       nazwisko = input(" Podaj nazwisko studenta: ")
       for x in lista_studentow:
           if (x.nazwisko == nazwisko):
             x.wypisz_ocene()
            # print(f" Oceny studenta {nazwisko} to: {x.wypisz_ocene()}")

   elif (menu == 'S'):
       nazwisko = input(" Podaj nazwisko studenta: ")
       for x in lista_studentow:
           if (x.nazwisko == nazwisko):
             x.policz_srednia()

   elif (menu == 'K'):
     break
   else:
     print (f" Nierozpoznana opcja MENU ")


