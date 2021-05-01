def list_manipulator(data_list, *args):
    command = args[0]
    side = args[1]
    numbers = []

    if len(args) > 2:
        for i in range(2, len(args)):
            numbers.append(args[i])
    new_list = []
    if command == 'remove':
        if side == 'beginning':
            if numbers:
                n = numbers[0]
                new_list = data_list[n:]
            else:
                new_list = data_list[1:]
        else:
            if numbers:
                n = numbers[0]
                new_list = data_list[:-n]
            else:
                new_list = data_list[:-1]
    else:
        if side == 'beginning':
            new_list = numbers + data_list
        else:
            new_list = data_list + numbers
    return new_list
