import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# 九九の表を得る
for x in range(1, 10):
    for y in range(1, 10):
        cell = sheet.cell(row=x, column=y)
        cell.value = x * y
        
book.save("9x9.xlsx")