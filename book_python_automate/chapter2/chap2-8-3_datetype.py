import openpyxl as xl

book = xl.Workbook()
sheet = book.active

# 数値を設定 --- (*1)
cell = sheet["A1"]
cell.value = 345
sheet["B1"] = "data_type=" + cell.data_type

# 文字列を設定 --- (*2)
cell = sheet["A2"]
cell.value = "abc"
sheet["B2"] = "data_type=" + cell.data_type

# 日時を設定 --- (*3)
cell = sheet["A3"]
from datetime import date
cell.value = date(2021, 4, 1)
sheet["B3"] = "data_type=" + cell.data_type
# ファイルへ保存
book.save("data_type.xlsx")
