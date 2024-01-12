"""
Packageとは？
・複数のPythonモジュールをディレクトリにまとめたもの
・「.」を使うことでモジュールにアクセスできるようになる
・通常ディレクトリに__init__.pyという特殊なファイルを作成することで、
　そのディレクトリ空間がパッケージとして認識される
・__init__.pyがないと「名前空間パッケージ」と認識される

名前空間とは？
・mymodule1のmufuncはmyfirstpackage.mymodule1.myfunc(という名前空間)に属する
・同じ関数名であっても、属する名前空間が異なれば別物として扱うことができる
・__init__がないパッケージ
・異なるパスに存在する同名のパッケージを共通のものとしてまとめることが可能
・特に理由がなければ、__init__.pyを作って通常のパッケージとすること
"""

module.mymodule1.myfunc()
module.subdir.mymodule2.myfunc()

# This is myfunc from module1
# This is myfunc from module2


# 下記のように書けば、myfirstpackage.は不要
from myfirstpackage import mymodule1
from myfirstpackage.subdir import mymodule2

mymodule1.myfunc()
mymodule2.myfunc()


# 関数だけimportすることもできる
from myfirstpackage.mymodule1 import myfunc

myfunc()