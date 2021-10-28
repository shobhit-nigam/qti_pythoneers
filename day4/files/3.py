fa = open("books.txt", "r")

stra = fa.read(6)
print(stra)

stra = fa.read(8)
print(stra)

fa.close()
