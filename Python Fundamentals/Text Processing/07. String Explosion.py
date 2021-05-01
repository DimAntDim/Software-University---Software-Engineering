text = input()

index = 0
index2 = 0
substring = ''
explode_number = 0
while True:
    text = text.replace(substring, '', 1)
    substring = ''
    if index == len(text):
        break
    char = text[index]
    if text[index] == '>':
        index2 = index
        while True:
            index2 += 1
            char1 = text[index2]
            if text[index2].isdigit():
                explode_number += int(text[index2])
            else:
                break

        for i in range(1, explode_number+1):
            if text[index+i] != '>':
                substring += text[index+i]
                explode_number -= 1
            else:
                break


    index += 1

print(text)