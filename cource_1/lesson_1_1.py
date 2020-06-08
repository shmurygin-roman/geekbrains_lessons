# Урок 1. Задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 5
b = 2.5
c = 'hello'

print(f'a = {a}')
print(type(a))

print(f'b = {b}')
print(type(b))

print(f'c = {c}')
print(type(c))

c = int(input('Введите число: '))
print(f'c = {c}')
print(type(c))

a = float(input('Введите дробное число: '))
print(f'a = {a}')
print(type(a))

b = input('Введите строку: ')
print(f'b = {b}')
print(type(b))
