sell_games = int(input())
counter = 0
h = 0
f = 0
o = 0
others = 0
for g in range(sell_games):
    game_name = input()
    if game_name == 'Hearthstone':
        h += 1
    elif game_name == 'Fornite':
        f += 1
    elif game_name == 'Overwatch':
        o += 1
    else:
        others += 1

print(f"Hearthstone - {h/sell_games*100:.2f}%")
print(f"Fornite - {f/sell_games*100:.2f}%")
print(f"Overwatch - {o/sell_games*100:.2f}%")
print(f"Others - {others/sell_games*100:.2f}%")
