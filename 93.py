
import pymysql

try:
    conn=pymysql.connect("localhost", "root", "alxalx", "db93", charset="utf8")
    c=conn.cursor()
    print("Polaczenie OK")
except:
    print("błąd połączenia")

def wyswietl():
    c.execute("SELECT * FROM db93.pracownicy")
    dane=c.fetchall()
    print("Id imie Nazwisk. pensja PESEL")
    for i in dane:
        print(i[0], i[1],i[2],i[3], i[4])

def dodaj(imie, nazwisko, pensja, PESEL):

    c.execute(f"INSERT INTO pracownicy(imie, nazwisko, pensja, PESEL) VALUES( %s, %s, %s, %s)",  (imie, nazwisko, pensja, PESEL))

    decyzja=input("czy chcesz zapisac dane: T/N").upper()
    if(decyzja=="T"):
        conn.commit()
        print("Dane dodano do tabeli: pracownicy")
    else:
        conn.rollback()
        print("Danych nie wprowadzono")

def zmien(pesel, noweImie, noweNazwisko, nowaPensja):
    c.execute("SELECT * FROM db93.pracownicy WHERE pesel=%s", pesel)
    dane = c.fetchall()
    print(dane)
    imie = dane[0][1]
    nazwisko = dane[0][2]
    pensja = dane[0][3]

    if(noweImie!=""):
        imie=noweImie
    if (noweNazwisko != ""):
        nazwisko = noweNazwisko
    if (int(nowaPensja) > 0):
            pensja = nowaPensja

    c.execute(f"UPDATE pracownicy SET imie=%s, nazwisko=%s, pensja=%s WHERE pesel=%s", (imie, nazwisko, pensja, pesel))

    decyzja = input("czy chcesz zapisac dane: T/N").upper()
    if (decyzja == "T"):
        conn.commit()
        print("Dane zmieniono z pracownicy")
    else:
        conn.rollback()
        print("Danych nie zmieniono")


def usun(pesel):
    c.execute("SELECT pesel FROM db93.pracownicy WHERE pesel=%s", pesel)
    dane = c.fetchall()

    if(dane!= ()):
        c.execute("DELETE FROM pracownicy WHERE pesel=%s", (pesel))
    else:
        print("Nie ma goscia o tym PESELU")
    # dane = c.fetchall()

    decyzja = input("czy chcesz zapisac dane: T/N").upper()
    if (decyzja == "T"):
        conn.commit()
        print("Dane usunieto z pracownicy")
    else:
        conn.rollback()
        print("Danych nie usunieto")

def wyszukaj(fraza):

    c.execute(f"SELECT * FROM db93.pracownicy WHERE nazwisko LIKE '%{fraza}%' OR imie LIKE '%{fraza}%'")
    dane = c.fetchall()
    # print(dane)

    for i in dane:
        print(i[1], i[2])

while (True):

    menu=input(" D-dodaj, P-pokaz, U-usun, Z-zmien, S-szukaj, K-koniec ").upper()

    if(menu=="D"):
        imie = input("Podaj imie do dodania")
        nazwisko = input("Podaj nazwisko do dodania")
        pensja = input("Podaj pensje do dodania")
        pesel = input("Podaj PESEL do dodania")
        dodaj(imie, nazwisko, pensja,pesel)
    elif (menu == "P"):
        wyswietl()
    elif (menu == "U"):
        pesel = input("Podaj pesel do usuniecia")
        usun(pesel)
    elif (menu == "Z"):
        pesel = input("Podaj pesel pracownika do zmiany")
        noweImie = input("Podaj nowe imie do zmiany")
        noweNazwisko = input("Podaj nowe nazwisko do zmiany")
        nowaPensja = input("Podaj nowa pensje do zmiany")
        zmien(pesel, noweImie, noweNazwisko, nowaPensja)
    elif (menu == "S"):
        fraza = input("Podaj szukana")
        wyszukaj(fraza)
    elif (menu == "K"):
        print("Koniec programu")
        c.close()
        break
    else:
        print("Nierozpoznana opcja menu")
