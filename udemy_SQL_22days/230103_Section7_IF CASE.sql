/*------------------------------------22.IF式------------------------------------*/

select database();
show tables;


#IF(条件式、真の値、偽の値)
select if(10>20,"A","B");

select * from users;

#出身地をIF文区別して国籍のカラムを追加する
select 
	*,
	if(birth_place="日本", "日本人", "その他") as "国籍"
FROM
	users;
	
select 
	*,
	if(birth_place="日本", "日本人", "その他") as "国籍" ,
	if(age<20, "未成年", "成人") as "成人有無"	
FROM
	users;
	
select 
	*
from 
	students ;
	
select 
	*,
	if(class_no=6 and height >=170, "6組で170cm以上", "その他") AS "Class6&170cm以上"
from 
	students ;
	
select
	*,
	if(birth_place="日本", "日本人", "その他") as "国籍" ,
	if(age<20, "未成年", "成人") as "成人有無" ,
	if(name like "%田%" ,"名前に田を含む", "その他") as "●田の人"
FROM
	users;
	


/*------------------------------------23.CASE式の使い方=基本=------------------------------------*/

SELECT * FROM users;

SELECT 
	*,
	case birth_place 
	when "日本" then "日本人"
	when "Iraq" then "イラク人"
	else "外国人"
	end as "国籍"
from
	users
where 
	id > 30
limit 10
;


SELECT * FROM prefectures ;

SELECT 
	*,
	CASE 
		when name in("香川県", "愛媛県",  "徳島県", "高知県") then "四国"
		when name in("兵庫県", "大阪府",  "京都府", "滋賀県", "三重県", "和歌山県") then "近畿"
		else "その他"
	END as "地方名"
from
	prefectures 
;
	

-- 計算式

SELECT 
	*,
	CASE 
		when DATE_FORMAT(birth_day, "%Y") %4 = 0 and DATE_FORMAT(birth_day, "%Y") %100 <> 0 
			then "うるう年"   -- うるう年
		else "うるう年でない"
	END as "うるう年か"
from users;

SELECT 
	*,
	case 
		when student_id % 3 =0 then test_score_1
		when student_id % 3 =1 then test_score_2
		when student_id % 3 =2 then test_score_3
	end as "Score"
FROM 
	tests_score
;

/*------------------------------------23.CASE式の使い方=ORDER BY , UPDATE=------------------------------------*/

select
	*,
	case 
		when name in("香川県", "愛媛県",  "徳島県", "高知県") then "四国"
		when name in("兵庫県", "大阪府",  "京都府", "滋賀県", "三重県", "和歌山県") then "近畿"
		else "その他"
	End as "地域名"
FROM 
	prefectures 
order by
	case 
		when name in("香川県", "愛媛県",  "徳島県", "高知県") then "四国"
		when name in("兵庫県", "大阪府",  "京都府", "滋賀県", "三重県", "和歌山県") then "近畿"
		else "その他"
	END desc  -- descで降順に並び変えることができる
;


select
	*,
	case 
		when name in("香川県", "愛媛県",  "徳島県", "高知県") then "四国"
		when name in("兵庫県", "大阪府",  "京都府", "滋賀県", "三重県", "和歌山県") then "近畿"
		else "その他"
	End as "地域名"
FROM 
	prefectures 
order by
	case 
		when name in("香川県", "愛媛県",  "徳島県", "高知県") then 0  -- 四国が1個目
		when name in("兵庫県", "大阪府",  "京都府", "滋賀県", "三重県", "和歌山県") then 1 -- 近畿が2個目
		else 2  -- その他が3個目
	END  
;


-- UPDATE + CASE
select *from users;

alter table 
	users 
add 
 	birth_era Varchar(2) 
 After
 	birth_day;
 	
 
 select 
 	*,
 	case 
 		when birth_day < "1989-01-07" then "昭和"
 		when birth_day < "2019-05-01" then "平成"
 		when birth_day >= "2019-05-01" then "令和"
 		else "不明" 
 	end as "元号"
 from users ;
 

UPDATE users 
	set birth_era = case 
 		when birth_day < "1989-01-07" then "昭和"
 		when birth_day < "2019-05-01" then "平成"
 		when birth_day >= "2019-05-01" then "令和"
 		else "不明" 
 	end ;
 	
 
 
 /*------------------------------------24.CASE式の使い方=NULL=------------------------------------*/
 
 select * from customers WHERE name is null;

 select 
 	*, 
 	case 
 		when name is null then "不明"    -- NULLを区別する際は、 name is NULL と書く
 		when name is not null then "NULL以外"    -- NULLを区別する際は、 name is NULL と書く
  		else ""
 		end as "NULL_CHECK"
 from 
 	customers ;
 
 
 