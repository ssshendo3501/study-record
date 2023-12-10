/*----------------SQL復習------------------------*/

show tables;

select databases();

use my_db;

show databases

show tables;

select * from people;

select * from students;

use day_4_9_db;

show tables;

select * from users;

select id, name as "名前", age as "年齢" from users ;

select id, name as "名前", age as "年齢" from users 
where name like "%成美%";

show tables;

describe users;

select * from users;

select * from users 
order by age DESC 
limit 10;


select * from users 
order by birth_day, birth_place
limit 10

#DISTINCT 

select 
	distinct birth_day, name
from 
	users
order by
	birth_day;


select * from users 



