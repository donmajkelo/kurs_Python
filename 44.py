
x = float(input(" Podaj 1 liczbe "))
dzialanie = input(" Podaj dzialanie z nastepujacych: [*  +  -  /] ")
y  = float(input(" Podaj 2 liczbe "))

if(dzialanie=="*"):
    z=x*y
    print(f" wynik to: {z} ")
elif(dzialanie=="/"):
    if (y == 0):
        print(" nie dziel przez 0")
    else:
        z = x / y
        print(f" wynik to: {z} ")
elif(dzialanie=="+"):
    z = x + y
    print(f" wynik to: {z} ")
elif(dzialanie=="-"):
    z = x -y
    print(f" wynik to: {z} ")