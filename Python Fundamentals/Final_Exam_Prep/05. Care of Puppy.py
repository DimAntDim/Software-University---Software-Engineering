food = int(input())*1000
dog_food = 0

while True:
    eaten_food = input()

    if eaten_food == 'Adopted':
        break

    dog_food = int(eaten_food)

    food -= dog_food

if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams." )
else:
    print(f"Food is not enough. You need {abs(food)} grams more.")