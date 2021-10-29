from openpyxl import Workbook
from openpyxl import load_workbook

objw = load_workbook('stat.xlsx')

objs = objw['mon']

datacell = objs['B5']
print("value =", datacell.value)
print("comment text =", datacell.comment.text)
print("comment author =", datacell.comment.author)
