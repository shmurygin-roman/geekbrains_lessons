import random

print('Игра: Загадай число от 1 до 100!')
user_number = int(input('Введите число: '))

number = None
min_random = 1
max_random = 100
number_history = []
answer = None
is_new_number = False

while answer != '=':
    while not is_new_number:
        number = random.randint(min_random, max_random)
        if number in number_history:
            continue
        else:
            is_new_number = True
    is_new_number = False
    print(number)
    number_history.append(number)
    answer = input()
    if answer == '>':
        min_random = number + 1
    elif answer == '<':
        max_random = number - 1
    #print(min_random, max_random)
else:
    print(number_history)