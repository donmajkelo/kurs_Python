
def dodaj(imie, nazwisko,grupa):
    plik=open("85_c.txt", "a")
    plik.write(f" {imie}; {nazwisko} ; {grupa} \n")
    plik.close()

def usun(nazwisko):
    plik = open("85_c.txt", "r")
    listaStudentow = plik.readlines()  # konwersja danych z pliku do listy  wtedy otrzymamy listę
    plik.close()

    for i in listaStudentow:
        student=i.split(";")
        if (student[1].strip() == nazwisko):
            listaStudentow.remove(i)
            print(f" Usunieto studenta: {student[1]}")
            break
    plik = open("85_c.txt", "w")
    plik.writelines(listaStudentow)
    plik.close()

def pokaz():
   plik=open("85_c.txt", "r")
   lista=plik.readlines()  # konwersja danych z pliku do listy  wtedy otrzymamy listę
   for i in lista:
       daneList=i.split(";")
       print(f" Imie: {daneList[0]} Nazwisko: {daneList[1]} Nr Indeksu: {daneList[2].strip()}")
   plik.close()

def zmiana(nazwisko, nowe_Imie,nowe_Nazwisko):
    plik = open("85_c.txt", "r")
    listaStudentow = plik.readlines()  # konwersja danych z pliku do listy  wtedy otrzymamy listę
    plik.close()
    for i,v in enumerate(listaStudentow):
        student=v.split(";")
        if (student[1].strip() == nazwisko):
            if(nowe_Imie!=""):
                student[0]=nowe_Imie
            if (nowe_Nazwisko != ""):
                student[1] = nowe_Nazwisko
            listaStudentow[i]= f" {student[0]}; {student[1]}; {student[2]}"
            break
            # student[0]=nowe_Imie
            # student[1]=nowe_Nazwisko
            # listaStudentow.remove(i)
            # print(f" dokonano zmiany danych studenta: {student[1]}")
            # for i in listaStudentow:
            #     print(i)

            break
    plik = open("85_c.txt", "w")
    plik.writelines(listaStudentow)
    plik.close()






# listaStudentow=[]

while(True):
    menu=input("D-dodaj, U-usun, P-pokaz studenta, Z- zimiana, Q-wyjscie").upper()
    if(menu=="D"):
        imie = input(" Podaj imie st. do dodania: ")
        nazwisko = input(" Podaj nazwisko do dodania: ")
        grupa = input(" Podaj grupe studenta: ")
        dodaj(imie, nazwisko, grupa)
    elif (menu == "U"):
        nazwisko = input(" Podaj nazwisko do usuniecia: ")
        if(nazwisko!=""):
              usun(nazwisko)
        else:
            print(" Nie ma studenta w bazie!!! ")
    elif (menu == "P"):
        # nazwisko = input(" Podaj nazwisko do wyswietlenia: ")
        pokaz()
    elif (menu == "Z"):
        nazwisko = input(" Podaj nazwisko do zmiany: ")
        nowe_Imie = input(" Podaj nowe imie : ")
        nowe_Nazwisko = input(" Podaj nowe nazwisko : ")
        zmiana(nazwisko, nowe_Imie,nowe_Nazwisko)
    elif (menu == "Q"):
        print(f" Koniec programu ")
        break
    else:
        print(f" Nierozpoznana opcja menu")
