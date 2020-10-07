
from tkinter import *   #importujemy biblioteke

root = Tk()

root.wm_title(" Ksiazka telefoniczna")
root.geometry("700x300")

#  dzialanie kodu:


kontakty=[]

def dodajKontakt():
    imie= text1_Imie.get()
    nazwisko=text2_Nazwisko.get()
    telefon=text3_telefon.get()
    email=text4_Email.get()
    print(imie, nazwisko, telefon, email)

    dane=[imie, nazwisko, telefon, email]
    kontakty.append(dane)
    text1_Imie.delete(0,END)                     # czyscimy pola od poczatku -0 do konca - end
    text2_Nazwisko.delete(0, END)
    text3_telefon.delete(0, END)
    text4_Email.delete(0, END)
    text1_Imie.focus()             # USTAW KURSOR MRUGAJACY NA POLE text1_Imie

    print(kontakty)
    listaKontakt()   #aby ta funkcja na nowo sie wywolywalo

def listaKontakt():
    listabox_listaKontakow.delete(0,END)                   # czysli liste kontaktow
    for index, value in enumerate(kontakty):
        listabox_listaKontakow.insert(index, value[0]+" "+ value[1])    # WYSWIETLA DANE W LISCIE LOKTAKTOW w lewej ramce


def SzczegolyKontaktu():
    index = listabox_listaKontakow.index(ACTIVE)   # Pobranie aktywnego (zaznaczonego pola - indeksu)
    print(index)
    imie= kontakty[index][0]
    nazwisko = kontakty[index][1]
    telefon = kontakty[index][2]
    email = kontakty[index][3]
    label6_Imie_wyswietl.config(text=imie)
    label7_Nazwisko_wyswietl.config(text=nazwisko)
    label8_telefon_wyswietl.config(text=telefon)
    label9_Email_wyswietl.config(text=email)



def usunKontakt():
    index = listabox_listaKontakow.index(ACTIVE)   # Pobranie aktywnego (zaznaczonego pola - indeksu)
    kontakty.pop(index)
    listaKontakt()


def edytujKontakt():
    index = listabox_listaKontakow.index(ACTIVE)  # Pobranie aktywnego (zaznaczonego pola - indeksu)

    imie = kontakty[index][0]
    nazwisko = kontakty[index][1]
    telefon = kontakty[index][2]
    email = kontakty[index][3]

    text1_Imie.insert(0,imie)
    text2_Nazwisko.insert(0,nazwisko)
    text3_telefon.insert(0,telefon)
    text4_Email.insert(0,email)

    button1_dodajKontakt.config(text="Zmien kontakt", command= zmienkontakt)

def zmienkontakt():
    print("zmien kontakt")
    index = listabox_listaKontakow.index(ACTIVE)  # Pobranie aktywnego (zaznaczonego pola - indeksu)
    imie= text1_Imie.get()
    nazwisko=text2_Nazwisko.get()
    telefon=text3_telefon.get()
    email=text4_Email.get()
    # print(imie, nazwisko, telefon, email)

    # modyfikacja wersja 1:
    kontakty[index][0]=imie
    kontakty[index][1] = nazwisko
    kontakty[index][2] = telefon
    kontakty[index][3] = email

                                                        # modyfikacja wersja 2:
                                                        # dane = [imie, nazwisko, telefon, email]
                                                        # kontakty[index] = dane

# czyszczenie pol
    text1_Imie.delete(0, END)  # czyscimy pola od poczatku -0 do konca - end
    text2_Nazwisko.delete(0, END)
    text3_telefon.delete(0, END)
    text4_Email.delete(0, END)
    text1_Imie.focus()  # USTAW KURSOR MRUGAJACY NA POLE text1_Imie

    button1_dodajKontakt.config(text="Dodaj kontakt", command=dodajKontakt)

    # listabox_listaKontakow.delete(0, END)  # czysli liste kontaktow
    # for index, value in enumerate(kontakty):
    #     listabox_listaKontakow.insert(index, value[0] + " " + value[1])

    listaKontakt()



    print(kontakty[index])




# tworzymy ramki - beda 3 ramki

