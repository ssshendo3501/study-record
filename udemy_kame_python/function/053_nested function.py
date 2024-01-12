# 関数の中で関数を定義（nested function）

msg = 'I am global'
def outer():
    msg = 'I am outer'

    def inner():
        msg = 'I am inner'
        print('This is inner function.')
        print(msg)
    inner()
    print(msg)


outer()
print(msg)

# I am inner
# I am outer
# I am global

# inner() # NameError: name 'inner' is not defined.：外からはinner()の関数がみえないのでエラーになる


msg = 'I am global'
def outer():
    msg = 'I am outer'

    def inner():
        nonlocal msg
        msg = 'I am inner'
        print('This is inner function.')
        print(msg)
    inner()
    print(msg)


outer()
print(msg)

# This is inner function.
# I am inner
# I am inner
# I am global
