class MyIterator:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self

myiterator = MyIterator(10)
print(myiterator)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(id(myiterator))
print(id(iter(myiterator)))
print(iter(myiterator))

# <__main__.MyIterator object at 0x1063053d0>
# 10
# 11
# 12
# 13
# 14
# 4502885568
# 4502885568
# <__main__.MyIterator object at 0x10c6494c0>



# challenge
# 指定した数字から2までの偶数の値を返すgeneratorを作ろう

def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


class EvenIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 2で止めたいのでStopIteratrionを出す
        if self.current < 2:
            raise StopIteration
        # 最初のstartが偶数のとき、そのまま値を返し、2引く
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        # 最初のstartが奇数の時、-1するが、それだけだとそのままの数字が帰ってきてしまう
        # そこで、__next__()をもう1回呼べば良い（トリッキーやり方）
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self

if __name__ == '__main__':
    eveniterator = EvenIterator(10)
    print(next(eveniterator))
    print(next(eveniterator))
    print(next(eveniterator))
    print(next(eveniterator))
    print(next(eveniterator))
    print(next(eveniterator))
    print(next(eveniterator))

# 10
# 8
# 6
# 4
# 2
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/generator_iterator/119_custom_iterator.py", line 71, in <module>
#     print(next(eveniterator))
#           ^^^^^^^^^^^^^^^^^^
#   File "/Users/endousou/Desktop/PythonLecture/generator_iterator/119_custom_iterator.py", line 52, in __next__
#     raise StopIteration
# StopIteration


"""
generatorとiteratorの違い
・generatorはiteratorの一種。そのため、iteratorの方が定義が広い
・iteratorはクラスで定義する
・generatorは関数で定義する
・iteratorはyieldを使わない
・generatorはyieldを使う
・使い方は同じ
"""