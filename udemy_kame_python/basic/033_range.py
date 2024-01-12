# range(start, stop, step)
for i in [1,2,3,4,5,6]:
    print(i)

for i in range(1, 7, 1): # 開始:1、止まる:7未満(6)、刻み:1
    print(i)

for i in range(1, 7): # stepは省略できる
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6

for i in range(1, 7): # 開始:1、止まる:7未満(6)、刻み:1
    print(i)

for i in range(2, 5):
    print(i)
# 2
# 3
# 4

for i in range(10): # rangeは0から始まることに注意
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for _ in range(10): # helloを10回繰り返す、iが何も使わない時は'_'を書く
    print('hello')

"""
• Challenge: FizzBuzzゲームを作ろう!
1~50の数字をそれぞれprint()して，3の倍数で「Fizz」5の倍数で 「Buzz」,3と5の倍数で「FizzBuzz」とprint()する
"""

for i in range(1,51):
    if i % 15 == 0:
        print(f"{i} is FizzBuzz!!")
    elif i % 3 == 0:
        print(f"{i} is Fizz!!")
    elif i % 5 == 0:
        print(f"{i} is Buzz!!")
    else:
        print(f"{i}")