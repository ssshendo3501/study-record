# Closure: クロージャ

# pythonは全てをオブジェクトとして扱う
# そのため、関数もオブジェクト

def compute_square(num):
    return num * num

f = compute_square
print(type(f)) # <class 'function'>
print(f(10)) # 100

# 関数もオブジェクトなのでlistの中にいれることができる
function_list = ['1', 1, True, f]
print(function_list[-1](10)) # 100

# 関数も引数として渡せる
def execute_func(func, param):
    return func(param)

print(execute_func(f, 10)) # 100


# 関数をreturnする

def return_func():

    def inner_func():
        print("This is an inner function")
    return inner_func  # inner_func()と()がついていないので、inner_funcをオブジェクトとして返す

f = return_func()
print(type(f))
f()

# <class 'function'>
# This is an inner function


# Closure: ネスト関数を使って状態をキープした関数を作ることができる
# 状態が静的の例
def power(exponent):

    def inner_power(base):
        return base ** exponent
    return inner_power

power_four = power(4)
print(power_four(2)) # 16 = 2 ** 4

power_five = power(5)
print(power_five(2)) # 32 = 2 ** 5

power_two = power(2)
print(power_two(5)) # 5 = 5 ** 2

# 状態が動的の例
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))  # 5.0 = 5 / 1
print(average_nums(15)) # 10.0 = (5+15) / 2
print(average_nums(15)) # 11.666666
print(average_nums(10)) # 11.25


