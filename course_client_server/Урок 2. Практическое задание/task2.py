"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


file_json = 'orders.json'
list_dict = [
    {
        'item': 'принтер',
        'quantity': '10',
        'price': '5000',
        'buyer': 'Gazprom',
        'date': '20.08.2021'
    },
    {
        'item': 'scanner',
        'quantity': '15',
        'price': '7500',
        'buyer': 'Rosneft',
        'date': '21.08.2021'
    }
]


def write_order_to_json(el_dict):
    with open(file_json, 'r', encoding='utf-8') as f:
        content = f.read()
        obj = json.loads(content)
        obj_list = obj['orders']
    f.close()

    obj_list.append(el_dict)
    obj['orders'] = obj_list

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)
    f.close()


for el in list_dict:
    write_order_to_json(el)
