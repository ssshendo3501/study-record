"""
・クラスに書くdocstringも関数の時と同様に、クラスの中に書く
・Attributes（属性）とMethods（メソッド）を書くとわかりやすい

"""


class Duck:
    """
    This is a class for Duck

    Attributes:
        name: the name of duck

    Methods:
        walk: print ***
        quack: print ***
        fly: print ***
    """
    def __init__(self, name):
        """
        The constructor for duck class
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack, quack...!!!")

    def fly(self):
        print("flying...")


print(help(Duck))

"""
class Duck(builtins.object)
 |  Duck(name)
 |
 |  This is a class for Duck
 |
 |  Attributes:
 |      name: the name of duck
 |
 |  Methods:
 |      walk: print ***
 |      quack: print ***
 |      fly: print ***
 |
 |  Methods defined here:
 |
 |  __init__(self, name)
 |      The constructor for duck class
 |      :param name: the name of the duck
 |
 |  fly(self)
 |
 |  quack(self)
 |
 |  walk(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 """


print(help(Duck.__init__))

"""
Help on function __init__ in module __main__:

__init__(self, name)
    The constructor for duck class
    :param name: the name of the duck

None
"""


print(help(Duck.__init__.__doc__))

"""
No Python documentation found for 
    'The constructor for duck class\n        
    :param name: the name of the duck'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
"""

