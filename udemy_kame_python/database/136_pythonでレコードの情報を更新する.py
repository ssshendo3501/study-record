import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

target_name = input("誰のレコードを更新しますか？")
new_age = input("新しい年齢を入力してください")
print(target_name, new_age)

# SQL Injectionの脆弱性あり
# 新しい年齢を入力してください31; Drop table user; はSQL Injectionと呼ばれる有名な攻撃方法
# 他者がuserテーブルをdropしてしまう
# そのため、文字列を操作してSQLを操作するやり方は脆弱性があるので注意

update_query = f"UPDATE user Set age = {new_age} WHERE name = '{target_name}'"
cursor.executescript(update_query)

# 誰のレコードを更新しますか？John
# 新しい年齢を入力してください31; Drop table user;
# John 31; Drop table user;
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/database/136_pythonでレコードの情報を更新する.py", line 13, in <module>
#     cursor.executescript(update_query)
# sqlite3.OperationalError: near "WHERE": syntax error


# 下記のように記載するのが良い
# SQL文を作る場合は、文字列ではなく必ず？で渡す書き方を採用する
update_query = 'UPDATE user Set age = ? WHERE name = ?'
cursor.execute(update_query, (new_age, target_name))
con.commit()


