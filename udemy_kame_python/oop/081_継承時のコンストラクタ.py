"""
・親クラスとサブクラスに両方とも__init__：コンストラクタがある場合、
　サブクラスでインスタンスを生成すると、サブクラス内のコンストラクタ優先される。
・開発では、親クラスとサブクラスのコンストラクタで別のことしたいなど、親/サブ両方で
　__init__を作ることがよくある
・その時は、サブクラス内で親クラスを呼ぶ、super()のビルトインファンクションを使えばOK
・サブクラスでは、super().__init__(name=name)　のように、親クラスのメソッドを一行で呼ぶことができる
　そのため。親クラスで定義したメソッドの後に追加した処理を書くことができる
"""

class Animals(object):
    def __init__(self, name):
        self.name = name
        print("Animal class called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animals):
    def __init__(self, name):
        super().__init__(name=name)
        print("Dog init is called")


class Cat(Animals):
    pass


pochi = Dog("Pochi")
tama = Cat("Tama")
print(pochi.name)
print(tama.name)