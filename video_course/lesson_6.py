import random

print('Игра: Угадай число от 1 до 100!')

number = random.randint(1, 100)
# print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Уровень сложности: 1 - 10 попыток, 2 - 5 попыток, 3 - 3 попытки. Введите уровень: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i + 1}: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли :(')
        break
    for user in users:
        print(f'Ход пользователя {user}')
        print(f'Попытка № {count}')
        user_number = int(input('Введите число: '))
        if number == user_number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победа!!! Поздравляем {winner_name}')
