

tekst = input("Podaj ciag znakow:")
a = len(tekst)
print(f" Znakow jest: {a}")

# ilosc spacji
b = tekst.count(" ")
print(f" Licza spacji (I): {b}")

c = tekst.replace(" ", "")
print(f" Licza spacji (II): {a-len(c)}")


# print(napis.capitalize())
# print(napis.count("o"))
# print(napis.upper())
# print(napis.replace("o", "x"))
# print("eo" in napis)
# print(len(napis))