/*------------------65.複雑なUPDATE処理の記述----------------------------*/
show databases;
use day_10_14_db;

select * from employees ;

update employees set age = age +1 
where id = 1;

-- UPDATE 更新したいテーブル SET 更新したい列 = 更新する値

select * from employees as emp
where emp.department_id = (select id from departments where name = "営業部" );

-- 営業部の人の年齢を＋２する
update  employees as emp
set emp.age = emp.age +2
where emp.department_id = (select id from departments where name = "営業部" );



-- INNER JOIN 

select * from employees ;

alter table employees 
add department_name varchar(255);

-- LEFT JOIN

select 
	emp.*,
	coalesce(dt.name, "不明")
from employees as emp
left join departments as dt
on emp.department_id = dt.id ;



update employees as emp
left join departments as dt
on emp.department_id = dt.id 
set  emp.department_name = coalesce(dt.name, "不明")



/*------------------65.複雑なUPDATE処理とDELET処理の記述----------------------------*/


-- WITHを使ってUPDATE

select * from stores;


alter table stores 
add all_sales int;

select * from items;
select * from orders;


select 
	it.store_id ,
	sum(od.order_amount * od.order_price)
from items as it
inner join orders as od 
on it.id = od.item_id 
group by it.store_id;



with tmp_sales as(
	select 
		it.store_id ,
		sum(od.order_amount * od.order_price) as summary
	from items as it
	inner join orders as od 
	on it.id = od.item_id 
	group by it.store_id
)
update stores as st
inner join tmp_sales as ts 
on st.id = ts.store_id
set st.all_sales = ts.summary;


-- delete 

delete from employees 
where department_id in (
	select id from departments where name = "開発部"
) ;

select * from employees ;


/*------------------67.INSERT処理の応用----------------------------*/

create table customers_orders(
	name varchar(255),
	order_date date,
	sales int ,
	total_sales int
);

select * from customers_orders;

insert into customers_orders
select 
	concat(ct.last_name, ct.first_name) ,
	od.order_date ,
	od.order_amount * od.order_price ,
	sum(order_amount * od.order_price) over(PARTITION by concat(ct.last_name, ct.first_name) order by od.order_date) 
from customers as ct
inner join orders as od 
on ct.id = od.customer_id ;


/*------------------68. カラムの制約(NOT NULL, UNIQUE)----------------------------*/

show databases;

create database day_15_18_db;
use day_15_18_db;
show tables;


create table users (
	id int primary key,
	first_name varchar(255),
	last_name varchar(255) default '' NOT NULL
);

insert into users(id) values(1);

select * from users;



-- NULL値を入れることができない
create table users_2(
	id int primary key,
	first_name varchar(255),
	last_name varchar(255) default '' NOT NULL,
	age int default 0
);


insert into users_2(id, first_name) values(1,"太郎", "山田")

select * from users_2;

insert into users_2 values(2, "Jiro", "Suzuki", NULL);



-- unique制約
create table login_users(
	id int primary key ,
	name varchar(255) not null ,
	email varchar(255) not null unique
);

insert into login_users values(1, "Shingo" , "abc@mail.com");
insert into login_users values(2, "Shingo" , "abcd@mail.com");

select * from login_users;


create table tmp_names(
	name varchar(255) unique
);

select * from tmp_names;

insert into tmp_names values("Taro");
insert into tmp_names values(NULL);  -- NULLは何回やっても許される


-- check 制約

create table customers (
	id int primary key,
	name varchar(255),
	age int check(age >= 20)
);

insert into customers values(1, "Taro", 21);
insert into customers values(1, "Taro", 18);


-- 複数のカラムに対するCHECK制約

create table students (
	id int primary key ,
	name varchar(255) ,
	age int ,
	gender char(1) ,
	constraint chk_students check ((age >=15 and age <= 20) and (gender ="F" or gender = "M"))
);

insert into students values(1, "Taro" , 18, "M");
insert into students values(2, "Sachiko" , 18, "F");
insert into students values(4, "Sachiko" , 33, "F");


create table employees(
	company_id int ,
	employee_code char(8) ,
	name varchar(255) ,
	age int ,
	primary key (company_id , employee_code)
);

insert into employees values(1, "00000001", "Taro", 19);
insert into employees values(NULL, "00000001", "Taro", 19);  -- 主キーはNULLを入れることができない
insert into employees values(1, "00000002", "Taro", 19);  -- 主キーはNULLを入れることができない

select * from employees;


