#!/bin/bash

way_to_project="/home/kolmilki/TestTaskAquarius/TestTaskAquarius/"
git diff --cached --name-only | grep '\.py$' | grep -v '__init__.py' > log.txt
while IFS= read -r line; do
    changed_file="$way_to_project$line"
    ruff check "$changed_file"
    vulture "$changed_file"
    pydocstyle "$changed_file"
    black "$changed_file"
done < log.txt
rm log.txt