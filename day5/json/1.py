import json

with open("example_1.json", "r") as fa:
    dicta = json.load(fa)

print(dicta)

print(dicta['size'])
