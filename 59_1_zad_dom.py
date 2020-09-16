
def dzialanie():
    lista2 = []
    for i in range(10):
        import random
        x= random.randint(1,10)
        y= random.randint(1,10)
        lista = ["*", "+", "-"]
        indeks=random.randint(0,2)
        print(f" Ile to jest: {x} {lista[indeks]} {y}")

        if(indeks==0):
            z=x*y
        elif (indeks == 1):
            z = x + y
        elif (indeks == 2):
            z = x - y

        wynik1 = int(input("Podaj wynik "))
        if (z == wynik1):
            print(f" wartosc prawidlowa")
            lista2.append("1")
        else:
            print(f" wartosc bledna")
            lista2.append("0")

    print(f" ----- STATYSTYKA -----  ")
    print(f" Ilosc prawidlowych odpowiedzi: {lista2.count('1')}")
    print(f" Ilosc blednych odpowiedzi: {lista2.count('0')}")

dzialanie()
