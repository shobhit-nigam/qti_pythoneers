avengers = ['iron man', 'captain', 'black widow', 'wanda', 'thor']
marvel = ['wolverine', 'magneto', avengers]

print("avengers =", avengers)
print("marvel =", marvel)
print("-----")

avengers.sort()
avengers.insert(1, 'hulk')
avengers.pop()
avengers.pop(2)

print("avengers =", avengers)
print("marvel =", marvel)
