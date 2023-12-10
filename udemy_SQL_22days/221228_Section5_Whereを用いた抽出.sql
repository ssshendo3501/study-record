/*--------------14.Whereの基本的な使い方-------------------*/

create database day_4_9_db;
use day_4_9_db ;
show tables;

# usersの定義確認
describe users;
select * from users limit 10;

#特定の言葉を抽出
select * from users where name = "奥村 成美"
select * from users where birth_place  = "日本";

#xx以外を抽出
select * from users where birth_place <> "日本" order by age Limit 10;


select * from users where age >-50 order by id Limit 10;

describe users;

select * from users where birth_day < "2011-01-02" order by id Limit 10;

select * from users where is_admin = 1 order by id;

#UPDATE
select * from users;
UPDATE users set name = "奥山 成美" where id = 1;

delete from users where id >190;

/*--------------15.NULL BETWEEN LINK-------------------*/

select database();
describe customers ;

select * from customers;
select * from customers where name is null ;
select * from customers where name is not  null ;

select *from prefectures  where name = "";

#BETWEEN
select * from users where age not between 5 and 10;
select * from users where age between 5 and 10;

#LIKE NOT LIKE
select * from users where name like "村%"; -- 前方一致
select * from users where name like "%郎"; -- 後方一致
select * from users where name like "%a%"; -- 中間一致
select * from prefectures where name like "福_県"; -- _は任意の一文字

/*--------------16.IN ANY ALL AND OR NOT-------------------*/
select database();
describe customers ;

#IN > エクセルのフィルタ処理
select * from users where birth_place  IN("France", "Germany", "Italy");
select * from users where birth_place  NOT IN("France", "Germany", "Italy");

#select + in
select * from customers where id in (select customer_id from receipts);

	#receiptsのテーブルの中からcustomer_idを抽出
	select customer_id from receipts;
	select * from receipts;
	
	#receiptsのテーブルの中からcustomer_idを抽出
	select * from customers;  -- customersテーブルの全抽出
	select * from customers where id in (select customer_id from receipts);

#ALL ANY
select * from employees where salary >5000000; 
	-- 従業員データから年収500万円より多い人を抽出

select age  from employees where salary >5000000;
	-- 従業員データから年収500万円より多い人の年齢を抽出
select age  from employees where salary >5000000 order by age ;
	-- 23~45歳の年齢リストを抽出

#select > All, Any
select * from users where age >all (select age from employees where salary >5000000);
	-- 45歳より大きい人のusersテーブルを抽出
select * from users where age >any (select age from employees where salary >5000000);
	-- 23歳より大きい人のusersテーブルを抽出
select * from users where age = any (select age from employees where salary >5000000);
	-- 23~45と等しいusersテーブルを抽出

#AND NOT
select * from employees ;
select * from employees where department = " 営業部 "  and name like "%田%" ;
select * from employees where department = " 営業部 "  and name like "%田%" and age < 35;
select * from employees where department = " 営業部 "  and (name like "%田%" or name like "%西%") and age < 35;
select * from employees where department = " 営業部 " or department = " 開発部 ";
# ↑↓は同義
select * from employees where department in ( " 営業部 "  , " 開発部 "  ) ;


/*--------------17.NULLについての注意点-------------------*/
show tables;


select * from customers;

select * from customers where name is null;

select * from customers where name in ("河野 文典", "稲田 季雄");

#NULLを取り出す際はIS NULL で抽出する
select * from customers where name in ("河野 文典", "稲田 季雄") or name is null;


select * from customers where name not in ("河野 文典", "稲田 季雄");

select * from customers where name not in ("河野 文典", "稲田 季雄") and name is not null;


#ALL、INの時はNULLがあるときは気を付ける！！！

#idが10より小さい誕生日を抜き出す 
select * from users;
select birth_day  from customers where id < 10 ; 
	-- 6行目にNULLが入るリストができる
select * from users where birth_day <= all (select birth_day  from customers where id < 10) ; 
	-- NULLがあるリストであるためうまく抽出できない
select * from users where birth_day <= all (select birth_day  from customers where id < 10 and birth_day is not null) ; 
	-- and is not null でNULLをなくしリストを作成→抽出する
	-- 顧客テーブルからidが10より古い誕生日リストを作成し、その誕生日とマッチングするusersから抽出するSQL



