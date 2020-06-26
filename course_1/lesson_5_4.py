# Урок 5. Задание 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as f1:
    lines = [line.split('-') for line in f1]
    print(lines)
    for i in range(len(lines)):
        result = translator.translate(text=lines[i].pop(0), src='en', dest='ru')
        lines[i].insert(0, result.text)
    print(lines)

    with open('text_44.txt', 'w', encoding='utf-8') as f2:
        for i in range(len(lines)):
            f2.write(lines[i][0] + '-' + lines[i][1])


