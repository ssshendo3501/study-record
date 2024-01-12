"""
親クラスとサブクラスで同じ名前のメソッドを持つとき
親クラスでは、親クラス内のメソッドを呼びたいが、継承時にオーバーライドで上書きされるので
親クラスの__init__で呼ぶことができない。そこで、名前修飾"__"して解決する。
名前修飾すると、プライベート関数になってしまうので、

"""
class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    """mymethodを"__"をつける(名前修飾する)ことで、継承時にName Clashを阻止することができる"""
    def __mymethod(self):
        print("Person method is called")

    """名前修飾しない同一のmymethodも用意して親クラスで参照できるようにする書き方"""
    def mymethod(self):
        print("Person method is called")

    # """これでも良い"""
    # __mymethod = mymethod()


class Baby(Person):
    def mymethod(self):
        """親クラスのmymethodをオーバーライドするmymethod"""
        print("Baby method is called")


# self.は「インスタンス自身」を表す意味であり、
# インスタンス生成時はPersonの__mymethodが呼ばれる
# Babyインスタンスを生成してmymethodを実行すると、Babyインスタンスのメソッドを返す
taro_baby = Baby("Taro")
print(taro_baby.name)
taro_baby.mymethod()

# Person method is called
# Taro
# Baby method is called


# 名前修飾するとクラス名.mymethodを呼べなくなる
# 名前修飾するとプライベートメソッドになってしまうため
taro_person = Person("Taro")
taro_person.mymethod()

# Person method is called
# Person method is called