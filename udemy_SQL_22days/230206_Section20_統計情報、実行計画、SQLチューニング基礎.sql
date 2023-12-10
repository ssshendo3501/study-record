/* ---------------------------------85. SQLチューニング-----------------------------------*/

use day_10_14_db;

show tables ;

select * from customers where id =3;

-- バインド変数
Set @customer_id = 5;
select * from customers where id = @customer_id;


/* ---------------------------------86. コストベースオプティマイザ-----------------------------------*/

show databases;

create database day_19_21_db;
use day_19_21_db;
show tables;

-- 統計情報の確認
select * from mysql.innodb_table_stats where database_name = "day_19_21_db";

select * from prefectures ;

insert into prefectures values("48", "不明");

delete from prefectures where prefecture_code = "48" and name = "不明";

-- 統計情報の手動更新
analyze table prefectures;

-- 200件
select * from customers ;


-- SQL実行せずに実行計画だけ表示
explain select * from customers ;

explain analyze  select * from customers ;


--  -> Limit: 200 row(s)  (cost=52695.24 rows=200) (actual time=0.081..0.237 rows=200 loops=1)
--    -> Table scan on customers  (cost=52695.24 rows=497198) (actual time=0.079..0.216 rows=200 loops=1)



/* ---------------------------------87. フルスキャン、インデックススキャン-----------------------------------*/

explain analyze select * from customers ;

-- -> Limit: 200 row(s)  (cost=52695.24 rows=200) (actual time=0.173..0.456 rows=200 loops=1)
--    -> Table scan on customers  (cost=52695.24 rows=497198) (actual time=0.170..0.431 rows=200 loops=1)

explain analyze select * from customers where id =1;

-- -> Limit: 200 row(s)  (cost=0.00..0.00 rows=1) (actual time=0.001..0.002 rows=1 loops=1)
--    -> Rows fetched before execution  (cost=0.00..0.00 rows=1) (actual time=0.000..0.000 rows=1 loops=1)

explain analyze select * from customers where id <10;

-- -> Limit: 200 row(s)  (cost=2.82 rows=9) (actual time=0.025..0.086 rows=9 loops=1)
--    -> Filter: (customers.id < 10)  (cost=2.82 rows=9) (actual time=0.024..0.084 rows=9 loops=1)
--        -> Index range scan on customers using PRIMARY over (id < 10)  (cost=2.82 rows=9) (actual time=0.022..0.081 rows=9 loops=1)


select * from customers ;

explain analyze select * from customers where  first_name = "Olivia";
select * from customers where  first_name = "Olivia";

-- -> Limit: 200 row(s)  (cost=52695.24 rows=200) (actual time=0.088..159.695 rows=200 loops=1)
--    -> Filter: (customers.first_name = 'Olivia')  (cost=52695.24 rows=49720) (actual time=0.087..159.613 rows=200 loops=1)
--        -> Table scan on customers  (cost=52695.24 rows=497198) (actual time=0.083..143.513 rows=192550 loops=1)

create index idx_customers_first_name on customers(first_name);

explain analyze select * from customers where  first_name = "Olivia";

-- -> Limit: 200 row(s)  (cost=271.20 rows=200) (actual time=0.499..1.371 rows=200 loops=1)
--     -> Index lookup on customers using idx_customers_first_name (first_name='Olivia')  (cost=271.20 rows=503) (actual time=0.497..1.350 rows=200 loops=1)

explain analyze  select * from customers where gender = "F";
-- -> Limit: 200 row(s)  (cost=51028.49 rows=200) (actual time=0.090..0.457 rows=200 loops=1)
--    -> Filter: (customers.gender = 'F')  (cost=51028.49 rows=49720) (actual time=0.089..0.436 rows=200 loops=1)
--        -> Table scan on customers  (cost=51028.49 rows=497198) (actual time=0.085..0.369 rows=381 loops=1)

create index idx_customers_gender on customers(gender);
explain analyze  select * from customers where gender = "F";

-- -> Limit: 200 row(s)  (cost=29563.12 rows=200) (actual time=0.356..0.875 rows=200 loops=1)
--    -> Index lookup on customers using idx_customers_gender (gender='F'), with index condition: (customers.gender = 'F')  (cost=29563.12 rows=248599) (actual time=0.354..0.854 rows=200 loops=1)

drop index idx_customers_gender on customers;
drop index idx_customers_first_name on customers;


/* ---------------------------------88. ネステッドループ、ハッシュ、ソートマージ-----------------------------------*/

explain analyze
select 
	* 
from customers as ct
inner join prefectures as pr
on ct.prefecture_code = pr.prefecture_code ;

-- -> Limit: 200 row(s)  (cost=225306.84 rows=200) (actual time=0.103..0.630 rows=200 loops=1)
--    -> Nested loop inner join  (cost=225306.84 rows=497198) (actual time=0.102..0.604 rows=200 loops=1)
--       -> Filter: (ct.prefecture_code is not null)  (cost=51287.54 rows=497198) (actual time=0.085..0.258 rows=200 loops=1)
--            -> Table scan on ct  (cost=51287.54 rows=497198) (actual time=0.084..0.229 rows=200 loops=1)
--        -> Single-row index lookup on pr using PRIMARY (prefecture_code=ct.prefecture_code)  (cost=0.25 rows=1) (actual time=0.001..0.001 rows=1 loops=200)










