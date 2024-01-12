"""
Error
・Syntax error（構文エラー）
  Pythonの書き方が正しくないケース
・Exception（例外）
  書き方は合っているがプログラムが動かないケース

Errorの対処法：Tracebackを読む
・どこでエラーが起きているか
・なぜエラーが出ているか
・エラーメッセージをきちんと読む

・Tracebackは下から上に読む
"""

# Syntax error
x = 0
if x == 0
    print(x / 0)

# /Users/endousou/Desktop/PythonLecture/error_exception/venv/bin/python /Users/endousou/Desktop/PythonLecture/error_exception/096_error.py
#   File "/Users/endousou/Desktop/PythonLecture/error_exception/096_error.py", line 18
#     if x == 0
#              ^
# SyntaxError: expected ':'

# Exception
x = 0
if x == 0:
    print(x / 0)

# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/error_exception/096_error.py", line 18, in <module>
#     print(x / 0)
#           ~~^~~
# ZeroDivisionError: division by zero