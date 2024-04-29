import sqlite3

# 以下2つはおまじないなので覚えておくこと
# sample.dbに接続（ない場合新たにdbが作られる）
con = sqlite3.connect("sample.db")

# .curesorオブジェクトにクエリを実行することでSQLを実行できる
cursor = con.cursor()

create_user_table_query = """
create table if not exists user (
    UserId integer primary key not null,
    name text default 'anonymous',
    email text not null,
    age integer check(age > 0) 
)
"""
cursor.execute(create_user_table_query)


insert_user_query = """
insert into user values (1, 'John', 'john@email.com', 30);
"""
cursor.execute(insert_user_query)


# databaseを更新する時には原則commitが必要
# con.commit()をすることで、このconnectionオブジェクトに関する今までのクエリを全てcommitしてくれる
# commitすることでレコードをセーブして永続化される
# create tableはオートコミットだったのでこの操作は不要だったが、insertはコミットが必要
# また、ターミナル上で実施するsql操作はオートコミットが実装されている
con.commit()
