use day_4_9_db;

UPDATE customers 
set age = 44 where id = 1;

UPDATE customers 
set age = 44 where id = 2;


select * from customers where id =1;

-- DEAD LOCK
START TRANSACTION;

-- users ⇒ customers
UPDATE users 
set age=12 where id =1;

UPDATE customers 
set age=12 where id =1;

-- DEAD LOCKを発生させないためには、更新するテーブルの順番を揃える