# Урок 8. Задание 3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание:
# длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка:
# для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_int(x):
    if str(x).isdigit():
        return int(x)
    else:
        raise OwnError(f'Error! "{x}" не число')


a = 0
result = 0

while a == 0:
    for i in list(input('Введите числа или "=" для завершения: ').split()):
        if i == '=':
            a = 1
            break
        else:
            try:
                result += get_int(i)
            except OwnError as err:
                print(err)
    print(result)
