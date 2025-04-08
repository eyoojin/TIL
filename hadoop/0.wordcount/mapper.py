#!/usr/bin/env python3

import sys

for line in sys.stdin: # 파일을 한줄로 쪼개기
    line = line.strip() # 좌우 공백 없애기
    words = line.split() # 한줄을 단어로 쪼개기

    for word in words:
        print(f'{word}\t1') # \t: tap

# shell
# cat text.txt | python3 mapper.py
# 왼쪽의 출력값을 오른쪽의 입력값으로 사용