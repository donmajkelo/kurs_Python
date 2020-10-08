import requests


res=requests.get("https://api.chucknorris.io/jokes/categories")
dane= res.json()  # konwersja ze string DO POSTACI OBIEKTOWEJ

for i in dane:
    print(i, end=" ")
    # print("\n")

menu=input(" Wybierz kategorie zartu ktory cie interesuje: ")
if menu not in dane:
    print("Nie ma takiej kategorii")
else:
    res2 = requests.get(f"https://api.chucknorris.io/jokes/random?category={menu}")
    dane2 = res2.json()
    # dane3=str(dane2.replace("Chuck Norris", "Don majkelo"))
    print(dane2["value"].replace("Chuck Norris", "Don majkelo"))

