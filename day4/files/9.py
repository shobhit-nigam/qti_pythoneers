with open("books.txt", "r") as fa:
    lista = fa.readlines()

fb = open("new_books.txt", "w")

for line in lista:
    if line[0] == 't' or line[0] == 'T':
        fb.write(line)

fb.close()
