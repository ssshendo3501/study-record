/*---------------------------------44.EXISTの使い方------------------------------- */

use day_10_14_db;

select * from departments ;

select * from employees ;

-- EXISTS

select * 
from employees as em
where exists(
	SELECT * from departments as dt where em.department_id =dt.id   -- employees_id = departments_id で紐づけられたもののみを抜き出す  -- (A)
);


select * 
from employees as em
where exists(
	SELECT 1 from departments as dt where em.department_id =dt.id   -- Select XX from X のXXのところは何でもよい、分かりやすく１と書くことが多い
);



-- (A)を副問い合わせで書くと下記になる
SELECT id from departments as dt 
where (
	select id as dt_em_id 
	from employees as em 
	where em.id = dt.id 
) ;


-- IN  (EXISTSはINで代用可能)
select * from employees  as em

where em.department_id in (select id from departments);


SELECT * from employees as em
where exists(
	select * from departments as dt 
	where dt.name in("営業部", "開発部") and em.department_id = dt.id
)

SELECT * from employees as em
where exists(
	select 1 from departments as dt 
	where dt.name in("営業部", "開発部") and em.department_id = dt.id
)

select * from departments as dt 
where dt.name in("営業部", "開発部");


/*---------------------------------45.EXISTの使い方2------------------------------- */

SELECT * from customers ;
SELECT * from orders  ;
SELECT * from employees ;

select * from customers as ct
where exists 
(SELECT * from orders as od where ct.id = od.customer_id and od.order_date = "2020-12-31");

select * from customers as ct
where not exists 
(SELECT * from orders as od where ct.id = od.customer_id and od.order_date = "2020-12-31");


SELECT * from employees as em1
where exists
(select 1 from employees as  em2 where em2.manager_id = em1.id )



/*---------------------------------46.NULLとEXISTS------------------------------- */

SELECT * from customers ;
SELECT * from customers_2 ;   -- customers と customers_2 でテーブルは同じ(NULLがある)

-- 上記2つをEXISTSで参照するとNULLのものが偽になるため出てこなくなる

SELECT * from customers as cs1
where EXISTS (
SELECT * from customers_2 as cs2
where 
	cs1.first_name = cs2.first_name and 
	cs1.last_name = cs2.last_name and
	cs1.phone_number = cs2.phone_number 
);


-- NULLのものを取り出したい場合はANDとORを使う
SELECT * from customers as cs1
where EXISTS (
SELECT * from customers_2 as cs2
where 
	cs1.first_name = cs2.first_name and 
	cs1.last_name = cs2.last_name and
	(cs1.phone_number = cs2.phone_number OR
		(cs1.phone_number is null and 
		 cs2.phone_number is null)
	)
);

-- NOT EXISTS > NULLの人も抽出される(EXISTSで紐づけられなかった人)

select * from customers as cs1
where not exists(
select * from customers_2 as cs2 
WHERE 
	cs1.first_name = cs2.first_name and 
	cs1.last_name = cs2.last_name and
	cs1.phone_number = cs2.phone_number 
);

-- NOT IN > 

SELECT * from customers as cs1
where (first_name, last_name, phone_number) not in (
select first_name , last_name , phone_number from customers_2 
);



-- 下記(A)と(B)のSQL文は同義
SELECT * from customers as cs1
where (first_name, last_name, phone_number) in (
select first_name , last_name , phone_number from customers_2 
);          --  (A)

select * from customers as cs1
where exists(
select * from customers_2 as cs2 
WHERE 
	cs1.first_name = cs2.first_name and 
	cs1.last_name = cs2.last_name and
	cs1.phone_number = cs2.phone_number 
);    -- (B)


-
/*---------------------------------47. INTERSEPTとEXCEPTをEXISTSで実装する------------------------------- */

-- EXCEPTをEXISTSで書く

select * from customers 
union
select * from customers_2  ;  -- 重複削除してレコードを抽出する

SELECT * from customers as cs1
where not EXISTS (
	SELECT * from customers_2 as cs2 
	WHERE 
		cs1.id = cs2.id and
		cs1.first_name  = cs2.first_name and
		cs1.phone_number = cs2.phone_number AND 
		cs1.age =cs2.age
);               -- cs1に存在して、cs2に存在しないテーブルを抜き出している。 しかし、nullについては注意が必要

SELECT * from customers as cs1
where not EXISTS (
	SELECT * from customers_2 as cs2 
	WHERE 
		cs1.id = cs2.id and
		cs1.first_name  = cs2.first_name and
		cs1.phone_number = cs2.phone_number AND 
		cs1.age =cs2.age
);               -- cs1に存在して、cs2に存在しないテーブルを抜き出している。 しかし、nullについては注意が必要


SELECT * from customers as cs1
where not EXISTS (
	SELECT * from customers_2 as cs2 
	WHERE 
		cs1.id = cs2.id and
		cs1.first_name  = cs2.first_name and
		(cs1.phone_number = cs2.phone_number or
			(cs1.phone_number is null and  cs2.phone_number is null)) and	
		cs1.age =cs2.age
);               -- cs1に存在して、cs2に存在しないテーブルを抜き出している。 しかし、nullについては注意が必要



-- INTERSEPTをEXISTSで表現する

SELECT * from customers as cs1
where EXISTS (
	SELECT * from customers_2 as cs2 
	WHERE 
		cs1.id = cs2.id and
		cs1.first_name  = cs2.first_name and
		(cs1.phone_number = cs2.phone_number or
			(cs1.phone_number is null and  cs2.phone_number is null)) and	
		cs1.age =cs2.age
);               -- cs1に存在して、cs2に存在しないテーブルを抜き出している。 しかし、nullについては注意が必要





