import re
pattern = r'\d+'

string = input().upper()
unique_symbols = []
for s in string:
    if s not in unique_symbols and not s.isdigit():
        unique_symbols.append(s)
while ' ' in unique_symbols:
    unique_symbols.remove(' ')

result = ''
match = re.findall(pattern, string)
i = 0
start = 0
while len(string) > 0:
    index = string.index(match[i])
    word = string[start:index]
    result += word*int(match[i])
    i += 1
a =5

