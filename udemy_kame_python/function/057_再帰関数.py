# 再帰関数（recurive function）：関数内で自身の関数をCallする関数

# 階乗：3! = 3 * 2 * 1
# n! = n * (n-1) * (N-2) * … * 1
# n! = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))


# • Challenge1: Fibonacci数を計算する関数を再帰で実装してみよう.
# • Fibonacci数列: 0, 1, 1, 2, 3, 5, 8, ... 例: fibonacchi(6) = 8
# • Challenge2: Fibonacci数を計算する関数を再帰なしで実装して， 再帰と比べてどちらが早いか確認してみよう.


# Challenge1
def fibonacchi_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacchi_recursive(n-2) + fibonacchi_recursive(n-1)

print(fibonacchi_recursive(6))  # 8

# Challenge2 再起じゃないバージョン
def fibonacchi(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result

print(fibonacchi(6)) # 8


# 再起を使った場合と使わない場合の処理速度の確認 -> 再起を使ったほうが明らかに遅くなる！！
# 再帰関数を使うと短くわかりやすい文章になるが、処理が遅くなることを覚えておくこと
for i in range(50):
    # print(i, fibonacchi_recursive(i))
    print(i, fibonacchi(i))
