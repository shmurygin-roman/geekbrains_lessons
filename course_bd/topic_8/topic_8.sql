/*
Задание 1.
Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

select IF(count(men.user_id) > count(women.user_id), concat('men = ',count(men.user_id)), concat('women = ',count(women.user_id))) as 'who put more likes'
  from likes l
       left join profiles men on l.user_id = men.user_id and men.gender = 1
       left join profiles women on l.user_id = women.user_id and women.gender = 0;

/*
Задание 2.
Подсчитать количество лайков которые получили 10 самых молодых пользователей.
*/

select u.first_name,
       u.last_name,
       p.birthday,
       count(distinct l_u.id)+count(distinct l_msg.id)+count(distinct l_mda.id)+count(distinct l_pst.id) as qty_likes
  from users u
       join profiles p on u.id = p.user_id
       left join likes l_u on u.id = l_u.target_id and l_u.target_type_id = 2 /*лайки пользователей*/
       left join messages msg on u.id = msg.from_user_id
       left join likes l_msg on msg.id = l_msg.target_id and l_msg.target_type_id = 1 /*лайки сообщений*/
       left join media mda on u.id = mda.user_id
       left join likes l_mda on mda.id = l_mda.target_id and l_mda.target_type_id = 3 /*лайки медиафайлов*/
       left join posts pst on u.id = pst.user_id
       left join likes l_pst on pst.id = l_pst.target_id and l_pst.target_type_id = 4 /*лайки постов*/
group by u.id, p.birthday
order by p.birthday desc
limit 10;

/*
Задание 3.
Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
(критерии активности необходимо определить самостоятельно).
*/

/*
Критерием активности будет минимум 5 любых действий:
- состоит в группе;
- ставит лайки;
- загружает медиафайлы;
- пишет сообщения и  посты;
*/

select u.id,
       u.first_name,
       u.last_name,
       count(distinct cu.community_id)+count(distinct l.id)+count(distinct mda.id)+count(distinct msg.id)+count(distinct p.id) as qty_actions
  from users u
       left join communities_users cu on u.id = cu.user_id /*состоит в группе*/
       left join likes l on u.id = l.user_id /*ставит лайки*/
       left join media mda on u.id = mda.user_id /*загружает медиафайлы*/
       left join messages msg on u.id = msg.from_user_id /*пишет сообщения*/
       left join posts p on u.id = p.user_id /*пишет посты*/
group by u.id
order by qty_actions, u.id
limit 10;
