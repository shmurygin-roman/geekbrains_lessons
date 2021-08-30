"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

input_var = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_qty': 4,
    'item_price': {
        'computer': '1000\u20ac',
        'printer': '200\u20ac',
        'keyboard': '25\u20ac',
        'mouse': '5\u20ac'
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(input_var, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
f.close()

with open('file.yaml', 'r', encoding='utf-8') as f:
    content = yaml.load(f, Loader=yaml.FullLoader)
    print(content)
f.close()
