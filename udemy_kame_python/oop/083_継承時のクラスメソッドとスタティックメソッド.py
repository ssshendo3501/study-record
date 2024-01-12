"""
メソッドでインスタンスを作る際はできるだけクラスメソッドで作るのが望ましい
その理由は、スタティックメソッドでインスタンスを作ってしまうと（create_from_dob2）、
親クラスを継承されたサブクラスは、サブクラスのインスタンスではなく、親クラスのクラスを返してしまうため
クラスメソッドのclsは継承先のクラスメソッドの値が入ってくる
"""

import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    """create_from_dob：生年月日を指定してインスタンスを生成するクラスメソッド"""
    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)

    """create_from_dob2：生年月日を指定してインスタンスを生成するスタティックメソッド"""
    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)


"""Personクラスを継承するBabyクラス"""
class Baby(Person):
    pass




# インスタンスメソッドで年齢を引数にしてインスタンスを生成
john = Person('John', 20)
print(john.name)
print(type(john))

# John
# <class '__main__.Person'>


# classmmethodでインスタンス生成
so = Person.create_from_dob("So", 1992, 9, 19)
print(so.age)
print(type(so))

# 31
# <class '__main__.Person'>


# staticmethodでインスタンス生成
shiori = Person.create_from_dob2("Shiori", 1991, 8, 26)
print(shiori.age)
print(type(shiori))


# Babyクラスのインスタンスを生成する
# スタティックメソッドで生成したものだけ、Personクラスになる
john2 = Baby('John', 20)
so2 = Baby.create_from_dob('So', 1992, 9, 19)
shiori2 = Baby.create_from_dob2('Shiori', 1991, 8, 26)

print(type(john2))
print(type(so2))
print(type(shiori2))

# <class '__main__.Baby'>
# <class '__main__.Baby'>
# <class '__main__.Person'>  # Personクラスになる
