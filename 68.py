
class Zawodnik:
    def __init__(self, imie, wzrost, waga):
        self.imie=imie
        self.wzrost=wzrost
        self.waga=waga

    # def bmi (self):
    #     wynik  = round(self.waga / self.wzrost ** 2, 2)
    #     # wynik  = self.waga / self.wzrost ** 2
    #     print(wynik)
    #
    # def przedstaw_sie (self):
    #     print (f" Mam na imie: {self.imie} ")



    def bmi (self):
        wynik  = round(self.waga / self.wzrost ** 2, 2)
        return wynik

    def przedstaw_sie (self):
        print (f" Mam na imie: {self.imie} i mam BMI: {self.bmi()} ")



    # def __str__(self):
    #     return f" {self.imie} {self.wzrost} {self.waga}. {self.bmi()}"

obj1=Zawodnik("Michal", 1.82, 83)
obj2=Zawodnik("Adam", 1.60, 100)
obj3=Zawodnik("Jurek", 1.60, 10)

obj1.bmi()
obj2.bmi()
obj3.bmi()

obj1.przedstaw_sie()
obj2.przedstaw_sie()
obj3.przedstaw_sie()


# bmi=round(x/y**2,2)
#
# if (bmi <= 24.9 and bmi >= 18.5 ):
#     print(f" Wartosc BMI: {bmi} oznacza wage prawidlowa!!! ")
# elif(bmi > 24.9):
#     print(f" Wartosc BMI: {bmi} oznacza NADWAGE :(  ")
# else:
#     print(f" Wartosc BMI: {bmi} - idz sie najedz chlopaku!!!  ")




