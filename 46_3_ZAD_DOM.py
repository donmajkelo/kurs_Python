# GRA W KOLKO I KRZYZYK
# 8 MOZLIWYCH WYGRANYCH
# GDY POLE ZAJETE TO ZMIANA GRACZA
# JESLI WSZYSTKIE POLA ZAJETE TO GRA NIEROZSTRZYGNIETA I KONIEC GRY

gra=[["*","*","*"], ["*","*","*"], ["*","*","*"]]
gracz="O"

while(True):

    for i in gra:
        for j in i:                     # w tym przypadku i to jest lista
            print(j, end= " ")
        print()

    wsp= input(f" Gracz '{gracz}' Podaj wspolrzedne (wartosci X i Y) z zakrsu 0-2") #" np. 21
    x = int(wsp[0])
    y = int(wsp[1])

    if (gra[x][y] == "O" or gra[x][y]== "X"):  # STRATA KOLEJKI gdy pole jest zajete
        print(f" Tracisz kolejke bo pole jest zajete ")
    else:                                   # pole nie jest zajete wiec stawiamy znak 'X' lub 'O'
        print(f" OK. Dozwolony ruch ")
        gra[x][y] = gracz

    # 1 wariant
    if (gra[0][0] == gra[1][1] and gra[0][0] == gra[1][1] and gra[1][1] == gra[2][2] and gra[1][1] != "*"):
        for i in gra:
            for j in i:                     # w tym przypadku i to jest lista
                print(j, end= " ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
    # 2 wariant
    elif (gra[0][0] == gra[0][1] and gra[0][1] == gra[0][2] and gra[0][2] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
    # 3 wariant
    elif (gra[0][0] == gra[1][0] and gra[1][0] == gra[2][0] and gra[2][0] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
    # 4 wariant
    elif (gra[0][1] == gra[1][1] and gra[1][1] == gra[2][1] and gra[2][1] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
    # 5 wariant
    elif (gra[0][2] == gra[1][2] and gra[1][2] == gra[2][2] and gra[2][2] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
    # 6 wariant
    elif (gra[1][0] == gra[1][1] and gra[1][1] == gra[1][2] and gra[1][2] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
        # 7 wariant
    elif (gra[2][0] == gra[2][1] and gra[2][1] == gra[2][2] and gra[2][2] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
        # 8 wariant
    elif (gra[0][2] == gra[1][1] and gra[1][1] == gra[2][0] and gra[2][0] != "*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" Wygral zawodnik {gracz}")
        break
        # SPRAWDZAMY CZY WSZYSTKIE POLA SA ZAJETE - usprawnic algorytm sprawdzajacy!!!
    elif(gra[0][0]!="*" and gra[0][1]!="*" and gra[0][2]!="*" and gra[1][0]!="*" and gra[1][1]!="*" and gra[1][2]!="*" and gra[2][0]!="*" and gra[2][1]!="*" and gra[2][2]!="*"):  # if sprawdzajacy wygrana
        for i in gra:
            for j in i:  # w tym przypadku i to jest lista
                print(j, end=" ")
            print()
        print(f" GRA NIEROZSTRZYGNIETA")
        break

    if(gracz=="O" ):   # ZAMIANA GRACZY and gra[x][y]== "X"
        print(f" zmiana gracza ")
        gracz= "X"
    else:
        print(f" zmiana gracza ")
        gracz="O"