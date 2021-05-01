mine_field = []


def matrix(count):
    for _ in range(count):
        mine_field.append(list(map(lambda x: int(x), input().split(' '))))
    return mine_field


def boom(board, explosion, x, y):
    # {n} - global var is the square proportion N x N
    board_limit = n - 1
    if board[x][y] > 0:
        # destroy Up
        if 0 < x <= board_limit:
            if board[x-1][y] and board[x-1][y] > 0:
                board[x-1][y] -= explosion

        # destroy Down
        if 0 <= x < board_limit:
            if board[x + 1][y] and board[x + 1][y] > 0:
                board[x + 1][y] -= explosion

        # destroy on Right side
        if 0 < y < board_limit:
            if board[x][y + 1] and board[x][y + 1] > 0:
                board[x][y + 1] -= explosion

        # destroy on Left side
        if 0 < y < n:
            if board[x][y - 1] and board[x][y - 1] > 0:
                board[x][y - 1] -= explosion

        # Right tilt diagonal
        # Up Right
        if 0 < x <= board_limit and 0 <= y < board_limit:
            if board[x-1][y+1] and board[x-1][y+1] > 0:
                board[x-1][y+1] -= explosion
        # Down Left
        if 0 <= x < n - 1 and 0 < y <= board_limit:
            if board[x + 1][y - 1] and board[x + 1][y - 1] > 0:
                board[x + 1][y - 1] -= explosion

        # Left tilt diagonal
        # Up Left
        if 0 < x <= board_limit and 0 < y <= board_limit:
            if board[x - 1][y - 1] and board[x - 1][y - 1] > 0:
                board[x - 1][y - 1] -= explosion
        # Down Right
        if 0 <= x < n - 1 and 0 <= y < board_limit:
            if board[x + 1][y + 1] and board[x + 1][y + 1] > 0:
                board[x + 1][y + 1] -= explosion
    # bomb explode and become 0
    board[x][y] = 0


def print_out():
    sum_of_positive = []

    for line in mine_field:
        for el in line:
            if el > 0:
                sum_of_positive.append(el)
    print(f"Alive cells: {len(sum_of_positive)}\nSum: {sum(sum_of_positive)}")

    for line in mine_field:
        line_print = list(map(lambda x: str(x), line))
        print(' '.join(line_print))


n = int(input())
matrix(n)

bombs = input().split(' ')
for b in bombs:
    b = b.split(',')
    bomb_x = int(b[0])
    bomb_y = int(b[1])
    if mine_field[bomb_x][bomb_y] > 0:
        explode = mine_field[bomb_x][bomb_y]
        boom(mine_field, explode, bomb_x, bomb_y)

print_out()
