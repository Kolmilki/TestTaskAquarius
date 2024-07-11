import os


def get_absolute_path():
    abs_path = os.path.dirname(__file__)
    return str(abs_path) + "/"


def create_files():
    """
    Creates files for correct code work
    """
    letters = ["a", "b", "c"]
    list_of_strings = []
    for i in range(1, 11):
        new_line = f"Строка {i}\n"
        list_of_strings.append(new_line)
    for letter in letters:
        with open(
            f"{get_absolute_path()}{letter}.txt", "w", encoding="UTF-8"
        ) as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir(f"{get_absolute_path()}fileDirectoryDE")
    letters = ["d", "e"]
    for letter in letters:
        with open(
            f"{get_absolute_path()}fileDirectoryDE/{letter}.txt", "w", encoding="UTF-8"
        ) as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir(f"{get_absolute_path()}fileDirectoryFGH")
    letters = ["f", "g", "h"]
    for letter in letters:
        with open(
            f"{get_absolute_path()}fileDirectoryFGH/{letter}.txt", "w", encoding="UTF-8"
        ) as def_file_out:
            def_file_out.writelines(list_of_strings)
