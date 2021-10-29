import json

with open("example_2.json", "r") as fa:
    dicta = json.load(fa)

def func(d):
    for k, v in d.items():
        if type(v) is dict:
            func(v)
        else:
            print(k)
            print(v)
        print("---")

func(dicta)
