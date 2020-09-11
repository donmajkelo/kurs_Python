
sklep = {"chleb":1.99, "mleko":2.50, "cukierki":12.99 }

x=input("Podaj ile chlebów chcesz kupić? ")
y=input("Podaj ile mleka chcesz kupić? ")
z=input("Podaj ile cukierkow chcesz kupić? ")

sumaChleba = int(x)*sklep["chleb"]
sumaMleka = int(y)*sklep["mleko"]
sumaCukierkow = int(z)*sklep["cukierki"]

calosc = sumaChleba+sumaMleka+sumaCukierkow


print(f" Razem do zaplaty: {calosc}  zł ")
# print(zamiana[x])
