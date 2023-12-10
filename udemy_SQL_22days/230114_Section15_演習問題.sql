/*---------------------------------60 演習 ---------------------------*/

# 1. employeesテーブルとcustomersテーブルの両方から、それぞれidが10より小さいレコードを取り出します。
# 両テーブルのfirst_name, last_name, ageカラムを取り出し、行方向に連結します。
# 連結の際は、重複を削除するようにしてください。


select * from employees ;
select * from customers ;

-- Inner join
select * from employees as emp
inner join customers as cs
ON emp.first_name = cs.first_name and emp.last_name = cs.last_name
where emp.id < 10;


-- UNIONは重複を削除できる
select 
	emp.first_name,
	emp.last_name, 
	emp.age
from employees as emp
where emp.id < 10
union
(select 
	cs.first_name,
	cs.last_name, 
	cs.age
from customers as cs
where cs.id < 10)



# 2. departmentsテーブルのnameカラムが営業部の人の、月収の最大値、最小値、平均値、合計値を計算してください。
# employeesテーブルのdepartment_idとdepartmentsテーブルのidが紐づけられ
# salariesテーブルのemployee_idとemployeesテーブルのidが紐づけられます。
# 月収はsalariesテーブルのpaymentカラムに格納されています

select * from departments ;
select * from employees ;
select * from salaries ;

select 
	emp.first_name,
	emp.last_name,
	emp.age,
	dp.name as department,
	max(payment) as max_pay,
	min(payment) as min_pay,
	floor(avg(payment)) as avg_pay,
	sum(payment) as sum_pay
FROM 
	employees as emp
inner join departments as dp
	on emp.department_id = dp.id
inner join salaries as sal
	on emp.id = sal.employee_id 
where dp.name = "営業部"
group by
	emp.first_name 

	
	
# 3. classesテーブルのidが、5よりも小さいレコードとそれ以外のレコードを履修している生徒の数を計算してください。
# classesテーブルのidとenrollmentsテーブルのclass_id、enrollmentsテーブルのstudent_idとstudents.idが紐づく
# classesにはクラス名が格納されていて、studentsと多対多で結合される

select * from classes ;
select * from enrollments ;
select * from students ;


-- Caseを使ったGroup by
select 
	case 
		when cls.id > 5 then "id<5"
		else "id>=5"
	end as cls_id ,
	count(*)
from enrollments as enl
inner join classes as cls
	on enl.class_id = cls.id
group by 
	case 
		when cls.id < 5 then "id<5"
		else "id>=5"
	end 

	

	
# 4. ageが40より小さい全従業員で月収の平均値が7,000,000よりも大きい人の、月収の合計値と平均値を計算してください。
# employeesテーブルのidとsalariesテーブルのemployee_idが紐づけでき、salariesテーブルのpaymentに月収が格納されています
	
select * from enrollments ;
select * from employees ;
select * from salaries ;

select 
	emp.first_name ,
	emp.last_name ,
	emp.age ,
	sum(sal.payment) as sum_payment,
	floor( avg(sal.payment)) as avg_payment
from employees as emp
inner join salaries as sal
	on emp.id = sal.employee_id 
where emp.age < 40
group by emp.id                                              -- 忘れないように！
having avg(sal.payment) > 7000000;

	
	
	
# 5. customer毎に、order_amountの合計値を計算してください。
# customersテーブルとordersテーブルは、idカラムとcustomer_idカラムで紐づけができます
# ordersテーブルのorder_amountの合計値を取得します。
# SELECTの対象カラムに副問い合わせを用いて値を取得してください。
	
SELECT * FROM customers ;
SELECT * FROM orders ;	

-- inner join
select 
	cs.id,
	sum(odr.order_amount) as sum_order_amount
from customers as cs
inner join orders as odr 
	on cs.id = odr.customer_id
group by cs.id;
	
-- 副問い合わせ
SELECT 
	*,
	(select sum(order_amount) from orders as od
	 where od.customer_id = cs.id) as sum_order_amount
from customers as cs
	

# 6. customersテーブルからlast_nameに田がつくレコード、
# ordersテーブルからorder_dateが2020-12-01以上のレコード、
# storesテーブルからnameが山田商店のレコード同士を連結します
# customersとorders, ordersとitems, itemsとstoresが紐づきます。
# first_nameとlast_nameの値を連結(CONCAT)して集計(GROUP BY)し、そのレコード数をCOUNTしてください。

