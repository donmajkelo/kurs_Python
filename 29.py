
chleb = 6.50
sok = 4
paczek = 5.50

numer1 = int(input (f"Ile bochenkow chleba chcesz kupic? "))
numer2 = int(input (f"Ile litrów soku chcesz kupic? "))
numer3 = int(input (f"Ile paczków sobie zyczysz? "))

suma = round((numer1*chleb+numer2*sok+numer3*paczek),2)

print(f" KUPIŁES {numer1} bochenkow chleba. ")
print(f" KUPIŁES {numer2} litrow soku. ")
print(f" KUPIŁES {numer3} szt. paczkow.  ")
print(f" Za wszystko placisz {suma} złotych a nie EURO :)")


