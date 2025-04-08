#!/usr/bin/env python3

import sys

last_word = None
total_count = 0

for line in sys.stdin: # 앞서 출력했던 데이터가 정렬되어 한줄씩 들어옴
    word, value = line.split('\t')
    value = int(value)

    if last_word == word:
        total_count += value
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word
        total_count = value

if last_word == word:
    print(f'{last_word}\t{total_count}')

# shell
# cat text.txt | python3 mapper.py | sort
# cat text.txt | python3 mapper.py | sort | python3 reducer.py