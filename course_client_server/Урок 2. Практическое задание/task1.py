"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий
новый «отчетный» файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия
столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re
import csv

files_txt = ['info_1.txt', 'info_2.txt', 'info_3.txt']
file_csv = 'file.csv'


def get_data(files):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if re.match('Изготовитель системы', line) is not None:
                    os_prod = re.findall(r':(.*)', line)
                    os_prod_list.append(os_prod[0].strip())
                elif re.match('Название ОС', line) is not None:
                    os_name = re.findall(r':(.*)', line)
                    os_name_list.append(os_name[0].strip())
                elif re.match('Код продукта', line) is not None:
                    os_code = re.findall(r':(.*)', line)
                    os_code_list.append(os_code[0].strip())
                elif re.match('Тип системы', line) is not None:
                    os_type = re.findall(r':(.*)', line)
                    os_type_list.append(os_type[0].strip())
        f.close()

    for i in files:
        main_data.append([])

    for i in range(1, len(main_data)):
        main_data[i].append(os_prod_list[i - 1])
        main_data[i].append(os_name_list[i - 1])
        main_data[i].append(os_code_list[i - 1])
        main_data[i].append(os_type_list[i - 1])

    return main_data


def write_to_csv(file, files):
    data = get_data(files)
    with open(file, 'w', newline='', encoding='utf-8') as f:
        f_writer = csv.writer(f, delimiter=';')
        for row in data:
            f_writer.writerow(row)
    f.close()


write_to_csv(file_csv, files_txt)

print(get_data(files_txt))
with open(file_csv, encoding='utf-8') as f:
    print(f.read())
