/*---------------------------------39.テーブル名に別名をつけて参照する------------------------------- */

show databases;

CREATE database day_10_14_db;

use day_10_14_db;

show tables;

-- テーブルに別名をつける

SELECT 
	cs.name 
from 
	classes as cs
	
SELECT 
	cs_2.id,
	cs_2.name 
from 
	classes as cs_2
	
	
/*---------------------------------40.副問い合わせ------------------------------- */

	
-- 部署一覧
select * FROM departments ;
select * FROM employees ;


-- INで絞り込む
SELECT * from employees WHERE department_id in(1,2);

-- 副問い合わせを使う
SELECT * from departments WHERE name in("経営企画部", "営業部");
SELECT id from departments WHERE name in("経営企画部", "営業部");


SELECT 
	*
from 
	employees
WHERE 
	department_id in(
		SELECT id from departments 
		WHERE name in("経営企画部", "営業部")
	);
	


SELECT * from students ;
SELECT * FROM users;
SELECT first_name ,last_name from users;


-- 複数のカラムのIN(副問い合わせ)
SELECT * FROM students 
where 	(first_name, last_name) in(            -- in
SELECT first_name ,last_name from users
)
;

SELECT * FROM students 
where 	(first_name, last_name) not in(      -- not in
SELECT first_name ,last_name from users
)
;


-- 副問い合わせ3： 集計と使う
SELECT max(age) FROM employees ;

SELECT * from employees WHERE age< (SELECT max(age) FROM employees)  ;




/*---------------------------------41.副問い合わせ2(FROMの取得先に使う、SELECTの行に入れる)------------------------------- */


SELECT 
	max(avg_age) as "部署ごとの平均年齢の最大",
	min(avg_age) as "部署ごとの平均年齢の最低"
from(
	SELECT 
		department_id,
		avg(age) as avg_age
	from
		employees 
	group by
		department_id 
	) as tmp_emp;

-- 年代の集計
SELECT 
	max(age_count), min(age_count)
from
	(SELECT  floor(age/10)*10 as "年代",  count(*) as age_count
	from employees  group by floor(age/10) ) as age_summary


	
-- 副問い合わせ５ ： SELECT の中に書く

select * from customers;

SELECT * from orders ;

SELECT 
	cs.id,
	cs.first_name,
	cs.last_name,
	(
		SELECT max(order_date) from orders as order_max
		WHERE cs.id = order_max.customer_id 
	) as "最近の注文日" ,
	(
		SELECT min(order_date) from orders as order_max
		WHERE cs.id = order_max.customer_id 
	) as "古い注文日" ,
	(
		SELECT SUM(order_amount*order_price) from orders as order_max
		WHERE cs.id = order_max.customer_id 
	) as "全支払い金額" 
from
	customers as cs
WHERE 
	cs.id<10;

		SELECT max(order_date) from orders as order_max
		WHERE cs.id = order_max.customer_id ;


/*---------------------------------42.副問い合わせ3(CASEとともに使う)------------------------------- */

SELECT 
	emp.*,
	CASE 
		when emp.department_id  = (SELECT id from departments WHERE name ="経営企画部")
			then "経営層"
		else "その他" 
	END as "役割"
FROM 
	employees as emp
	

select * from salaries ;
SELECT * FROM employees ;


SELECT 
	emp.*,
	CASE 
		when emp.id in(
			SELECT DISTINCT employee_id  from salaries 
			WHERE  payment > (SELECT AVG(payment) from salaries )
		)
		 	then "〇"
		 else "×"
	END as "給料が平均より高いか"
FROM 	
	employees as emp

SELECT DISTINCT employee_id  from salaries 
WHERE  payment > (SELECT AVG(payment) from salaries )


/*---------------------------------43.SELECTの結果をCREATEで使う------------------------------- */

-- CREATE SELECT INSERT 

show tables ;

CREATE table tmp_students 
SELECT * from students;

SELECT * from tmp_students;

describe tmp_students ;  -- PRI Keyなし カラムの設定は反映されていない
describe students ;  -- PRI Keyあり


-- テーブルの削除
drop table tmp_students ;

-- 新規でテーブル追加
create table tmp_students
select * from students WHERE id <10

select * from tmp_students ;


insert into tmp_students 
SELECT id+9 as id ,first_name , last_name , 2 as grade from users;  -- このテーブルをtmp_studentsに追加する


-- name のテーブルをunionで作る
CREATE table name
SELECT first_name, last_name from students  
union
SELECT first_name, last_name from employees 
union
SELECT first_name, last_name from customers  ;