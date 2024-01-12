# クラスは最初の変数大文字で記載する（CalmelCase（<->snakecase））
# 今回はPersonクラスを作成していく
# 変数(属性)：name, age, gender  メソッド：歩く、走る
# クラスの中には基本的にメソッドを記載していくが、変数はメソッドの中に記載していく

# インスタンス変数：name, age, genderのように、インスタンスに紐づく変数を、インスタンス変数と呼ぶ
# クラスからインスタンスを生成する時には、__init__というメソッドが呼ばれる
# この__init__をインスタンスを生成するため、「コンストラクタ」と呼ぶ
# __init__の中の第1引数には必ずselfを書く（selfは自分自身の意味）
# self.name = nameはnameという変数を自分自身に入れれば良いという考え方
# Person(object)みたいになっている書き方は、クラスを継承している意味

# クラス変数：すべてのインスタンスで共有可能な変数
# クラス変数はnum_legsのような、インスタンスによらない、クラス全体で保持したい変数のこと
# クラス変数はクラスの最上位に書く（インスタンス変数よりも前）
# 各インスタンス(John, Taro, Emmaなど)で足が2本であることは変わらないため、すべてのインスタンスからアクセスが可能

class Person:
    # クラス変数
    num_legs = 2
    count = 0 # インスタンスが作られる度にカウントアップさせる

    # インスタンス変数（constractor）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1 # インスタンスが作られる度にカウントアップさせる

    def walk(self):
        print(f"{self.name} is walking... with {Person.num_legs} legs!!")

    def run(self):
        print(f"{self.name} is running... with {Person.num_legs} legs!!")

# インスタンス生成
john = Person("John", 28, "male")
taro = Person("Taro", 18, "male")
emma = Person("Emma", 40, "female")


# インスタンス変数：「.」に繋げてアクセス可能
print(john.name)
print(taro.gender)
print(emma.age)

# John
# male
# 40


# 属性はクラス生成後も変更可能
print(f"変更前の太郎の年齢：{taro.age}")
taro.age = 32
print(f"変更後の太郎の年齢：{taro.age}")

# 変更前の太郎の年齢：18
# 変更後の太郎の年齢：32


# walkやrunはインスタンスによって結果が変わる
# このようなインスタンスに紐づくメソッドをインスタンスメソッドと呼ぶ
john.walk()
emma.walk()

# John is walking.
# Emma is walking.

# num_legsはクラス変数であるため、各インスタンスで共有可能
# クラス名.クラス変数名　で呼び出すことも可能
print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)
john.walk()

# 2
# 2
# 2
# John is walking... with 2 legs!!

# クラス変数名もインスタンス変数と同様に外から変更可能
print(f"変更前：{Person.num_legs}")
Person.num_legs = 3
print(f"変更後：{Person.num_legs}")

# 変更前：2
# 変更後：3


# 各インスタンスに紐づくクラス変数のみを変更することも可能
print("変更前")
print(john.num_legs)
print(taro.num_legs)
john.num_legs = 4
print("変更後")
print(john.num_legs)
print(taro.num_legs)

# 変更前
# 3
# 3
# 変更後
# 4
# 3