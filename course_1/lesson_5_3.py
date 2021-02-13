# Урок 5. Задание 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for i in lines:
        print(i)
    staff = [i.split() for i in lines]
    staff_20 = [staff[i][0] for i in range(len(staff)) if float(staff[i][1]) < 20000.00]
    print(f"Cотрудники с окладом менее 20 тыс.: {', '.join(staff_20)}.")
    avg_salary = 0
    sum_salary = 0
    for i in range(len(staff)):
        sum_salary += float(staff[i][1])
    avg_salary = sum_salary / len(staff)
    print(f'Средняя величина дохода сотрудников = {round(avg_salary, 1)}')
