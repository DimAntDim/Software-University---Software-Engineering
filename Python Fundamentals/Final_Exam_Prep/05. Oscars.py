actor = input()
points = float(input())

jury = int(input())
total_points = points
for j in range(jury):
    jury_name = input()
    jury_score = float(input())
    jury_points = len(jury_name)*jury_score/2
    total_points += jury_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5-total_points:.1f} more!")