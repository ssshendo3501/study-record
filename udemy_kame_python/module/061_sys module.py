import sys

print(sys.path)

# ['/Users/endousou/Desktop/PythonLecture/module', '/Users/endousou/Desktop/PythonLecture/module', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload', '/Users/endousou/Desktop/PythonLecture/module/venv/lib/python3.12/site-packages', '/Users/endousou/Desktop/PythonLecture/function/']


# sysのpathに前回作ったfunctionのdocstringの関数を呼び出し
# importすると、docstringが出力されてしまうため。対処する必要がある
sys.path.append("/Users/endousou/Desktop/PythonLecture/function/")
import docstring

print(docstring.multiply(3, 4))

#     multiply num1 with num2 and return the result
#     :param num1: first number that you want to multiply
#     :param num2: second number that you want to multiply
#     :return: num1 * num2
#
# Help on function multiply in module docstring:
#
# multiply(num1, num2)
#     multiply num1 with num2 and return the result
#     :param num1: first number that you want to multiply
#     :param num2: second number that you want to multiply
#     :return: num1 * num2
#
# 12

# importのモジュールを呼び出す順番
# import xxx, yyy, zzzなど、連続で書けるが、この書き方はあまり推奨されない
# import xxx
# import yyy
# import zzz
# 上記のように書くのが一般的
# 標準ライブラリ（sysとか）。サードパーティライブラリ（pandasとか）、自分たちのライブラリ、ローカルのライブラリ
# それぞれのライブラリをアルファベット順で書くとわかりやすくなる
# また、標準ライブラリやサードパーティなど種類が異なるライブラリをimportする際は、１行空けるなどをする
