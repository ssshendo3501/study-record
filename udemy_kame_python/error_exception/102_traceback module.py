
"""
EAFP(easier to ask for forgiveness than permission)
・許可をもらうより許しをもらう方が楽
・有効であると仮定してコードを書いていく、その仮定が誤っていたら例外を出す
・これにより手早くコードを書くことが可能
・try exceptを多く書くことになるが、それ自体は悪いことではない
"""

# numにthreeを入れるとValueErrorが出る
# split_billとcheck関数の開発者が異なる場合
# check関数の開発者はsplit_bill関数のコードを改修することは不可
# そのため、check関数でValueErrorが出ることを知っているなら、
# check関数の中でtryキャッチして例外処理すれば良い
# 今回のような、メソッドで2重にもtryキャッチしていく方法をEAFPと呼ぶ
def split_bill(price):
    num = input("割り勘する人数を入力してください")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0以外の数字を入力してください")
    else:
        print(f"1人{each}円です")

def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        print("エラーが出ました。やり直してください。")


if __name__ == "__main__":
    bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}
    check(bill)

# 割り勘する人数を入力してくださいthree
# エラーが出ました。やり直してください。


# EAFPでメソッド間でtryキャッチを接続していくと、
# どこでエラーになったのかわかりにくくなる。
# そこでtracebackモジュールを使って解決する
# traceback.print_exc()を実施すれば、split_billでエラーが出ているのがわかる
import traceback


def split_bill(price):
    num = input("割り勘する人数を入力してください")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0以外の数字を入力してください")
    else:
        print(f"1人{each}円です")

def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        traceback.print_exc()
        print("エラーが出ました。やり直してください。")


if __name__ == "__main__":
    bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}
    check(bill)
    print("プログラムは問題なく終了しました")

# 割り勘する人数を入力してくださいthree
# エラーが出ました。やり直してください。
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/error_exception/102_traceback module.py", line 54, in check
#     split_bill(total_bill)
#   File "/Users/endousou/Desktop/PythonLecture/error_exception/102_traceback module.py", line 45, in split_bill
#     each = price / int(num)
#                    ^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'three'
# プログラムは問題なく終了しました