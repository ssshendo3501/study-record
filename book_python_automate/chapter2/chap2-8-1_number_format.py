import openpyxl as xl
# ブックを作りシートを得る
book = xl.Workbook()
sheet = book.active

# A1,B1,C1に全て同じ値を設定 --- (*1)
val = 3.14159
sheet.append([val, val, val])

# 小数点以下を省略して表示 --- (*2)
sheet["A1"].number_format = '0'
# 小数点以下を2桁だけ表示 --- (*3)
sheet["B1"].number_format = '0.00'
# 小数点以下を4桁だけ表示 --- (*4)
sheet["C1"].number_format = '0.0000'

# 保存
book.save("number_format1.xlsx")


# セルに値とフォーマットを与える関数を定義
def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt

# 3桁ごとにカンマ区切りを指定 --- (*1)
keta3_fmt = '#,##0'
sheet["A1"] = keta3_fmt
set_cell("B1", 12345, keta3_fmt)
set_cell("C1", 123456789, keta3_fmt)

# 通貨形式を指定 --- (*2)
cur_fmt = '"¥"#,##0;"¥"\\-#,##0'
sheet["A2"] = cur_fmt
# 正数(0以上の数)を指定
set_cell("B2", 12345, cur_fmt)
# 負数(0以下の数)を指定
set_cell("C2", -12345, cur_fmt)

# 数値のマイナス値を△で表し、赤色にする --- (*3)
num_fmt = '#,##0;[red]"△ "#,##0'
sheet["A3"] = num_fmt
set_cell("B3", 12345, num_fmt)
set_cell("C3", -12345, num_fmt)

# 保存
book.save("number_format2.xlsx")
