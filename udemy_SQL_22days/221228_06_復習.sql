#DB一覧を表示
Show databases;

DBの中に入り利用する
use performance_schema;
use my_db;

#利用中のデータベースを表示
select database();

#テーブル一覧表示
show tables;

#user テーブルの作成
CREATE TABLE users(
  id int,  -- idカラムint型
  name VARCHAR(10), -- 名前、可変長文字列
  age int,
  phone_number char(13), -- 固定長 
  message text 
)

describe users;

drop table users;

#user テーブルの作成,主キー付き
CREATE TABLE users(
  id int primary key,  -- idカラムint型
  name VARCHAR(10), -- 名前、可変長文字列
  age int,
  phone_number char(13), -- 固定長 
  message text 
);

select database();

show tables;

#テーブル名変更
alter table users rename to users_table2;

#テーブルの定義確認
describe users_table2;

#カラムの削除
ALTER Table users_table2 drop column message;

#カラムの追加
ALTER Table users_table2 
add post_code char(8);

#最初の列にカラムの追加
ALTER Table users_table2 
add new_id int first;

#new_idカラムの削除
ALTER Table users_table2 drop column new_id;

#カラムの定義変更
ALTER Table users_table2 MODIFY name VARCHAR(50);

#カラム名の変更
ALTER Table users_table2 Change column  name 名前 VARCHAR(50);

describe users_table2;

#主キーの削除
ALTER table users_table2 drop primary key;


ALTER Table users_table2 Change column  name 名前 VARCHAR(50);

#------------------------------------------------------------------------------------#
select database();
show tables;

describe students ;
select * from students;