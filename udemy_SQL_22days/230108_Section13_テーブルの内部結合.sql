/*---------------------------------49.内部結合------------------------------- */

-- JOIN > 列方向に連結

show databases;
use day_10_14_db;
show tables;



SELECT * from employees ;
select * from departments ;


-- inner join テーブル2 on テーブル１カラム = テーブル2カラム
select * from employees as emp
inner join departments as dp     
on emp.department_id = dp.id ;

select 
	emp.id , 
	emp.first_name , 
	emp.last_name , 
	emp.department_id , 
	dp.name as department_name 
from 
	employees as emp
inner join
	departments as dp     
on 
	emp.department_id = dp.id ;
	


-- 複数のレコードを紐づける
select * from students as std;
SELECT * from users;

select * from students as std
inner join users as usr 
on 
	std.first_name = usr.first_name and 
	std.last_name = usr.last_name ;
	

-- =以外で紐づける
SELECT * from employees as emp
inner join students as std 
on emp.id < std.id;




/*---------------------------------50.外部結合 (LEFT JOIN, RIGHT JOIN)------------------------------- */

-- LEFT JOIN > 右のテーブルからは紐づけられたレコードのみ取り出し、それ以外はNULL
-- RIGHT JOIN > 右のテーブルは全て抽出して、紐づけられたレコードのみ抽出する、其れ以外はNULL

select 
	emp.id , 
	emp.first_name , 
	emp.last_name , 
	emp.department_id 
from 
	employees as emp

-- LEFT JOIN
select 
	emp.id , 
	emp.first_name , 
	emp.last_name , 
	emp.department_id , 
	dp.name as department_name 
from 
	employees as emp
left join
	departments as dp     
on 
	emp.department_id = dp.id ;

-- RIGHT JOIN
select 
	emp.id , 
	emp.first_name , 
	emp.last_name , 
	emp.department_id , 
	dp.name as department_name 
from 
	employees as emp
right join
	departments as dp     
on 
	emp.department_id = dp.id ;


-- INNER JOIN
select 
	emp.id , 
	emp.first_name , 
	emp.last_name , 
	emp.department_id , 
	dp.name as department_name 
from 
	employees as emp
inner join
	departments as dp     
on 
	emp.department_id = dp.id ;
	


select * from enrollments ;
select * from classes ;

select * from enrollments as enr
left join classes as cls 
on enr.class_id = cls.id ;


select * from students as std
left join 
	enrollments as enr
on 
	std.id = enr.student_id 
left join 
	classes as cls 
on
	enr.class_id = cls.id ;


select * from students as std
right join 
	enrollments as enr
on 
	std.id = enr.student_id 
right join 
	classes as cls 
on
	enr.class_id = cls.id ;


-- FULL JOIN > LEFT とRIGHTを足し合わせたもの

select * from students as std
left join 
	enrollments as enr
on 
	std.id = enr.student_id 
left join 
	classes as cls 
on
	enr.class_id = cls.id 
union 
select * from students as std
right join 
	enrollments as enr
on 
	std.id = enr.student_id 
right join 
	classes as cls 
on
	enr.class_id = cls.id ;



/*---------------------------------51.複雑なJOIN------------------------------- */

-- customers, orders, items storesを紐づける
-- customers.odで並び替える

select * from customers ;
select * from orders ;
select * from items;
select * from orders;

select 
	*
from customers as ct
inner join orders as od 
	on ct.id = od.customer_id 
inner join items as it 
	on od.item_id = it.id 
inner join stores as st
	on it.store_id = st.id
order by  ct.id, order_date


-- customers, orders, items storesを紐づける
-- customers.odで並び替える
-- customers.id が10で、od.orders_dateが2020-08-01よりあとに絞り込む

-- where で書く
select *
from customers as ct
inner join orders as od 
	on ct.id = od.customer_id 
inner join items as it 
	on od.item_id = it.id 
inner join stores as st
	on it.store_id = st.id
