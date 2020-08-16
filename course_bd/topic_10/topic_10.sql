/*
Задание 1.
Проанализировать какие запросы могут выполняться наиболее часто в процессе работы приложения и добавить необходимые индексы.
*/

CREATE INDEX messages_from_user_id_to_user_id_idx ON messages (from_user_id, to_user_id);
CREATE INDEX likes_target_id_target_type_id_idx ON likes(target_id, target_type_id);
CREATE INDEX media_filename_idx ON media(filename);
CREATE INDEX profiles_birthday_idx ON profiles(birthday);
CREATE INDEX profiles_city_idx ON profiles(city);
CREATE INDEX profiles_country_idx ON profiles(country);
CREATE INDEX users_last_name_first_name_idx ON users(last_name, first_name);

/*
Задание 2. Задание на оконные функции
Построить запрос, который будет выводить следующие столбцы:
-- имя группы
-- среднее количество пользователей в группах
-- самый молодой пользователь в группе
-- самый старший пользователь в группе
-- общее количество пользователей в группе
-- всего пользователей в системе
-- отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100
*/

select distinct c.id,
       c.name,
       count(cu.user_id) over () / (select count(*) from communities) as avg_qty_users_community, /*AVG в данном случае считает не верно, использую вложенный запрос,
                                                                                                    т.к. не смог как получить кол-во групп в системе через оконную функцию*/
       first_value(concat(u.last_name,' ',u.first_name,',',p.birthday)) over (partition by cu.community_id order by p.birthday desc) as youngest,
       last_value(concat(u.last_name,' ',u.first_name,',',p.birthday)) over (partition by cu.community_id order by p.birthday desc
           range between unbounded preceding and unbounded following) as oldest,
       count(cu.user_id) over (partition by cu.community_id) as qty_users_community,
       (select count(*) from users) as qty_users_all, /*использую вложенный запрос, т.к. не смог как получить кол-во пользователей в системе через оконную функцию*/
       count(cu.user_id) over (partition by cu.community_id) / (select count(*) from users) * 100 as '%%'
  from communities_users cu
       join communities c on cu.community_id = c.id
       join users u on cu.user_id = u.id
       join profiles p on u.id = p.user_id

/*
Задание 3. Задание на денормализацию
Разобраться как построен и работает следующий запрос:
Найти 10 пользователей, которые проявляют наименьшую активность
в использовании социальной сети.

SELECT users.id,
COUNT(DISTINCT messages.id) + COUNT(DISTINCT likes.id) + COUNT(DISTINCT media.id) AS activity
FROM users
LEFT JOIN messages ON users.id = messages.from_user_id
LEFT JOIN likes ON users.id = likes.user_id
LEFT JOIN media ON users.id = media.user_id
GROUP BY users.id
ORDER BY activity
LIMIT 10;

Правильно-ли он построен?
Какие изменения, включая денормализацию, можно внести в структуру БД
чтобы существенно повысить скорость работы этого запроса?
 */

-- Все таблицы связаны верно.
-- Первичный ключ таблицы users, связывается с верным внешним ключом в таблицах messages, likes и media.
-- Сейчас запрос отрабатывает за доли секунды, но когда записей в таблице станет более миллиона, то время запроса увеличится.
-- Если запрос будет использоваться не часто, например как отчет, то не вижу смысла делать денормализацию.
-- Но если запрос к примеру будет отрабатывать при каждом обновлении страницы в VK, то нужны изменения.
-- Что предлагаю:
-- Добавить таблицу со счетчиками лайков, которая будет содержать расчетные значения по каждому пользователю.



