# import pdb
# pdb.set_trace()

x = int(input("podaj liczbę 1"))
y = int(input("podaj liczbę 2"))
znak = input("Podaj znak działania")

if znak == "+":
    wynik = x + y
elif znak == "-":
    wynik = x - y
elif znak == "*":
    wynik = x * y
elif znak == "/":
    wynik = x / y

print(wynik)
