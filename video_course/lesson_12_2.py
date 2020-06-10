# Создать модуль . В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.
import json
import pickle

with open('group.json', 'r') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group)
print(type(my_favourite_group))

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)

print(my_favourite_group)
print(type(my_favourite_group))