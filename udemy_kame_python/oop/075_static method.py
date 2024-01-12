# 075＿Static Method

"""
スタティックメソッド
・インスタンスに紐づかないメソッド
・@staticmethodデコレータを使う
・主にクラス内で便利関数のように使用する
・引数にselfを取らない（インスタンスの情報は使わない）
・クラスからアクセスしてcallする（クラス名.スタティックメソッド名）
・クラスの情報を使う場合はクラスメソッドを使う
"""

class MyClass:

    def mymethod(self):
        print("This is normal method")

    @staticmethod
    def mystaticmethod():
        print("This is static method")


# Normal Methodはインスタンスを生成してからメソッドを呼び出す
c = MyClass()  # クラスからインスタンスを生成
print(c)  # インスタンスであるか確認
c.mymethod() # インスタンスからメソッドを呼び出す

# <__main__.MyClass object at 0x105be3920>
# This is normal method


# Statuc Methodは、クラス名から直接呼び出すことができる
# Static methodは実はインスタンスからも呼び出すことができる
# Pythonはインスタンス名.メソッド名でメソッドを呼ぶと最初にインスタンンスの中のメソッドを探し、なかったらクラスのstatic methodなどを呼ぶ
# mymethod()で〰波線のエラー通知が出ている理由は、mymethodのselfを使っていないので、インスタンスメソッドである必要がなく、
# スタティックメソッドで記載した方が良いのでは？という提案の通知

MyClass.mystaticmethod()
c.mystaticmethod()

# This is static method
# This is static method


"""
Challenge
• 前回のChallengeで作成したAccountクラスに，取引(transaction)
 を記録する仕組みを追加する
• 取引(transaction)として保持する情報は 
    • ”withdraw/depositの金額”
    • “新しい残高”
    • “日時”
• それぞれの取引情報をdictionaryとして保持し，それをlistでインスタンス変数で保持すればOK
• “日時”を作る関数をstaticmethodで作ってみよう
"""

import time


class Account:

    # クラス変数
    count = 0

    # インスタンス変数
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self.add_transaction(-amount)
        else:
            print(f"残高{self.balance}円が足りません")

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.add_transaction(amount)

    def show_balance(self):
        print("{0.name}(口座番号：{0.account_number})の残高は{0.balance}円です。".format(self))

    def add_transaction(self, amount):
        transaction = {
            "withdraw/deposit" : amount,
            "new_balance" : self.balance,
            "time" : Account.get_time_str()
        }
        self.transaction_history.append(transaction)

    # 取引日時を保持するスタティックメソッド
    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    # transaction_historyの辞書を出力するメソッド
    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for key, value in transaction.items():
                transaction_str_list.append(f"{key}: {value}")
            print(", ".join(transaction_str_list))



myaccount = Account(name="satou", balance=10000)
print(myaccount.name)
print(myaccount.balance)
myaccount.withdraw(200)
print(myaccount.transaction_history)
print(Account.get_time_str()) # get_time_str()はStaticmethodなので、クラス名から呼ぶ
myaccount.show_balance()
myaccount.show_transaction_history()

# satou
# 10000
# satou(口座番号：0)の残高は9800円です。
# [{'withdraw/deposit': -200, 'new_balance': 9800, 'time': '2024年1月11日9時49分'}]
# 2024年1月11日9時49分
# satou(口座番号：0)の残高は9800円です。
# withdraw/deposit: -200, new_balance: 9800, time: 2024年1月11日9時49分