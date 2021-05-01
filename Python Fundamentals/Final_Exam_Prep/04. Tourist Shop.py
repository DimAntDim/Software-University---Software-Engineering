budget = float(input())
counter = 0
total = 0
while True:
    item = input()
    if item == 'Stop':
        print(f"You bought {counter} products for {total:.2f} leva.")
        break
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price = price /2

    if price > budget:
        print(f"You don't have enough money!")
        print(f"You need {abs(budget-price):.2f} leva!")
        break
    budget -= price
    total = total + price