#!/bin/bash

git diff --name-only > names.txt
while read -r line
do
  git diff | grep b/"$line" -A 1
done < names.txt