import re

text = input()
pattern = r"( |^)([a-zA-Z0-9]+)([\.\-\_]*([a-zA-Z0-9]+))*@[a-zA-Z]+(-[a-zA-Z]+)*((\.[a-zA-Z]+)+(-[a-zA-Z]+)*)+"

matches = re.finditer(pattern, text)

for i in matches:
    print(i[0])
