# Урок 3. Задание 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_del(var_1, var_2):
    try:
        result = round(int(var_1) / int(var_2), 2)
    except ZeroDivisionError:
        return 'Error! Деление на ноль'
    except ValueError:
        return 'Error! Ввели не число'
    return result


a = input('Введите первое число - делимое: ')
b = input('Введите второе число - делитель: ')
print(my_del(a, b))
