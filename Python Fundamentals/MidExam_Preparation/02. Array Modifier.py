elements = list(map(lambda x: int(x), input().split()))
while True:
    command = input()
    if command == 'end':
        break
    command = command.split()
    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        temp_1 = elements[index1]
        elements[index1] = elements[index2]
        elements[index2] = temp_1

    elif command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        elements[index1] = elements[index1]*elements[index2]

    else:
        for e in range(len(elements)):
            elements[e] -= 1

print_list = list(map(lambda x: str(x), elements))
print(', '.join(print_list))