text = input()
emoticon_list = []

for i in range(len(text)):
    if text[i] == ':':
        emoticon = text[i]+text[i+1]
        emoticon_list.append(emoticon)
for i in emoticon_list:
    print(i)
