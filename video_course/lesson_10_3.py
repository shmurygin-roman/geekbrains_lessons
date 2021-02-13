# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание:Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

import video_course.lesson_10_1 as lesson_10_1
from video_course.lesson_10_2 import get_random_by_list

# lesson_10_1.create_dir()

print(get_random_by_list([7,8,9,10,11]))

# lesson_10_1.del_dir()