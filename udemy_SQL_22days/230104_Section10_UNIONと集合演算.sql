/*---------------------------------35.UNION, UNION ALLの利用------------------------------- */

show databases;
use day_4_9_db;
show tables;


-- union ：重複削除する
select * from new_students
union
select * from students
order by id
;

-- UNUON ALL : 重複削除しない
select * from new_students
union all
select * from students
order by id
;

-- UNUON ALL : 重複削除しない
select * from new_students where id >= 250
union all
select * from students where id <= 15
order by id
;

-- idとageは変数の型が同じであるため結合することができる
select 	id, name from students where id < 10
union
select age, name from users where id <10


/*---------------------------------36.集計関数------------------------------- */

select * FROM customers where name is null;
select * FROM users ;

-- COUNT
select count(*) from customers ;   -- 何行のデータが入っているか？
select count(id) from customers ;   -- 何行のデータが入っているか？
select count(name) from customers ;   -- 列指定(この列に何行入っているか(NULLはカウントしない))

SELECT count(name) from customers WHERE id>80

-- MAX、 min
SELECT 
	max(age),
	min(age)
FROM 
	users
where 
	birth_place ="日本"
;


-- SUM合計、AVG平均
SELECT 
	max(birth_day),
	min(birth_day),
	sum(age),
	avg(age)
FROM 
	users
where 
	birth_place ="日本"
;


-- AVG: NULLの場合が面倒

CREATE table tmp_count(
	num int
);

insert into tmp_count value(1);
insert into tmp_count value(2);
insert into tmp_count value(3);
insert into tmp_count value(NULL);

select * from tmp_count;

SELECT avg(num) from tmp_count;   -- NULLを省略して平均を出力
SELECT avg(COALESCE (num,0)) from tmp_count;   -- NULL=0として平均を出力



/*---------------------------------37.グループに分ける------------------------------- */

-- GROUP BY

SELECT 
	age , 
	count(*),
	max(birth_day) ,
	min(birth_day) 
from
	users 
where
	birth_place = "日本"
group by
	age
order by
	COUNT(*)
	; 


SELECT 
	department ,
	sum(salary),
	floor( avg(salary)),
	max(salary),
	min(salary)
from
	employees 
where 
	age > 40
group by
	department
order BY 
	sum(salary) DESC 
; 

SELECT 
	*
FROM 
	users 
group by 
	case
		when birth_place = "日本" then "日本人"
		else "その他"
	end
	;

SELECT 
	case
		when birth_place = "日本" then "日本人"
		else "その他"
	end as "国籍" ,
	count(*),
	max(age)
FROM 
	users 
group by 
	case
		when birth_place = "日本" then "日本人"
		else "その他"
	end
	;


SELECT * from prefectures ;

SELECT 
	CASE 
		when name in("香川県", "高知県", "愛媛県", "徳島県") then "四国"
		ELSE "その他"
	END as "地方名" ,
	count(*)
FROM 
	prefectures 
group by
	CASE 
		when name in("香川県", "高知県", "愛媛県", "徳島県") then "四国"
		ELSE "その他"
	END 



-- case 
	
SELECT 
	case 
		when age < 20 then "未成年"
		else "成人"
	end as "分類" ,
	count(*)
from 
	users 
group by
	case 
		when age < 20 then "未成年"
		else "成人"
	end 
order BY 
	age 
;
	
	
/*---------------------------------38.集計結果の絞り込み(Having)------------------------------- */	
	
-- HAVING 

SELECT 
	department ,
	floor(avg(salary)) as "ave_salary"
FROM 
	employees 
group by
	department 
HAVING 
	avg(salary) > 3980000   -- 集計した結果に対して層別することができる
;


SELECT 
	birth_place ,
	avg(age),
	count(*)
FROM 
	users
group by 
	birth_place ,age
HAVING 	
	count(*) > 1
order by
	birth_place 
;


-- Havingのみ

select 
	"重複無し"
FROM
	users 
having
	count(DISTINCT name) = count(name)

















































