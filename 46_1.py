

x=int(input("Podaj pierwsza liczbe  "))
y=int(input("Podaj druga liczbe "))
z=int(input("Podaj trzecia liczbe "))

if (x > y ):
    if(x > z):
        print(f" Najwieksza liczba to: {x}")
    else:
        print(f" Najwieksza liczba to: {z}")
elif(y>z):
    print(f" Najwieksza liczba to: {y}")
else:
    print(f" Najwieksza liczba to: {z}")

