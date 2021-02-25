play_book = {}
players_skils = {}


def fight(position):
    total_point_p1 = play_book[player1][position]
    total_point_p2 = play_book[player2][position]
    if total_point_p1 > total_point_p2:
        del play_book[player2]
    elif total_point_p1 < total_point_p2:
        del play_book[player1]
    else:
        pass
    return play_book


while True:
    data = input()
    if data == 'Season end':
        break
    if 'vs' in data:
        data = data.split(' vs ')
        player1 = data[0]
        player2 = data[1]
        fight_flag = False
        if player1 in play_book and player2 in play_book:
            for v in play_book.values():
                for key_positions, points in v.items():
                    if key_positions in play_book[player1] and key_positions in play_book[player2]:
                        fight(key_positions)
                        fight_flag = True
                        break
                if fight_flag:
                    break


    else:
        data = data.split(' -> ')
        player = data[0]
        position = data[1]
        skill = int(data[2])
        if player not in play_book:
            play_book[player] = {}
            play_book[player][position] = skill
        else:
            if position in play_book[player]:
                if play_book[player][position] < skill:
                    play_book[player][position] = skill
            else:
                play_book[player][position] = skill

for key, value in play_book.items():
    total = sum(value.values())
    players_skils[key] = total

for player, total in sorted(players_skils.items(), key= lambda x: (-x[1], x[0])):
    print(f"{player}: {total} skill")
    for a, b in sorted(play_book[player].items(), key= lambda x: (-x[1], x[0])):
        print(f"- {a} <::> {b}")


