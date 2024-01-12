# 変数定義

# pythonでは、イコールを揃えて記述するのはダメ
# wrong
xxxxx = 1
yyy   = 1
# correct
xxxxx = 1
yyy = 1

# 関数の引数の「=」にはスペース不要
def complex(real, image=0)
    return magic(r=real, i=image)

# operator周りのスペース1個
x = x + 1
x += 1
x = x*2 + 1
x = x*x + y*y
c = (a + 1) + (b + 1)

# カンマの後にはスペースを入れる
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# カンマの後に閉じ括弧がくる場合はスペース不要
# correct
foo = (0,)
# wrong
foo = (0, )

# Pythonでは最後にカンマがついてもOK
# ただし最後にコンマがくる場合は、閉じ括弧は次の行に書く
# correct
files = [
    'setup.cfg',
    'toc.ini',
    'tox.ini',
    ]
# wrong
files = ['setup.cfg', 'toc.ini', 'tox.ini', ]



