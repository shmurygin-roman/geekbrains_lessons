/*
Задание 1.
Создайте таблицу logs типа Archive.
Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs помещается время и дата создания записи,
название таблицы, идентификатор первичного ключа и содержимое поля name.
*/

CREATE TABLE logs (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
    table_name VARCHAR(100) COMMENT 'Название таблицы',
    table_id INT COMMENT 'Идентификатор первичного ключа',
    name VARCHAR(255) COMMENT 'Содержимое поля name',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки'
) ENGINE = Archive COMMENT 'Лог';

create trigger insert_logs_users after insert on users
for each row begin
    insert into logs(table_name, table_id, name, created_at) values ('users', new.id, new.name, new.created_at);
end;

create trigger insert_logs_catalogs after insert on catalogs
for each row begin
    insert into logs(table_name, table_id, name) values ('catalogs', new.id, new.name);
end;

create trigger insert_logs_products after insert on products
for each row begin
    insert into logs(table_name, table_id, name, created_at) values ('products', new.id, new.name, new.created_at);
end;

/*
Задание 2.
Создайте SQL-запрос, который помещает в таблицу users миллион записей.
*/

create table helper (
  id int
);

insert into helper values (0),(1),(2),(3),(4),(5),(6),(7),(8),(9);

start transaction;

insert into users(name, birthday_at)
select concat('Тест',h6.id*100000+h5.id*10000+h4.id*1000+h3.id*100+h2.id*10+h1.id),
       CURRENT_TIMESTAMP
  from helper h1,
       helper h2,
       helper h3,
       helper h4,
       helper h5,
       helper h6;

commit;
