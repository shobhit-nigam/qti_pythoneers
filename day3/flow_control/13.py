lista = ['tt', 'dd', 'rr', 'tt', 'ss', 'gg',
        'kk', 'tt', 'ss', 'gg', 'dd', 'tt']

# create a dict, with frequency of members of lista

dictc = {}

for x in lista:
    if x in dictc:
        dictc[x] = dictc[x] + 1
    else:
        dictc[x] = 1
#    print(dictc)

print(dictc)
