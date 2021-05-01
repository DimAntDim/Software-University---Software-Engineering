def create_matrix(size):
    for _ in range(size):
        matrix.append(list(map(lambda x: int(x), input().split())))
    return matrix


def coordinates_validator(row_, col_):
    if 0 <= row_ < n and 0 <= col_ < n:
        return True
    return False


def modification(matrix_modification):
    while True:
        command = input().split()
        action = command[0]
        if action == 'END':
            print_matrix(matrix_modification)
            exit()
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])

        if coordinates_validator(row, col):
            if action == 'Add':
                matrix_modification[row][col] += value
            elif action == 'Subtract':
                matrix_modification[row][col] -= value

        else:
            print('Invalid coordinates')


def print_matrix(matrix_print):
    print(*[' '.join(map(lambda x: str(x), el)) for el in matrix_print], sep='\n')


matrix = []
n = int(input())
create_matrix(n)
modification(matrix)

