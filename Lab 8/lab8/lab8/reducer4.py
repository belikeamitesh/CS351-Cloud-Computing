#!/usr/bin/python3
import sys
current_word=None
current_count=0
words={}
for line in sys.stdin:
    line=line.strip().split(',')            
    word,offset=line[0],line[1]
    if word in words:
        words[word].append(offset)
    else:
        words[word]=[offset]
#words.sort
for i in words:
    print(f'{i} , {words[i]}')
    