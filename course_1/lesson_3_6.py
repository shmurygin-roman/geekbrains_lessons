# Урок 3. Задание 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    letters = list(word)
    res = 0
    for i in range(len(letters)):
        if ord(letters[i]) in range(97, 123):
            res += 1
    if res == len(letters):
        letters.insert(0, letters.pop(0).upper())
        return ''.join(letters)
    else:
        return word


my_list = input('Введите строку из слов, разделенных пробелом: ').split()

for i in range(len(my_list)):
    my_list.insert(i, int_func(my_list.pop(i)))

my_str = ' '.join(my_list)

print(my_str)

