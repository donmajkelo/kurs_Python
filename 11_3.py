
sklep = {"chleb":1.99, "mleko":2.50, "cukierki":12.99 }

x=input("Co chcesz kupic? ")
zmienna = x
y=input(f"Ile {zmienna} chcesz kupic ")

# z=input("Podaj ile cukierkow chcesz kupić? ")

calosc = sklep[x] * int(y)

print(f" Razem do zaplaty: {calosc}  zł ")
# print(zamiana[x])
