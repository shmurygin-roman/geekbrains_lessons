# Урок 5. Задание 7
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    firm_list = []
    for line in f:
        firm_list.append(line.split())
    profit = []
    for i in range(len(firm_list)):
        firm_list[i].append(int(firm_list[i][2]) - int(firm_list[i][3]))
        if int(firm_list[i][2]) - int(firm_list[i][3]) > 0:
            profit.append(int(firm_list[i][2]) - int(firm_list[i][3]))
    firms = [{firm_list[i][0]: firm_list[i][4] for i in range(len(firm_list))}, {'average_profit': sum(profit) / len(profit)}]
    print(firms)
    with open('text_7.json', 'w', encoding='utf-8') as f2:
        json.dump(firms, f2, indent=4)

