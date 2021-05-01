import math
tournaments = int(input())
start_points = int(input())
points = start_points
counter = 0
for t in range(tournaments):
    stage = input()
    if stage == 'W':
        start_points += 2000
        counter += 1
    elif stage == 'F':
        start_points += 1200
    else:
        start_points += 720

print(f"Final points: {start_points}")
averadge = (start_points - points)/tournaments
print(f"Average points: {math.floor(averadge)}")
print(f"{counter/tournaments*100:.2f}%")