#!/bin/bash

way_to_project="/home/kolmilki/TestTaskAquarius/TestTaskAquarius/"
git diff --cached --name-only | grep '\.py$' | grep -v '__init__.py' > log.txt
while IFS= read -r line; do
    changed_file="$way_to_project$line"
    pylint "$changed_file"
    autopep8 "$changed_file"
    mypy "$changed_file"
done < log.txt
rm log.txt