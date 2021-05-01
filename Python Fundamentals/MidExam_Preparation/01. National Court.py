import math
p_1 = int(input())
p_2 = int(input())
p_3 = int(input())

person_per_h = p_1+p_2+p_3

total_person = int(input())
hours = 0

while True:
    hours += 1
    total_person -= person_per_h
    if hours % 4 == 0:
        hours += 1
    if total_person <= 0:
        break

print(f"Time needed: {hours}h.")
