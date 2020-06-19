# Урок 3. Задание 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def get_int(x):
    if str(x).isdigit():
        return int(x)
    else:
        return 0


a = 0
result = 0

while a == 0:
    for i in list(input('Введите числа или "=" для завершения: ').split()):
        if i == '=':
            a = 1
            break
        else:
            result += get_int(i)
    print(result)