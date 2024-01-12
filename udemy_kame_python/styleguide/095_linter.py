"""
Linterの種類
・Stylistic Lint：
    iｍport os, sys
    例：一行で二つのモジュールをimportされている
・Logical Lint
    import os, sys
    例：使われていないモジュールがimportされている

PythonのLinter
・Stylistic Lintの代表的なlinter: pycodestyle(元pep8)
・Logical Lintの代表的なlinter: pyflakes

・pycodestyleとpyflakesのラッパーライブラリ：flake8
  ラッパーライブラリ：両方をラッピングしている

・flake8より厳しいlinter: pylint

pycodestyleなどはPycharmで動かす以外にライブラリをインストールしてターミナルで動かす
例：
 pycodestyle 095_linter.py
 pycodestyle --show-source --show-pep8 095_linter.py
 pycodestyle --statics -qq 095_linter.py
 pylint 095_linter.py
"""


import os, sys

x = 1
y =1
print           (x,y)
