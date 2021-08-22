"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words = ('разработка', 'администрирование', 'protocol', 'standard')

byte_words = list()
words_2 = list()

for word in words:
    byte_words.append(word.encode('utf-8'))

print(byte_words)

for word in byte_words:
    words_2.append(word.decode('utf-8'))

print(words_2)
