# Урок 2. Задание 2
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_str = input('Введите список элементов через пробел: ')
my_list = list(my_str.split())
print(my_list)

end_el = None
if len(my_list) % 2 != 0:
    end_el = my_list.pop()

list_a = my_list[::2]
list_b = my_list[1::2]
new_list = []
i = 0

while i < len(my_list) / 2:
    a = list_a.pop()
    new_list.append(a)
    b = list_b.pop()
    new_list.append(b)
    i += 1

new_list.reverse()

if end_el is not None:
    new_list.append(end_el)

print(new_list)
