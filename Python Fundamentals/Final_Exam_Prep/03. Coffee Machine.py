drink = input()
sugar = input()
quantity = int(input())

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.9 - 0.9*0.35
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.20
    if quantity >= 5:
        price -= price*0.25
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 0.65
    elif sugar == 'Normal':
        price = 1.2
    else:
        price = 1.60
else:
    if sugar == 'Without':
        price = 0.50-0.50*0.35
    elif sugar == 'Normal':
        price = 0.60
    else:
        price = 0.70

total = quantity*price
if total > 15:
    total -= total*0.20
print(f"You bought {quantity} cups of {drink} for {total:.2f} lv.")