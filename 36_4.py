import random

x= random.randint(1,9)
y= random.randint(1,9)
lista = ["*", "+", "-"]
indeks=random.randint(0,2)


print(f" Jaki bedzie rezultat dzialania {x} {lista[indeks]} {y}")

if(indeks==0):
    z=x*y
elif (indeks == 1):
    z = x + y
elif (indeks == 2):
    z = x - y

wynik1 = int(input("podaj wynik "))
if (z == wynik1):
    print(f" wartosc prawidlowa")
else:
    print(f" wartosc bledna")



# if(indeks==0):
#     print(f" Podaj wynik {x} {lista[0]} {y}")
#     z=x*y
#     wynik1=int(input("podaj wynik"))
#     if(z==wynik1):
#         print(f" wartosc prawidlowa")
#     else:
#         print(f" wartosc bledna")
# elif (indeks == 1):
#     print(f" Podaj wynik {x} {lista[1]} {y}")
#     z = x + y
#     wynik1 = int(input("podaj wynik"))
#     if (z == wynik1):
#         print(f" wartosc prawidlowa")
#     else:
#         print(f" wartosc bledna")
# elif (indeks == 2):
#     print(f" Podaj wynik {x} {lista[2]} {y}")
#     z = x - y
#     wynik1 = int(input("podaj wynik"))
#     if (z == wynik1):
#         print(f" wartosc prawidlowa")
#     else:
#         print(f" wartosc bledna")




        #
        #
        # {y})

#
#
# x = float(input(" Podaj 1wszy bok prostokata "))
# y = float(input(" Podaj 2gi bok prostokata "))
# dzialanie = input(" Podaj co chcesz policzyc: [pole czy obwod] ")
# # y  = float(input(" Podaj 2 liczbe "))
#
# if(x<=0 or y<=0):
#     print(f" Podaj liczbe dodatnia ")
# elif((x>0 and y>0) and (dzialanie!="pole" and dzialanie!="obwod")):
#     print(f" Podaj pole lub obwod i nie zartuj sobie")
# elif((x>0 and y>0) and dzialanie=="pole"):
#     pole1=x*y
#     print(f" Pole rowne: {pole1}")
# else:
#     obwod1=x*2+y*2
#     print(f" Obwod rowny: {obwod1}")

