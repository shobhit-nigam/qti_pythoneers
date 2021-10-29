import pandas as pd

dfa = pd.read_excel("stat.xlsx")

print(dfa)

print(dfa['id'].mean())
