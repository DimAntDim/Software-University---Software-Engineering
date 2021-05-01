grocery = input().split('!')

while True:
    command_line = input().split()
    if command_line[0] == 'Go':
        break
    if command_line[0] == 'Urgent':
        item = command_line[1]
        if item not in grocery:
            grocery.insert(0, item)
    elif command_line[0] == 'Unnecessary':
        item = command_line[1]
        while item in grocery:
            grocery.remove(item)
    elif command_line[0] == 'Correct':
        old_item = command_line[1]
        new_item = command_line[2]
        if old_item in grocery:
            index = grocery.index(old_item)
            grocery.insert(index, new_item)
            while old_item in grocery:
                grocery.remove(old_item)
    elif command_line[0] == 'Rearrange':
        item = command_line[1]
        if item in grocery:
            grocery.remove(item)
            grocery.append(item)

print(', '.join(grocery))