money = float(input())
sex = input()
age = int(input())
sport = input()
tax = 0

if sport == 'Gym' and sex == 'm':
    tax = 42
elif sport == 'Boxing' and sex == 'm':
    tax = 41
elif sport == 'Yoga' and sex == 'm':
    tax = 45
elif sport == 'Zumba' and sex == 'm':
    tax = 34
elif sport == 'Dances' and sex == 'm':
    tax = 51
elif sport == 'Pilates' and sex == 'm':
    tax = 39

if sport == 'Gym' and sex == 'f':
    tax = 35
elif sport == 'Boxing' and sex == 'f':
    tax = 37
elif sport == 'Yoga' and sex == 'f':
    tax = 42
elif sport == 'Zumba' and sex == 'f':
    tax = 31
elif sport == 'Dances' and sex == 'f':
    tax = 53
elif sport == 'Pilates' and sex == 'f':
    tax = 37

if age <= 19:
    tax -= tax*0.2

if money >= tax:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${tax-money:.2f} more.")

