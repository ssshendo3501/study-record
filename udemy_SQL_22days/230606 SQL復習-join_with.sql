show databases;
use day_10_14_db;
show tables;


select * from employees ;
--where department_id =3;

SELECT  * from departments ;

select 
	*
	,COALESCE(dt.id,"該当なし")
from employees as emp
left join departments as dt 
on emp.department_id = dt.id



select * from enrollments ;
select * from classes;
select * from students 

select * from enrollments as enr
right join students as std on enr.student_id = std.id
right join classes as cls on enr.class_id = cls.id ;

-- customers, orders , items, storesを紐づける
-- customers id で並び替える

select * from customers ;
select * from orders ;
select * from items;
select * from stores;

select * from customers as ct
left join orders od on ct.id = od.customer_id 
left join items it on od.item_id = it.id 
left join stores st on it.store_id = st.id;

select * from customers as ct
inner join orders od on ct.id = od.customer_id 
inner join items it on od.item_id = it.id 
inner join stores st on it.store_id = st.id
where ct.id = 10 and od.order_date > "2020-08-01"
order by ct.id



select 
	ct.id
	,order_summary.summary_price
from customers as ct
inner join (
	select 
		customer_id 
		,sum(order_amount * order_price) as summary_price
	from orders od 
	group by customer_id 
	) as order_summary
on ct.id = order_summary.customer_id


-- with 

-- departments から営業部の人を取り出して、emplooyeesと結合する

	select * from departments as dt
	where name = "営業部"

with 営業マスタ as (
	select * from departments as dt
	where name = "営業部"
	)
select * from employees as emp
inner join 営業マスタ on emp.department_id  = 営業マスタ.id



-- storeテーブルからid 1,2,3を取り出す （where）
-- itemsテーブルと紐づけ、itemsテーブルとordersテーブルを紐づける innerjoin
-- orders テーブルのorder_amount * order_pricvceの合計値をstoresテーブルのstore_name毎に集計する groupby

select * from stores where id in(1,2,3);
select * from items;
select * from orders

with tmp_stores as (
	select * from stores where id in(1,2,3)
	)
	, tmp_items_orders as (
	select 
		tmp_stores.id as store_id
		,tmp_stores.name as store_name
		,it.id as item_id
		,od.id as order_id
		,od.order_price 
		,od.order_amount
	from tmp_stores 
	inner join items as it 
		on tmp_stores.id = it.store_id
 	inner join orders as od 
 		on it.id = od.item_id
	)
select 
	store_name
	,sum(order_price * order_amount)
from tmp_items_orders
group by store_name