where 
	ct.id = 10 and od.order_date > "2020-08-01"
order by  ct.id

-- 副問い合わせで書く
select *
from (select * from customers where id = 10) as ct
inner join (select * from orders where order_date > "2020-08-01") as od 
	on ct.id = od.customer_id 
inner join items as it 
	on od.item_id = it.id 
inner join stores as st
	on it.store_id = st.id
order by  ct.id


-- group byの紐づけ
select * from customers as ct
inner join
	(select customer_id , sum(order_amount * order_price) as summary_price
		from orders 
	group by customer_id 
	) as order_summary
on ct.id = order_summary.customer_id;


select customer_id , sum(order_amount * order_price) as summary_price
from orders 
group by customer_id ;



/*---------------------------------51.交差結合(CROSS JOIN)------------------------------ */

-- SELF JOIN(自己結合)
select * from employees as emp1;


select 
	concat(emp1.last_name, emp1.first_name) as "部下の名前" ,
	emp1.age as "部下の年齢",
	concat(emp2.last_name , emp2.first_name) as "上司の名前",
	emp2.age as "上司の年齢"
from employees as emp1
inner join employees as emp2
on emp1.manager_id = emp2.id;

select 
	concat(emp1.last_name, emp1.first_name) as "部下の名前" ,
	emp1.age as "部下の年齢",
	COALESCE(concat(emp2.last_name , emp2.first_name), "該当なし") as "上司の名前",
	COALESCE(emp2.age, "該当なし") as "上司の年齢"
from employees as emp1
Left join employees as emp2
on emp1.manager_id = emp2.id;



-- CROSS JOIN
select * 
from employees as emp1, employees as emp2
where emp1.id =1;

select * from employees as emp1
cross join employees as emp2
on emp1.id < emp2.id;


-- 計算結果とCASEで紐づけ
select 
	*,
	case
			when cs.age > summary_customers.avg_age then "〇"
			else "×"
	end as "平均年齢よりも年齢が高いか"
from customers as cs
cross join
	(select avg(age) as avg_age from customers ) as summary_customers;



SELECT 
	emp.id, 
	floor(avg(payment)) ,
	summary.avg_payment ,
	case 
		when floor(avg(payment)) >= summary.avg_payment then "〇"
		else "×"
	end as "平均月収以上か？"
from employees as emp
inner join salaries as sa
	on emp.id = sa.employee_id 
cross join
	(select floor(avg(payment)) as avg_payment from salaries) as summary
group by emp.id

select 
	avg(payment) as avg_payment 
from salaries ;


/*---------------------------------52.WITH------------------------------ */

-- WITH
-- departmentsから営業部の人を取り出して、employeesと結合する

select *
from employees as e
inner join departments as d
on e.department_id =d.id 
where d.name = "営業部" ;



with tmp_departments as(
	select * from departments where name = "営業部"  -- 一度絞り込んだものを
)
select * from employees as e
inner join tmp_departments                                          -- joinする
on e.department_id = tmp_departments.id;



-- storesテーブルから id1,2,3のものを取り出す > where
-- itemsテーブルと紐づけ、itemsテーブルとordersテーブルを紐づける > inner join
-- ordersテーブルのorder_amount * order_priceの合計値をstoresテーブルのstore_name毎に集計する > group by



-- with 中間テーブル名 as select文

with 
	tmp_stores as 
		(SELECT 
			* 
		from stores where id in(1,2,3)), 
	tmp_items_orders as 
		(SELECT 
			items.id as item_id , 
			tmp_stores.id as store_id ,
			orders.order_amount as order_amount , 
			orders.order_price as order_price ,
			tmp_stores.name as store_name
		from tmp_stores
		inner join items 
			on tmp_stores.id = items.store_id
		inner join orders 
			on items.id = orders.item_id)
select 
	store_name,
	sum(order_amount * order_price)
from tmp_items_orders
group by store_name;




























