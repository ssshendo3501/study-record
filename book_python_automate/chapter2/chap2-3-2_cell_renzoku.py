import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# 連続でセルに値を設定する
for i in range(10):
    cell = sheet.cell(row=(i+1), column=1, value=i)

book.save("renzoku.xlsx")