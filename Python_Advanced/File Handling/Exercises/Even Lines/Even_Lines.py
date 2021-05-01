import re

regex_pattern = r"[,\-\!\?\.]"

with open('text.txt', 'r') as file:
    lines = file.readlines()
    for _ in lines:
        _.replace('\n', '')
    even_ = [lines[i] for i in range(len(lines)) if i % 2 == 0]


for line in even_:
    result = re.sub(regex_pattern, "@", line)
    result = result.split()
    print_ = []
    while result:
        print_.append(result.pop())
    print(' '.join(print_))
