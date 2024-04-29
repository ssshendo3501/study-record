"""
csvモジュール
・csv.reader(f): 各行をリストで取得
・csv.DictReade(f) 各行を辞書で取得
・csv.writer(f): 各行をリストで書き込み
・csv.DictWriter(f) 各行を辞書で書き込み
"""

# csvの読み込み
import csv


# csv_reader(f): 各行をリストで返す
with open("example.csv") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)

# ['', 'First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id']
# ['1', 'Dulce', 'Abril', 'Female', 'United States', '32', '15/10/2017', '1562']
# ['2', 'Mara', 'Hashimoto', 'Female', 'Great Britain', '25', '16/08/2016', '1582']
# ['3', 'Philip', 'Gent', 'Male', 'France', '36', '21/05/2015', '2587']
# ['4', 'Kathleen', 'Hanner', 'Female', 'United States', '25', '15/10/2017', '3549']
# ['5', 'Nereida', 'Magwood', 'Female', 'United States', '58', '16/08/2016', '2468']
# ['6', 'Gaston', 'Brumm', 'Male', 'United States', '24', '21/05/2015', '2554']
# ['7', 'Etta', 'Hurn', 'Female', 'Great Britain', '56', '15/10/2017', '3598']


# csv_DictReader(f): 各行を辞書で返す
with open("example.csv") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)

# {'': '1', 'First Name': 'Dulce', 'Last Name': 'Abril', 'Gender': 'Female', 'Country': 'United States', 'Age': '32', 'Date': '15/10/2017', 'Id': '1562'}
# {'': '2', 'First Name': 'Mara', 'Last Name': 'Hashimoto', 'Gender': 'Female', 'Country': 'Great Britain', 'Age': '25', 'Date': '16/08/2016', 'Id': '1582'}
# {'': '3', 'First Name': 'Philip', 'Last Name': 'Gent', 'Gender': 'Male', 'Country': 'France', 'Age': '36', 'Date': '21/05/2015', 'Id': '2587'}
# {'': '4', 'First Name': 'Kathleen', 'Last Name': 'Hanner', 'Gender': 'Female', 'Country': 'United States', 'Age': '25', 'Date': '15/10/2017', 'Id': '3549'}
# {'': '5', 'First Name': 'Nereida', 'Last Name': 'Magwood', 'Gender': 'Female', 'Country': 'United States', 'Age': '58', 'Date': '16/08/2016', 'Id': '2468'}
# {'': '6', 'First Name': 'Gaston', 'Last Name': 'Brumm', 'Gender': 'Male', 'Country': 'United States', 'Age': '24', 'Date': '21/05/2015', 'Id': '2554'}
# {'': '7', 'First Name': 'Etta', 'Last Name': 'Hurn', 'Gender': 'Female', 'Country': 'Great Britain', 'Age': '56', 'Date': '15/10/2017', 'Id': '3598'}


# 辞書の方が何かと扱いやすくなる
with open("example.csv") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line['Country'])

# United States
# Great Britain
# France
# United States
# United States
# United States
# Great Britain


# csvの書き込み
# writerowはcsvに一行書き込めるメソッド
with open('sample.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['value1', 'value2'])
    writer.writerow(['value3', 'value4'])

# value1,value2
# value3,value4


# csv_DictWriter
with open('sample.csv', mode='w') as f:
    writer = csv.DictWriter(f, ['col1', 'col2'])
    writer.writeheader()
    writer.writerow({'col1': 'value1', 'col2': 'value2'})
    writer.writerow({'col1': 'value3', 'col2': 'value4'})

# col1,col2
# value1,value2
# value3,value4