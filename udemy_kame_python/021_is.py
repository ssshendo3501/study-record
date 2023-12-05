# is演算子：同じオブジェクトかどうかを判定する
# Pythonは同じ文字列であるかをよく使う

a = 1
b = 1
c = 2
d = a

print(a is b) # True
print(a is not b) # False
print(a is not c) # True
print(a is d) # True
print(d is b) # True

# a,b,dはすべて「1」の同じアドレスを指す
print(f"a:{id(a)}, b:{id(b)}, c:{id(c)}, d:{id(d)}")

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello is hello2)
print(f"hello:{id(hello)}, hello2:{id(hello2)}")
hello = "konnichiha"
print("hello:4560785248, hello2:4560785248")
print(f"hello:{id(hello)}, hello2:{id(hello2)}")
print(hello2)
print(hello)

# isはよくNoneかどうかの判定に使う
# Noneはundefinedとは違うので注意
nothing = None
print(None)
print(nothing is None) # True
print(f"nothing:{id(nothing)}, None:{id(None)}")
# nothing:4475961264, None:4475961264