/* ---------------------------------83. Viewの作成-----------------------------------*/

use day_10_14_db;

show tables ;

select  * from items;
select * from stores;

-- viewの作成
create view stores_items_view as
select 
	st.name as store_name ,
	it.name as item_name 
from stores as st 
inner join items as it
on it.store_id = st.id;

-- 注意！テーブルができているわけではない
select *from stores_items_view;

update items set name = "new item 山田1" where name = "Item 山田 1";


-- テーブルとView の一覧
show tables;

select * from information_schema.views  where table_schema = "day_10_14_db"

-- view の詳細確認
show create view stores_items_view;

select * FROM stores_items_view where store_name = "山田商店";


-- View の定義変更
alter view stores_items_view as
select 
	st.id as store_id,
	it.id as item_id,
	st.name as store_name ,
	it.name as item_name 
from stores as st 
inner join items as it
on it.store_id = st.id;

select * from stores_items_view;

-- view の名前変更
rename table stores_items_view to new_stores_items_view;



