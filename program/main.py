import os
from file_creation import create_files
from filling_json import forming_json_file, choosing_mode


def get_answer(users_input):
    positive_answer = ['yes', 'Yes', 'y', 'Y', 'н', 'Н']
    users_answer = users_input
    if users_answer in positive_answer:
        return True
    else:
        print('Продолжение без создания файлов')
        return False


def read_configuration_file(configuration_file, configuration_setting):
    file_in = open(f"{get_absolute_path()}{configuration_file}", encoding="UTF-8")
    content = file_in.readlines()
    print('Конфигурация найдена' if f'#{configuration_setting}\n' in content else 'Конфигурация не найдена')
    line_in_text = content.index(f'#{configuration_setting}\n')
    config_number_for_json = content[line_in_text].removeprefix('#').removesuffix('\n')
    mode_for_json = content[line_in_text + 1].removeprefix('#mode: ').removesuffix('\n')
    path_for_json = content[line_in_text + 2].removeprefix('#path: ').removesuffix('\n').replace('\\', '/').split(', ')
    file_in.close()
    return config_number_for_json, mode_for_json, path_for_json


def get_absolute_path():
    abs_path = os.path.dirname(__file__)
    return str(abs_path) + '/'


def remove_directories():
    files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
                 'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']
    for path in files:
        os.remove(f'{get_absolute_path()}{path}')
    os.removedirs(f'{get_absolute_path()}fileDirectoryDE/')
    os.removedirs(f'{get_absolute_path()}fileDirectoryFGH/')


if __name__ == '__main__':
    answer = get_answer(input("Создать файлы и директории? (Y/N)"))
    if answer:
        create_files()
    configuration_file = input("Введите название конфигурационного файла: ")
    configuration_setting = int(input("Введите номер конфигурации: "))
    k = int(input("Введите начальное значение строки (k): "))
    x = int(input("Введите конечное значение строки (x): "))
    if k > x: k, x = x, k
    config_number_for_json, mode_for_json, path_for_json = read_configuration_file(configuration_file, configuration_setting)
    forming_json_file(configuration_file, config_number_for_json, mode_for_json, path_for_json)
    choosing_mode(mode_for_json, path_for_json, k, x)
    remove_directorys()
    path = f"{get_absolute_path()}data.json"
    print("Абсолютный путь к созданному json файлу:", path)
