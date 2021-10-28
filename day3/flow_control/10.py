basket_b = {'melon', 'guava', 'plum', 'avocado', 'apple'}
lista = ['tt', 'dd', 'rr', 'tt', 'ss', 'gg',
        'kk', 'tt', 'ss', 'gg', 'dd', 'tt']

# for with range

for x in range(len(lista)):
    if lista[x] == 'gg':
        print("gg found")
        break

print("----")

for x in range(len(lista)):
    if lista[x] == 'zz':
        print("found")
        break
else:
    print("zz not found")
