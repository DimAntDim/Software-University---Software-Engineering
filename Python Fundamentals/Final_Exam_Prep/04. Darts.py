player_start_points = 301
player_name = input()
counter_positive = 0
counter_negative = 0
while True:
    impact = input()
    if impact == 'Retire':
        print(f"{player_name} retired after {counter_negative} unsuccessful shots.")
        break
    elif player_start_points == 0:
        print(f"{player_name} won the leg with {counter_positive-counter_negative} shots.")
        break
    hit_points = int(input())
    if impact == 'Single':
        hit_points = hit_points
        counter_positive += 1
    elif impact == 'Double':
        hit_points *= 2
        counter_positive += 1
    elif impact == 'Triple':
        hit_points *= 3
        counter_positive += 1
    if hit_points <= player_start_points:
        player_start_points -= hit_points
    else:
        player_start_points -= 0
        counter_negative += 1
