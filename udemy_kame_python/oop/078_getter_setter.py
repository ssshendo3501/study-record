class Person:

    # ageのgetterとsetterを作っているのでインスタンス変数であるageはノンパブリックにするべき
    def __init__(self, name, age):
        self.name = name
        self._age = age

    # ageのgetterメソッド
    def get_age(self):
        print("get_age called")
        return self._age

    # ageのsetterメソッド
    def set_age(self, age):
        print("set_age called")
        if age < 0:
            print("0以上の値を入れて下さい")
        else:
            self._age = age

    # propertyを使う際はインスタンス変数はノンパブリック"_"をつけることを忘れない
    # propertyはbuilt in function
    age = property(get_age, set_age)


john = Person("John", 20)

print(john.age)

# get_age called
# 20

# インスタンス名.変数名でset_ageメソッドを使わなくても実行できる
john.age = 15
print(john.age)

# set_age called
# get_age called
# 15

john.age = -10

# set_age called
# 0以上の値を入れて下さい

# propertyに入れてもインスタンス._ageで実行すると年齢が書き換えられてしまうので注意
john._age = -100
print(john.age)

# get_age called
# -100