targets = list(map(lambda x: int(x), input().split()))

command_input = input()

while command_input != 'End':
    comm = command_input.split()
    command = comm[0]
    index = int(comm[1])
    power = int(comm[2])
    if command == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, power)
        else:
            print("Invalid placement!")
    else:
        range_shot = power
        if index + range_shot < len(targets)-1 and index - range_shot >= 0:
            del targets[index-range_shot:index+range_shot+1]
        else:
            print("Strike missed!")
    command_input = input()

list_to_print = [str(i) for i in targets]
print('|'.join(list_to_print))