select * from customers ;
select * from orders ;
select * from stores ;
select * from items;


select
	concat(cs.last_name , cs.first_name),
	count(*)
from
	customers as cs
		inner join orders as odr 
			on cs.id = odr.customer_id 
		inner join items as itm
			on odr.item_id = itm.id
		inner join stores as str
			on itm.store_id = str.id 
where
	cs.last_name like "%田%" and
	odr.order_date >= "2020-12-01" and
	str.name = "山田商店"
group by
	concat(cs.last_name , cs.first_name)
	

select * from customers as cs
where last_name like "%田%"

select * from orders as odr
where order_date > "2020-12-01"

select * from stores as str
where name = "山田商店"

SELECT 
	concat(customers.first_name, customers.last_name),
	count(*)
FROM 
	(select * from customers as cs where last_name like "%田%") as customers
	inner join (select * from orders where order_date >= "2020-12-01") as orders
		on customers.id = orders.customer_id 
	inner join items 
		on orders.item_id = items.id 
	inner join (select * from stores where name = "山田商店") as stores
		on stores.id = items.store_id 
	group by
		concat(customers.first_name, customers.last_name)
	
	


# 7. salariesのpaymentが9,000,000よりも大きいものが存在するレコードを、employeesテーブルから取り出してください。
# employeesテーブルとsalariesテーブルを紐づけます。
# EXISTSとINとINNER JOIN、それぞれの方法で記載してください

select * from salaries ;
select * from employees ;

-- 副問い合わせ
select * from employees 
where id in(select employee_id  from salaries where payment > 9000000)

-- inner join
select * from employees as emp
	inner join salaries as sal
		on emp.id = sal.employee_id 
where sal.payment >9000000
	group by emp.id
		
-- EXISTS
select * from employees as emp
where EXISTS (
	select 1 from salaries as sal 
	where 
		emp.id = sal.employee_id and 
		sal.payment > 9000000
	);


# 8. employeesテーブルから、salariesテーブルと紐づけのできないレコードを取り出してください。
# EXISTSとINとLEFT JOIN、それぞれの方法で記載してください	

-- 副問い合わせ
select * 
from employees as emp
where id not in(select employee_id from salaries)

-- Left join
select * from employees as emp
left join salaries as sal
on emp.id = sal.employee_id 
where sal.id is null

-- not exists
select * from employees as emp
where not exists(
	select 1 from salaries as sal
	where emp.id = sal.employee_id 
)




# 9. employeesテーブルとcustomersテーブルのage同士を比較します
# customersテーブルの最小age, 平均age, 最大ageとemployeesテーブルのageを比較して、
# employeesテーブルのageが、最小age未満のものは最小未満、最小age以上で平均age未満のものは平均未満、
# 平均age以上で最大age未満のものは最大未満、それ以外はその他と表示します
# WITH句を用いて記述します


select * from employees ;
select * from customers ;


with cst as
(select min(age) as cs_min , avg(age) as cs_avg , max(age) as cs_max from customers)
select 
	*,
	case	
		when emp.age < cst.cs_min then "最小未満" 
		when emp.age < cst.cs_avg then "平均未満" 
		when emp.age < cst.cs_max then "最大未満" 
		else  "最大以上" 
	end as "分類"
from 
	employees as emp 
cross join cst ;



select 
	min(age) as cs_min , 
	avg(age) as cs_avg , 
	max(age) as cs_max
from customers



# 10. customersテーブルからageが50よりも大きいレコードを取り出して、ordersテーブルと連結します。
# customersテーブルのidに対して、ordersテーブルのorder_amount*order_priceのorder_date毎の合計値。
# 合計値の7日間平均値、合計値の15日平均値、合計値の30日平均値を計算します。
# 7日間平均、15日平均値、30日平均値が計算できない区間(対象よりも前の日付のデータが十分にない区間)は、空白を表示してください。

with cs_50 as
(select * from customers where age > 50 )
select 
	odr.id,
	odr.order_date ,
	cs_50.first_name,
	cs_50.last_name,
	SUM(odr.order_amount * odr.order_price)
from orders as odr
inner join cs_50
on cs_50.id = odr.customer_id 
group by odr.id, odr.order_date 


select * from customers where age > 50 


