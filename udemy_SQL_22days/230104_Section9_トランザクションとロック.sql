 /*-------------------------------------------30.トランザクション、ロック、コミット------------------------------------------------------*/
 
show databases; 
use day_4_9_db;
show tables;

select * from users;

-- TRANSACTIONの開始

start transaction ;

-- UPDATE処理の開始

UPDATE users set name = "中山 成美" where id =1;
SELECT * FROM users;

-- ROLLBACK(トランザクションの開始前に戻す)

ROLLBACK;

-- COMMIT(トランザクションをDBへ反映)
COMMIT;


 /*-------------------------------------------31.オートコミットの設定変更-----------------------------------------------------*/
 # 多くのDBMSでは明示的にトランザクションを開始しない限りSQLを実行すると自動的にコミットされる。
 # これを自動コミットモードという。

-- ROLLBACK
rollback;



select * from students order by id desc;

-- id = 300 を削除
delete from students where id = 300;

-- AUTO COMMIT確認
show variables where variable_name = "autocommit" ;
set autocommit = 0;

-- id = 299 を削除
delete from students where id = 299;

-- SQLの反映
COMMIT;
select * from students order by id desc;

-- AUTO COMMITをもとに戻す

set autocommit = 1;


 /*-------------------------------------------33.ロック-----------------------------------------------------*/

start transaction;
SELECT * from customers ;

-- 主キーでUPDATE（行ロック）
update customers 
set age = 43 where id =1;

rollback;


start transaction;


-- テーブル全体のロック
update customers 
set age =42 
where name = "河野 文典";

rollback;


-- DELETE
start transaction;

-- 行ロック
delete from customers where id =1;

select * from customers ;

commit;


-- INSERT 
start transaction;

INSERT into	 customers 
values(1, "田中 一郎", 21, "1999-06-17");

select * from customers ;


-- SELECTのロック
-- FOR SHARE(共有ロック)
-- FOR UPDATE(排他ロック)

start transaction;
select * from customers where id=1 
for share;   -- id=1 の行を別のユーザーが更新、削除できない(selectはできる)  > 共有ロック

start transaction;
select * from customers where id=1 
for update;   -- id=1 の行を別のユーザーが更新、削除,Select できない > 排他ロック
rollback;




 /*--------------------------------------------34.明示的にテーブルロック、デッドロック--------------------------------------------------*/

-- LOCK TABLE READ
LOCK TABLE customers read;
select * from customers ;
   -- SELECTはできるが、更新UPDATEできない

update  customers 
set age = 42 where id =1;

UNLOCK TABLES;

-- LOCK TABLE WRITE
LOCK TABLE customers write;
select * from customers ;
   -- SELECTも更新UPDATEできない

update  customers 
set age = 42 where id =1;

UNLOCK TABLES;

-- DEAD LOCK
START TRANSACTION;

-- customers ⇒ users
UPDATE customers 
set age = 12 where id = 1; 

UPDATE users
set age = 12 where id = 1; 






