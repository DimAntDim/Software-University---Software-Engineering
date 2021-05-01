import math
easter_bread = int(input())
sugar_count = 0
flower_count = 0
flower_max = 0
sugar_max = 0
for i in range(1, easter_bread+1):
    sugar = int(input())
    sugar_count += sugar
    flower = int(input())
    flower_count += flower
    if sugar > sugar_max:
        sugar_max = sugar
    if flower > flower_max:
        flower_max = flower
print(f"Sugar: {math.ceil(sugar_count/950)}")
print(f"Flour: {math.ceil(flower_count/750)}")
print(f"Max used flour is {flower_max} grams, max used sugar is {sugar_max} grams.")