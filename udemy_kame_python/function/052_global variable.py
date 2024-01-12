# call_countを関数間で共有したい時、globalを使う

call_count = 0
CALL_COUNT = 0 # constant変数：pythonの命名規則では、変数名を大文字で書くと後から変更されたくないと共通認識できる

def print_count1():
    global call_count
    call_count += 1
    print(f"関数1: {call_count}回目")


def print_count2():
    global call_count
    call_count += 1
    print(f"関数2: {call_count}回目")


print_count1()
print_count2()
print_count1()
print_count1()
print(f'call_count: {call_count}')

# 関数1: 1回目
# 関数2: 2回目
# 関数1: 3回目
# 関数1: 4回目
# call_count: 4