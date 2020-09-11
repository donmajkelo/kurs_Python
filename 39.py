

a=int(input("podaj 1 bok trojkata prostokatnego "))
b=int(input("podaj 2 bok trojkata prostokatnego "))
c=int(input("podaj 3 bok trojkata prostokatnego "))


if(((a**2+b**2)==c**2) or ((a**2+c**2)==b**2) or ((b**2+c**2)==a**2)):
    print("da sie utworzyc trojkata prostokatny")
else:
    print("nie da sie utworzyc trojkata prostokatny")