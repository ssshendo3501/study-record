# pip install msoffcrypto-tool     

# 暗号化したエクセルファイルはopenpyxlで開くことができない
# そこで、msoffcrypto-tool  のライブラリを用いてパスワード付きExcelファイルを開くことができる

import openpyxl as excel
import msoffcrypto

# 暗号化したエクセルファイルを指定
fin = open("uriage-encrypt.xlsx", "rb")
msfile = msoffcrypto.OfficeFile(fin)
# パスワードの指定
msfile.load_key(password="abcd")
# 複合化したファイルを保存
fout = open("uriage-decrypt.xlsx", "wb")
msfile.decrypt(fout)

# ワークブックを開いて内容を表示
book = excel.load_workbook("uriage-decrypt.xlsx")
sheet = book.active
for row in sheet["A2":"F99"]:
    values = [v.value for v in row]
    if values[0] is None: break
    print(values)