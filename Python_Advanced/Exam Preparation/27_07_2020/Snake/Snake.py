def print_board():
    for row in board:
        print(''.join(row))


def game_over():
    print("Game over!")
    print(f"Food eaten: {food_quantity[0]}")
    print_board()
    exit()


def validate_pos(pos):
    if 0 <= pos < size:
        return True
    return False


def snake_move(move):
    snake_x = snake_position[0]
    snake_y = snake_position[1]
    current_pos = [snake_x, snake_y]
    if move == 'left':
        check_position = snake_y - 1
        if validate_pos(check_position):
            snake_y -= 1
        else:
            board[snake_x][snake_y] = '.'
            game_over()
    elif move == 'right':
        check_position = snake_y + 1
        if validate_pos(check_position):
            snake_y += 1
        else:
            board[snake_x][snake_y] = '.'
            game_over()
    elif move == 'up':
        check_position = snake_x - 1
        if validate_pos(check_position):
            snake_x -= 1
        else:
            board[snake_x][snake_y] = '.'
            game_over()
    else:
        check_position = snake_x + 1
        if validate_pos(check_position):
            snake_x += 1
        else:
            board[snake_x][snake_y] = '.'
            game_over()

    if board[snake_x][snake_y] == 'B':
        board[snake_x][snake_y] = '.'
        snake_x = teleport[1][0]
        snake_y = teleport[1][1]

    if board[snake_x][snake_y] == '*':
        board[snake_x][snake_y] = '.'
        board[current_pos[0]][current_pos[1]] = '.'
        board[snake_x][snake_y] = 'S'
        food_quantity[0] += 1
        if food_quantity[0] == 10:
            print("You won! You fed the snake.\nFood eaten: 10")
            print_board()
            exit()
    board[current_pos[0]][current_pos[1]] = '.'
    board[snake_x][snake_y] = 'S'
    snake_position[0], snake_position[1] = snake_x, snake_y


def create_matrix(n):
    for i in range(n):
        row = []
        line = input()
        for char in range(len(line)):
            row.append(line[char])
            if line[char] == 'S':
                snake_position.append(i)
                snake_position.append(char)
            elif line[char] == 'B':
                teleport.append([i, char])
        board.append(row)


board = []
snake_position = []
teleport = []
food_quantity = [0]

size = int(input())
create_matrix(size)
while True:
    m = input()
    snake_move(m)
