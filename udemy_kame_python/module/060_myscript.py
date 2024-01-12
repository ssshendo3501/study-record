# 060_module

# 同じ階層のmymoduleを別のスクリプトで使えるようにするためには、importを実施
# mymodule.関数()　でimportした関数を呼び出すことができる
# 変数も呼び出すことができる
import mymodule

mymodule.myfunc()
print(mymodule.myvaliable)

# This is my function!
# This is global valiable


# from mymodule import myfunc でmyfunc()のみで関数を呼び出すことができる
from mymodule import myfunc, myvaliable, anotherfunc

myfunc()
print(myvaliable)
anotherfunc()

# This is my function!
# This is global valiable
# This is another function!


# from mymodule import * でmymoduleのすべての関数を呼び出すことが可能
# ただし、from mymodule import *　は"_関数名"のものは呼び出すことができない->エラーになる
# この理由は、_関数は、外からアクセスできない関数であるということを意味しているため（ノンパブリックファンクション）
# -> mymoduleの中でしか_anotherfuncは使えない
# また、from mymodule import *　は非推奨であるため注意！
from mymodule import *
myfunc()
print(myvaliable)
anotherfunc()

# import mymodule as mm とすることで、毎回mymoduleと書かなくて済む
# ただし、これは自作の関数ではあまり推奨されないので注意
import mymodule as mm
mm.myfunc()
mm.anotherfunc()
print(mm.myvaliable)


# 061_sys module

import sys
print(sys.path)
