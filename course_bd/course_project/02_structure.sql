/*Создание таблиц*/
create table catalogs(
    id serial comment 'Идентификатор строки' primary key,
    name varchar(255) not null comment 'Название раздела',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки',
    constraint unique_name unique (name)
) comment 'Категории товара';

create table products(
    id serial comment 'Идентификатор строки' primary key,
    name varchar(255) not null comment 'Название',
    code varchar(255) null comment 'Артикул',
    barcode bigint unsigned null comment 'Штрих-код',
    description text null comment 'Описание',
    catalog_id bigint unsigned not null comment 'Ссылка на категорию товара',
    price_id bigint unsigned null comment 'Актуальная цена',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Товарные позиции';

create table products_specifications(
    id serial comment 'Идентификатор строки' primary key,
    product_id bigint unsigned not null comment 'Ссылка на товар',
    name enum('country','age','brand','gender') not null comment 'Характеристика',
    value_id bigint unsigned not null comment 'Ссылка на значение характеристики',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Характеристики товара';

create table specifications(
    id serial comment 'Идентификатор строки' primary key,
    name enum('country','age','brand','gender') not null comment 'Характеристика',
    value varchar(255) not null comment 'Значение характеристики',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Справочник характеристик товара';

create table media(
    id serial comment 'Идентификатор строки' primary key,
    product_id bigint unsigned not null comment 'Ссылка на товар',
    filename varchar(255) not null comment 'Путь к файлу',
    size int not null comment 'Размер файла',
    media_type enum('image','video') not null comment 'Тип файла',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Медиафайлы по товарам';

create table prices(
    id serial comment 'Идентификатор строки' primary key,
    product_id bigint unsigned not null comment 'Ссылка на товар',
    price_type enum('novelty','normal','discount','sale','super sale') not null comment 'Тип цены',
    price float not null comment 'Цена',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки'
) comment 'Цены';

create table orders(
    id serial comment 'Идентификатор строки - номер заказа' primary key,
    user_id bigint unsigned not null comment 'Ссылка на покупателя',
    pay_type enum('cash','card') not null comment 'Тип оплаты',
    status enum('open','canceled','close') not null comment 'Статус заказа',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Заказы';

create table orders_products(
    id serial comment 'Идентификатор строки' primary key,
    order_id bigint unsigned not null comment 'Ссылка на заказ',
    product_id bigint unsigned not null comment 'Ссылка на товар',
    qty int unsigned default '1' null comment 'Количество заказанных товарных позиций',
    total float not null comment 'Стоимость товарных позиций',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Состав заказа';

create table storehouses(
    id serial comment 'Идентификатор строки' primary key,
    name varchar(100) not null comment 'Название склада',
    description varchar(255) not null comment 'Описание склада',
    address varchar(255) not null comment 'Адрес склада',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Склады';

create table storehouses_products(
    id serial comment 'Идентификатор строки' primary key,
    storehouse_id bigint unsigned not null comment 'Ссылка на склад',
    product_id bigint unsigned not null comment 'Ссылка на товар',
    value int unsigned not null comment 'Запас товарной позиции на складе',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки'
) comment 'Товары на складе';

create table users(
    id serial comment 'Идентификатор строки' primary key,
    first_name varchar(100) not null comment 'Имя покупателя',
    last_name varchar(100) not null comment 'Фамилия покупателя',
    email varchar(100) not null comment 'Почта',
    phone varchar(100) not null comment 'Телефон',
    birthday date null comment 'Дата рождения',
    city varchar(130) not null comment 'Город доставки',
    address varchar(255) not null comment 'Адрес доставки',
    created_at datetime default CURRENT_TIMESTAMP null comment 'Время создания строки',
    updated_at datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'Время обновления строки',
    constraint email unique (email),
    constraint phone unique (phone)
) comment 'Покупатели';

/* Создание внешних ключей */
alter table products
    add constraint products_catalog_id_fk foreign key (catalog_id) references catalogs (id),
    add constraint products_price_id_fk foreign key (price_id) references prices (id);
alter table products_specifications
    add constraint products_specifications_product_id_fk foreign key (product_id) references products (id),
    add constraint products_specifications_value_id_fk foreign key (value_id) references specifications (id);
alter table media
    add constraint media_product_id_fk foreign key (product_id) references products (id);
alter table prices
    add constraint prices_product_id_fk foreign key (product_id) references products (id);
alter table orders
    add constraint orders_user_id_fk foreign key (user_id) references users (id);
alter table orders_products
    add constraint orders_products_order_id_fk foreign key (order_id) references orders (id),
    add constraint orders_products_product_id_fk foreign key (product_id) references products (id);
alter table storehouses_products
    add constraint storehouses_products_storehouse_id_fk foreign key (storehouse_id) references storehouses (id),
    add constraint storehouses_products_product_id_fk foreign key (product_id) references products (id);

/*Создание дополнительных индексов*/
create index products_name_idx on products(name);
create index products_code_idx on products(code);
create index products_barcode_idx on products(barcode);
create index products_specifications_product_id_name_idx on products_specifications(product_id, name);