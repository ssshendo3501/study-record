# + 演算子でlistを結合できる

print([1,2,3]+ [4,5,6])

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

# listの結合をする時は、+ と appendの
a.append(b)
print(a) # [1, 2, 3, [4, 5, 6]]

a += b # a = a + b
print(a)
