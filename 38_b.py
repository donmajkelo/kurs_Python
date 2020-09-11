

x=int(input("Podaj pierwsza liczbe  "))
y=int(input("Podaj druga liczbe "))
z=int(input("Podaj trzecia liczbe "))

if (x < y and x < z ):
    if(x < z):
        print(f" {x}, {y}, {z}")
    else:
        print(f" {x}, {z}, {y}")
if (y < x and y < z):
    if (x < z):
        print(f" {y}, {x}, {z}")
    else:
        print(f" {y}, {z}, {x}")
if (z < x and z < y):
    if (x < y):
        print(f" {z}, {x}, {y}")
    else:
        print(f" {z}, {y}, {x}")


