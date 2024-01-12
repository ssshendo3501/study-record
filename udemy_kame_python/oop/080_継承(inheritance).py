"""
継承（Inheritance）
・オブジェクト思考の要
・他のクラスをベースとして継承して、別クラスを作ることができる
・super class（親クラス、基底クラス）の機能を引き継ぎ、sub class（子クラス、派生クラス）として拡張することができる

例：車クラスをベースにトラッククラスを作る
・アクセル、ブレーキなどのメソッドやメーカー、燃費、モデル名などの属性は車クラスから継承し、
　積める荷物のよう席やタイヤの数などをトラッククラスで新たに定義する

・継承はis-aの関係になっている
  Dog is an animals
  Cat is an animals
  Truck is a car
"""

class Animals(object):

    def __init__(self, name):
        self.name = name
        print("Animal class called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animals):
    pass


class Cat(Animals):
    pass


pochi = Dog("Pochi")
tama = Cat("Tama")
print(pochi.name)
print(tama.name)

# Animal class called
# Animal class called
# Pochi
# Tama

# 継承元のAnimalsクラスにbreathがあるのでbreathメソッドを実行できる
pochi.breath()
tama.breath()

# Pochi is breathing
# Tama is breathing