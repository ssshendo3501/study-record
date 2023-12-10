/* ---------------------------------91.インデックスを用いたSQLチューニング-----------------------------------*/

use day_19_21_db;


-- 外部lキーにインデックス
explain analyze 
select * from prefectures as pr
inner join customers as ct 
on pr.prefecture_code = ct.prefecture_code and pr.name = "北海道" ;

/*
-> Limit: 200 row(s)  (cost=224484.10 rows=200) (actual time=0.128..21.112 rows=200 loops=1)
    -> Nested loop inner join  (cost=224484.10 rows=49720) (actual time=0.127..21.079 rows=200 loops=1)
        -> Filter: (ct.prefecture_code is not null)  (cost=50464.80 rows=497198) (actual time=0.074..7.110 rows=8583 loops=1)
            -> Table scan on ct  (cost=50464.80 rows=497198) (actual time=0.073..6.206 rows=8583 loops=1)
        -> Filter: (pr.`name` = '北海道')  (cost=0.25 rows=0.1) (actual time=0.001..0.001 rows=0 loops=8583)
            -> Single-row index lookup on pr using PRIMARY (prefecture_code=ct.prefecture_code)  (cost=0.25 rows=1) (actual time=0.001..0.001 rows=1 loops=8583)
*/

select * from prefectures as pr
inner join customers as ct 
on pr.prefecture_code = ct.prefecture_code and pr.name = "北海道" ;

create index idx_customers_prefecture_code on customers(prefecture_code);

/*
-> Limit: 200 row(s)  (cost=16501.32 rows=200) (actual time=0.836..2.066 rows=200 loops=1)
    -> Nested loop inner join  (cost=16501.32 rows=59919) (actual time=0.835..2.044 rows=200 loops=1)
        -> Filter: (pr.`name` = '北海道')  (cost=4.95 rows=5) (actual time=0.056..0.056 rows=1 loops=1)
            -> Table scan on pr  (cost=4.95 rows=47) (actual time=0.052..0.052 rows=1 loops=1)
        -> Index lookup on ct using idx_customers_prefecture_code (prefecture_code=pr.prefecture_code)  (cost=2506.25 rows=12749) (actual time=0.777..1.965 rows=200 loops=1)

*/


/* ---------------------------------92.インデックスが利用できないSQLチューニング-----------------------------------*/

-- index無し
select * from customers where upper (first_name ) = "JOSEPH"


explain analyze select * from customers where upper (first_name ) = "JOSEPH"

/*
 -> Limit: 200 row(s)  (cost=50464.80 rows=200) (actual time=0.084..18.899 rows=200 loops=1)
    -> Filter: (upper(customers.first_name) = 'JOSEPH')  (cost=50464.80 rows=497198) (actual time=0.083..18.827 rows=200 loops=1)
        -> Table scan on customers  (cost=50464.80 rows=497198) (actual time=0.076..14.729 rows=20321 loops=1)
 */


create index idx_customers_age on customers(age);

explain analyze select * from customers where age+2=27;

/*
 
 * -> Limit: 200 row(s)  (cost=50464.80 rows=200) (actual time=0.101..8.659 rows=200 loops=1)
    -> Filter: ((customers.age + 2) = 27)  (cost=50464.80 rows=497198) (actual time=0.100..8.615 rows=200 loops=1)
        -> Table scan on customers  (cost=50464.80 rows=497198) (actual time=0.077..7.636 rows=9365 loops=1)
 */



-- 文字列と数値の比較
explain analyze  select * from customers where prefecture_code = "21";

/*
-> Limit: 200 row(s)  (cost=50464.80 rows=200) (actual time=0.086..7.462 rows=200 loops=1)
    -> Filter: (customers.prefecture_code = 21)  (cost=50464.80 rows=49720) (actual time=0.085..7.433 rows=200 loops=1)
        -> Table scan on customers  (cost=50464.80 rows=497198) (actual time=0.075..6.302 rows=7863 loops=1)

 */


describe customers ;

/*
 -> Limit: 200 row(s)  (cost=4429.20 rows=200) (actual time=0.528..1.512 rows=200 loops=1)
    -> Index lookup on customers using idx_customers_prefecture_code (prefecture_code='21'), with index condition: (customers.prefecture_code = '21')  (cost=4429.20 rows=21942) (actual time=0.526..1.490 rows=200 loops=1)

*/


-- 前方一致、後方一致
