
dane=[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# for i in dane:
#     print(i)


for i in range(len(dane)):
    dane[i][i]=1
    x=len(dane)
    dane[x-i-1][i]=1

for i in range(len(dane)):
    for j in range(len(dane[i])):
        print(dane[i][j], end= " ")

    print()