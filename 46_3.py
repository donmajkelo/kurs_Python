

gra=[["*","*","*"], ["*","*","*"], ["*","*","*"]]
gracz="O"

while(True):

    for i in gra:
    # print(i)
        for j in i:                     # w tym przypadku i to jest lista
            print(j, end= " ")
        print()

    wsp= input(f" Gracz '{gracz} Podaj wspolrzedne (wartosci X i Y) ") #" np. 21
    x = int(wsp[0])
    y = int(wsp[1])
    gra[x][y]= gracz
    if (gra[0][0] == gra[1][1] and gra[0][0] == gra[1][1] and gra[1][1] != "*"):                 # if sprawdzajacy wygrana
        print(f" Wygral zawodnik {gracz}")
        break
    if(gracz=="O"):   # ZAMIANA GRACZY
        gracz= "X"
    else:
        gracz="O"



#
#
# for i in range(len(dane)):
#     dane[i][i]=1
#     x=len(dane)
#     dane[x-i-1][i]=1
#
# for i in range(len(dane)):
#     for j in range(len(dane[i])):
#         print(dane[i][j], end= " ")
#
#     print()