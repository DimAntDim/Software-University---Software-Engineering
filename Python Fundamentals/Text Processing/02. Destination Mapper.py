import re
text = input()
match = []
string = ''
index = 0
i = 0
while len(text) > 0:
    if text[i] == '=':
        while True:
            string += text[index]
            index += 1
            if text[index] == '=':
                string += text[index]
                break
    elif text[i] == '/':
        while True:
            string += text[index]
            index += 1
            if text[index] == '/':
                string += text[index]
                break
    text = text.replace(string, '',1)

    match.append(string)
    index = 0
    string = ''

editing = match
for semple in match:
    for char in semple[1:-1]:
        if char.isdigit() or not char.isalpha():
            editing.remove(semple)
            break
print(editing)
