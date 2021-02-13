# Урок 3. Задание 2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_person(name, surname, year, city, tel):
    return f'name - {name}; surname - {surname}; year - {year}; city - {city}; tel - {tel};'

def my_person_2(**kwards):
    result = ''
    for key, value in kwards.items():
        result += f'{key} - {value}; '
    return result


print(my_person(name='Ivan', surname='Petrov', year=1991, city='Moscow', tel='+79876543210'))
print(my_person_2(name='Ivan', surname='Petrov', year=1991, city='Moscow', tel='+79876543210'))


