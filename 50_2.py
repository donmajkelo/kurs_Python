
kontakty=[]

while (True):
    menu= input("D-dodaj, P-pokaz, U-usun, K-koniec").upper()

    if (menu == "D"):
        imie=input(" Podaj imie ")
        nazwisko = input(" Podaj nazwisko ")
        telefon = input(" Podaj telefon ")
        kontakty.append([imie,nazwisko,telefon])
    elif (menu == "P"):
        print(f" Ksiazka telefoniczna: {kontakty}")
        for x in kontakty:
            print(f" Imie: {x[0]}")
            print(f" Nazwisko: {x[1]}")
            print(f" Telefon: {x[2]}")
    elif (menu == "U"):
        nazwisko = input((f" Podaj nazwisko do usuniecia "))
        znaleziono=False
        for i, q  in enumerate(kontakty):
            if(q[1]==nazwisko):
                kontakty.pop(i)
                print(f" POMYSLNIE USUNIETO")
                znaleziono=True
        if (znaleziono== False):
            print(f" nazwiska nie ma w bazie")
    elif (menu == "K"):
        break
    else:
        print(f" Nierozpoznana opcja, sprobuj jeszcze raz")
