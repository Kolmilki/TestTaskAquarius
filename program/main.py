from file_creation import create_files
from filling_js import forming_json_file, choosing_mode


answer = input("Создать файлы и директории? (Y/N)")
if answer == 'Y':
    create_files()
configuration_file = input("Введите название конфигурационного файла: ")
# configuration_file = "config.txt"
configuration_setting = int(input("Введите номер конфигурации: "))
k = int(input("Введите начальное значение строки (k): "))
x = int(input("Введите конечное значение строки (x): "))
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

config_number = config_number_for_json.replace('#', '').rstrip('\n')
mode = mode_for_json.replace('#mode: ', '').rstrip('\n')
path_for_json[0] = path_for_json[0].replace('#path: ', '')
path_for_json[-1] = path_for_json[-1].rstrip('\n')
for i in range(len(path_for_json)):
    path_for_json[i] = path_for_json[i].replace(' ', '')
    path_for_json[i] = path_for_json[i].replace("\\", "/")
path = path_for_json
string_path = ""
for element in path:
    string_path += element + ', '
string_path = string_path.rstrip(", ")

forming_json_file(configuration_file, configuration_setting, mode, string_path)
choosing_mode(mode, path, k, x)

# relative_path = "/data.json"
# print("Абсолютный путь к созданному json файлу", os.path.abspath(relative_path))
