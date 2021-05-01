import math
students = int(input())
lectures = int(input())
initial_bonus = int(input())

bonus = 0
attended_lectires = 0
for i in range(students):
    attendancies = int(input())
    ad_bonus = (attendancies/lectures)*(5+initial_bonus)
    if ad_bonus > bonus:
        bonus = ad_bonus
        attended_lectires = attendancies

print(f"Max Bonus: {math.ceil(bonus)}.")
print(f"The student has attended {attended_lectires} lectures.")

