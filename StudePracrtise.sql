show data_directory

create table subjects (subj_id int, subj_name text)

select * from subjects

insert into subjects (subj_id, subj_name) values (4,'Chem')

update subjects set subj_name = 'Chemistry' where subj_id = 4

create table students (stud_id int, name text, group_id int)

create table groups (group_id int, group_name text)

create table grades (stud_id int, subj_id int, value int)

create view v1 as
select stu."name", sub.subj_name , gro.group_name , gra.value 
from students stu,
	 grades gra,
	 "groups" gro,
	 subjects sub
where stu.group_id = gro.group_id 
and gra.stud_id = stu.stud_id 
and gra.subj_id = sub.subj_id 
S
select * from v1

select * from grades g 

ALTER TABLE students ADD PRIMARY KEY (stud_id)
	
ALTER TABLE "groups"  ADD PRIMARY KEY (group_id);

ALTER TABLE subjects ADD PRIMARY KEY (subj_id);

ALTER TABLE students 
ADD CONSTRAINT stud_group_fk 
FOREIGN KEY (group_id) 
REFERENCES "groups" (group_id);

ALTER TABLE grades
ADD constraint grades_stud_fk
FOREIGN KEY (stud_id) 
REFERENCES students (stud_id);

show data_directory

create table subjects (subj_id int, subj_name text)

select * from subjects

select * from students

insert into subjects (subj_id, subj_name) values (4,'Chem')

update subjects set subj_name = 'Chemistry' where subj_id = 4

create table students (stud_id int, name text, group_id int)

create table groups (group_id int, group_name text)

create table grades (stud_id int, subj_id int, value int)

create view v1 as
select stu."name", sub.subj_name , gro.group_name , gra.value 
from students stu,
	 grades gra,
	 "groups" gro,
	 subjects sub
where stu.group_id = gro.group_id 
and gra.stud_id = stu.stud_id 
and gra.subj_id = sub.subj_id 

select stu."name", sub.subj_name , gro.group_name , gra.value 
from students stu,
	 grades gra,
	 "groups" gro,
	 subjects sub
where stu.group_id = gro.group_id 
and gra.stud_id = stu.stud_id 
and gra.subj_id = sub.subj_id
and stu.stud_id = 1

alter table grades add grade_date date

select * from v1

select * from grades g

update grades set grade_date = '14-OCT-2022'

ALTER TABLE students ADD PRIMARY KEY (stud_id)
	
ALTER TABLE "groups"  ADD PRIMARY KEY (group_id);

ALTER TABLE subjects ADD PRIMARY KEY (subj_id);

ALTER TABLE students 
ADD CONSTRAINT stud_group_fk 
FOREIGN KEY (group_id) 
REFERENCES "groups" (group_id);

ALTER TABLE grades
ADD constraint grades_stud_fk
FOREIGN KEY (stud_id) 
REFERENCES students (stud_id)


ALTER TABLE grades
ADD constraint grades_subj_fk
FOREIGN KEY (subj_id) 
REFERENCES subjects (subj_id)

CREATE SEQUENCE stud_id_seq START 1;

CREATE SEQUENCE group_id_seq START 1;

CREATE SEQUENCE subj_id_seq START 1;