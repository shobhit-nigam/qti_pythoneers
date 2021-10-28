def funca(la, lb=200, lc=100):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)

# default values over written
funca(99, 88, 77)
print("----")
# one default value over written
funca(11, 22)
print("-----")
# default values used
funca(44)
print("-----")
# error
funca()
