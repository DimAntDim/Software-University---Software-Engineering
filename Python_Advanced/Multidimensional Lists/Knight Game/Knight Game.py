possible_pos = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]

trouble_horses = {}

chess_board = []


def board(rows):

    for i in range(rows):
        line = input()
        row = []
        for ch in line:
            row.append(ch)
        chess_board.append(row)
    return chess_board


def check(chess):

    count = 0
    while True:
        for i in range(len(chess)):
            r = chess_board[i]
            for pos in range(len(r)):
                if r[pos] == 'K':
                    horse_position = [i, pos]

                    for p in possible_pos:
                        x = horse_position[0] + p[0]
                        y = horse_position[1] + p[1]
                        if 0 <= x < len(chess_board) and 0 <= y < len(chess_board[0]):
                            if chess_board[x][y] == 'K':
                                horse_problem = f"{[x, y]}"
                                if horse_problem not in trouble_horses:
                                    trouble_horses[horse_problem] = 0
                                trouble_horses[horse_problem] += 1

            if len(trouble_horses) > 0:
                sorted(trouble_horses.items(), key=lambda z: -z[1])
                horse = list(trouble_horses.keys())[0]
                coordinates = []
                for ch in horse:
                    if ch.isdigit():
                        coordinates.append(int(ch))

                chess_board[coordinates[0]][coordinates[1]] = 0
                del(trouble_horses[horse])
            else:
                print(count)
                exit()
            count += 1


board(int(input()))
check(chess_board)



