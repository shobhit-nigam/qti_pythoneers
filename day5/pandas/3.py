import pandas as pd

objx = pd.ExcelFile("stat.xlsx")

print(objx.sheet_names)

dfa = pd.read_excel("stat.xlsx", sheet_name='mon')

print(dfa)
