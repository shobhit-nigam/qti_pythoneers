with open("data.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()

col = []

for line in lista:
    temp = line.split()
    col.append(int(temp[2]))

print(col)
