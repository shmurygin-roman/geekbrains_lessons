import random
MAX_ERRORS = 8

words_bank = (
   'автострада', 'бензин', 'инопланетянин',
   'самолет', 'библиотека', 'шайба', 'олимпиада',
)

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))
errors_counter = 0

while True:
    letter = input('введите ОДНУ букву:').lower()
    if len(letter) != 1:
        continue

    if letter in secret_word:
        for idx,symbol in enumerate(secret_word):
            #print(idx,symbol)
            if symbol == letter:
                gamer_word[idx] = letter
        if gamer_word.count('*') == 0:
            print('вы выиграли!!!')
            break
    else:
        errors_counter += 1
        print(f'ошибок допущено {errors_counter}')
        if errors_counter == MAX_ERRORS:
            print('вы проиграли(')
            break

    print(''.join(gamer_word))