ramka_lewa=Frame(root, pady=20)
ramka_prawa=Frame(root)
ramka_dol=Frame(root)

#  definiujemy rozmieszczenie ramek
ramka_lewa.grid(row=0, column=0, padx=(10,30))
ramka_prawa.grid(row=0, column=1)
ramka_dol.grid(row=1, column=0, columnspan=2, sticky=W)

# ramka lewa ramka_lewa

label1_listaKontakow = Label(ramka_lewa, text="Lista kontaktow")
listabox_listaKontakow = Listbox(ramka_lewa,width=20, height=7)
button1_PokazKontakt = Button(ramka_lewa, text="Pokaz szczegoly kontaktow", command= SzczegolyKontaktu)
button2_UsunKontakt = Button(ramka_lewa, text="Usun kontakt", command=usunKontakt)
button3_EdytujKontakt = Button(ramka_lewa, text="Edytuj kontakt", command=edytujKontakt)

label1_listaKontakow.grid(row=0, column=0, columnspan=3)
listabox_listaKontakow.grid(row=1, column=0, columnspan=3)
button1_PokazKontakt.grid(row=2, column=0)
button2_UsunKontakt.grid(row=2, column=1)
button3_EdytujKontakt.grid(row=2, column=2)


# ramka_prawa

label1_NowyKontakt = Label(ramka_prawa, text="Nowy kontakt:")
label2_Imie = Label(ramka_prawa, text="Imie:")
label3_Nazwisko = Label(ramka_prawa, text="Nazwisko:")
label4_telefon = Label(ramka_prawa, text="Telefon:")
label5_Email = Label(ramka_prawa, text="Email:")

text1_Imie = Entry(ramka_prawa)
text2_Nazwisko = Entry(ramka_prawa)
text3_telefon = Entry(ramka_prawa)
text4_Email = Entry(ramka_prawa)

button1_dodajKontakt = Button(ramka_prawa, text="Dodaj kontakt", command=dodajKontakt)


label1_NowyKontakt.grid(row=0, column=0, columnspan=2)
label2_Imie.grid(row=1, column=0)
label3_Nazwisko.grid(row=2, column=0)
label4_telefon.grid(row=3, column=0)
label5_Email.grid(row=4, column=0)

text1_Imie.grid(row=1, column=1, sticky=W, pady=2)
text2_Nazwisko.grid(row=2, column=1, sticky=W, pady=2)
text3_telefon.grid(row=3, column=1, sticky=W, pady=2)
text4_Email.grid(row=4, column=1, sticky=W, pady=2)

button1_dodajKontakt.grid(row=5, column=1, columnspan=2)

# ramka dolna


label1_SzczegolyKontaktu = Label(ramka_dol, text="Szczegoly kontaktu:")
label2_Imie2 = Label(ramka_dol, text="Imie:")
label3_Nazwisko2 = Label(ramka_dol, text="Nazwisko:")
label4_telefon2 = Label(ramka_dol, text="telefon:")
label5_Email = Label(ramka_dol, text="Email:")

label6_Imie_wyswietl = Label(ramka_dol, text="...", width=10)             # wyswietlanie wartosci
label7_Nazwisko_wyswietl = Label(ramka_dol, text="...", width=10)        # wyswietlanie wartosci
label8_telefon_wyswietl = Label(ramka_dol, text="...", width=10)          # wyswietlanie wartosci
label9_Email_wyswietl = Label(ramka_dol, text="...", width=10)            # wyswietlanie wartosci

label1_SzczegolyKontaktu.grid(row=0, column=0, columnspan=8)
label2_Imie2.grid(row=1, column=0, sticky=W)
label3_Nazwisko2.grid(row=1, column=1, sticky=W)
label4_telefon2.grid(row=1, column=2, sticky=W)
label5_Email.grid(row=1, column=3, sticky=W)

label6_Imie_wyswietl.grid(row=2, column=0, sticky=W)
label7_Nazwisko_wyswietl.grid(row=2, column=1, sticky=W)
label8_telefon_wyswietl.grid(row=2, column=2, sticky=W)
label9_Email_wyswietl.grid(row=2, column=3, sticky=W)




root.mainloop()
