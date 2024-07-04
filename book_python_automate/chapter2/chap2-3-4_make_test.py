import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for y in range(1, 101):
    for x in range(1, 101):
        cell = sheet.cell(row=y, column=x)
        cell.value = cell.coordinate
        
book.save("test100.xlsx")