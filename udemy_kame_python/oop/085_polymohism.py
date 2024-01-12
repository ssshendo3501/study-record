"""
ポリモーフィズム
・多態性の意味
・intもstrもprint()することでprintすることができる
・print_int()やprint_str()などのように型のあった関数を呼ぶ必要がない
・継承はポリモーフィズムを実現する手段の一つ

動的型付け言語
・Pythonは実行して初めにその変数型づけを行う
・対義語は静的型付け言語
・Pythonでは「型」よりも「振る舞い」に関心がある
　例：intかどうかかよりも、＋演算ができるかどうかに関心がある
"""

class MyClass:
    def __str__(self):
        return "MyClassの__str__"


# すべての型で出力可能：プリンタブル（ポリモーフィズムの一種）
mc = MyClass()
print(mc) # mc.__str__()
print(1) # 1.__str__()
print("1") # "1".__str__()
print(True) # True.__str__()
print([1,2,3]) # [1,2,3].__str__()

# MyClassの__str__
# 1
# 1
# True
# [1, 2, 3]


# 型が変わってもprint可能
# printが__str__のメソッドを使っているため
various_types = [1, "1", True, [1,2,3], (1, 2), {"1":1}]
for element in various_types:
    print(element)   # .__str__

# 1
# 1
# True
# [1, 2, 3]
# (1, 2)
