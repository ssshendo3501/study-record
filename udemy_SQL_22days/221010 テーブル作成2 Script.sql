use my_db

select database();

#テーブル作成
create table users(
	id INT ,						   		-- idカラム、INT型
	name VARCHAR(10) ,    	-- 名前カラム、可変長文字列
	age INT ,  							-- 年齢カラム、INT型
	phone_number CHAR(13),	-- 電話番号、固定長
	message TEXT					-- messageカラム
)

#テーブル一覧表示
show tables;

#テーブルの定義確認
describe users;

#テーブルの削除
drop table users;

show tables;

#テーブル作成(主キー付き)
create table users(
	id INT primary key,					-- idカラム、INT型
	name VARCHAR(10) ,    			-- 名前カラム、可変長文字列
	age INT ,  									-- 年齢カラム、INT型
	phone_number CHAR(13),			-- 電話番号、固定長
	message TEXT							-- messageカラム
)

describe users;

# ---------------------------- #

select database();

#テーブル一覧
SHOW TABLES;

#テーブル名変更(RENAME TO)
ALTER table users RENAME to users_table;

SHOW TABLES;

DESCRIBE users_table;

#カラムの削除（DROP COLUMN）
ALTER TABLE users_table DROP COLUMN message;

#カラムの追加(ADD)
ALTER TABLE users_table 
ADD post_code CHAR(8);

ALTER TABLE users_table 
ADD gender CHAR(1) AFTER age;

describe users_table


#一番最初のカラムにADDする
ALTER TABLE users_table 
ADD new_id INT FIRST;

#カラムの定義変更
ALTER table users_table MODIFY name VARCHAR(50);




