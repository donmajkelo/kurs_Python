#
# krotka = (1,2,3)
#
# print(type(krotka))
# print(krotka)

zbior=set()

liczba=int(input(f" Podaj pierwsza liczbe:") )
zbior.add(liczba)
liczba=int(input(f" Podaj druga liczbe:") )
zbior.add(liczba)
liczba=int(input(f" Podaj trzecia liczbe:") )
zbior.add(liczba)
liczba=int(input(f" Podaj czwarta liczbe:") )
zbior.add(liczba)
liczba=int(input(f" Podaj piata liczbe:") )
zbior.add(liczba)

print(f" Podales {len(zbior)} unikatowych wartosci")
