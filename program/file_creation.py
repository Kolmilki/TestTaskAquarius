import os


def create_files():
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