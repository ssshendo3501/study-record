# importのStyle

# correct
import os
import sys
# wrong
import os, sys

# correct
from subprocess import Popen, PIPE


# 書く順番
# 1. 標準ライブラリ（time,sys,,,）
# 2. サードパーティライブラリ（numpy,pandas,,,）
# 3. 自分たちのチームのライブラリ
# 4. ローカルライブラリ
# それぞれ一行あける (abc順)

# absolute import
import myokg.sibling
from mypkg import sibling
from mypkg.sibling import example
