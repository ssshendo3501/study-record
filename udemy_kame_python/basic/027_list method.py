# append : 新しいオブジェクトを作る

fruits = ['apple', 'peach', 'melon', 'grapes']

fruits.append('banana')
print(fruits)

# insert : 指定したindexに指定したオブジェクトを入れる
fruits.insert(3, 'lemon')
print(fruits) # ['apple', 'peach', 'melon', 'lemon', 'grapes', 'banana']

# remove ： マッチした最初のオブジェクトを取り除く
fruits.remove('peach')
print(fruits)

# sort ： 照準で並び替える
fruits.sort() # 昇順
print(fruits)

fruits.sort(reverse=True) # 昇順
print(fruits)

# len() : リストの要素数を取得する
len(fruits)
print(len(fruits))