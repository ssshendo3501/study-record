# dictionary: キーと値の組み合わせを複数保持するデータ型

fruits_colors = {'apple' : 'red', 'lemon' : 'yellow', 'grapes' : 'purple'}
print(fruits_colors)

# 辞書から値を取り出したい時：キーを指定する
# リストの時はindexを指定していたが、辞書型ではindexではなくキーを保持する
# 注意！）辞書型は順番を保持していない
print(fruits_colors['apple']) # red

# 辞書に値を追加したい時
fruits_colors['peach'] = 'pink'
print(fruits_colors)
# {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple', 'peach': 'pink'}

# 辞書の中に辞書やリストを入れることも可能
# dict_sampleにある'dict'を取ってきたい場合はどうすれば良いか？ > 2重リストと同じような考え方
dict_sample = {1 : 'one', 2 : 'two', 3 : 'three', 'four' : {'inner' : 'dict'}}
print(dict_sample['four']['inner'])

# 辞書の中には順番がないので注意！
colors = {}
colors[1] = 'blue'
colors[0] = 'yellow'
colors[2] = 'green'
print(colors)
# {1: 'blue', 0: 'yellow', 2: 'green'}

# 辞書型をfor文で回すときに使う便利な使い方
# .keys(), .values()
fruits_colors = {'apple' : 'red', 'lemon' : 'yellow', 'grapes' : 'purple'}

for fruit in fruits_colors.keys():
    print(fruit)
# apple
# lemon
# grapes

for color in fruits_colors.values():
    print(color)
# red
# yellow
# purple

# keysやvalueを指定しないとキーが返ってくる
# 　> デフォルトでは.keys()であることを覚えておくとともに、わかりやすいために.keysや.valuesを覚えておく
for x in fruits_colors:
    print(x)
# apple
# lemon
# grapes

# items():keyとvalueをセットにしてタプルでfor文で回す
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}!!")
# apple is red!!
# lemon is yellow!!
# grapes is purple!!

