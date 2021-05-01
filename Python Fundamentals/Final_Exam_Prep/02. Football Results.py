score_first = input()
score_second = input()
score_tird = input()
won = 0
lost = 0
drawn = 0
if int(score_first[0]) > int(score_first[2]):
    won += 1
elif int(score_first[0]) < int(score_first[2]):
    lost += 1
else:
    drawn += 1

if int(score_second[0]) > int(score_second[2]):
    won += 1
elif int(score_second[0]) < int(score_second[2]):
    lost += 1
else:
    drawn += 1

if int(score_tird[0]) > int(score_tird[2]):
    won += 1
elif int(score_tird[0]) < int(score_tird[2]):
    lost += 1
else:
    drawn += 1
print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")