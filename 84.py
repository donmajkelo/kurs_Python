

plik=open("nowy_zad_84.txt", "w")

print(" Podaj 5 imion")
for i in range(1,6):
    imie=input(f" Podaj imie nr {i} ")
    # plik.write(imie)
    # plik.write("\n")
    plik.write(f" {imie} \n")

plik.close()

plik=open("nowy_zad_84.txt", "a")

for i in range(1,101):
    plik.write(str(i))
    plik.write("\n")

plik.close()
