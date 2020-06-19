# Урок 4. Задание 6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def my_iter(start, stop, step):
    try:
        start, stop, step = int(start), int(stop), int(step)
        result = []
    except ValueError:
        return 'Ошибка в переданых параметрах. Нужны целые числа.'
    else:
        for i in count(start, step):
            if i > stop:
                return result
            else:
                result.append(i)


def my_cycle(my_list, stop):
    result = []
    a = 1
    for i in cycle(my_list):
        if a > stop:
            return result
        else:
            result.append(i)
            a += 1


print(my_iter(10, 50, 5))
print(my_cycle([1, 2, 3, 4, 5], 30))
