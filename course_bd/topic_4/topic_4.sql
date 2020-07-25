/*
Задание 2.
Подобрать сервис который будет служить основой для вашей курсовой работы.
*/
-- Т.к. в моих планах разработать интернет магазин детских игрушек, то для курсовой работы мне хотелось бы взять именно этот сервис.

/*
Задание 3.
Предложить свою реализацию лайков и постов.
*/
-- Реализация лайков

-- Если хотим реализовать лайки на все возможное, то предлагаю хранить информацию что лайкнул пользователь в двух атрибутах:
-- sourse_type - это код таблицы. Пример: MDA - таблица media, MSG - messages, CMT - communities.
-- sourse_pk - это первичный ключ в таблице из source_type.

CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
  sourse_type VARCHAR(3) NOT NULL COMMENT 'Код таблицы: MDA - таблица media, MSG - messages, CMT - communities',
  sourse_pk INT UNSIGNED NOT NULL COMMENT 'Ссылка на первичный ключ в таблице из source_type',
  user_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на пользователя',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
  UNIQUE KEY (sourse_type, sourse_pk) COMMENT 'Уникальный ключ',
  CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES users (id)
) COMMENT 'Лайки';

-- Реализация постов

-- Разделил бы на 2 части:
-- 1. Пост на стене пользователя
-- По сути это сообщение одного пользователя другому, только для общего обозрения
-- Поэтому в этих целях модифицируем таблицу messages
-- добавим атрибут is_private: значение true - это личное сообщение, false - сообщение на стене

ALTER TABLE messages ADD COLUMN is_private BOOLEAN AFTER is_modified;

-- 2. Пост в группе
-- В данной части мы можем реализовать 2 вида постов: сообщения в группе и групповой чат
-- Чтобы не добавлять новые таблицы участников группового чата можем хранить в таблице communities_users
-- Для этого добавим в таблицу communities атрибут type - тип группы: 1 - Группа, 2 - Групповой чат

ALTER TABLE communities ADD COLUMN type CHAR(1) COMMENT 'Тип группы: 1 - Группа, 2 - Групповой чат' AFTER name;

CREATE TABLE community_messages (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
    community_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на группу',
    from_user_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на отправителя сообщения',
    to_user_id INT UNSIGNED COMMENT 'Ссылка на получателя сообщения. Для случая если сообщение в группе адресовано конкретному пользователю',
    body TEXT COMMENT 'Текст сообщения',
    is_modified BOOLEAN COMMENT 'Признак изменения',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
    CONSTRAINT community_fk FOREIGN KEY (community_id) REFERENCES communities (id),
    CONSTRAINT from_user_fk FOREIGN KEY (from_user_id) REFERENCES users (id),
    CONSTRAINT to_user_fk FOREIGN KEY (to_user_id) REFERENCES users (id)
) COMMENT 'Групповые сообщения';