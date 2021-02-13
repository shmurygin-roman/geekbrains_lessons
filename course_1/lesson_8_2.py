# Урок 8. Задание 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_del(var_1, var_2):
    try:
        var_1 = int(var_1)
        var_2 = int(var_2)
        if var_2 == 0:
            raise OwnError('Error! Деление на ноль')
    except OwnError as err:
        return err
    except ValueError:
        return 'Error! Ввели не число'
    else:
        return round(var_1 / var_2, 2)


a, b = (input('Введите первое число - делимое: '), input('Введите второе число - делитель: '))
print(my_del(a, b))
