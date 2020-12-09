"""
Most football fans love it for the goals and excitement. Well, this problem doesn't.
You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
the game is stopped immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number.
e.g. the card 'B-7' means player #7 from team B received a card.
The task: Given a list of cards (could be empty), return the number of remaining players on each team
at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}".
If the game was terminated print an additional line: "Game was terminated"
Note for the random tests: If a player that has already been sent off receives another card - ignore it.
input
A-1 A-5 A-10 B-2 A-10 A-7 A-3
output
Team A - 6; Team B - 10
Game was terminated
input
A-1 A-5 A-10 B-2
output
Team A - 8; Team B - 10


"""
index = input()
x = index.split()
team1 = 11
team2 = 11
x = list(dict.fromkeys(x)) #remove doubles books
print(x)
for i in x:
    if i.find('A'):
        team1 -= 1
        if team1 < 7:
            break
    elif i.find('B'):
        team2 -= 1
        if team2 < 7:
            break
if team1 < 7 or team2 < 7:
    print(f"Team A - {team2}; Team B - {team1}\nGame was terminated")
else:
    print(f"Team A - {team2}; Team B - {team1}")