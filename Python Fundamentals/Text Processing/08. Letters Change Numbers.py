data = input().split()
number = ''
summary = 0
for text_text in data:
    text = text_text
    for i in range(len(text)):
        if text[i].isdigit():
            number += text[i]
    text = text.replace(number, '')
    if text[0].isupper():
        calc_number = ord(text[0].upper())-64
        summary += int(number)/calc_number
    elif text[0].islower():
        calc_number = ord(text[0].upper()) - 64
        summary += int(number) * calc_number
    if text[1].isupper():
        calc_number = ord(text[1].upper()) - 64
        summary -= calc_number
    elif text[1].isalpha() and text[1].islower():
        calc_number = ord(text[1].upper()) - 64
        summary += calc_number
    number = ''
summary = round(summary, 2)
print(f"{summary:.2f}")
