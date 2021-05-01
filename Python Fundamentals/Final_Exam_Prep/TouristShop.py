budget = float(input())
counter_product = 0
total = 0
product = input()
while True:
    if product == 'Stop':
        print(f"You bought {counter_product} products for {total:.2f} leva.")
        break
    price = float(input())
    counter_product += 1
    if counter_product % 3 == 0:
        price = price / 2
    total += price
    rest_money = budget - price
    if rest_money < price:
        print("You don't have enough money!")
        print(f"You need {total - budget:.2f} leva!")
        break
    product = input()


budget = float(input())

counter = 0
bill = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {counter} products for {bill:.2f} leva.")
        break

    item_price = float(input())

    if (counter + 1) % 3 == 0:
        item_price *= 0.5

    if item_price + bill > budget:
        diff = item_price + bill - budget
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break

    counter += 1
    bill += item_price