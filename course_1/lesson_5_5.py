# Урок 5. Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as f:
    for i in range(25):
        f.write(str(randint(1, 100)) + ' ')
    f.seek(0)
    lines = f.read()
    lines = lines.rstrip().split()
    print(lines)
    num_list = map(int, lines)
    print((sum(num_list)))
