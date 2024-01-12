"""
例外（Exception）：
・例外が起きると、プログラムはクラッシュする。
・例外が起こる可能性が亜ある場合は、例外処理（exception handling）する必要がある
・Pythonにはすでに色々な例外がクラスとして定義されている。

例：
　ZeroDivisionError：0で割った時に起こる例外
　TypeError：関数の演算子のタイプに問題がある時に起きる例外（例：1 + "1"）
　ValueError：関数や演算子の引数のタイプは正しいが値に問題がある時に起きる例外（例：int("one")）

try exceptでハントリングする
try:
    例外が起こりうるコード
except <例外> as <変数>:
    例外が起きた時に実行するコード
"""

# 下記はnumに0が入ってしまうとZeroDivisionErrorになる
def split_bill(price):
    num = input("何人で割り勘しますか？")
    each = price / int(num)
    print(f"1人{each}円です")


# try exceptで処理する
def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except:
        print("エラーが発生しました。正しい値を入力してください。")
        each = price
    print(f"1人{each}円です")

if __name__ == "__main__":
    split_bill(10000)

# 何人で割り勘しますか？0
# エラーが発生しました。正しい値を入力してください。
# 1人10000円です


# except 例外　とすることで、ZeroDivisionErrorの時のものをキャッチできる
def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0で割ることはできません。正しい値を入力してください。")
        each = price
    print(f"1人{each}円です")


if __name__ == "__main__":
    split_bill(10000)

# 何人で割り勘しますか？0
# 0で割ることができません。正しい値を入力してください。
# 1人10000円です


# except 例外 as 変数 とすることで、エラーメッセージを表示できる
# 0以外のstringが入れられるとValueErrorなど他のエラーが発生してしまう可能性もあるため、
# except 例外で繋げる
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
    print(f"1人{each}円です")


if __name__ == "__main__":
    split_bill(10000)

# 何人で割り勘しますか？0
# 0で割ることはできません。正しい値を入力してください。
# division by zero
# 1人10000円です


