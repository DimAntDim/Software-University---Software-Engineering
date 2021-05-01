days = int(input())
food = float(input())
dog_food = 0
cat_food = 0
coockes = 0
for d in range(1, days+1):
    dog = int(input())
    cat = int(input())
    if d % 3 == 0:
        coockes += (cat+dog)*0.10
    dog_food += dog
    cat_food += cat


eaten_food = dog_food+cat_food

print(f"Total eaten biscuits: {round(coockes)}gr.")
print(f"{eaten_food/food*100:.2f}% of the food has been eaten.")
print(f"{dog_food/eaten_food*100:.2f}% eaten from the dog.")
print(f"{cat_food/eaten_food*100:.2f}% eaten from the cat.")

