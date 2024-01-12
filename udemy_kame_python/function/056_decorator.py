#　Decorator：関数に機能を付属する（デコレートする）

def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!!")
        func(*args, **kwargs)
        print("Nice to meet you!")
    return inner

# デコレータ関数の書き方：機能追加したい関数に@をつける
# 下記では、say_name関数にgreeting関数をデコレート関数として記載している
@greeting
def say_name(name):
    print(f"I'm {name}")

# @greeting ########### errorになる -> greetingのinner関数がnameのみしか変数がないため
# デコレータ関数を汎用的に使うTipsとして、inner関数を"*args､ **kwargs"とする
@greeting
def say_name_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")

# greetingの関数の中に、say_nameの関数：funcを入力している
# I'm Jiroしか出力しなかったsay_nameの関数に、greetingの機能が追加されている
# say_nameがgreetingによりデコレータされ機能追加され、新たなsay_name関数が生成されている
say_name = greeting(say_name)
say_name("Jiro")

# Hello!!
# I'm Jiro
# Nice to meet you!

say_name_origin("Taro", "Tokyo")

# Hello!!
# I'm Taro, I'm from Tokyo
# Nice to meet you!

