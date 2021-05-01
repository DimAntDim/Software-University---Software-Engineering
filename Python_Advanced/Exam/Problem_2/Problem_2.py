def create_matrix(size):
    field = []
    for i in range(size):
        line = input().split()
        row = []
        for char in range(len(line)):
            if line[char] == 'P':
                player_pos.append(i)
                player_pos.append(char)
                row.append(line[char])
            else:
                row.append(line[char])
        field.append(row)

    return field


def print_output():
    if coins[0] >= 130:
        print(f"You won! You've collected {coins[0]} coins.")
        print("Your path:")
        for moves in path[:]:
            print(f"[{moves[0]}, {moves[1]}]")
    else:
        print(f"Game over! You've collected {coins[0]-1} coins.")
        print("Your path:")
        for moves in path[:-1]:
            print(f"[{moves[0]}, {moves[1]}]")
    exit()


def validate_pos(pos):
    if 0 <= pos < size_of_field:
        return True
    return print_output()


def check_for_walls(x, y):
    if matrix[x][y] != 'X':
        return True
    return print_output()


def move_player(command):
    if command == 'right':
        if validate_pos(player_pos[1] + 1):
            if check_for_walls(player_pos[0], player_pos[1]+1):
                coins[0] += int(matrix[player_pos[0]][player_pos[1]+1])
                path.append((player_pos[0], player_pos[1]+1))
                player_pos[1] += 1
            else:
                path.append((player_pos[0], player_pos[1] + 1))
                print_output()

    if command == 'left':
        if validate_pos(player_pos[1] - 1):
            if check_for_walls(player_pos[0], player_pos[1]-1):
                coins[0] += int(matrix[player_pos[0]][player_pos[1]-1])
                path.append((player_pos[0], player_pos[1]-1))
                player_pos[1] -= 1
            else:
                path.append((player_pos[0], player_pos[1] - 1))
                print_output()

    elif command == 'up':
        if validate_pos(player_pos[0] - 1):
            if check_for_walls(player_pos[0] - 1, player_pos[1]):
                coins[0] += int(matrix[player_pos[0] - 1][player_pos[1]])
                path.append((player_pos[0]-1, player_pos[1]))
                player_pos[0] -= 1
            else:
                path.append((player_pos[0] - 1, player_pos[1]))
                print_output()

    elif command == 'down':
        if validate_pos(player_pos[0] + 1):
            if check_for_walls(player_pos[0] + 1, player_pos[1]):
                coins[0] += int(matrix[player_pos[0] + 1][player_pos[1]])
                path.append((player_pos[0]+1, player_pos[1]))
                player_pos[0] += 1
            else:
                path.append((player_pos[0] + 1, player_pos[1]))
                print_output()

    if coins[0] >= 130:
        print_output()


coins = [0]
path = []
player_pos = []
size_of_field = int(input())
matrix = create_matrix(size_of_field)


while True:
    command_line = input()
    if not command_line:
        break
    move_player(command_line)

print_output()
