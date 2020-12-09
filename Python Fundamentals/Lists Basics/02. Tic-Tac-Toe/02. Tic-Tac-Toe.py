"""
Memory: 8.41 MB
Time: 0.071 s
"""
first_player = False
second_player = False

game = []
for r in range(3):
    board = input().split()
    game.append(board)

for i in range(3):
    if (game[i][0] == '1' and game[i][1] == '1' and game[i][2] == '1') or \
            (game[0][0] == '1' and game[1][1] == '1' and game[2][2] == '1') or \
            (game[0][2] == '1' and game[1][1] == '1' and game[2][0] == '1'):
        first_player = True
        break
    elif game[0][i] == '1' and game[1][i] == '1' and game[2][i] == '1':
        first_player = True

    elif (game[i][0] == '2' and game[i][1] == '2' and game[i][2] == '2') or \
            (game[0][0] == '2' and game[1][1] == '2' and game[2][2] == '2') or \
            (game[0][2] == '2' and game[1][1] == '2' and game[2][0] == '2'):
        second_player = True
        break
    elif game[0][i] == '2' and game[1][i] == '2' and game[2][i] == '2':
        second_player = True

if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
else:
    print("Draw!")

"""
LITE VERSION
Memory: 8.36 MB
Time: 0.056 s
first_player = False
second_player = False
draw = False
game = []
for i in range_shot(3):
    board = input().split()
    game.append(board)

if '2' == game[0][0] and '2' == game[0][1] and '2' == game[0][2]:
    second_player = True
elif '2' == game[1][0] and '2' == game[1][1] and '2' == game[1][2]:
    second_player = True
elif '2' == game[2][0] and '2' == game[2][1] and '2' == game[2][2]:
    second_player = True
elif '2' == game[0][0] and '2' == game[1][0] and '2' == game[2][0]:
    second_player = True
elif '2' == game[0][1] and '2' == game[1][1] and '2' == game[2][1]:
    second_player = True
elif '2' == game[0][2] and '2' == game[1][2] and '2' == game[2][2]:
    second_player = True
elif '2' == game[0][0] and '2' == game[1][1] and '2' == game[2][2]:
    second_player = True
elif '2' == game[0][2] and '2' == game[1][1] and '2' == game[2][0]:
    second_player = True
elif '1' == game[0][0] and '1' == game[0][1] and '1' == game[0][2]:
    first_player = True
elif '1' == game[1][0] and '1' == game[1][1] and '1' == game[1][2]:
    first_player = True
elif '1' == game[2][0] and '1' == game[2][1] and '1' == game[2][2]:
    first_player = True
elif '1' == game[0][0] and '1' == game[1][0] and '1' == game[2][0]:
    first_player = True
elif '1' == game[0][1] and '1' == game[1][1] and '1' == game[2][1]:
    first_player = True
elif '1' == game[0][2] and '1' == game[1][2] and '1' == game[2][2]:
    first_player = True
elif '1' == game[0][0] and '1' == game[1][1] and '1' == game[2][2]:
    first_player = True
elif '1' == game[0][2] and '1' == game[1][1] and '1' == game[2][0]:
    first_player = True
else:
    draw = True
if first_player:
    print("First player won")
if second_player:
    print("Second player won")
if draw:
    print("Draw!")
"""



