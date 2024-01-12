# *arg : 不特定の多数を渡すことが可能

def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num

# get_averageの引数の中身が何個でも可能
average = get_average(1,2,3,4,5,6,7,8)
print(average)

# **kwargs : 辞書型で*argsを受け取る
def kwargs_func(**kwargs):
    param1 = kwargs.get('param1', 1) # デフォルト1
    param2 = kwargs.get('param2', 2) # デフォルト2
    param3 = kwargs.get('param3', 3) # デフォルト3
    print(f'param1: {param1}, param2: {param2}, param3: {param3}')


kwargs_func(param1=10, param2=6, param4=5)
# param1: 10, param2: 6, param3: 3


# *と**やunpacking operator
numbers = (1,2,3)
print(*numbers)
print(1,2,3)