fruits = ['apple', 'peach', 'melon', 'grapes']

# for文のelse

for fruit in fruits:
    print(fruit)
else:
    print("ループは終了しました。")

# apple
# peach
# melon
# grapes
# ループは終了しました。

# for fruit in fruits:
#     choice = input(f"あなたが探しているフルーツは{fruit}ですか？ -> y/n")
#     if choice == "y":
#         print(f"{fruit}ですね！見つかってよかったですね！")
#         break
#     else:
#         print("そうですか...")
#         continue  # ここは省略可能
# else:
#     print("この中にはあなたの探しているフルーツはないようです")

# whileのelse

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("ループは終了しました")

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# ループは終了しました

balance = 1000
game_price = 100

while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しますか？　(残高：{balance}円) -> y/n")
    if choice == "y":
        balance -= game_price
        print(f"現在の残高：{balance}円")
        continue
    elif choice == "n":
        print("また遊びましょう！")
        break
    else:
        print("y or n で答えてください")
else:
    print(f"あなたの残高は{balance}円です。もうお金は無くなっちゃいました。")

