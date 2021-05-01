words = input().split()

command_line = input()

while command_line != 'Stop':

    data = command_line.split()

    if data[0] == 'Delete':
        index = int(data[1])
        if index+1 in range(len(words)):
            words.remove(words[index+1])
    elif data[0] == 'Swap':
        w1 = data[1]
        w2 = data[2]
        if w1 in words and w2 in words:
            w1_i = words.index(w1)
            w2_i = words.index(w2)
            words[w1_i] = w2
            words[w2_i] = w1
    elif data[0] == 'Put':
        w1 = data[1]
        index = int(data[2])
        if 0 <= index - 1 <= len(words):
            words.insert(index-1, w1)
    elif data[0] == 'Sort':
        words.sort(reverse=True)
    else:
        w_1 = data[1]
        w_2 = data[2]
        if w_2 in words:
            w2_i = words.index(w_2)
            words[w2_i] = w_1
    command_line = input()

print(' '.join(words))