lista = [12, 11, 6, 10, 8, 3]
listb = [8, 6, 4, 5, 10, 20]

def calc(a, b):
    # some calculation
    return 2*a + 4*b - 3


listc = list(map(calc, lista, listb))


"""
listc = []

if len(lista) <= len(listb):
    for i in range(len(lista)):
        ret = calc(lista[i], listb[i])
        listc.append(ret)

"""

print(listc)
