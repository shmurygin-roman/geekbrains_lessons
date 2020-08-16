/*
Задание 1.
В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
*/

start transaction;
use shop;
select @name := u.name, @birthday := u.birthday_at from users u where u.id = 1;
use sample;
insert into users(name, birthday_at) values (@name, @birthday);
commit;

/*
Задание 2.
Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
*/

create or replace view test_view as
select p.name as product_name,
       c.name as catalog_name
  from products p
       left join catalogs c on p.catalog_id = c.id;

select * from test_view;

/*
Задание 3.
Пусть имеется таблица с календарным полем created_at. В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17.
Составьте запрос, который выводит полный список дат за август, выставляя в соседнем поле значение 1, если дата присутствует в исходном таблице и 0, если она отсутствует.
*/

create or replace view calendar as
select STR_TO_DATE('2018-01-01','%Y-%m-%d') + INTERVAL d.day_of_year DAY as calendar_day
  from (select (c.num*100+b.num*10+a.num) as day_of_year
          from (select 0 as num union select 1 union select 2 union select 3 union select 4 union select 5 union select 6 union select 7 union select 8 union select 9) as a
               join (select 0 as num union select 1 union select 2 union select 3 union select 4 union select 5 union select 6 union select 7 union select 8 union select 9) as b
               join (select 0 as num union select 1 union select 2 union select 3 union select 4 union select 5 union select 6 union select 7 union select 8 union select 9) as c
        limit 365) as d;

select c.calendar_day,
       IF(u.created_at is null, 0, 1) as flag
  from calendar c
       left join users u on c.calendar_day = date_format(u.created_at,'%Y-%m-%d')
where c.calendar_day between '2018-08-01' and '2018-08-31';


/*
Задание 4.
Пусть имеется любая таблица с календарным полем created_at. Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.
*/

create or replace view tbl_valid_rows as
select created_at
  from tbl
order by created_at desc
limit 5;

delete from tbl
where created_at not in (select created_at from tbl_valid_rows);
