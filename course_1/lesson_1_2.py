# Урок 1. Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input('Введите время в секундах: '))

# if sec // 60 >= 0:
#     if sec % 60 < 10:
#         ss = f'0{str(sec % 60)}'
#     else:
#         ss = sec % 60
# else:
#     ss = sec
#
# if sec // 60 >= 60:
#     if sec % 60 < 10:
#         mm = f'0{str(sec % 60)}'
#     else:
#         mm = sec % 60
# else:
#     if sec // 60 < 10:
#         mm = f'0{str(sec // 60)}'
#     else:
#         mm = sec // 60
#
# if sec // 3600 > 0:
#     if sec // 3600 < 10:
#         hh = f'0{str(sec // 3600)}'
#     else:
#         hh = sec // 3600
# else:
#     hh = '00'

hh = sec // 3600
mm = (sec // 60) - (hh * 60)
ss = sec % 60

print(f'{hh:02}:{mm:02}:{ss:02}')
