# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 49
}

enemy_name = input('Введите имя врага: ')
enemy = {
    'name': enemy_name,
    'health': 150,
    'damage': 39
}


def attack(person1, person2):
    # person2_health = person2['health'] - person1['damage']
    # del person2['health']
    # person2['health'] = person2_health
    person2['health'] -= person1['damage']

print('До атаки:')
print(player)
print(enemy)

attack(player, enemy)
attack(enemy, player)

print('После атаки:')
print(player)
print(enemy)
