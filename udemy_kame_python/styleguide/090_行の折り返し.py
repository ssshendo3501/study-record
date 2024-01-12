# 行の折り返し

# 長い引数の行の折り返し
# correct
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
foo = long_function_name(var_one,
                         var_two,
                         var_three,
                         var_four)
# wrong
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 関数の中身で引数が長い場合は最初に改行する->そうすると８マス開く
def long_var_name(
        var_one, var_two, var_three, var_four):
    print("var_one")

# "\"で区切って改行する
# 下記のような書き方の際は演算子を最初にして折り返す
# correct
a = 1000000000000000000000 \
    + 100000000000000000000 \
    + 10000 \
    + 10000000
# wrong
a = 100000000000000000000000000 + \
    100000000000000000000 + \
    10000 + \
    10000000


# 関数間は二行開ける
def func1():
    print(a)


def func2():
    print(b)


# クラスのメソッド間は一行
class MyClass:
    def __init__(self):
        pass

    def func1(self):
        pass

    def func2(self):
        pass



