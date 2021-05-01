def inventory_(heroes):
    inventory = {}
    for hero in heroes:
        if hero not in inventory:
            inventory[hero] = {}

    command = input()
    while command != 'End':
        data = command.split('-')
        name = data[0]
        item = data[1]
        cost = int(data[2])
        if name in inventory:
            if item not in inventory[name]:
                inventory[name][item] = cost

        command = input()
    return inventory


def print_inventory(heroes):
    print(*[f"{name} -> Items: {len(stats)}, Cost: {sum(stats.values())}" for name, stats in heroes.items()], sep='\n')


print_inventory(inventory_(input().split(', ')))
