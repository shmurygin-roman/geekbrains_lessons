# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 49,
    'armor': 1.5
}

enemy_name = input('Введите имя врага: ')
enemy = {
    'name': enemy_name,
    'health': 150,
    'damage': 39,
    'armor': 0.5
}


def get_damage(damage, armor):
    return damage / armor


def attack(person1, person2):
    person2['health'] -= get_damage(person1['damage'],person2['armor'])


print('До атаки:')
print(player)
print(enemy)

attack(player, enemy)
attack(enemy, player)

print('После атаки:')
print(player)
print(enemy)
