
# imie= ["Mike", "Zdzich", "Rysio"]
#
# def przywitajSie(imie):
#     for i in range(10):
#         print(f"Hello {imie}")
#
# for i in range(len(imie)):
#     przywitajSie(imie[i])
# #
# def suma(liczba1, liczba2, liczba3, liczba4):
#     wynik=liczba1+liczba2+liczba3+liczba4
#     print(wynik)
#
# suma(2,34,23,42)

def szymon(liczba1, liczba2=0, liczba3=0, liczba4=0):
    wynik=liczba1+liczba2+liczba3+liczba4
    print(wynik)

# suma(2,34,23,42)
def bartek(liczba1, liczba2=0, liczba3=0, liczba4=0):
    wynik=liczba1+liczba2+liczba3+liczba4
    return wynik

x=bartek(3,18)
y=szymon(3,8)
print(x)
print(y)