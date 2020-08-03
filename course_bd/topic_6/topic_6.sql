/*
Задание 1.
Создать все необходимые внешние ключи и диаграмму отношений.
*/

-- таблица communities_users
ALTER TABLE communities_users
  ADD CONSTRAINT communities_users_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT communities_users_community_id_fk FOREIGN KEY (community_id) REFERENCES communities (id);
-- таблица friendship
ALTER TABLE friendship
  ADD CONSTRAINT friendship_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT friendship_friend_id_fk FOREIGN KEY (friend_id) REFERENCES users (id),
  ADD CONSTRAINT friendship_status_id_fk FOREIGN KEY (status_id) REFERENCES friendship_statuses (id);
-- таблица likes
ALTER TABLE likes
  ADD CONSTRAINT likes_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT likes_target_type_id_fk FOREIGN KEY (target_type_id) REFERENCES target_types (id);
-- таблица media
ALTER TABLE media
  ADD CONSTRAINT media_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT media_type_id_fk FOREIGN KEY (media_type_id) REFERENCES media_types (id);
-- таблица messages
ALTER TABLE messages
  ADD CONSTRAINT messages_from_user_id_fk FOREIGN KEY (from_user_id) REFERENCES users (id),
  ADD CONSTRAINT messages_to_user_id_fk FOREIGN KEY (to_user_id) REFERENCES users (id);
-- таблица posts
ALTER TABLE posts
  ADD CONSTRAINT posts_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT posts_community_id_fk FOREIGN KEY (community_id) REFERENCES communities (id),
  ADD CONSTRAINT posts_media_id_fk FOREIGN KEY (media_id) REFERENCES media (id);
-- таблица profiles
ALTER TABLE profiles
  ADD CONSTRAINT profiles_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id),
  ADD CONSTRAINT profiles_photo_id_fk FOREIGN KEY (photo_id) REFERENCES media (id);

/*
Задание 2.
Создать и заполнить таблицы лайков и постов.
*/

-- Создал, заполнил и выгрузил дампы таблиц.

/*
Задание 3.
Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

select 'men' as gender,
       count(*) as qty
  from likes l
 where l.user_id in (select p.user_id from profiles p where p.gender = 1)
union
select 'women',
       count(*)
  from likes l
 where l.user_id in (select p.user_id from profiles p where p.gender = 0);

/*
Задание 4.
Подсчитать количество лайков которые получили 10 самых молодых пользователей.
*/

select sum(t2.qty_likes) sum_likes
from (
/*получаем 10 самых молодых пользователей и кол-во полученых лайков каждого*/
select t.user_id,
       (select p.birthday from profiles p where p.user_id = t.user_id) as bd_user,
       count(*) qty_likes
from (
/*находим всех пользователей которые получали лайки за свои сообщения, профиль, медиафайлы и посты*/
select (select m.from_user_id from messages m where m.id = l.target_id) as user_id
  from likes l
 where l.target_type_id = (select tt.id from target_types tt where tt.name = 'messages')
union all
select (select u.id from users u where u.id = l.target_id)
  from likes l
 where l.target_type_id = (select tt.id from target_types tt where tt.name = 'users')
union all
select (select m.user_id from media m where m.id = l.target_id)
  from likes l
 where l.target_type_id = (select tt.id from target_types tt where tt.name = 'media')
union all
select (select p.user_id from posts p where p.id = l.target_id)
  from likes l
 where l.target_type_id = (select tt.id from target_types tt where tt.name = 'posts')
) t
group by t.user_id
order by bd_user desc
limit 10
) t2;

/*
Задание 5.
Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
(критерии активности необходимо определить самостоятельно).
*/

/*
Критерием активности будет минимум 5 любых действий:
- состоит в группе;
- ставит лайки;
- загружает медиафайлы;
- пишет сообщения и  посты;
Мы выберем пользователей совершившие более 1 и менее 5 действий.
*/
select t.user_id,
       (select concat(first_name, ' ', last_name)
          from users u WHERE u.id = t.user_id) as user,
       sum(t.qty) as sum_qty
from (
/*кол-во групп в которых состоит пользователь*/
select cu.user_id, count(*) as qty
  from communities_users cu
group by cu.user_id
union all
/*кол-во лайков которые поставил пользователь*/
select l.user_id, count(*)
  from likes l
group by l.user_id
union all
/*кол-во медиафайлов которые загрузил пользователь*/
select m.user_id, count(*)
  from media m
group by m.user_id
union all
/*кол-во сообщений которых написал пользователь*/
select m.from_user_id, count(*)
  from messages m
group by m.from_user_id
union all
/*кол-во постов которых написал пользователь*/
select p.user_id, count(*)
  from posts p
group by p.user_id
) t
group by t.user_id
having sum_qty < 5
order by sum_qty
limit 10;