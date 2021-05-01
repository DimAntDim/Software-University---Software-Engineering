import re
pattern = r"www.[a-zA-Z0-9]+(([\-\.])*[a-zA-Z0-9]*)*\.[a-zA-Z]+"
text = input()
while text != "":
    match = re.finditer(pattern, text, re.MULTILINE)
    for i in match:
        print(i[0])
    text = input()
