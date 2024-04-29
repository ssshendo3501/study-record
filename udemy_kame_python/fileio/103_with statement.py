# カレントディレクトリのファイルはopen関数でファイルを開く
f = open("pep8_introduction.txt")

for line in f:
    print(line, end="")

# open関数で開いたファイルはずっとメモリに保存される。
# そのためclose関数で毎回閉じる必要がある
f.close()

# Introduction
# This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python [1].
#
# This document and PEP 257 (Docstring Conventions) were adapted from Guido's original Python Style Guide essay, with some additions from Barry's style guide [2].
#
# This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.
#
# Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.


# print文のendのデフォルトの引数はend="\n"
print("hello", end="")
print("world", end="")

# helloworld


# try finallyでopenを呼んだら必ずファイルを閉じる操作を実施できる
try:
    f = open("pep8_introduction.txt")
    for line in f:
        print(line, end="")
finally:
    f.close()


# 実際には上記のように書くのではなく、withステートメントを使う
# withステートメント
with open ("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")