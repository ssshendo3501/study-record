# 数値型(Numeric)：integer、float、complex

print(type(100))
print(type(0.1))
print(0.3 + 0.3 + 0.3)  # コンピュータは単純に0.9と打つことはできない

# 数値演算子(Numeric Operator)
print(1 + 0.4)
print(2 * 3)
print(1 / 2)
print(6*6 - 6/2)

result = 1 + 1.0
print(f'type of result:{result} is {type(result)}')

# その他の演算
print(14 // 3) # 4が返る（あまりの前）　float dvision
print(14 % 3) # あまりが返る　modulo
print(2 ** 3) # べき乗計算　exponentiation 冪乗

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(remain)

# argument assignment（+=, -=, *=, /=）
a = 1
print(a)
a += 1 # a = a + 1 と同じ
print(a)