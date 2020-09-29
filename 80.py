
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa=nazwa
        self.cena=cena

    def __str__(self):
        return f" Nazwa: {self.nazwa}, Cena: {self.cena}"

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        self.jezyk = jezyk
        self.system = system
        super().__init__(nazwa, cena)       #  wysyla do klasy Produkt: nazwa, cena bo sam uzywa jezyk, system

    def __str__(self):
        return f" Nazwa: {self.nazwa}, Cena: {self.cena}, jezyk: {self.jezyk}, system: {self.system}"

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        self.termin = termin
        super().__init__(nazwa, cena, jezyk, system)   #  wysyla do klasy Opogrm.: nazwa, cena, jezyk, system, bo sam tego nie potrzebuje

    def __str__(self):
        return f" {self.nazwa}, {self.cena}, {self.jezyk}, {self.system}, {self.termin}"

k1=Szkolenia("Szkol. PYTHON", 100, "Python", "Windows", "2020-11-19" )
print(k1)

o1=Oprogramowanie("Szkol. PYTHON", 100, "Python", "Windows")
print(o1)

p1=Produkt("Szkol. PYTHON", 100)
print(p1)
