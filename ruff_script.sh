#!/bin/bash

way_to_log="/home/kolmilki/TestTaskAquarius/TestTaskAquarius/temp/"
way_to_project="/home/kolmilki/TestTaskAquarius/TestTaskAquarius/"
git diff --cached --name-only | grep '\.py$' | grep -v '__init__.py' > "$way_to_log"log.txt
while IFS= read -r line; do
    changed_value="$way_to_project$line"
    ruff check "$changed_value"
done < "$way_to_log"log.txt

rm "$way_to_log"log.txt