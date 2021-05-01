win_counter = 0
lost_counter = 0
tournament_counter = 0
while True:
    tournament = input()
    if tournament == 'End of tournaments':
        break
    games = int(input())
    for g in range(1, games+1):
        points_desi = int(input())
        points_other_team = int(input())
        if points_desi > points_other_team:
            print(f"Game {g} of tournament {tournament}: win with {points_desi-points_other_team} points.")
            win_counter += 1
        else:
            print(f"Game {g} of tournament {tournament}: lost with {points_other_team-points_desi} points.")
            lost_counter += 1
        points_desi = 0
        points_other_team = 0
        tournament_counter += 1

print(f"{win_counter/tournament_counter*100:.2f}% matches win")
print(f"{lost_counter/tournament_counter*100:.2f}% matches lost")