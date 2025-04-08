import sys
import re # 정규표현식

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()

    match = time_pattern.search(line)

    if match:
        hour = match.group(1)
        print(f'{hour}\t1')

# head ~/damf2/data/access.log | python3 mapper.py 