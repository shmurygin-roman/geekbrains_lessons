/*
Задание 1.
Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток.
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро",
с 12:00 до 18:00 функция должна возвращать фразу "Добрый день",
с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
*/

create function hello()
returns nvarchar(255) deterministic
begin
    declare t time;
    set t = now();
    if t between '06:00' and '11:59'
        then return 'Доброе утро';
    elseif t between '12:00' and '17:59'
        then return 'Добрый день';
    elseif t between '18:00' and '23:59'
        then return 'Добрый вечер';
    else return 'Доброй ночи';
    end if;
end;

/*
Задание 2.
В таблице products есть два текстовых поля: name с названием товара и description с его описанием.
Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема.
Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены.
При попытке присвоить полям NULL-значение необходимо отменить операцию.
*/

create trigger check_products before insert on products
for each row begin
    if new.name is null and new.description is null then
        signal sqlstate '45000' set message_text = 'INSERT canceled';
    elseif new.name is not null and new.description is null then
        set new.description = new.name;
    elseif new.name is null and new.description is not null then
        set new.name = new.description;
    end if;
end;

/*
Задание 3.
Напишите хранимую функцию для вычисления произвольного числа Фибоначчи.
Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел.
Вызов функции FIBONACCI(10) должен возвращать число 55.
*/

create function fibonacci(n int)
returns int deterministic
begin
    declare i, a, b int default 1;
    if n > 2 then
        set i = 3;
        while n >= i do
            set b = a + b;
            set a = b - a;
            set i = i + 1;
        end while;
    elseif n = 0 then
        set b = 0;
    end if;
    return b;
end;


