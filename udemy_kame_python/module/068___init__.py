"""
__init__
・__init__.pyを置くことで、Pythonはそのディレクトリをパッケージとして認識する
・__init__.pyには初期化用コードを記述する（import時に実行される）
・__init__.pyにimport文を書くことでモジュール名をスキップしてpackageの後に
　関数名やクラス名にアクセスできる
・__init__.pyに__all__を定義することで、そのパッケージがimport *でインポートされた際、
　インポートされる関数やクラスを定義することができる
"""

from myfirstpackage.subdir.mymodule2 import myfunc

myfunc()

# This is myfunc from module2


# __init__にfrom myfirstpackage.subdir.mymodule2 import myfuncを書いておけば
# import myfirstpackageでmymodule2のmyfuncを呼び出すことができる
# ライブラリ名.関数名で実施できる（pandas.read_csv()みたいなものと同じ）

module.myfunc()

# This is myfunc from module2


# subdirの__init__.pyにfrom .mymodule2 import *と__all__ = ['myfunc']を書くと
# パッケージ名を書かなくても関数を呼び出すことができる
from myfirstpackage.subdir import *

myfunc()
# myfunc2()　#エラーになる