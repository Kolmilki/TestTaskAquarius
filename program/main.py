import json
import os
import file_creation as fc


def file_creation():
    letters = ['a', 'b', 'c']
    list_of_strings = []
    for i in range(1, 11):
        new_line = f"Строка {i}\n"
        list_of_strings.append(new_line)
    for letter in letters:
        with open(f"{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir('fileDirectoryDE')
    letters = ['d', 'e']
    for letter in letters:
        with open(f"fileDirectoryDE/{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir('fileDirectoryFGH')
    letters = ['f', 'g', 'h']
    for letter in letters:
        with open(f"fileDirectoryFGH/{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)


def dir_works(def_path, k, x):
    out_data = {}
    for index, item in enumerate(def_path, start=1):
        written_files = os.listdir(item)
        for file_index, element in enumerate(written_files, start=1):
            with open(os.path.join(item, element), encoding="UTF-8") as file_out:
                lines = file_out.readlines()
                out_data[str(file_index)] = {}
                for line_index in range(k - 1, x):
                    if line_index < len(lines):
                        out_data[str(file_index)][f"{line_index + 1}"] = lines[line_index].strip()
                    else:
                        out_data[str(file_index)][
                            f"{line_index + 1}"] = " "
    with open("data.json", encoding="UTF-8") as json_file:
        config_data = json.load(json_file)
    config_data.update({"out": out_data})
    with open("data.json", "w", encoding="UTF-8") as json_file:
        json.dump(config_data, json_file, indent=2, ensure_ascii=False)


def file_works(def_path, k, x):
    out_data = {}
    for file_index, element in enumerate(def_path, start=1):
        with open(os.path.join(element), encoding="UTF-8") as file_out:
            lines = file_out.readlines()
            out_data[str(file_index)] = {}
            for line_index in range(k - 1, x):
                if line_index < len(lines):
                    out_data[str(file_index)][f"{line_index + 1}"] = lines[line_index].strip()
                else:
                    out_data[str(file_index)][f"{line_index + 1}"] = " "
    with open("data.json", encoding="UTF-8") as json_file:
        config_data = json.load(json_file)
    config_data.update({"out": out_data})
    with open("data.json", "w", encoding="UTF-8") as json_file:
        json.dump(config_data, json_file, indent=2, ensure_ascii=False)


answer = input("Создать файлы и директории? (Y/N)")
if answer == 'Y':
    fc.file_creation()
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

json_formation = {
    "configFile": f"{configuration_file}",
    "configurationID": f"{configuration_setting}",
    "configurationData": {
        "mode": f"{mode}",
        "path": f"{string_path}"
    },
}

with open("data.json", "w", encoding="UTF-8") as file_out:
    json.dump(json_formation, file_out, ensure_ascii=False, indent=2)

if mode == "dir":
    dir_works(path, k, x)
else:
    file_works(path, k, x)

relative_path = "/data.json"
print("Абсолютный путь к созданному json файлу", os.path.abspath(relative_path))
