import openpyxl as excel

# 新規のワークブックを作成
book = excel.Workbook()

# 新規シートのアクティブ化
sheet = book.active

# Aiのセルに書き込む
sheet["A1"] = "勤勉な人の計画は必ず成功する"

# A2(row=2, column=1)に値を書き込む
cell = sheet.cell(row=2, column=1)
cell.value = "探すのに時があり諦めるのに時がある"

# 保存
book.save("cell_w.xlsx")