/*
Задание 3.
Проанализировать структуру БД vk, которую мы создали на занятии, и внести предложения по усовершенствованию (если такие идеи есть).
Напишите пожалуйста, всё-ли понятно по структуре.
 */
-- 1. Чтобы исключить нарушение целостности данных в связанных таблицах добавить внешние ключи
-- таблица messages
ALTER TABLE messages
  ADD CONSTRAINT from_user_fk FOREIGN KEY (from_user_id) REFERENCES users (id);
ALTER TABLE messages
  ADD CONSTRAINT to_user_fk FOREIGN KEY (to_user_id) REFERENCES users (id);
-- таблица friendship
ALTER TABLE friendship
  ADD CONSTRAINT friendship_user_fk FOREIGN KEY (user_id) REFERENCES users (id);
ALTER TABLE friendship
  ADD CONSTRAINT friendship_friend_fk FOREIGN KEY (friend_id) REFERENCES users (id);
ALTER TABLE friendship
  ADD CONSTRAINT status_fk FOREIGN KEY (status_id) REFERENCES friendship_statuses (id);
-- таблица communities_users
ALTER TABLE communities_users
  ADD CONSTRAINT communities_users_user_fk FOREIGN KEY (user_id) REFERENCES users (id);
ALTER TABLE communities_users
  ADD CONSTRAINT community_fk FOREIGN KEY (community_id) REFERENCES communities (id);
-- таблица media
ALTER TABLE media
  ADD CONSTRAINT media_user_fk FOREIGN KEY (user_id) REFERENCES users (id);
ALTER TABLE media
  ADD CONSTRAINT media_type_fk FOREIGN KEY (media_type_id) REFERENCES media_types (id);

-- 2. Создать таблицу friendship_history
-- которая будет хранить историю изменения дружбы
-- т.к. пользователи могут принять дружбу, потом через время удалить друга, потом через время опять добавить его в друзья
-- интересно было бы наблюдать как менялись взаимоотношения между людьми в сети
-- в этос случае немного изменим таблицу friendship
DROP TABLE friendship;

CREATE TABLE friendship (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
  user_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на инициатора дружеских отношений',
  friend_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на получателя приглашения дружить',
  status_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на статус (текущее состояние) отношений',
  requested_at DATETIME DEFAULT NOW() COMMENT 'Время отправления приглашения дружить',
  confirmed_at DATETIME COMMENT 'Время подтверждения приглашения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
  UNIQUE KEY (user_id, friend_id) COMMENT 'Составной первичный ключ'
) COMMENT 'Таблица дружбы';

CREATE TABLE friendship_history (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
  friendship_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на запись о дружеских отношениях',
  status_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на статус отношений',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  CONSTRAINT friendship_fk FOREIGN KEY (friendship_id) REFERENCES friendship (id),
  CONSTRAINT friendship_history_status_fk FOREIGN KEY (status_id) REFERENCES friendship_statuses (id)
) COMMENT 'История дружбы';

-- 3. Создать таблицу likes
CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор строки',
  media_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на медиафайл',
  user_id INT UNSIGNED NOT NULL COMMENT 'Ссылка на пользователя',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
  CONSTRAINT media_fk FOREIGN KEY (media_id) REFERENCES media (id),
  CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES users (id)
) COMMENT 'Лайки';