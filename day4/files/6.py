"""fa = open("books.txt", "r")
stra = fa.read()
fa.close()"""

with open("books.txt", "r") as fa:
    stra = fa.read()

print(stra)
