# Third party library

# ライブラリ：複数のパッケージをまとめてインストール可能にしたもの
# ・pyPI（the Python Package Index）：
# Pythonのサードパーティのライブラリやパッケージを管理しているリポジトリ
# PyPIから様々なライブラリをインストールすることが可能
# https://pypi.org/
#
# ・pip
# Pythonパッケージ管理システム
# PuPIからパッケージをダウンロードして、システムにインストールできる
# Pythonの標準ライブラリとして入っている


# ターミナルでpip install numpy実施

import sys
import numpy as np


print(np.__file__)
print(sys.path)