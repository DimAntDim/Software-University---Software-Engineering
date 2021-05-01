items = input().split(', ')

command_line = input()
item = str
old_item = str
new_item = str
while command_line != 'Craft!':
    data = command_line.split(' - ')
    command = data[0]
    if command == 'Collect':
        item = data[1]
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        item = data[1]
        if item in items:
            items.remove(item)
    elif command == 'Combine Items':
        d = data[1].split(':')
        old_item = d[0]
        new_item = d[1]
        if old_item in items:
            old_item_index = items.index(old_item)
            if old_item_index in range(len(items)):
                items.insert(old_item_index+1, new_item)
    elif command == 'Renew':
        item = data[1]
        if item in items:
            item_copy = item
            items.remove(item)
            items.append(item_copy)
    command_line = input()

print(', '.join(items))
