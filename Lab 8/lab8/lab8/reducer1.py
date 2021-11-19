#!/usr/bin/python3

import sys

current_word = None

for line in sys.stdin:
    line = line.strip().split()
    word = line[0]

    print(word)
