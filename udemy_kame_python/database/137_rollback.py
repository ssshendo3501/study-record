"""
ロールバック
・ロールバックを使うと、コミットする前のペンディングになっているSQLをキャンセルすることができる
・本元のテーブルと、更新履歴を管理したい時などにロールバックを利用することがある
・複数のテーブルを同時に更新する際に、どちらかでエラーが出たら、Rollbackする必要がある
・Rollbackしないと、データの辻褄が合わなくなってしまう
"""

import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()
create_history_table_query = '''
CREATE TABLE IF NOT EXISTS History (
    Name TEXT,
    Age INTEGER
)
'''

cursor.execute(create_history_table_query)
target_name = input("誰の年齢を変更しますか？")
new_age = input("年齢を入力してください")

update_user_query = 'UPDATE user SET age = ? WHERE name = ?'
insert_history_query = 'INSERT INTO History VALUES (?, ?)'


# 普通は、userテーブルの本元のテーブルを更新してからHistoryのテーブルを更新するが、
# HistoryのテーブルのINSERTを先に書いてから年齢を-100などにすると、
# Historyのデータは更新されるが、userテーブルは更新されない
try:
    cursor.execute(insert_history_query, (target_name, new_age))  # userと年齢の更新テーブル
    cursor.execute(update_user_query, (new_age, target_name))  # userテーブル
# 年齢が-100歳などになった時のエラー対応
except sqlite3.Error:
    print("sqlite3 error occured")
    # Historyのテーブルを元に戻すために、
    con.rollback()
else:
    con.commit()
