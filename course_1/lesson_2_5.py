# Урок 2. Задание 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_rating = [11, 7, 4, 4, 2]
new_element = None

while new_element != 0:
    new_element = int(input('Введите новый элемент рейтинга или 0 для завершения: '))
    # проверка на отрицательное значение
    if new_element < 0:
        print('Вы ввели отрицательное значение - это недопустимо!')
        continue
    element_qty = my_rating.count(new_element)
    # если новый элемент уже есть в рейтинге
    if element_qty > 0:
        x = my_rating.index(new_element)
        my_rating.insert(x + element_qty, new_element)
    # если новый элемент мах в рейтинге
    elif new_element > max(my_rating):
        my_rating.insert(0, new_element)
    else:  # новый элемент отсутствует в рейтинге
        find_element = new_element
        # ищем место для вставки нового элемента
        while element_qty == 0:
            find_element += 1
            element_qty = my_rating.count(find_element)
        else:
            x = my_rating.index(find_element)
            my_rating.insert(x + element_qty, new_element)
    print(my_rating)
