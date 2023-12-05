# enumerate
# オブジェクト（apple, peacなどの要素）とindex（0,1,2,3...）を同時に取り出すことができる
fruits = ['apple', 'peach', 'melon', 'grapes']

# idxはindexでよく使われる変数名
for idx, fruit in enumerate(fruits):
    print(f"{idx},{fruit}")
# 0,apple
# 1,peach
# 2,melon
# 3,grapes

# xはタプル型で返ってくる
for x in enumerate(fruits):
    print(x)
# (0, 'apple')
# (1, 'peach')
# (2, 'melon')
# (3, 'grapes')

