gifts_list = input().split()

command = input().split()

while command[0] != 'No' and command[1] != 'Money':

    if command[0] == 'OutOfStock':
        for pos, gift in enumerate(gifts_list):
            if gift == command[1]:
                gifts_list[pos] = 'None'

    elif command[0] == 'Required':
        pos = int(command[2])
        if 0 <= pos < len(gifts_list):
            gifts_list[pos] = command[1]

    elif command[0] == 'JustInCase':
        gifts_list[-1] = command[1]

    command = input().split()

while 'None' in gifts_list:
    gifts_list.remove('None')

print(' '.join(gifts_list))
