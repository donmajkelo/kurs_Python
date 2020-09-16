
def dzialanie():
    print(f" Prosze odowiedziec na 5 pytan z mnozenia dwoch liczb")
    for i in range(5):
        import random
        x= random.randint(1,10)
        y= random.randint(1,10)
        print(f" Jaki jest wynik iloczynu dwóch liczb: {x} i {y}")
        z = x * y

        wynik1 = int(input("Podaj wynik "))
        if (z == wynik1):
            print(f" Wartosc prawidlowa. Gratulacje")
        else:
            while(z != wynik1):
                wynik1 = int(input(f" wartosc bledna. Sproboj jeszcze raz: "))

dzialanie()
