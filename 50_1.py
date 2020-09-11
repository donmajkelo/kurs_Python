
print(f"Obliczamy srednia z podanych liczb")
x=0
suma=0
lista=[]
while(True):
    x=int(input(f"Podaj liczbe: "))
    if(x!=0):
        lista.append(x)
    if(x==0):
        for a in lista:
            suma=suma+a
        srednia=suma/len((lista))
        print(f"Koniec. srednia wynosi:) {srednia}")
        break
   