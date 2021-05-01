size_of_the_field = int(input())

coins = 0
path_traversed = []


movement_mapper = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}


def create_the_field(size):
    m3x = []
    for _ in range(size):
        m3x.append(input().split())
    return m3x


def find_starting_position(field):
    for row in field:
        if 'P' in row:
            row_index = field.index(row)
            col_index = row.index("P")
            return (row_index, col_index)


def move(m3x, mapper, player_position, move_direction, path):
    global coins
    while move_direction:
        if move_direction in mapper:
            (start_row, start_col) = player_position
            (row_move, col_move) = mapper[move_direction]
            player_pos_row = start_row + row_move
            player_pos_col = start_col + col_move
            if in_range(player_pos_row, player_pos_col, m3x) and not_wall(player_pos_row, player_pos_col, m3x):
                coins += int(m3x[player_pos_row][player_pos_col])
                path.append([player_pos_row, player_pos_col])
                player_position = (player_pos_row, player_pos_col)
                if coins >= 100:
                    print_you_won(coins, path)
                    exit(0)
            else:
                coins /= 2
                print_game_over(coins, path)
                exit(0)
        move_direction = input()


def in_range(p_pos_row, p_pos_col, field):
    if p_pos_row in range(len(field)) and p_pos_col in range(len(field)):
        return True


def not_wall(p_pos_row, p_pos_col, field):
    if not field[p_pos_row][p_pos_col] == 'X':
        return True


def print_game_over(coins_left, path):
    print(f"Game over! You've collected {round(coins_left)} coins.")
    print(f"Your path:")
    for step in path:
        print(step)


def print_you_won(coins_left, path):
    print(f"You won! You've collected {coins_left} coins.")
    print(f"Your path:")
    for step in path:
        print(step)


the_field = create_the_field(size_of_the_field)
player_starting_position = find_starting_position(the_field)
commands = input()
move(the_field, movement_mapper, player_starting_position, commands, path_traversed)




