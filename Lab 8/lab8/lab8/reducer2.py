#!/usr/bin/python3

import sys

current_word = None
count = 1

for line in sys.stdin:
    line = line.strip().split(',')
    word = line[0]

    if current_word == None:
        current_word = word
        count = 1
    elif current_word == word:
        count += 1
    else:
        print(f'{current_word},{count}')
        current_word = word
        count = 1

print(f'{current_word},{count}')
