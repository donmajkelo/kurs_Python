# import pdb
# pdb.set_trace()

def oblicz(x, y, znak):
    if znak == "+":
        wynik = x + y
    elif znak == "-":
        wynik = x - y
    elif znak == "*":
        wynik = x * y
    elif znak == "/":
        wynik = x / y

    return wynik

x = int(input("podaj liczbę 1"))
y = int(input("podaj liczbę 2"))
znak = input("Podaj znak działania")

print(oblicz(x, y, znak))
