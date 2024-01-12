# 074 challenge

"""
Challenge
• 銀行口座のAccountクラスを作ろう
• 残高(balance)と口座名(name)をもとに口座(Account)を作る
• withdrawメソッドとdepositメソッドで残高を変更する
• 残高が足りなければ引き落とせないようにする
• 口座番号(account_number)はいままで作成された口座のIDとなるように連番を振る(0, 1, 2, 3, 4, ...)
• 残高が変更されたら口座名，口座番号とその残高を表示する
"""

# 自分で書いたコード
class Account:

    # クラス変数
    account_number = 0

    # インスタンス変数
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        Account.account_number +=1

    def withdraw(self):
        withdraw = int(input("いくら引き出しますか？"))

        while True:
            if withdraw > self.balance:
                print(f"残高不足です、{self.balance}より小さい金額を入れてください")
                withdraw = int(input("いくら引き出しますか？"))
            else:
                self.balance -= withdraw
                print(f"{self.name}さん、あなたの今の残高：{self.balance}円です。")
                break

    def deposit(self):
        deposit = int(input("いくら預けますか？"))
        self.balance += deposit
        print(f"{self.name}さん、あなたの今の残高：{self.balance}円です。")



# satou = Account(4000, "Satou")
# print(satou.name)
# print(satou.balance)
# print(satou.account_number)
# satou.withdraw()
# satou.deposit()


# 回答
class Account:

    # クラス変数
    count = 0

    # インスタンス変数
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        Account.count += 1

    def withdraw(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            self.show_balance()
        else:
            print(f"残高{self.balance}円が足りません")

    def deposit(self, ammount):
        self.balance += ammount
        self.show_balance()

    def show_balance(self):
        # print(f"{self.name}の残高は{self.balance}円です。")
        print("{0.name}(口座番号：{0.account_number})の残高は{0.balance}円です。".format(self))


myaccount = Account(name="my account", balance=10000)
print(myaccount.balance)
print(myaccount.name)
myaccount.withdraw(200)
