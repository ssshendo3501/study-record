/*------------------------------------18.算術演算子日付関数の利用方法------------------------------------*/

select 1+ 1;

select * from users limit 10;

#age+3のカラムを「age_3」として追加し、name、ageとともにリストを作成（10行以内）
select name, age, age+3 as age_3 from users limit 10;

select  age-1 as age_1 from users limit 10;

select  birth_day, birth_day+2  as birth_day_2 from users limit 10;


#掛け算割り算
select 3*5;

select 
	department ,
	name, 
	age,
	salary ,
	salary*0.9 as next_salary
from employees ; 

select 
	department ,
	name, 
	age,
	salary ,
	salary/10 as next_salary
from employees ; 

#あまり
select 10 % 3; -- 10を3で割った余りが1
select age % 12 from users ;; -- 12で割ったあまりが抽出できる

#CONCAT; 文字の連結 -> エクセルの＆関数
select 
	concat(department ,”:”, name) as ”部署: 名前”
from employees ;

select 
	concat(department ,": ", name) as "部署: 名前"
from employees ;

select 
	concat(name ,"(", age ,")") as "名前(年齢)"
from users ;

#時間NOW、CURDATE、DATE FORMAT
select 
	now()
from users ;

select 
	now(),
	name,
	age
from users ;

select 
	now(), -- 現在の日時
	curdate(), -- 日付の日付
	date_format(now(), "%Y/%m/%d %H時")
from users ;


/*------------------------------------19.文字列関数------------------------------------*/
# LENGTH、CHAR LENGTH
select LENGTH("ABCD") ; -- 4Byte
select LENGTH("あいう") ; -- 9Byte

select CHAR_LENGTH("ABCD") ; -- 4文字
select CHAR_LENGTH("あいう") ; -- 3文字

SELECT 
	name,
	 CHAR_LENGTH(name) as "文字数"  -- スペースキー含む
FROM 
	users;

# TRIM、LIMIT、RTRIM 空白削除
SELECT LTRIM("    A B  C    ");   -- 左スペース削除
SELECT RTRIM("    A B  C    ");  -- 右スペース削除 
SELECT LTRIM("    A B  C    ");  -- 左右スペース削除

#顧客データの中からスペースキーが混じっていて文字数と通常の文字数とマッチングしない人を抽出するSQL
SELECT
	name,
	CHAR_LENGTH(name) as "name_length"
FROM
	employees
WHERE
	CHAR_LENGTH(name) <> CHAR_LENGTH(TRIM(name));

#顧客データの中からスペースキーが混じっていて文字数と通常の文字数とマッチングした人を抽出するSQL
SELECT
	name,
	CHAR_LENGTH(name) as "name_length"
FROM
	employees
WHERE
	CHAR_LENGTH(name) = CHAR_LENGTH(TRIM(name));

#UPDATEして空白を削除したものにする > 5行アップデートされましたと表示
UPDATE employees 
	SET name = TRIM(name)  -- nameをTRIM(左右スペースキー削除)
WHERE 
	CHAR_LENGTH(name)<>CHAR_LENGTH(TRIM(name));  -- 名前文字数がTRIMしたものと一致しないもののみ
	


/*------------------------------------20.文字列関数------------------------------------*/
# REPLACE ； 置換 > apple lemon
SELECT REPLACE ("I like an apple", "apple", "lemon");
	
SELECT * FROM USERS;

#Mrs ＞Msへ置換する
SELECT 
	REPLACE(name, "Mrs", "Ms" ) 
FROM
	users 
WHERE
	name LIKE "Mrs%"	;
	
# 1行UPDATEされましたと表示
UPDATE users 
	Set name = REPLACE(name, "Mrs", "Ms" ) WHERE name LIKE "Mrs%"	;



# UPPER LOWER（大文字 小文字)

SELECT UPPER("apple");   --  > APPLE
SELECT LOWER("APPLE");   --  > apple

SELECT 
	name,
	UPPER(name) AS "U_NAME",
	LOWER(name) AS "l_name"
FROM
	users;

#SUBSTRING 一部取り出し
#名前の2,3文字目を取り出す
SELECT 
	SUBSTRING(name, 2,3),
	name
FROM
	users;

#2文字目が田の人を取り出す
SELECT 
	*
FROM
	employees 
WHERE
	SUBSTR(name, 2,1) = "田";


#REVERSE；文字列を逆順
SELECT REVERSE(name), name from employees ；

/*------------------------------------21.数学関数------------------------------------*/

SELECT ROUND(13.14 , 2); -- 四捨五入
SELECT FLOOR(13.14); -- 切り捨て
SELECT CEILING(13.14); -- 切り上げ

SELECT RAND();  -- 0~1をランダムで抽出
SELECT 
	RAND() as "RANDOM_Number" , -- 0~1をランダムで
	FLOOR(RAND()*10)
;

#POWER > べき乗 (３の4乗)
SELECT POWER (3,4);

SELECT
	weight / POWER(height/100,2) AS "BMI"
FROM
	students 
;


#COALESCE > 最初に登場するNULLでない値を取り出す

elect 
	*
from 
	tests_score
;

select coalesce(NULL, NULL, NULL, "A", NULL, "B");   -- > A

select 
	*,
	coalesce (test_score_1, test_score_2, test_score_3) AS score
FROMs
	tests_score
;



