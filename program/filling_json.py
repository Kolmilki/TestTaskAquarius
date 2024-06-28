from mode_choice import dir_works, file_works
import json


def forming_json_file(configuration_file, configuration_setting, mode, string_path):
    path_of_creation = '/home/kolmilki/project/TestTaskAquarius/program/'
    json_formation = {
        "configFile": f"{configuration_file}",
        "configurationID": f"{configuration_setting}",
        "configurationData": {
            "mode": f"{mode}",
            "path": f"{string_path}"
        },
    }
    with open(f"{path_of_creation}data.json", "w", encoding="UTF-8") as file_out:
        json.dump(json_formation, file_out, ensure_ascii=False, indent=2)


def choosing_mode(mode, path, k, x):
    if mode == "dir":
        dir_works(path, k, x)
    else:
        file_works(path, k, x)
