#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    words = re.findall(r'\w+', line)
    
    for word in words:
        print(word)
