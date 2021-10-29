import json

with open("example_2.json", "r") as fa:
    dicta = json.load(fa)

print(dicta["quiz"]["maths"]["q1"]["question"])
