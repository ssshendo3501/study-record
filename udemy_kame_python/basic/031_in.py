# in演算子: あるオブジェクトがそのlistに入っているかどうかをTrueかFalseで返す

fruits = ['apple', 'peach', 'grapes', 'banana']

print('apple' in fruits) # True
print('lenmon' in fruits) # False
print('lenmon' not in fruits) # True
print('h' in 'hello') # True

"""
• Challenge: ユーザに好きなフルーツを入力してもらい，
そのフルーツがfruitsリストにあればそのフルーツを削除し，
なければそのフルーツを追加するプログラムを作る
"""
fruits = ['apple', 'peach', 'grapes', 'banana']
selected_fruits = input('何かフルーツを指定してください')

if selected_fruits in fruits:
    # フルーツを削除
    fruits.remove(selected_fruits)
else:
    # フルーツを追加
    fruits.append(selected_fruits)
print(fruits)