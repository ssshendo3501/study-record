from .mymodule3 import myfunc3
# from ..subdir import mymodule3  # これも同じ

from .. import mymodule1 # mympdule1を呼び出す時
from ..mymodule1 import myfunc as mymodule1_func # myfuncが被るのでこういう書き方もできる

def myfunc():
    print("This is myfunc from module2")


def myfunc2():
    print("This is myfunc2 from module2")
    myfunc3()
    mymodule1.myfunc()
    mymodule1_func()
