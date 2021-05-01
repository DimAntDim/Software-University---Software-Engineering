text = input()
new_text = text
index = 0
repeating_symbol = ''
while True:
    if index == len(text):
        break
    char = text[index]
    for i in range(index, len(text)):
        if char != text[i]:
            break
        else:
            repeating_symbol += char
    text = text.replace(repeating_symbol, char, 1)
    repeating_symbol = ''
    index += 1
print(text)
