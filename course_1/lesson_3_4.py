# Урок 3. Задание 4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    """Возведение числа x в степень y.
    Параметры:
    x - действительное положительное число
    y - целое отрицательное число
    """
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return 'Error! Одно из введеных значений не является числом'
    else:
        if x < 0:
            return 'Error! X - должен быть положительным числом'
        if y > 0:
            return 'Error! Y - должен быть отрицательным числом'
        z = 1
        for i in range(abs(y)):  # возведение в степень
            z = z * x
        try:
            return 1 / z
        except ZeroDivisionError:
            return 'Error! Ноль нельзя возвести в отрицательную степень'

# Верно
print(my_func(2, -3))
# Обработано на ошибки
print(my_func(-2, -3))
print(my_func(2, 3))
print(my_func(0, -3))
print(my_func('x', -3))
