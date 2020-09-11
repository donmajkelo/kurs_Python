
x = float(input(" Podaj 1wszy bok prostokata "))
y = float(input(" Podaj 2gi bok prostokata "))
dzialanie = input(" Podaj co chcesz policzyc: [pole czy obwod] ")
# y  = float(input(" Podaj 2 liczbe "))

if(x<=0 or y<=0):
    print(f" Podaj liczbe dodatnia ")
elif((x>0 and y>0) and (dzialanie!="pole" and dzialanie!="obwod")):
    print(f" Podaj pole lub obwod i nie zartuj sobie")
elif((x>0 and y>0) and dzialanie=="pole"):
    pole1=x*y
    print(f" Pole rowne: {pole1}")
else:
    obwod1=x*2+y*2
    print(f" Obwod rowny: {obwod1}")

