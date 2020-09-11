
lista = []

x = input (f" podaj liczbe nr 1: ")
lista.append(x)
x = input (f" podaj liczbe nr 2: ")
lista.append(x)
x = input (f" podaj liczbe nr 3: ")
lista.append(x)
x = input (f" podaj liczbe nr 4: ")
lista.append(x)
x = input (f" podaj liczbe nr 5: ")
lista.append(x)

print(f" LISTA TWOICH LICZB:  {lista}")

suma = int(lista[0])+int(lista[1])+int(lista[2])+int(lista[3])+int(lista[4])
srednia= int(suma)/len(lista)

print(f" SUMA:  {suma}")
print(f" srednia:  {srednia}")
