# scope

# 下記のように関数の中に定義された変数(first_name, last_name)をローカル変数と呼ぶ
# 関数の中で定義された変数は、関数の外で使うことができない
def print_name_local():
    first_name = 'Taro'
    last_name = 'Yamada'
    print(f"I'm {first_name} {last_name}")

print_name_local() # I'm Taro Yamada
# print(first_name) # NameError: name 'first_name' is not defined

# 関数の外で定義される変数をグローバル変数と呼ぶ
# グローバル変数のageとローカル変数のageはscopeが違うので参照しない
age = 30 # グローバル変数
def print_age():
    age = 20 # ローカル変数
    print(f"I'm {age} years old")

print_age()
print(age)
# I'm 20 years old
# 30

# ローカル変数をコメントアウトするとグローバル変数が参照され問題なく実行できる
# pythonは最初にローカル変数を確認し、なければグローバル変数を参照して実行する
age = 30 # グローバル変数
def print_age():
    # age = 20 # ローカル変数をコメントアウト
    print(f"I'm {age} years old")

print_age()
print(age)
#I'm 30 years old
# 30


# 関数の中に "global 変数名" を記載することで、ローカル変数ではなくグローバル変数と定義できる
age = 30 # グローバル変数
def print_age():
    global age # ageはローカル変数ではなくグローバル変数と定義できる
    age = 20 # グローバル変数age=30に対して20を上書きしている意味
    print(f"I'm {age} years old")

print_age()
print(age)
#I'm 30 years old
# 30
