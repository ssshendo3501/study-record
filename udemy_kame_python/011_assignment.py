# 変数へ代入

# 変数を変える時は右クリックでrefactor→renameできる
hello = "hello"
world = "world"

print(hello + world)

# ハードコーディング：変数を使わないこと
# pythonでは推奨されない
print("hey" + "Sakai")

# format
print("{} {}".format(hello, world))

name = "Emily"
print("Hey! {}!".format(name))

balance = 100
print("balance: {}".format(balance))

# fstring
print(f'{hello} {world}!!')
print(f'balance: {balance}')
print(f'Hey! {name}! How are you doing?')