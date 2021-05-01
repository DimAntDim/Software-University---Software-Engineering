targets = list(map(int, input().split('|')))
point = 0


def shoot_target(shooting_index):
    if targets[shooting_index] < 5:
        targets[shooting_index] = 0
    else:
        targets[shooting_index] -= 5


def shoot_left(start_index, lenght):
    while lenght > 0:
        if start_index == -1:
            start_index = len(targets)-1
        start_index -= 1
        lenght -= 1
    shoot_target(start_index)


def shoot_right(start_index, lenght):
    while lenght > 0:
        if start_index == len(targets):
            start_index = 0
        start_index += 1
        lenght -= 1
    shoot_target(start_index)

while True:
    command = input()
    if command == 'Game over':
        break
    data = command.split('@')
    if len(data) > 1:
        index = int(data[1])
        if 0 <= index < len(targets):
            if data[0] == 'Shoot Left':
                point += 5
                index = int(data[1])
                lenght = int(data[2])
                shoot_left(index, lenght)
            if data[0] == 'Shoot Right':
                point += 5
                index = int(data[1])
                lenght = int(data[2])
                shoot_right(index, lenght)
    if data[0] == 'Reverse':
        targets = targets[::-1]

print(' - '.join(map(str, targets)))
print(f"Iskren finished the archery tournament with {point} points!")
