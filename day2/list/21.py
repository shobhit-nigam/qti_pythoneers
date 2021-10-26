avengers = ['iron man', 'captain', 'black widow', 'wanda', 'thor']
ave = avengers.copy()

print("avengers =", avengers)
print("ave =", ave)
print("-----")

avengers.sort()
avengers.insert(1, 'hulk')
avengers.pop()
avengers.pop(2)

print("avengers =", avengers)
print("ave =", ave)
