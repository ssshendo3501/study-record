# ファイルの読み込み方法1
# for文でループを回す
# for文で回す場合、lineに入るのは各行になる
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")


# ファイルの読み込み方法2
# .read()のファイルの中身をすべて一つのstringで表す
# f.readはすべてを返すので、容量の大きいファイルを操作する時は注意する
with open("pep8_introduction.txt") as f:
    print(f.read())


# ファイルの読み込み方法3
# .readline()で一行ずつ取得してstringで返す
# readlineでは一行ずつ取得して最後にNoneが入ることになる
# while文でNoneになるまで一行ずつもってくる
with open("pep8_introduction.txt") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()


# ファイルの読み込み方法4
# readlines()ですべての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)

# ['Introduction\n', 'This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python [1].\n', '\n', "This document and PEP 257 (Docstring Conventions) were adapted from Guido's original Python Style Guide essay, with some additions from Barry's style guide [2].\n", '\n', 'This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.\n', '\n', 'Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.']