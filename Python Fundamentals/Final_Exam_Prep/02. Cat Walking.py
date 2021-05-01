minutes = int(input())
times_per_day = int(input())
calories = int(input())

calories_per_day = minutes*times_per_day*5
enught_burt_calories = calories / 2

if calories_per_day >= enught_burt_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_per_day}.")
