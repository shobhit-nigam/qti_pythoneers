avengers = ['iron man', 'captain', 'black widow', 'wanda', 'thor']
wakanda = ["panther", "shuri", "m'baku"]

print("len of avengers =", len(avengers))
print("avengers =", avengers)
print("wakanda =", wakanda)
print("-----")

avengers.extend(wakanda)

print("len of avengers =", len(avengers))
print("avengers =", avengers)
