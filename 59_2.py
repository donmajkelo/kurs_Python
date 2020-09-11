import random
los=random.randint(1,100)

print(f"Gramy w gre: Zgadnij liczbe w 5 probach ")

x = 0
suma = 0
lista = []
while (True):
    x = int(input(f"Podaj liczbe: "))
    lista.append(x)
    if(len(lista)==5):
        print(f" Przegrales, za duzo prob ")
        break
    if (los == x):
        print(f"Brawo!!!, Zgadles ")
        break
    elif (los > x):
        print(f"Za mało. podqaj wieksza liczbe ")
    elif (los < x):
        print(f"Za duzo. podqaj mniejsza liczbe ")


