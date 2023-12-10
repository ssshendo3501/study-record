/*------------------75.文字型(CHAR,VARCHAR、TEXT)----------------------------*/

use day_15_18_db;

create table message (
	name_code varchar(8),
	name varchar(255),
	message text                  -- 65535文字
);

insert into message values("00000001", "Yoshida Takeshi", "aaaba");
insert into message values("00000002", "Yoshida Takeshi", "aaabb");

select * from message;


/*------------------76.数値型----------------------------*/

create table patients(
	id smallint unsigned primary key auto_increment,  -- 0~65535
	name varchar(50),
	age tinyint unsigned default 0  -- 0~255
)

describe patients;

insert into patients (name ,age ) values("Sachiko", 34);
insert into patients (name ,age ) values("Sachiko", 255)

select * from patients;


insert into patients (id , age ) values(6000, 255);

alter table patients modify id mediumint unsigned auto_increment;  -- mediumint 0~1677215


-- heightカラム、weightカラム
alter table patients add column (height float);
alter table patients add column (weight float);

insert into patients (name , age , height, weight) values("Taro", 44, 175.769826020, 65.62527181);


create table int_float(
	num float
);

insert into int_float values(123456.654321);

select * from int_float;

create table tmp_double(
	num double
);

insert into tmp_double values(123456789.87654321234);

select * from tmp_double;



create table tmp_decimal2(
	num_float float,
	num_double double,
	num_decimal decimal(20,10)
);

insert into tmp_decimal2 values(111.11111111111111111111111111111111111,111.11111111111111111111111111111111111,111.11111111111111111111111111111111111)

select * from tmp_decimal2;


-- 論理型

create table managers(
	id int primary key auto_increment ,
	name varchar(50),
	id_superuser boolean
);

insert into managers (name , id_superuser) values("Taro", true);
insert into managers (name , id_superuser) values("Jiro", false);

select * from managers;



/*------------------78.日付型----------------------------*/

create table alarms (
	id int primary key auto_increment , 
	alarm_day date ,
	alarm_time time ,
	create_at timestamp default current_timestamp ,
	update_at timestamp default current_timestamp on update current_timestamp
);


select * from alarms;

select current_timestamp , now(), current_date, current_time;

insert into alarms (alarm_day , alarm_time) values ("2019-01-01", "19:50:21");
insert into alarms (alarm_day , alarm_time) values ("2021-11-01", "195041");

select * from alarms;
update alarms set alarm_time  = current_timestamp where id =1 ;

select hour (alarm_time) , alarm_time  from alarms;
select date_format (alarm_day, "%d") , second (alarm_time) , alarm_time  from alarms;

create table tmp_time(
	num time(5)
)

insert into tmp_time Values("21:05:21.5432")

select * from tmp_time;


-- datetime , timestamp

create table tmp_datetime _timestamp(
	val_datetime datetime,
	val_timestamp timestamp,
	val_datetime_3 datetime(3),
	val_timestamp_3  timestamp(3)
);

select * from tmp_datetime_timestamp;


/*------------------80.インデックス、関数インデックス、複数カラムへのインデックス----------------------------*/

show tables;
select * from students;

show index from students;

explain select * from students where name = "Taro";

create index idx_students_name on students(name);

explain select * from students where lower(name)  = "taro";

create index idx_students_lower_name on students((lower(name)));


select * from users ;

create unique index idx_users_uniq_first_name on users (first_name);
insert into users values(id, first_name ) values (3,"abc";)































