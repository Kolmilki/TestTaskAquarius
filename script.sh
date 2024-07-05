#!/bin/bash

(git diff) > log.txt
changed_value=$(awk '/.txt$/')
echo "$changed_value"
