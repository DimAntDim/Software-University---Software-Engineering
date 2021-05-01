matrix = []


def create_matrix(size):
    for _ in range(size):
        row = [0 for _ in range(size)]
        matrix.append(row)


def check_pos(pos):
    if 0 <= pos < field_size:
        return True
    return False


def mine_planting(num_of_mines):
    for mine in range(num_of_mines):
        data = (input())
        mine_position = data[1:-1:1].split(', ')
        mine_x = int(mine_position[0])
        mine_y = int(mine_position[1])
        matrix[mine_x][mine_y] = '*'
        # up
        if check_pos(mine_x - 1):
            if matrix[mine_x - 1][mine_y] != '*':
                matrix[mine_x - 1][mine_y] += 1
        # down
        if check_pos(mine_x + 1):
            if matrix[mine_x + 1][mine_y] != '*':
                matrix[mine_x + 1][mine_y] += 1
        # left
        if check_pos(mine_y - 1):
            if matrix[mine_x][mine_y - 1] != '*':
                matrix[mine_x][mine_y - 1] += 1
        # right
        if check_pos(mine_y + 1):
            if matrix[mine_x][mine_y + 1] != '*':
                matrix[mine_x][mine_y + 1] += 1
        # up right
        if check_pos(mine_x - 1) and check_pos(mine_y + 1):
            if matrix[mine_x - 1][mine_y + 1] != '*':
                matrix[mine_x - 1][mine_y + 1] += 1
        # up left
        if check_pos(mine_x - 1) and check_pos(mine_y - 1):
            if matrix[mine_x - 1][mine_y - 1] != '*':
                matrix[mine_x - 1][mine_y - 1] += 1
        # down right
        if check_pos(mine_x + 1) and check_pos(mine_y + 1):
            if matrix[mine_x + 1][mine_y + 1] != '*':
                matrix[mine_x + 1][mine_y + 1] += 1
        # down left
        if check_pos(mine_x + 1) and check_pos(mine_y - 1):
            if matrix[mine_x + 1][mine_y - 1] != '*':
                matrix[mine_x + 1][mine_y - 1] += 1
        a = 5


def print_matrix():
    print(*[' '.join(map(str, row)) for row in matrix], sep='\n')


field_size = int(input())
create_matrix(field_size)
mines = int(input())
mine_planting(mines)
print_matrix()
