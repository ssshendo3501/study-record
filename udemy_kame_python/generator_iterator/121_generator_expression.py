"""
generator expression
・yieldを使わないでgeneratorを作る
・書き方はリスト内包表記を同様で、[]ではなく()を使う
・リスト内包表記との違いは[]を使うか、()を使うか
・generator関数よりも簡潔に書ける
・リスト内包表記で数値が大きくなりそうなら、generator expressionを使ってメモリを節約するのが良い
"""

# リスト内包表記：[]
square_list = [num * num for num in range(100)]
print(square_list)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# generator expression：()
square_gen = (num * num for num in range(100))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

# 0
# 1
# 4
# 9
# 16


import sys

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

# range(100)のとき、
# 920
# 200

# 偶数のスクエアのみを取得する
# リスト内包表記
even_squares_list = [num * num for num in range(10) if num % 2 == 0]
print(even_squares_list)

# [0, 4, 16, 36, 64]


even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))

for num in even_squares_gen:
    print(num)

# 0
# 4
# 16
# 36
# 64
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/generator_iterator/121_generator_expression.py", line 55, in <module>
#     print(next(even_squares_gen))
#           ^^^^^^^^^^^^^^^^^^^^^^
# StopIteration

