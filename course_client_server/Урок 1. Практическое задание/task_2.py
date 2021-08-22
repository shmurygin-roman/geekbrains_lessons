"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words = ('class', 'function', 'method')

byte_words = list()

for word in words:
    byte_words.append(b'' + bytearray(word, encoding='utf-8'))

print(byte_words)

for word in byte_words:
    print(word)
    print(type(word))
    print(len(word))
