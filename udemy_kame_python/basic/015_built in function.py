# built in function
# type
hello_type = type("Hello")
print(hello_type) # 戻り値：str
print(type("Hello"))
print(type(1))
print(type(1.0000000))

# idの中の"hello"をpythonではObjectと呼ぶ
hello_id = id("hello")
hello = "hello"
hello2 = "hello"
hello3 = "hello3"

# 下記3つのidのアドレスは全て同じ
print(hello_id)
print(id(hello))
print(id(hello2))
# これだけアドレスが違う
print(id(hello3))

