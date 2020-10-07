
from tkinter import *   #importujemy biblioteke

root = Tk()

root.wm_title(" Moja pierwsza aplikacja")
root.geometry("700x500")

ramka=Frame(root)
ramka.grid()

etykieta=Label(ramka, text="Tutaj jest tekscik")
etykieta.grid()

bttn1=Button(ramka, text="Tutaj jest przycisk nr 1")
bttn1.grid()

bttn2=Button(ramka, text="Tutaj jest przycisk nr 2")
bttn2.grid()

tekst1=Text(ramka, width=20, height=7, wrap=WORD)
tekst1.grid()

root.mainloop()
