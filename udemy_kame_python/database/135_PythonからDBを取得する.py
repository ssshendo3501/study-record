import sqlite3


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
insert into user values (2, 'Emily', 'emily@email.com', 28);
insert into user values (3, 'Taro', 'taro@email.com', 35);
"""
# .executescript: 複数行のinsert文の発行
# .executescriptはオートコミットされる
cursor.executescript(insert_user_query)


# 接続のcommit
con.commit()
