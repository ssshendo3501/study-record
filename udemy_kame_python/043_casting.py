# Casting：データの型変換

print(type(str(1)))
print(type(1 + int(("1"))))
print(list("hello"))
print(bool(0))
print(tuple([1, 2, 3, 4]))
print(set([1,1,1,1,2,2,2,4,4,3,3]))

# <class 'str'>
# <class 'int'>
# ['h', 'e', 'l', 'l', 'o']
# False
# (1, 2, 3, 4)
# {1, 2, 3, 4}