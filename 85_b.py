
def dodaj(imie, nazwisko,grupa):
    plik=open("85_b.txt", "a")
    plik.write(f" {imie}; {nazwisko} ; {grupa} \n")
    # plik.write(";")
    # plik.write(nazwisko)
    # plik.write(";")
    # plik.write(grupa)
    # plik.write("\n")
    plik.close()

def usun(nazwisko):
    pass

    znaleziono = False
    for i in lista_Studentow:
            lista_Studentow.remove(i)
            print(" Usunieto Studenta")
            znaleziono = True
    if (znaleziono == False):
        print(" Nie ma Studenta")


def pokaz():
   plik=open("85_b.txt", "r")
   lista=plik.readlines()  # konwersja danych z pliku do listy  wtedy otrzymamy listę
   for i in lista:
       daneList=i.split(";")
       print(f" Imie: {daneList[0]} Nazwisko: {daneList[1]} Nr Indeksu: {daneList[2].strip()}")
   plik.close()

listaStudentow=[]

while(True):
    menu=input("D-dodaj, U-usun, P-pokaz studenta, Q-wyjscie").upper()
    if(menu=="D"):
        imie = input(" Podaj imie st. do dodania: ")
        nazwisko = input(" Podaj nazwisko do dodania: ")
        grupa = input(" Podaj grupe studenta: ")
        dodaj(imie, nazwisko, grupa)
    elif (menu == "U"):
        nazwisko = input(" Podaj nazwisko do usuniecia: ")
        if(nazwisko!=""):
            usun(nazwisko)
        else:
            print(" Nie ma studenta w bazie!!! ")
    elif (menu == "P"):
        # nazwisko = input(" Podaj nazwisko do wyswietlenia: ")
        pokaz()
    elif (menu == "Q"):
        print(f" Koniec programu ")
        break
    else:
        print(f" Nierozpoznana opcja menu")

#
#
#     def dodajStudenta(self, imie, nazwisko, grupa):
#         student=Student(imie, nazwisko, grupa)
#         self.lista_Studentow.append(student)
#         print(" Dodano Studenta")
#
#     def usunStudenta(self, nazwisko):
#         znaleziono=False
#         for i in self.lista_Studentow:
#             if(i.get_Nazwisko()==nazwisko):
#                 self.lista_Studentow.remove(i)
#                 print(" Usunieto Studenta")
#                 znaleziono=True
#         if(znaleziono==False):
#             print(" Nie ma Studenta")
#
#     def pokazStudenta(self, nazwisko):
#         znaleziono=False
#         for i in self.lista_Studentow:
#             if(i.get_Nazwisko()==nazwisko):
#                 print(f" Dane studenta: {i}")
#                 znaleziono=True
#         if(znaleziono==False):
#             print(" Nie ma Studenta")
#
#     def wszyscyStudenci(self):
#         znaleziono=False
#         for i in self.lista_Studentow:
#             print(f" Dane studenta: {i} ")
#             print("\n")
#             znaleziono=True
#         if(znaleziono==False):
#             print(" Nie ma Studenta")
#
#
# class Uczelnia(StudentController):
#     def __init__(self, nazwa_uczelni):
#         super().__init__()
#         self.nazwa_uczelni=nazwa_uczelni
#         self.menu()
#
#
#     def menu(self):
#
#         plik=open("dane_85.txt","r")
#
#         self.lista_Studentow = readli
#
#         while(True):
#
#             menu=input("D-dodaj, U-usun, P-pokaz studenta, W- wszyscy studenci, Q-wyjscie").upper()
#
#             if(menu=="D"):
#                 imie = input(" Podaj imie st. do dodania: ")
#                 nazwisko = input(" Podaj nazwisko do dodania: ")
#                 grupa = input(" Podaj grupe studenta: ")
#                 self.dodajStudenta(imie, nazwisko, grupa)
#
#             elif (menu == "U"):
#                 nazwisko = input(" Podaj nazwisko do usuniecia: ")
#                 if(nazwisko!=""):
#                     # for i in self.lista_Studentow:
#                     #     if (i.get_Nazwisko == nazwisko):
#                     self.usunStudenta(nazwisko)
#                             # break
#                 else:
#                     print(" Nie ma studenta w bazie!!! ")
#             elif (menu == "P"):
#                 nazwisko = input(" Podaj nazwisko do wyswietlenia: ")
#                 self.pokazStudenta(nazwisko)
#             elif (menu == "W"):
#                 self.wszyscyStudenci()
#             elif (menu == "Q"):
#                 print(f" Koniec programu ")
#                 break
#             else:
#                 print(f" Nierozpoznana opcja menu")
#
#         for i in self.lista_Studentow:
#             plik.write(str(i))
#             plik.write("\n")
#
#
#         plik.close()
# ucz1=Uczelnia("WAT")
#
#
#
# # lista=["aaaaaa\n", "ggggggggg\n", "zzzz\n"]
# # plik=open("dane_zad_85.txt", "w", encoding="UTF-8")
# # plik.writelines(lista)
# # plik.close()
