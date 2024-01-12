# type annotation

def add_nums(num1, num2):
    return num1 + num2

print(add_nums(1, 2)) # 3


# 下記のように書くと型をヒントが確認できる -> type annotation
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

print(add_nums('1', '2')) # 12
# int型ではない変数を入れても問題なく出力できる
# type annotationは型を指定するものではなく、あくまでヒントである
# type annotationを使った開発はあまり多くない
# Pythonは動的型付け言語；変数がどういう型かということよりも、関数がきちんと出力できるかの振る舞いに価値をおく言語
# 動的型付け言語 <-> 静的型付け言語
