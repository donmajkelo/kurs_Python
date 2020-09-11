# PROGRAM - LOSOWANIE DWÓCH LICZB I ICH MNOŻENIE

import random

# losujemy 2 liczby z zakresu 1-10
los1=random.randint(1,10)
los2=random.randint(1,10)

print(f" PIERWSZA LICZBA: {los1}")
print(f" DRUGA LICZBA: {los2}")

wynik = los1*los2

troj_a = int(input (f" Jak myslisz chlopcze, jaki bedzie wynik iloczynu tych liczb? {los1} i {los2} "))

print(f" Twoja odpowiedz TO: {troj_a}")
print(f" POPRAWNY WYNIK TO: {wynik}")