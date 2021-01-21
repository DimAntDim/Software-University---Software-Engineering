journal = input().split(', ')


def collect(inventory, item):
    inventory.append(item)
    return inventory


def drop(inventory, item):
    inventory.remove(item)
    return inventory


def renew(inventory, item):
    renew_item = item
    inventory.remove(item)
    inventory.append(renew_item)
    return inventory


def combine_items(inventory, old_item, new_item):
    index_old_item = inventory.position_counter(old_item)
    inventory.insert(index_old_item+1, new_item)
    return inventory


while True:
    command = input().split(' - ')

    if command[0] == 'Craft!':
        break
    action = command[0]
    item = command[1]
    if action == 'Collect':
        if item not in journal:
            collect(journal, item)
    elif action == 'Drop':
        if item in journal:
            drop(journal, item)
    elif action == 'Renew':
        if item in journal:
            renew(journal, item)
    else:
        items = item.split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            combine_items(journal, old_item, new_item)

print(', '.join(journal))