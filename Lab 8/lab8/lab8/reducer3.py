#!/usr/bin/python3
import sys
current_word=None
current_count=0
words={}
for line in sys.stdin:
    word,count=line.strip().split(',')
    if word in words:
        words[word]+=count
    else:
        words[word]=count
#words.sort
for i in words:
    print(f'{i} , {words[i]}')
    