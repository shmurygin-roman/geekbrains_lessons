import os
import shutil
import datetime


# функция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# функция для создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже создана')


# функция просмотра списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# функция удаление файла или папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# функция копирования файлов и папок
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже создана')
    else:
        shutil.copy(name, new_name)


# функция записи о работе менеджера в файл
def save_info(massege):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massege}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


# функция изменения дериктории
def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f')
    create_folder('new_f1')
    get_list(True)
    delete_file('new_f1')
    # delete_file('text.dat')
    copy_file('new_f', 'new_f2')
    copy_file('text.dat', 'text2.dat')
    save_info('asd')
