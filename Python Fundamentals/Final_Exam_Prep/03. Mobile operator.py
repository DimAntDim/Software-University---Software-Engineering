contract_period = input()
contract_type = input()
internet = input()

mounth = int(input())

if contract_period == 'one':
    if contract_type == 'Small':
        price = 9.98
    elif contract_type == 'Middle':
        price = 18.99
    elif contract_type == 'Large':
        price = 25.98
    else:
        price = 35.99
else:
    if contract_type == 'Small':
        price = 8.58
    elif contract_type == 'Middle':
        price = 17.09
    elif contract_type == 'Large':
        price = 23.59
    else:
        price = 31.79
if internet == 'yes':
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    else:
        price += 3.85
total = mounth*price

if contract_period == 'two':
    total -= total*0.0375


print(f"{total:.2f} lv.")