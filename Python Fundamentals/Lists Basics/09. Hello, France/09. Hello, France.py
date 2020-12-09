collection_of_item = input().split('|')
budget = float(input())
buy_list = []
spend_sum = 0
for i in collection_of_item:
    product = i.split('->')
    item = product[0]
    price = float(product[1])
    if budget - price >= 0:
        if item == 'Clothes' and price <= 50.00 \
                or item == 'Shoes' and price <= 35.00 \
                or item == 'Accessories' and price <= 20.50:
            buy_list.append(price * 1.4)
            budget -= price
            spend_sum += price
for i in buy_list:
    print(f"{i:.2f}", end=" ")
profit = sum(buy_list) - spend_sum
print(f"\nProfit: {profit:.2f}")

if budget + sum(buy_list) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
