-- Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»
/*
Задание 1.
Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
*/
update users
   set created_at = current_timestamp,
       updated_at = current_timestamp;
/*
Задание 2.
Таблица users была неудачно спроектирована.
Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10.
Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
*/
update users
   set created_at = STR_TO_DATE(created_at, '%d.%m.%Y %H:%i'),
       updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i');

alter table users modify column created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
alter table users modify column updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
/*
Задание 3.
В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы.
Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value.
Однако нулевые запасы должны выводиться в конце, после всех записей.
*/
select *
  from storehouses_products sp
order by if(sp.value=0,4294967295,sp.value);
/*
Задание 4.
Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий (may, august)
*/
select *
  from users u
 where lower(monthname(u.birthday_at)) in ('may', 'august');
/*
Задание 5.
Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
*/
select *
  from catalogs
  where id in (5, 1, 2)
order by field(id, 5, 1, 2);

-- Практическое задание теме «Агрегация данных»
/*
Задание 1.
Подсчитайте средний возраст пользователей в таблице users.
*/
select round(avg(TIMESTAMPDIFF(YEAR, u.birthday_at, now())),0) as age_avg
  from users u;
/*
Задание 2.
Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
Следует учесть, что необходимы дни недели текущего года, а не года рождения.
*/
select dayname(STR_TO_DATE(concat(extract(YEAR from curdate()),'-',extract(MONTH from u.birthday_at),'-',extract(DAY from u.birthday_at)), '%Y-%m-%d')) as birthday,
       count(*) qty
  from users u
group by birthday;
/*
Задание 3.
Подсчитайте произведение чисел в столбце таблицы.
*/
select round(exp(sum(ln(u.id))))
  from users u