lista = ['tt', 'dd', 'rr', 'tt', 'ss', 'gg',
        'kk', 'tt', 'ss', 'gg', 'dd', 'tt']

# create a list which has indices of 'tt'

tt_index = []

for x in range(len(lista)):
    if lista[x] == 'tt':
        tt_index.append(x)

print(tt_index)
