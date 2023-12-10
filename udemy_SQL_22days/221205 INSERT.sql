SELECT DATABASE();

use my_db;

#テーブル作成
CREATE TABLE  people(
 id int PRIMARY KEY,
 name varchar(50),
 birth_day date default "1990-01-01"
);

insert into people VALUES(1, "Taro", "2001-01-01");

#Select
select * from people;

#insert カラム指定
insert into people (id, name) values(2,"Jiro");

#シングルフォーテーション
insert into people (id, name) values(3, "Saburo");

#シングルフォーテーション
insert into people values(4, "John's son", "2021-01-01");
