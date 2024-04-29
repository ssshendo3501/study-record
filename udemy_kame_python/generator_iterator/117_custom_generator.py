"""
ジェネレーターを自作する
・yieldは関数のreturnみたいなもの
・yieldを使うと、この関数はジェネレーターの機能を持つようになる

yield
・returnの代わりにyieldを使うと、その関数はgenerator（generator function）になる
・generator functionの戻り値はgenerator iteratorと呼ばれるもので、
　イテレーションによりyieldの値を返すオブジェクトになる
"""


# rangeを自作する
# myrangeがgenerator function
# mrがgenerator iterator
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
print(type(mr))  # <class 'generator'>

# for i in mr:
#     print(i)


# myrangeはgenerator functionなので、next()を呼ぶことでyieldの値を返す
# このとき状態を保持するので、next()が毎回変わっていく
# # 9まで出力されると、StopIterationが起こる
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))

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
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/generator_iterator/117_custom_generator.py", line 43, in <module>
#     print(next(mr))
#           ^^^^^^^^
# StopIteration


# Challenge
# 指定した数字から2までの偶数の値を返すgeneratorを作ろう

# 自分の回答
def even(start):
    while start != 0:
        if start % 2 == 0:
            yield start
            start -= 2
        else:
            start = start - 1
            yield start
            start -= 2

# 正当
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print("=" * 30)
for i in even(10):
    print(i)
