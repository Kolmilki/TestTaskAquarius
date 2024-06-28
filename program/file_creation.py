import os


def create_files():
    path_of_creation = '/home/kolmilki/project/TestTaskAquarius/program/'
    letters = ['a', 'b', 'c']
    list_of_strings = []
    for i in range(1, 11):
        new_line = f"Строка {i}\n"
        list_of_strings.append(new_line)
    for letter in letters:
        with open(f"{path_of_creation}{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir(f'{path_of_creation}fileDirectoryDE')
    letters = ['d', 'e']
    for letter in letters:
        with open(f"{path_of_creation}fileDirectoryDE/{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)

    os.mkdir(f'{path_of_creation}fileDirectoryFGH')
    letters = ['f', 'g', 'h']
    for letter in letters:
        with open(f"{path_of_creation}fileDirectoryFGH/{letter}.txt", "w", encoding="UTF-8") as def_file_out:
            def_file_out.writelines(list_of_strings)