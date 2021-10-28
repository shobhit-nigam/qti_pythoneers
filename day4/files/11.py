with open("data.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()

col = []

for line in lista:
    col.append(int(line.split()[4]))

print(col)
