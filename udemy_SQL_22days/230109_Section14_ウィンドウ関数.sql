/*---------------------------------54．ウィンドウ関数 ~PARTITION BY ~---------------------------*/

use day_10_14_db;
show tables;

select * from employees ;

-- WINDOW関数
select 
	*,
	avg(age) over() ,
	count(*) over()
from 
	employees ;
	

-- PARTIION BY : 分割してその中で集計する
select 
	*,
	avg(age) over(PARTITION by department_id) as avg_age,
	count(*) over(PARTITION by department_id) as count_department
from
	employees ;
	

select 
	*,
	count(*) over(PARTITION by floor(age/10)) as age_count,
	floor(age/10)*10
from employees ;


select 
	distinct concat(count(*) over(PARTITION by floor(age/10)),"人") as age_count,
	floor(age/10)*10
from employees ;


select 
	*,
	date_format (order_date, "%Y%m") as "month" ,
	sum(order_amount * order_price) over(partition by  date_format (order_date, "%Y%m"))  as sum_order_price
from orders


/*---------------------------------55．ウィンドウ関数 ~ORDER BY~ ---------------------------*/

-- ORDER BY 
select 
	*,
	count(*) over (order by age) as tmp_count
from 
	employees 

select 
	*,
	sum(order_price) over(order by order_date) 
from orders;


select 
	DISTINCT concat(floor(age/10)*10 ,"代") as "年代",
	count(*) over (order by floor(age/10) ) as "人数"
from employees 



/*---------------------------------56．PARTITION BY と ORDER BYの併用 ---------------------------*/

-- PARTITION BY + ORDER BY 

select 
	*,
	count(*) over (partition by department_id order by age) ,
	concat(department_id, "-", count(*) over (partition by department_id order by age))
from employees 


-- 人毎の最大収入
select 
	*,
	max(payment) over (partition by emp.id)
from 
	employees as emp
inner join salaries as sa
on emp.id = sa.employee_id ;
	
-- 月毎、合計をemployeesのIDで昇順に並び替えてだす 
select 
	*,
	sum(sa.payment) over (partition by sa.paid_date order by emp.id)
from 
	employees as emp
inner join salaries as sa
on emp.id = sa.employee_id ;




/*---------------------------------57 フレーム幅の変更 ---------------------------*/

-- salesテーブルのorder_price * order_amountの合計値の7日間の平均を求める
-- まずは日付ごとの合計値を求める
-- 7日平均を求める
select 
	*,
	sum(order_price * order_amount) 
		over(order by order_date
		rows between 6 preceding and current row)
from orders
order by order_date


with daily_summary as(
	select 
		order_date ,
		sum(order_price * order_amount) as sale
	from
		orders 
	group by
		order_date 
	)
select 
	*,
	floor(avg(sale) over (order by order_date rows between 6 PRECEDING and CURRENT row))  -- 6行前から現在の行
from 
	daily_summary
	

select 
	*,
	sum(summary_salary.payment)
		over(order by age range between UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as p_summary  
					-- between UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ； 最初から最後まで
from employees as emp
inner join 
	(select
		employee_id,
		sum(payment) as payment
	from salaries 
	group by employee_id ) as summary_salary
on emp.id = summary_salary.employee_id;


/*---------------------------------58 ウィンドウ関数一覧 ---------------------------*/

-- ROW_NUMBER、RANK、DENSE_RANK

select
	*,
	ROW_NUMBER () over (order by age) as ROW_NUM ,        -- ROW_NUMBER 行数取得
	RANK () over (order by age) as  row_rank ,                         -- ランキング
	DENSE_RANK () over (order by age) as ROW_dense          -- ランキング
from employees 


-- CUBE_DIST、PERCENT_RANK
select 
	* ,
	count(*) over () as cnt,                                                          -- 行数
 	rank() over(order by age) as row_rank ,                               -- ランキング 
	percent_rank() over (order by age) as p_age ,                   -- (RANK-1)/(行数-1)
	CUME_DIST () over (order by age) as c_age                       -- 現在の小さい行より小さい行の割合
from 
	employees ;


-- LAG、LEAD

select 
	age,
	lag(age) over(order by age) ,                                           -- 直前の値を返す
	lag(age,3,0) over(order by age)  ,                                     -- 3つ前、ない場合は０
	lead(age) over(order by age),                                            -- 
	lead(age,2,0) over(order by age)                                      -- 
from 
	customers ;


-- FIRST VALUE, LAST VALUE

select 
	*,
	first_value(first_name) over(PARTITION by department_id order by age) , 
	last_value(first_name) over(PARTITION by department_id order by age range between UNBOUNDED PRECEDING and UNBOUNDED FOLLOWING) 
from employees ;

select 
	*,
	first_value(first_name) over(PARTITION by department_id order by age) , 
	last_value(first_name) over(PARTITION by department_id ) 
from employees ;


-- NTILE
SELECT 
	age,
	ntile(7) over(order by age)                                 -- グループ分け
from  
	employees ;



-- ウィンドウ関数はwhere句で使えない > エラーになる
SELECT 
	age,
	ntile(7) over(order by age)                                 -- グループ分け
from  
	employees 
where ntile(7) over(order by age) = 2;  

-- 使いたい場合は副問い合わせにする


select * from
	(SELECT 
		age,
		ntile(7) over(order by age) as ntile_value
	from employees) as tmp
where tmp.ntile_value= 2;  
