/*------------------70.外部キー制約の基本的な書き方----------------------------*/

use day_15_18_db;
show tables;
drop table students;

create table schools(
	id int primary key,
	name varchar(255)
);

create table students(
	id int primary key ,
	name varchar(255) ,
	age int ,
	school_id int ,
	foreign key (school_id) references schools(id)
);

insert into schools values(1,"北高校"); 
insert into students values (1, "Taro", 18, 1);

select * from students;



/*------------------71.外部キー制約のオプション----------------------------*/

describe students;

drop table students;

create table students(
	id int primary key ,
	name varchar(255) ,
	age int ,
	school_id int ,
	foreign key (school_id) references schools(id)
	on delete cascade  on update cascade
);

insert into students values (1, "Taro", 18, 1);

select * from students;
update schools set id = 3 where id  = 1  -- 強制的にidを変更する

delete from schools;  -- 自動的に削除される


create table students(
	id int primary key ,
	name varchar(255) ,
	age int ,
	school_id int ,
	foreign key (school_id) references schools(id)
	on delete set null on update set null 
);


insert into schools values(2,"南高校");
insert into students values(2, "Taro", 16, 2);


update schools set id=3 where id =1

select * from students;

update students set school_id =3 where school_id is Null;
delete from schools where id = 3;


select * from schools;
insert into schools values (1,"北高校");
insert into students values(1, "Taro", 17, 1);



/*------------------72.制約の追加（UNIQUE制約）----------------------------*/

use day_15_18_db;

show tables;

select * from employees ;

describe employees ;

-- 制約の追加
ALTER table employees add constraint uniq_employees_name unique(name);

update employees set name ="Jiro" where employee_code = "00000002";

-- 制約一覧
select * from information_schema.KEY_COLUMN_USAGE
where table_name = "employees"

-- 制約削除
alter table employees drop constraint uniq_empolyees_name ;

-- CREATE文を確認
show create table employees ;


/*------------------73.制約の追加（DEFAULT、CHECK、NOT NULL制約）----------------------------*/

select * from customers ;

show create table customers ;

-- CHECK制約削除
alter table customers drop constraint customers_chk_1;


alter table customers 
alter age set default 20;

insert into customers (id,name) values(2,"Jiro");
  

-- NOT NULLの追加
alter table customers 
modify name varchar(255) not null;

insert into 
customers (id, name ) values(3, NULL);  -- NULLできない


-- CHECK制約の追加
alter table customers add constraint check_age check(age>=20);


alter table customers drop primary key;

describe customers ;


-- 主キーの追加
alter table customers 
add constraint pk_customers primary key(id, name)


-- 外部キー
describe students ;
show create table students;

alter table students drop constraint students_ibfk_1;

alter table students 
add constraint fk_schools_students
foreign key (school_id) references schools(id);



/*------------------74.その他のオプション----------------------------*/

create table animals(
	id int primary key auto_increment comment "主キーのID(Int型)",
	name varchar(50) not null comment "動物の名前"
);

-- COMMENTの確認
show full columns from animals;


insert into animals values (NULL,"dog");

select * from animals;

insert into animals (name) values ("cat");

-- 自動の値の確認
select AUTO_INCREMENT from information_schema.tables where table_name ="animals";
