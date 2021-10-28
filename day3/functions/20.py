ga = 20

print("outside ga =", ga)

def funca():
    global ga
    la = 33
    ga = 22
    print("la =", la)
    print("ga =", ga)

funca()
print("outside ga =", ga)
