# tuple：変更できないリスト、[]ではなく()で書く
# コードで書く際は変更する必要がないからタプルを使うイメージ

# 生年月日を保持する変数
date_of_birth = (1990, 2, 3)
print(date_of_birth)
# (1990, 2, 3)

# リストで変更しようと思った時
date_of_birth = [1990, 2, 3]
date_of_birth[0] = 1999
print(date_of_birth)
# [1999, 2, 3] # 変更可能

# タプルで変更は変更できない
# date_of_birth = (1990, 2, 3)
# date_of_birth[0] = 1999
# print(date_of_birth)
# TypeError: 'tuple' object does not support item assignment

# unpack：tupleに入ってたものをそれぞれの変数に割り当てることができる
# unpackはlistではやらない、その理由はlistがappendやremoveでindexが変わってしまうため
# unpackの処理をする際はlistではなくtupleでやるべき
year, month, date = date_of_birth
print(year)
print(month)
print(date)
# 1999
# 2
# 3