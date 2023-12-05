# リスト内包表記（list comprehension）

# forループ
square_list = [] # 0, 1, 4, 9, 16,...
for i in range(10):
    square_list.append(i ** 2)
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# リスト内包表記
# 書き方は、リストの数値になるものを最初に書いておく
square_list = [i ** 2 for i in range(10)]
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# for文のあとにif文を書くこともできる
square_list = [i ** 2 for i in range(10) if i % 2 == 0]
print(square_list)
# [0, 4, 16, 36, 64]
# 2で割ったあまりが0(iが偶数の時)の時のみべき上している