# class method

"""
クラスメソッド
・インスタンスに紐づかないメソッド
・＄classmethodデコレータを使う
・主にクラス内で便利関数のように使用する
・引数にclsからとってクラスの情報にアクセスできる
・クラスからアクセスしてcallする（クラス名.クラスメソッド名）
・クラスの情報を使わない場合はスタティックメソッドを使う
・クラスメソッド内でインスタンスを生成し返すことも可能（ファクトリーメソッドと呼ぶ）
"""

class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is normal method")

    # static method: self不要
    @staticmethod
    def mystaticmethod():
        print("This is static method")

    # class method: clsと記載
    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is class method and now the count is {cls.classmethod_count}.")


# class method
MyClass.myclassmethod()
MyClass.myclassmethod()




# factory method
import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # factory method：クラスメソッド内でインスタンスを生成して返すこともできる
    # create_from_dobは、年齢ではなく、生年月日を指定してインスタンスを生成するクラスメソッド
    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        # 誕生日の月日を見て、年齢の算出式を変えている
        # まだ誕生日が来ていないので-1する（Trueのとき）
        if (today.tm_mon, today.tm_mday) < (month, date):
            age = today.tm_year - year -1
        # 誕生日を過ぎているので-1する必要はない（Falseのとき）
        else:
            age = today.tm_year - year
        return cls(name=name, age=age)

        # 月と日から誕生日を算出するif文は、booleanを使って下記の書き方もある(True:1, False:0)
        # age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))


# インスタンスメソッドで年齢を引数にしてインスタンスを生成
john = Person('John', 20)
print(john.name)
print(type(john))

# classmmethodで誕生日を引数にしてインスタンスを生成
emma = Person.create_from_dob("Emma", 1992, 9, 19)
print(emma.age)
print(type(emma))

# John
# <class '__main__.Person'>
# 31
# <class '__main__.Person'>


#############################################
# タプルの比較演算
print((1,2) < (2,1))
print((1,2) < (2,1))
print((1,3) < (2,1))
print((1,3) < (1,1))

# True
# True
# True
# False
#############################################
