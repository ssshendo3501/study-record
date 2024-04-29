"""
iteratorとiterable
・generatorはiterableの一種
・iteratoとは、next()で回すことができて、iter()関数でiteratorを返すものの総称
・iter()関数でiteratorを返すものをiterableという
・つまり、iteratorもiterableである
・for文で回していたinのあとは必ずiteratorが来る必要がある
    for i in <iterator>:
"""


fruits = ['apple', 'lemon', 'peach']

# fuirtsのリストはiteratorではないので、nextで回せない
# print(next(fruits))

# TypeError: 'list' object is not an iterator

fruits_iterator = iter(fruits)

# fruits_iteratorはnextで回すことができる
# また、iter()でiteratorを返している
# iter関数でiteratorを返すものをiterableという
# つまり、fruits_iteratorはiterableである
print(next(fruits_iterator))
print(next(fruits_iterator))
print(iter(fruits_iterator))

# apple
# lemon
# <list_iterator object at 0x10144cf10>

print(id(fruits_iterator))
print(id(iter(fruits_iterator)))

# 4298984944
# 4298984944


# 前回作ったevenはiteratorなのか、iterableなのか？
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1

# evenはnext()で回すことができて、iter()でiteratorを返すことも確認できた
# つまり、evenはiteratorである
print("=" * 30)
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))  # evenはnextで回すことができる
print(iter(even_gen))
print(id(even_gen))
print(id(iter(even_gen)))  # evenはiterでiteratorを返す


"""
nextと.__next__()
・next(obj)はobj.__next__()と等しい
・__xxx__はmagic methodと呼ばれる特別なメソッド
・他のmagic methods：__init__, __len__, __str__, __doc__, ...
・next()で値を返すということは、__next__メソッドを実装しているということ
・同様に、iter()は__iter__()メソッドをcallしている

　-> つまり、iteratorは__next__()と__iter__()が正しく実装されたオブジェクト
　　　__next__()と__iter__()を実装することで、iteratorを自作することが可能
"""

fruits = ['apple', 'lemon', 'peach']
fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(fruits_iterator.__next__())

# apple
# lemon

