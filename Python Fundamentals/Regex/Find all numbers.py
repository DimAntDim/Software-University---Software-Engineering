import re
regex = re.compile(r'\d+')
while True:
    text = input()
    if not text:
        break
    else:
        match = re.findall(regex, text)
        for i in match:
            print(i, end= " ")
