# 文字列
print('hello-world!!')
print(1)

print("I'm fine!")

# シングルクォーテーションで文字型を書くとバグになることもある
# print('I'm fine!')

# ダブルクォーテーション3つで囲むことで改行できる
print("""
hello world
How are you?
""")

# \nで出力時に改行できる
print('hello \nworld!!')

# \tはタブ
print('hello \tworld!!')

# \nを文字列として扱う場合はバックスラッシュをもう１個つける
print('bash sleep:\\n')

# 上でバグになったものもこれで直せる
print('I\'m fine!')

# + で文字列を連結できる
print('hello' + 'world' + '!!')

# hello world
# How are you?
#
# hello
# world!!
# hello 	world!!
# bash sleep:\n
# I'm fine!
# helloworld!!