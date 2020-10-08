import matplotlib.pyplot as plt

dane1= [12,211,2,12,21,12,21,12,21,21,12,21,435,7,5,787,8,9,90,9]
dane2= [34,43,765,67,8,97,8,8,57,35,2,68,56]

plt.plot(dane1, label="Dane testowe 1")
plt.plot(dane2, label="Dane testowe 2")

plt.grid(color="lightblue", linestyle="-.", linewidth=1.6)
plt.legend()


plt.savefig('output.png', dpi=300)
plt.show()

