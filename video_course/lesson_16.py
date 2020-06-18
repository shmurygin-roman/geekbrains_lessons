import sys
from lesson_16_core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from lesson_6_home import game

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название удаляемого файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо указать название двух файлов или попок')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('помошь')
    elif command == 'change':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_dir(name)
    elif command == 'game':
        game()

save_info('Конец')
