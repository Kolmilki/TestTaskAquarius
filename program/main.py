from file_creation import create_files
from filling_js import forming_json_file, choosing_mode


def get_config_file_name():
    configuration_file_name = input("Введите название конфигурационного файла: ")
    return configuration_file_name


def get_configuration_setting():
    configuration_setting_number = int(input("Введите номер конфигурации: "))
    return configuration_setting_number


def get_indexes():
    index_k = int(input("Введите начальное значение строки (k): "))
    index_x = int(input("Введите конечное значение строки (x): "))
    return index_k, index_x


def get_answer():
    positive_answer = ['yes', 'Yes', 'y', 'Y']
    negative_answer = ['no', 'No', 'n', 'N']
    users_answer = input("Создать файлы и директории? (Y/N)")
    if users_answer in positive_answer:
        return True
    elif users_answer in negative_answer:
        print('Продолжение без создания файлов')
        return True
    else:
        return False


def clearing_extra(config, mode, path):
    config_number = config.replace('#', '').rstrip('\n')
    mode = mode.replace('#mode: ', '').rstrip('\n')
    path[0] = path[0].replace('#path: ', '')
    path[-1] = path[-1].rstrip('\n')
    for i in range(len(path)):
        path[i] = path[i].replace(' ', '')
        path[i] = path[i].replace("\\", "/")
    string_path = ""
    for element in path:
        string_path += element + ', '
    string_path = string_path.rstrip(", ")
    return config_number, mode, path, string_path


answer = get_answer()
if answer:
    create_files()

configuration_file = get_config_file_name()
configuration_setting = get_configuration_setting()

k_and_x = get_indexes()
k = k_and_x[0]
x = k_and_x[1]
if k > x:
    k1 = k
    k = x
    x = k1

file_in = open(f"{configuration_file}", encoding="UTF-8")
content = file_in.readlines()
print('Конфигурация найдена' if f'#{configuration_setting}\n' in content else 'Конфигурация не найдена')
line_in_text = content.index(f'#{configuration_setting}\n')
config_number_for_json = content[line_in_text]
mode_for_json = content[line_in_text + 1]
path_for_json = content[line_in_text + 2].split(',')
file_in.close()

attributes_for_json = clearing_extra(config_number_for_json, mode_for_json, path_for_json)
forming_json_file(configuration_file, attributes_for_json[0], attributes_for_json[1], attributes_for_json[3])
choosing_mode(attributes_for_json[1], attributes_for_json[2], k, x)

# relative_path = "/data.json"
# print("Абсолютный путь к созданному json файлу", os.path.abspath(relative_path))
