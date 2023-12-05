# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f'I love {fruit}!!')

# I love apple!!
# I love peach!!
# I love grapes!!
# I love banana!!

for char in "hello world!!":
    print(f'char: {char}!')

# char: h!
# char: e!
# char: l!
# char: l!
# char: o!
# char:  !
# char: w!
# char: o!
# char: r!
# char: l!
# char: d!
# char: !!
# char: !!

# iterationとiterator

'''
• Challenge1: ユーザに好きなフルーツを入力してもらい，
fruitsリストの各フルーツに対して「好き/好きじゃない」をprint()する
• Challenge2: fruitsリストの各フルーツに対して「好き/好きじゃない」をユーザに聞いて，
好きなフルーツリスト，好きじゃないフルーツリストを作成する
'''
# challenge1
# selected_fruit = input("好きなフルーツを入力してください。")
#
# for fruit in fruits:
#     if fruit == selected_fruit:
#         print(f"{fruit}は好きです")
#     else:
#         print(f"{fruit}は好きじゃないです")

# challenge2:自分の回答（これだと好きなものを最初にしか答えられない）
# selected_fruit = input("好きなフルーツを入力してください。")
# fabvorite_fruits_list = []
# not_fabvorite_fruits_list = []
#
# for fruit in fruits:
#     if fruit == selected_fruit:
#         print(f"{fruit}は好きです")
#         fabvorite_fruits_list.append(fruit)
#     else:
#         print(f"{fruit}は好きじゃないです")
#         not_fabvorite_fruits_list.append(fruit)
# print(fabvorite_fruits_list)
# print(not_fabvorite_fruits_list)

# challenge2 正解
fabvorite_fruits_list = []
not_fabvorite_fruits_list = []

for fruit in fruits:
    choise = input(f"{fruit}は好きですか? y/n")
    if choise == 'y':
        fabvorite_fruits_list.append(fruit)
    else:
        not_fabvorite_fruits_list.append(fruit)
print(f'fabvorite_fruits_list: {fabvorite_fruits_list}')
print(f'not_fabvorite_fruits_list: {not_fabvorite_fruits_list}')
