import json
import os


def get_absolute_path():
    abs_path = os.path.dirname(__file__)
    return str(abs_path) + "/"


def dir_works(def_path, k, x):
    """
    Gets data.json and fills it with strings from files located in path described in config file

    :param def_path: path to the directory where files are located
    :param k: first string taken from read file
    :param x: last string taken from read file
    :return: finished data.json
    """
    out_data = {}
    for index, item in enumerate(def_path, start=1):
        written_files = os.listdir(item)
        for file_index, element in enumerate(written_files, start=1):
            with open(os.path.join(item, element), encoding="UTF-8") as file_out:
                lines = file_out.readlines()
                out_data[str(file_index)] = {}
                for line_index in range(k - 1, x):
                    if line_index < len(lines):
                        out_data[str(file_index)][f"{line_index + 1}"] = lines[
                            line_index
                        ].strip()
                    else:
                        out_data[str(file_index)][f"{line_index + 1}"] = " "
    with open(f"{get_absolute_path()}data.json", encoding="UTF-8") as json_file:
        config_data = json.load(json_file)
    config_data.update({"out": out_data})
    with open(f"{get_absolute_path()}data.json", "w", encoding="UTF-8") as json_file:
        json.dump(config_data, json_file, indent=2, ensure_ascii=False)


def file_works(def_path, k, x):
    """
    Gets data.json and fills it with strings from files described in config file

    :param def_path: path to the directory where files are located
    :param k: first string taken from read file
    :param x: last string taken from read file
    :return: finished data.json
    """
    out_data = {}
    for file_index, element in enumerate(def_path, start=1):
        with open(os.path.join(element), encoding="UTF-8") as file_out:
            lines = file_out.readlines()
            out_data[str(file_index)] = {}
            for line_index in range(k - 1, x):
                if line_index < len(lines):
                    out_data[str(file_index)][f"{line_index + 1}"] = lines[
                        line_index
                    ].strip()
                else:
                    out_data[str(file_index)][f"{line_index + 1}"] = " "
    with open(f"{get_absolute_path()}data.json", encoding="UTF-8") as json_file:
        config_data = json.load(json_file)
    config_data.update({"out": out_data})
    with open(f"{get_absolute_path()}data.json", "w", encoding="UTF-8") as json_file:
        json.dump(config_data, json_file, indent=2, ensure_ascii=False)
