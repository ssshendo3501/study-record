"""
elseとfinally
・else
try:
    例外が起こりうるコード
except <例外> as <変数>:
    例外が起きた時に実行するコード
else:
    例外が起きなかった時に実行するコード

・finally
try:
    例外が起こりうるコード
except <例外> as <変数>:
    例外が起きた時に実行するコード
finally:
    必ず実行するコード

finally:が実行されるタイミング
    finallyのタイミングは複雑なので、必ず簡単なコードで試すこと
・tryでキャッチされない例外が発生した場合でもfinally:を実行してから例外を発生する
・except:やelse:で例外が発生しても、finally:の実行後に例外を発生する
・tryでbreakやcontinue、returnに達しても。その前にfinally:が実行される
・try:tofinally:にreturnがある場合、finally:のreturnが返される
"""


def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as zero_error:
        print("0で割ることはできません。正しい値を入力してください。")
        each = price
        print(zero_error)
    except TypeError as type_error:
        print("文字列は認識できません。正しい値を入力してください。")
        each = price
        print(type_error)
    else:
        print(f"1人{each}円です")
    finally:
        print("ご利用ありがとうございました")


if __name__ == "__main__":
    split_bill(10000)