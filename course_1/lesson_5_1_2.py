# Урок 5. Задания 1-2
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_1.txt', 'a+', encoding='utf-8') as f:
    while True:
        line = input('Введите строку для записи в файл: ')
        if line == '':
            break
        else:
            f.write(line + '\n')
    f.seek(0)
    lines = f.readlines()
    qty_line = len(lines)
    qty_words = 0
    for i in lines:
        qty_words += len(i.split())

    print(f'Количество строк = {qty_line}\nКоличество слов = {qty_words}')



