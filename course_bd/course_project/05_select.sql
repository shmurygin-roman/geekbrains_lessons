/*
Выборка 1.
Считает каким кол-вом товара представлена каждая категории.
*/

select c.id,
       c.name,
       count(p.id) as qty
  from catalogs c
       left join products p on c.id = p.catalog_id
group by c.id
order by c.id;

/*
Выборка 2.
Выводит весь ассортимент товаров с указанием текущей цены, общим количеством товара и на каком складе сколько есть в наличие.
*/

select c.name as catalog_name,
       p.name as product_name,
       p.code,
       p.barcode,
       pr.price_type,
       pr.price,
       if(sum(sp.value) is null, 0, sum(sp.value)) as value,
       group_concat(concat(s.name,'=', sp.value)) as storehouse
  from products p
       join catalogs c on p.catalog_id = c.id
       join prices pr on p.price_id = pr.id
       left join storehouses_products sp on p.id = sp.product_id
       left join storehouses s on sp.storehouse_id = s.id
group by c.id, c.name, p.name, p.code, p.barcode, pr.price_type, pr.price
order by c.id, value desc;

/*
Выборка 3.
Выводит топ-10 самых заказываемых товаров.
Каждой позиции выставляет место и делает сортировку от 10 до 1 места.
*/

select concat(row_number() over (), ' place') as place,
       t.product_name,
       t.catalog_name,
       t.qty
from (
select p.name as product_name,
       c.name as catalog_name,
       sum(op.qty) as qty
  from products p
       join catalogs c on p.catalog_id = c.id
       join orders_products op on p.id = op.product_id
group by p.name, c.name
order by qty desc
limit 10) t
order by row_number() over () desc;

/*
Выборка 4.
Выводит все товары по акции с указанием текущей цены, первоначальной цены и сколько процентов составила скидка.
*/

select c.name as catalog_name,
       p.name as product_name,
       pr.price as current_price,
       pr2.price as first_price,
       100 - round(pr.price / pr2.price * 100) as '%%'
  from products p
       join catalogs c on p.catalog_id = c.id
       join prices pr on p.price_id = pr.id
       left join storehouses_products sp on p.id = sp.product_id
       left join prices pr2 on p.id = pr2.product_id and pr2.price_type = 2
where sp.value is not null
  and  pr.price_type in (3,4,5)
order by c.id, p.name;

/*
Выборка 5.
Выводит топ-10 покупателей, которые заплатили больше всего за свои заказы.
*/

select u.id,
       u.last_name,
       u.first_name,
       u.city,
       count(distinct o.id) as qty_orders,
       round(sum(op.total), 2) as total_sum
  from users u
       join orders o on u.id = o.user_id
       join orders_products op on o.id = op.order_id
where o.status <> 2
group by u.id
order by total_sum desc
limit 10;