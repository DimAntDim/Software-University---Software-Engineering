budget = float(input())
fuel = float(input())*2.10
day = input()

total = fuel + 100
if day == 'Saturday':
    total -= total*0.10
else:
    total -= total*0.20

if budget >= total:
    print(f"Safari time! Money left: {budget-total:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {total-budget:.2f} lv.")