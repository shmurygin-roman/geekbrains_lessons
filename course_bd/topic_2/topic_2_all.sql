/*
Задание 2.
Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/
create database if not exists example;
use example;
create table users (
    id serial,
    name varchar(255)
);
insert into users values (null,'Иванов');
insert into users values (null,'Петров');
insert into users values (null,'Сидоров');

/*
Задание 3.
Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
*/
create database if not exists sample;
-- выполнялось в командной строке
mysqldump -u root -p example > example.sql
mysql -u root -p sample < example.sql

/*
Задание 4.
Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы help_keyword базы данных mysql.
Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/
-- выполнялось в командной строке
mysqldump -u root -p --opt --where="1 order by help_keyword_id limit 100" mysql help_keyword > help_keyword.sql