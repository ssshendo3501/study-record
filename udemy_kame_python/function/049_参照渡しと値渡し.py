# 参照渡し　<->　値渡し

def add_nums(a, b):
    print(f"第1引数aのID: {id(a)}")
    print(f"第2引数bのID: {id(b)}")
    return a + b


one = 1
two = 2
print(f"oneのID: {id(one)}")
print(f"twoのID: {id(two)}")
print(add_nums(one, two))

# oneとa,　twoとbはidが同じになる：Pythonは参照渡し
# oneのID: 4462145248
# twoのID: 4462145280
# 第1引数aのID: 4462145248
# 第2引数bのID: 4462145280
# 3


# 引数の渡し方はミュータブルとイミュータブルなオブジェクトで挙動が違ってくる
# 下記はint型：イミュータブルな場合は値渡しをしているように見える
def add_one(num):
    print(f"変更前のID: {id(num)}")
    num += 1
    print(f"変更後のID: {id(num)}")
    return num

one = 1
print(f'oneのid: {id(one)}')
print(f"関数呼び出し前のone: {one}")
add_one(one)
print(f'oneのid: {id(one)}')
print(f"関数呼び出し後のone: {one}")

# oneのid: 4543934176
# 関数呼び出し前のone: 1
# 変更前のID: 4543934176
# 変更後のID: 4543934208
# oneのid: 4543934176
# 関数呼び出し後のone: 1

# list型：ミュータブルなオブジェクトは参照渡しのような挙動
def add_fruits(fruits, fruit):
    print(fruits)
    print(f"変更前のID: {id(fruits)}")
    fruits.append(fruit)
    print(fruits)
    print(f"変更後のID: {id(fruits)}")
    return fruits


myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'

add_fruits(myfruits, myfruit)

# ['apple', 'banana', 'peach']
# 変更前のID: 4374497536
# ['apple', 'banana', 'peach', 'lemon']
# 変更後のID: 4374497536