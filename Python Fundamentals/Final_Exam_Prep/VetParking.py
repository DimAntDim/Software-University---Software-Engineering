days = int(input())
hours = int(input())
total = 0

for d in range(1, days+1):
    tax = 0
    day_total = 0
    hour_price = 0
    for h in range(1, hours+1):
        if d % 2 == 1 and h % 2 == 0:
            tax = 1.25
        elif d % 2 == 0 and h % 2 == 1:
            tax = 2.5
        else:
            tax = 1
        hour_price += tax
    day_total += hour_price
    total += day_total
    print(f"Day: {d} - {day_total:.2f} leva")

print(f"Total: {total:.2f} leva")
