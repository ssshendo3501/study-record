use my_db;

SELECT DATABASE();

# STUDENTSテーブルの作成
create table students(
	id INT PRIMARY KEY,
	name CHAR(10)
);

#CHAR型は末尾のスペースが削除される
INSERT INTO students VALUES(1, "ABCDEF  ");

select * from students;

# CHAR →VARCHARに変更
ALTER TABlE students modify name  VARCHAR(10);

insert into students values(2,"ABCDEF   ");

select * from students ;

#nameの文字列を実施
select name, char_length(name) from students;