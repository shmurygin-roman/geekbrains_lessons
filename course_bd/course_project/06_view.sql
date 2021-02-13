/*
Представление 1.
Выводит по товару одной записью описание, характеристики, медиафайлы, цену и наличие.
*/
create view v_products as
select distinct
       p.id,
       p.name,
       p.description,
       p.barcode,
       p.code,
       c.name as catalog_name,
       s1.value as country,
       s2.value as age,
       s3.value as brand,
       s4.value as gender,
       m1.filename as image,
       m2.filename as video,
       pr.price,
       pr.price_type,
       sum(sp.value) over (partition by sp.product_id) as qty
  from products p
       join catalogs c on p.catalog_id = c.id
       left join products_specifications ps1 on p.id = ps1.product_id and ps1.name = 1 /*country*/
       left join specifications s1 on ps1.value_id = s1.id
       left join products_specifications ps2 on p.id = ps2.product_id and ps2.name = 2 /*age*/
       left join specifications s2 on ps2.value_id = s2.id
       left join products_specifications ps3 on p.id = ps3.product_id and ps3.name = 3 /*brand*/
       left join specifications s3 on ps3.value_id = s3.id
       left join products_specifications ps4 on p.id = ps4.product_id and ps4.name = 4 /*gender*/
       left join specifications s4 on ps4.value_id = s4.id
       left join media m1 on p.id = m1.product_id and m1.media_type = 1 /*image*/
       left join media m2 on p.id = m2.product_id and m2.media_type = 2 /*video*/
       join prices pr on p.price_id = pr.id
       left join storehouses_products sp on p.id = sp.product_id;

/*
Представление 2.
Выводит заказ и все товары в заказе.
*/

create view v_orders as
select o.id,
       u.last_name,
       u.first_name,
       u.birthday,
       u.address,
       u.email,
       u.phone,
       o.pay_type,
       o.status,
       p.name,
       pr.price,
       op.qty,
       op.total,
       round(sum(op.total) over (partition by o.id), 2) as total_sum
  from orders o
       join users u on o.user_id = u.id
       join orders_products op on o.id = op.order_id
       join products p on op.product_id = p.id
       join prices pr on p.price_id = pr.id;