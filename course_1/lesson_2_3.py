# Урок 2. Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_list = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
season_list = ('зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима')

season_dict = {1: {'month': 'январь', 'season': 'зима'},
               2: {'month': 'февраль', 'season': 'зима'},
               3: {'month': 'март', 'season': 'весна'},
               4: {'month': 'апрель', 'season': 'весна'},
               5: {'month': 'май', 'season': 'весна'},
               6: {'month': 'июнь', 'season': 'лето'},
               7: {'month': 'июль', 'season': 'лето'},
               8: {'month': 'август', 'season': 'лето'},
               9: {'month': 'сентябрь', 'season': 'осень'},
               10: {'month': 'октябрь', 'season': 'осень'},
               11: {'month': 'ноябрь', 'season': 'осень'},
               12: {'month': 'декабрь', 'season': 'зима'}}

season_list_dict = [{'month': 'январь', 'season': 'зима'},
                    {'month': 'февраль', 'season': 'зима'},
                    {'month': 'март', 'season': 'весна'},
                    {'month': 'апрель', 'season': 'весна'},
                    {'month': 'май', 'season': 'весна'},
                    {'month': 'июнь', 'season': 'лето'},
                    {'month': 'июль', 'season': 'лето'},
                    {'month': 'август', 'season': 'лето'},
                    {'month': 'сентябрь', 'season': 'осень'},
                    {'month': 'октябрь', 'season': 'осень'},
                    {'month': 'ноябрь', 'season': 'осень'},
                    {'month': 'декабрь', 'season': 'зима'}]

my_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

# Используем список
print(f'Это месяц - {month_list[my_month-1]}, время года - {season_list[my_month-1]}')

# Используем справочник
result = season_dict.get(my_month)
print(f"Это месяц - {result.get('month')}, время года - {result.get('season')}")

# Используем список и справочник
result = season_list_dict[my_month-1]
print(f"Это месяц - {result.get('month')}, время года - {result.get('season')}")