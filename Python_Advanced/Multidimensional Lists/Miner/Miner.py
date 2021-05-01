def create_matrix(size):
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def start_position_finder():
    total_coals = 0
    start_found = False
    position = []
    for field in range(len(matrix)):
        row = matrix[field]

        for pos in range(len(row)):
            if row[pos] == 's':
                position = [field, pos]
            elif row[pos] == 'c':
                total_coals += 1

    position_x = position[0]
    position_y = position[1]
    return position_check(total_coals, position_x, position_y)


def position_check(total_coals, x, y):
    new_position = ''
    coals = 0
    for move in moves:
        if move == 'up' and x - 1 >= 0:
            new_position = matrix[x-1][y]
            x -= 1
        elif move == 'down' and x + 1 < size_of_field:
            new_position = matrix[x+1][y]
            x += 1
        elif move == 'right' and y+1 < size_of_field:
            new_position = matrix[x][y+1]
            y += 1
        elif move == 'left' and y-1 >= 0:
            new_position = matrix[x][y-1]
            y -= 1
        else:
            continue

        if new_position == 'c':
            matrix[x][y] = '*'
            coals += 1
        elif new_position == 'e':
            print(f"Game over! ({x}, {y})")
            exit()
        if coals == total_coals and total_coals != 0:
            print(f"You collected all coals! ({x}, {y})")
            exit()
    else:
        print(f"{total_coals-coals} coals left. ({x}, {y})")


matrix = []

size_of_field = int(input())
moves = input().split()
create_matrix(size_of_field)
start_position_finder()
