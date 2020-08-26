/*
Функция.
Возвращает текущую цену товара.
*/
create function get_price_by_product_id(p_product_id int)
returns float reads sql data
begin
    declare p_price float;
    select pr.price into p_price
      from products p
           join prices pr on p.price_id = pr.id
     where p.id = p_product_id;
    return p_price;
end;

/*
Триггер.
В таблице orders_products записывает или обновляет значение total.
*/

create trigger auto_update_total_on_insert before insert on orders_products
for each row
begin
    set new.total = round(get_price_by_product_id(new.product_id) * new.qty, 2);
end;

create trigger auto_update_total_on_update before update on orders_products
for each row
begin
    set new.total = round(get_price_by_product_id(old.product_id) * new.qty, 2);
end;