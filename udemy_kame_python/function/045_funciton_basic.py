# 関数（function）

# 華氏から摂氏に変更する

fahrenheit = 50
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# 関数と関数の間は２行開ける
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)