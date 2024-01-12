# private変数と名前修飾（name mangling）

"""
・private変数は外からアクセスできない変数
・Pythonには「private変数」はない
・変数名の接頭辞「_」(アンダースコア)をつけることで、non public変数にすることができる
    ・慣習であって強制力はない
・「__」(ダブルアンダースコア)をつけることで名前修飾する
    ・名前修飾された変数名は"_クラス名__attribute"のような形になる
      ・例：_Account__balance
    ・結果、private変数のような役割をつけることができる
"""


# non pubulic変数：_変数名
# pythonではprivate変数は存在しないため、non public変数と呼ぶのが正しい
# 参照は難しくなるが強制力は弱め。あくまで慣習。
class Account:

    def __init__(self, balance):
        self._balance = balance  # 残高は外からアクセスしたくない関数

    def deposit(self, price):
        self._balance += price

    def withdraw(self, price):
        if self._balance < price:
            print("残高不足")
        else:
            self._balance -= price

    def show_balance(self):
        print(f"残高は{self._balance}円です。")


myaccount = Account(10000)
myaccount.deposit(2000)
myaccount.withdraw(200)
myaccount.show_balance()

# 残高は11800円です。

# インスタンス変数に"balance"を引数に指定しておくと、外からアクセスできてしまい、簡単に残高を書き換えられてしまう
# そこで、引数"balance"を"_balance"にすることで外からアクセスできなくなる
myaccount = Account(1000)
# myaccount._balanceは外からアクセスされないように予測に出てこなくなる(指定すれば変換することは可能)
print(myaccount._balance)
myaccount.show_balance()

# 1000
# 残高は1000円です。

# myaccountインスタンスの属性をdir()で確認する > _balanceがあるのを確認
print(dir(myaccount))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  '__weakref__', '_balance', 'deposit', 'show_balance', 'withdraw']



# 名前修飾：__変数名
class Account2:

    def __init__(self, balance):
        self.__balance = balance  # 残高は外からアクセスしたくない関数

    def deposit(self, price):
        self.__balance += price

    def withdraw(self, price):
        if self.__balance < price:
            print("残高不足")
        else:
            self.__balance -= price

    def show_balance(self):
        print(f"残高は{self.__balance}円です。")


myaccount2 = Account2(10000)
myaccount2.withdraw(200)
myaccount2.deposit(1000)
myaccount2.show_balance()

print(dir(myaccount2))

# 残高は10800円です。
# print(myaccount2.__balance) # AttributeError: 'Account2' object has no attribute '__balance'.

# __変数名で名前修飾しておけば、show_balanceをした時には正しい残高の値が入っているのを確認
# print(myaccount2.__balance)　で-1000が出力される理由は、myaccount2.__balance というクラスとは別の変数が作られているということになる
myaccount2.__balance = -1000 # 意図的に残高を書き換えてみる
print("------myaccount2.__balance = -1000------")
myaccount2.show_balance()
print(myaccount2.__balance)

# ------myaccount2.__balance = -1000------
# 残高は10800円です。
# -1000

# myaccount2の属性確認：'_Account2__balance'が
print(dir(myaccount2))

# ['_Account2__balance', '__balance', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'deposit', 'show_balance', 'withdraw']
