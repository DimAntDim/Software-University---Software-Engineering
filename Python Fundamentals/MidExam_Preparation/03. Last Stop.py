painting_numbers = input().split()

command_line = input()

while command_line != 'END':
    data = command_line.split()
    command = data[0]
    if command == 'Change':
        num1 = data[1]
        num2 = data[2]
        if num1 in painting_numbers:
            num1_index = painting_numbers.index(num1)
            painting_numbers[num1_index] = num2
    elif command == 'Hide':
        num1 = data[1]
        if num1 in painting_numbers:
            painting_numbers.remove(num1)
    elif command == 'Switch':
        num1 = data[1]
        num2 = data[2]
        if num1 in painting_numbers and num2 in painting_numbers:
            n1_i = painting_numbers.index(num1)
            n2_i = painting_numbers.index(num2)
            painting_numbers[n1_i] = num2
            painting_numbers[n2_i] = num1
    elif command == 'Insert':
        place = int(data[1])
        num = data[2]
        if 0 <= place + 1 < len(painting_numbers):
            painting_numbers.insert(place+1, num)
    elif command == 'Reverse':
        painting_numbers = painting_numbers[::-1]

    command_line = input()

print(' '.join(painting_numbers))