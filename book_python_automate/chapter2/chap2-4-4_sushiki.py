import openpyxl as excel

# ワークブック
book = excel.Workbook()
sheet = book.active

# A1のセルに日付を指定
sheet['A1'] = "2024/07/04"
# B1のセルに計算式を設定
sheet['B1'] = '=TEXT(A1, "ggge年m月d日")'

book.save('suhiki.xlsx')
