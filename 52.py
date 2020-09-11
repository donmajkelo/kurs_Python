
# lista = []


podstawa=int(input(" Podaj podstawe"))
wykladnik=int(input(" Podaj wykladnik"))
a=1

if(wykladnik>0):
    for i in range(wykladnik):
        a = a*podstawa
        if (i==wykladnik-1):
            print(f" Wynik: {a} ")
elif(wykladnik==0):
    print(f" 1")
#
# for wykladnik in range(wykladnik):
#     podstawa=podstawa
#
#
#
#
# for i in range(1,101):
#     lista.append(i)
#     print (lista[i-1])
#
# for i in range(1, 101,3):
#     print(lista[i-1])

    # z=lista[i%3]
    # print(z)
    # i f( i % 7= =0 and i!= 0):
    #     print(f" {i} to liczba podzielna przez 7")
