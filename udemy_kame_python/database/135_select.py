import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

cursor.execute("select * from user")
print(next(cursor))
print(next(cursor))
print(next(cursor))

# (1, 'John', 'john@email.com', 30)
# (2, 'Emily', 'emily@email.com', 28)
# (3, 'Taro', 'taro@email.com', 35)


# .fetchall(): 現在のcusor以下全てのタプルのリストで返す
print(cursor.fetchall())
print(cursor.fetchall())

# [(1, 'John', 'john@email.com', 30), (2, 'Emily', 'emily@email.com', 28), (3, 'Taro', 'taro@email.com', 35)]
# []