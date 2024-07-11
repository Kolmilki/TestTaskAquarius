import json
import os

from mode_choice import dir_works, file_works


def get_absolute_path():
    abs_path = os.path.dirname(__file__)
    return str(abs_path) + "/"


def forming_json_file(configuration_file, configuration_setting, mode, string_path):
    """
    Creates data.json and fills it with chosen settings

    :param configuration_file: name of configuration file
    :param configuration_setting: number of chosen configuration
    :param mode: mode of chosen configuration
    :param string_path: path of chosen configuration
    :return: data.json file filled with configuration data
    """
    json_formation = {
        "configFile": f"{configuration_file}",
        "configurationID": f"{configuration_setting}",
        "configurationData": {"mode": f"{mode}", "path": f"{string_path}"},
    }
    with open(f"{get_absolute_path()}data.json", "w", encoding="UTF-8") as file_out:
        json.dump(json_formation, file_out, ensure_ascii=False, indent=2)


def choosing_mode(mode, path, k, x):
    """
    Chooses further function depending on mode of configuration

    :param mode: mode of chosen configuration
    :param path: path of chosen configuration
    :param k: first string taken from read file
    :param x: last string taken from read file
    :return: function for chosen configuration
    """
    if mode == "dir":
        dir_works(path, k, x)
    elif mode == "files":
        file_works(path, k, x)
