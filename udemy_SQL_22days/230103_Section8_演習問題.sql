 /*------------------------------------Section8 演習問題-----------------------------------*/

 /*-------------------------------------------------------------------------------------------------------------------------------*/
 
 
#  1. customersテーブルから、ageが28以上40以下でなおかつ、nameの末尾が「子」の人だけに絞り込んでください。
#  そして、年齢で降順に並び替え、検索して先頭の5件の人のnameとageだけを表示してください。 
 
SELECT 
	name,
	age
FROM
	customers 
WHERE 
	age >= 28 and age <= 40 and name like "%子"
ORDER BY 
	age DESC 
limit 5
;



 /*-------------------------------------------------------------------------------------------------------------------------------*/


# 2. receiptsテーブルに、「customer_idが100」「 store_nameがStore X」「priceが10000」のレコードを挿入してください。
# 3. 2で挿入してレコードを削除してください

SELECT 
	*
FROM 
	receipts 
order by 
	id DESC 
limit 5
;


-- INSERTでレコード(行)挿入
INSERT into receipts 
	(id, customer_id, store_name, price) values (301, 100, " Store X", 10000);  

-- delete from テーブル名 で レコード削除
delete from receipts where id = 301;


UPDATE set  receipts 
	store_name = "Store Y" 
WHERE 
	id = 301
	
	
 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 4. prefecturesテーブルから、nameが「空白もしくはNULL」のレコードを削除してください
	
SELECT 
	*
FROM 
	prefectures ;


DELETE FROM 
	prefectures 
WHERE
	name is NULL  or name = ""
;	


 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 5. customersテーブルのidが20以上50以下の人に対して、年齢を+1してレコードを更新してください  (ただし、BETWEENを使うこと)

SELECT 
	* ,
	age+1 as age_1
FROM 
	customers 
WHERE id BETWEEN 20 and 50;   -- BETWEEN A AND B


#UPDATE テーブル名 SET カラム名
UPDATE customers 
	set age = age+1 
WHERE id BETWEEN 20 and 50;

#確認
SELECT 
	* ,
	age+1 as age_1
FROM 
	customers ;
	
 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 6. studentsテーブルのclass_noが6の人すべてに対して、1～5のランダムな値でclass_noを更新してください

SELECT *, CEILING (rand()*5) FROM students where class_no =6;

UPDATE students 
	set class_no = CEILING (rand()*5) 
where class_no = 6




 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 7. class_noが3または4の人をstudentsテーブルから取り出します。取り出した人のheightに10を加算して、
# その加算した全値よりも、heightの値が小さくてclass_noが1の人をstudentsテーブルから取り出してください。

SELECT 
	*
FROM 
	students
WHERE 
	height < ALL (
		SELECT 
			height+10
		FROM 
			students 
		WHERE 
			class_no IN (3,4) ) and 
	class_no =1
;


SELECT 
	height+10
FROM 
	students 
WHERE 
	class_no =3 or class_no =4
order BY 
	height+10 ASC  ;


 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 8. employeesテーブルのdepartmentカラムには、「 営業部 」のような形で部署名の前後に空白が入っています。
# この空白を除いた形にテーブルを更新してください

SELECT 
	*,
	TRIM(department)
FROM 
	employees 
;

UPDATE employees 
	set department = trim(department); 



 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 9. employeesテーブルからsalaryが5000000以上の人のsalaryは0.9倍して、5000000未満の人のsalaryは1.1倍して下さい。
# (ただし、小数点以下は四捨五入します)

SELECT 
	*,
	CASE 
		when salary >= 5000000 then round(salary*0.9, 0)
		when salary < 5000000 then round(salary*1.1, 0)
	END as "salary_K2"
FROM 
	employees ;
	

UPDATE employees 
	set salary = case
		when salary >= 5000000 then round(salary*0.9, 0)
		when salary < 5000000 then round(salary*1.1, 0)
	END 

	
	
	
 /*-------------------------------------------------------------------------------------------------------------------------------*/
	
# 10. customersテーブルにnameが「名無権兵衛」、ageが0、birth_dayが本日日付の人を挿入してください。（ただし、日付関数を使うこと）
	
SELECT 
	*,
	date_format(now(),"%Y-%m-%d")
FROM 
	customers 
;

INSERT into customers 
	values(101, "名無権兵衛", 0, date_format(now(),"%Y-%m-%d"));


 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 11. customersテーブルに新たなカラムとして、「name_length INT」を作成します。
# name_lengthカラムをcustomersテーブルの各行の名前の文字数でアップデートしてください

SELECT 
	*,
	CHAR_LENGTH(name)
FROM 
	customers 
;

describe customers ;


# ALTER TABLE テーブル名 ADD カラム名 整数名
alter table customers 
add name_length INT ;

update customers 
set name_length = CHAR_LENGTH(name)
;



 /*-------------------------------------------------------------------------------------------------------------------------------*/

# 12. tests_scoreテーブルに新たなカラムとして、「score INT」を作成します。
# scoreカラムに、testsテーブルの各行のtest_score_1, test_score_2, test_score_3から、取り出したNULLでない最初の値で更新します。
# ただし取り出したtest_score_〇が、900以上の人は1.2倍して小数点以下を切り捨てて、600以下の人は0.8倍して小数点以下を切り上げてください。

SELECT 
	*,
	COALESCE (test_score_1, test_score_2, test_score_3) as score
FROM 
	tests_score 
;

alter table tests_score 
add score INT ;

describe tests_score ;

UPDATE tests_score 
set score = CASE 
	WHEN COALESCE (test_score_1, test_score_2, test_score_3) >= 900
		THEN FLOOR(COALESCE (test_score_1, test_score_2, test_score_3)*1.2)  -- 切り捨て
	WHEN COALESCE (test_score_1, test_score_2, test_score_3) <= 600
		THEN CEILING(COALESCE (test_score_1, test_score_2, test_score_3)*0.8)  -- 切り上げ
	ELSE COALESCE (test_score_1, test_score_2, test_score_3)
	END 

	
 /*-------------------------------------------------------------------------------------------------------------------------------*/
	
	
# 13. employeesテーブルを、 departmentが、マーケティング部 、研究部、開発部、総務部、営業部、経理部の順に
# なるように並び替えて表示してください。

SELECT * from employees 
order by
	case department 
		when "マーケティング部" THEN 1
		when "研究部" THEN 2
		when "開発部" THEN 3
		when "総務部" THEN 4
		when "営業部" THEN 5
		when "経理部" THEN 6
	end

