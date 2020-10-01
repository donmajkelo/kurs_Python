
class Student:
    def __init__(self, imie, nazwisko, grupa):
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__grupa=grupa

    def get_Imie(self):
        return self.__imie
    def get_Nazwisko(self):
        return self.__nazwisko
    def get_Grupa(self):
        return self.__grupa

    def set_Imie(self, imie):
        self.__imie=imie
    def set_Nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko
    def set_Grupa(self, grupa):
        self.__grupa=grupa

    def __str__(self):
        return f" Imie: {self.__imie} Nazwisko: {self.__nazwisko} Grupa: {self.__grupa}"

class StudentController:
    def __init__(self):
        self.lista_Studentow=[]

    def dodajStudenta(self, imie, nazwisko, grupa):
        student=Student(imie, nazwisko, grupa)
        self.lista_Studentow.append(student)
        print(" Dodano Studenta")

    def usunStudenta(self, nazwisko):
        znaleziono=False
        for i in self.lista_Studentow:
            if(i.get_Nazwisko()==nazwisko):
                self.lista_Studentow.remove(i)
                print(" Usunieto Studenta")
                znaleziono=True
        if(znaleziono==False):
            print(" Nie ma Studenta")

    def pokazStudenta(self, nazwisko):
        znaleziono=False
        for i in self.lista_Studentow:
            if(i.get_Nazwisko()==nazwisko):
                print(f" Dane studenta: {i}")
                znaleziono=True
        if(znaleziono==False):
            print(" Nie ma Studenta")

    def wszyscyStudenci(self):
        znaleziono=False
        for i in self.lista_Studentow:
            print(f" Dane studenta: {i} ")
            print("\n")
            znaleziono=True
        if(znaleziono==False):
            print(" Nie ma Studenta")


class Uczelnia(StudentController):
    def __init__(self, nazwa_uczelni):
        super().__init__()
        self.nazwa_uczelni=nazwa_uczelni
        self.menu()


    def menu(self):

        plik=open("dane_85.txt","a")

        while(True):

            menu=input("D-dodaj, U-usun, P-pokaz studenta, W- wszyscy studenci, Q-wyjscie").upper()

            if(menu=="D"):
                imie = input(" Podaj imie st. do dodania: ")
                nazwisko = input(" Podaj nazwisko do dodania: ")
                grupa = input(" Podaj grupe studenta: ")
                self.dodajStudenta(imie, nazwisko, grupa)

            elif (menu == "U"):
                nazwisko = input(" Podaj nazwisko do usuniecia: ")
                if(nazwisko!=""):
                    # for i in self.lista_Studentow:
                    #     if (i.get_Nazwisko == nazwisko):
                    self.usunStudenta(nazwisko)
                            # break
                else:
                    print(" Nie ma studenta w bazie!!! ")
            elif (menu == "P"):
                nazwisko = input(" Podaj nazwisko do wyswietlenia: ")
                self.pokazStudenta(nazwisko)
            elif (menu == "W"):
                self.wszyscyStudenci()
            elif (menu == "Q"):
                print(f" Koniec programu ")
                break
            else:
                print(f" Nierozpoznana opcja menu")

        for i in self.lista_Studentow:
            plik.write(str(i))
            plik.write("\n")


        plik.close()
ucz1=Uczelnia("WAT")



# lista=["aaaaaa\n", "ggggggggg\n", "zzzz\n"]
# plik=open("dane_zad_85.txt", "w", encoding="UTF-8")
# plik.writelines(lista)
# plik.close()
