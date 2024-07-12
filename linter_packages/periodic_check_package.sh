#!/bin/bash

#     CC score	Rank	Risk
#     1 - 5	A	low - simple block
#     6 - 10	B	low - well structured and stable block
#     11 - 20	C	moderate - slightly complex block
#     21 - 30	D	more than moderate - more complex block
#     31 - 40	E	high - complex block, alarming
#     41+	F	very high - error-prone, unstable block
path_for_errors_log="/home/kolmilki/TestTaskAquarius/TestTaskAquarius/temp/errors.txt"
while IFS= read -r line; do
  {
    pydocstyle "$line"
    isort "$line"
    ruff check "$line"
    printf "Проверка code complexity\n"
    radon cc "$line"
    printf "Проверка raw metrics\n"
    radon raw "$line"
    printf "Проверка устойчивости\n"
    radon mi "$line"
    printf "Проверка сложности Холстеда\n"
    radon hal "$line"
  } > "$path_for_errors_log"
done < project_directories.txt