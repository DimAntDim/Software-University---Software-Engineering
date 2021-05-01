def create_board():
    for _ in range(8):
        line = input().split()
        chess_board.append(line)


def find_the_king():
    king_index = []
    for x in range(len(chess_board)):
        row = chess_board[x]
        for y in range(len(row)):
            el = row[y]
            if el == 'K':
                king_index.append(x)
                king_index.append(y)
                break
    return king_index


def check_queens_chess(king_position):
    x, y = king_position[0], king_position[1]
    # check up
    for i in range(1, x + 1):
        if chess_board[x - i][y] == 'Q':
            queens_chess.append([x - i, y])
            break
        # check down
    for i in range(8 - x):
        if chess_board[x + i][y] == 'Q':
            queens_chess.append([x + i, y])
            break
        # check left
    for i in range(1, y + 1):
        if chess_board[x][y - i] == 'Q':
            queens_chess.append([x, y - i])
            break
        # check right
    for i in range(8 - y):
        if chess_board[x][y + i] == 'Q':
            queens_chess.append([x, y + i])
            break

    const = 1
    flag_up_left = False
    flag_up_right = False
    flag_down_right = False
    flag_down_left = False
    while True:
        # check up left
        if x - const >= 0 and not flag_up_left:
            if y + const < 8 and x > 0 and y > 0:
                if chess_board[x - const][y + const] == 'Q':
                    queens_chess.append([x - const, y + const])
                    flag_up_left = True
        else:
            flag_up_left = True
        # check up right
        if x > 0 and y < 7 and not flag_up_right:
            if x - const >= 0 and y - const >= 0:
                if chess_board[x - const][y - const] == 'Q':
                    queens_chess.append([x - const, y - const])
                    flag_up_right = True
        else:
            flag_up_right = True
        # check down left
        if x + const < 8 and y - const > 0 and 0 <= x < 8 and 0 < y <= 7 and not flag_down_left:
            if chess_board[x + const][y - const] == 'Q':
                queens_chess.append([x + const, y - const])
                flag_down_left = True
        else:
            flag_down_left = True
        # check down right
        if x + const < 8 and y + const < 8 and x < 7 and y < 7 and not flag_down_right:
            if chess_board[x + const][y - const] == 'Q':
                queens_chess.append([x + const, y + const])
                flag_down_right = True
        else:
            flag_down_right = True
        if flag_down_right and flag_up_right and flag_down_left and flag_up_left:
            break
        const += 1


chess_board = []
queens_chess = []


create_board()
check_queens_chess(find_the_king())
if len(queens_chess) > 0:
    print(*[i for i in queens_chess], sep='\n')
else:
    print('The king is safe!')
