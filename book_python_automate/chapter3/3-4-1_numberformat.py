# 日付のデータを全て西暦から和暦にするプログラム
# number_formatを使う

import openpyxl as excel

book = excel.load_workbook('date-sample.xlsx')
sheet = book.active
print(sheet['A4'].value)
print(sheet['A4'].number_format)
print(type(sheet['A4'].value))