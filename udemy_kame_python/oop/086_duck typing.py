"""
ダックタイピング
・動的型付け言語における考え方
・「もしアヒルのように歩き、アヒルようのに鳴くのなら、それはアヒルに違いない」
・Python的に言うと、「オブジェクトのクラス(型)には興味がなく、振る舞いに興味がある」と言うこと
・「アヒルかどうか」よりも「アヒルのように歩くか、鳴くか」に興味がある
・例：「intかどうか」よりも、「＋演算ができるかどうか」に興味があり、
　　　「＋演算できるならintとして扱っても良いよね」と言うこと
"""

class Duck:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack, quack...!!!")

    def fly(self):
        print("flying...")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,!!!")

    def quack(self):
        print("quack, quack...???")

    def swim(self):
        print("swimming...")


def walk_and_quack(duck):
    print(f"I`m {duck.name}")
    duck.walk()
    duck.quack()


# pinguはDuckクラスではないが、Duckクラスのように振る舞うことができる
# Duckクラスと同様にPenguinクラスもアヒルのように鳴くし歩くため
if __name__ == "__main__":
    donald = Duck("Donald")
    scrooge = Duck("Scrooge")
    daisy = Duck("Daisy")
    pingu = Penguin("pingu")

    donald.quack()
    donald.walk()
    pingu.quack()
    pingu.walk()

    # quack, quack...!!!
    # walking...
    # quack, quack...???
    # walking,,,!!!


    walk_and_quack(donald)
    walk_and_quack(pingu)

    # walking...
    # quack, quack...!!!
    # walking,,,!!!
    # quack, quack...???


    duck_list = [donald, pingu, scrooge, daisy]
    for duck in duck_list:
        walk_and_quack(duck)

    # I`m Donald
    # walking...
    # quack, quack...!!!
    # I`m pingu
    # walking,,,!!!
    # quack, quack...???
    # I`m Scrooge
    # walking...
    # quack, quack...!!!
    # I`m Daisy
    # walking...
    # quack, quack...!!!
