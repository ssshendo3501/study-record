# lambda関数（無名関数）

# lambdaを使わないバージョン
def square(x):
    return x * x


# lambdaバージョン
s = lambda x: x * x

print(square(3)) # 9
print(s(5)) # 5

# 実際、s = lambda x: x * x のように、関数オブジェクトを変数に入れるやり方はあまりしない
# ある関数を呼ぶ時に、引数としてlambda関数を使う

# lambda使わないバージョン
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

# lambda使うバージョン
def power(exponent):
    return lambda base: base ** exponent

third_power = power(3)
print(third_power(4)) # 64

numbers = [6, 2, 5, 4, 88, 65, 324, 111, 435]

# filter関数を使ってnumbersから奇数だけ残す関数を作る

# lambdaなしバージョン
def filterfunc(num):
    if num % 2 == 0:
        return False
    else:
        return True

for num in numbers:
    print(filterfunc(num))

filtered_num = filter(filterfunc, numbers)
print(list(filtered_num))

# lambda有りバージョン
filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))

# [5, 65, 111, 435]

