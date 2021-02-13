# Урок 3. Задание 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(3, 6, 9))
