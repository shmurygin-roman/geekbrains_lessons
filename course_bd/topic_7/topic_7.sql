/*
Задание 1.
Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
*/

select distinct
       u.id,
       u.name
  from users u
       join orders o on u.id = o.user_id;

/*
Задание 2.
Выведите список товаров products и разделов catalogs, который соответствует товару.
*/

select p.name,
       p.description,
       p.price,
       c.name as catalog_name
  from products p
       join catalogs c on p.catalog_id = c.id;

/*
Задание 3.
Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name).
Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.
*/

select f.id,
       cf.name as from,
       ct.name as to
  from flights f
       join cities cf on f.from = cf.label
       join cities ct on f.to = ct.label;