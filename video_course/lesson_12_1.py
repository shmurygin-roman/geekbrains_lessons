# Создать модуль. В этом модуле определить словарь для вашей любимой музыкальной группы.
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8.
import json
import pickle

my_favourite_group = {
    'name': 'Руки Вверх',
    'tracks': ['Крошка моя', 'Прости', '18 мне уже', 'Он тебя целует', 'Омут', 'Она меня целует'],
    'Albums': [{'name': 'Сделай погромче!', 'year': 1998},
               {'name': 'Без тормозов', 'year': 1999},
               {'name': 'Здравствуй, это я', 'year': 2000},
               {'name': 'Не бойся, я с тобой!', 'year': 2001},
               {'name': 'Конец попсе, танцуют все', 'year': 2002}]}

j_group = json.dumps(my_favourite_group)
print(j_group)

p_group = pickle.dumps(my_favourite_group)
print(p_group)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
