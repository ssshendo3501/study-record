"""
raise
・特定の例外を発生させることができる
・raise <例外クラス> もしくはraise <例外インスタンス>の形を取る
    ・raise ValueError / raise ValueError()
・例えばtry exceptをテストする際に使う
"""


try:
    # TODO あとで削除する
    raise ValueError()
except ValueError:
    print("Do something")
    raise  # exceptの中にraiseを書くことでその例外を発生させることができる

# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/error_exception/099_raise.py", line 8, in <module>
#     raise ValueError()
# ValueError
# Do something
