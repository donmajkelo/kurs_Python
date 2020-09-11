

x=int(input("Podaj pierwsza liczbe  "))
y=int(input("Podaj druga liczbe "))
z=int(input("Podaj trzecia liczbe "))

if (x < y ):
    if(x < z):
        print(f" {x}")
        if(y<z):
            print(f" {y}")
            print(f" {z}")
        else:
            print(f" {z}")
            print(f" {y}")
    elif(z<y):
        print(f" {z}")
        print(f" {x}")
        print(f" {y}")
elif(y<z):
    print(f" {y}")
    if(x<z):
        print(f" {x}")
        print(f" {z}")
    else:
        print(f" {z}")
        print(f" {x}")
else:
    print(f" {z}")
    print(f" {y}")
    print(f" {x}")


