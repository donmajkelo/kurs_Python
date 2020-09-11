

x=float(input("Podaj wage  "))
y=float(input("Podaj wzrost "))

bmi=round(x/y**2,2)

if (bmi <= 24.9 and bmi >= 18.5 ):
    print(f" Wartosc BMI: {bmi} oznacza wage prawidlowa!!! ")
elif(bmi > 24.9):
    print(f" Wartosc BMI: {bmi} oznacza NADWAGE :(  ")
else:
    print(f" Wartosc BMI: {bmi} - idz sie najedz chlopaku!!!  ")



