import openpyxl as excel

# 新規ワークブックを作る
book = excel.Workbook()

# 悪低部なワークシートを作る
sheet = book.active

# Aiのセルに値を設定
sheet["A1"] = "こんにちは"

# ファイルの保存
book.save("hello.xlsx")

# 既存のファイルの読み込み
book = excel.load_workbook("hello.xlsx")

# 先頭のワークシートを取り出す
sheet = book.worksheets[0]

# A1のセルの値を得る
cell = sheet["A1"]

# 読み出した結果を画面に出力
print(cell.value)