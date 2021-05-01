days = int(input())
hours = int(input())
bill = 0
total = 0
for d in range(1, days+1):
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 == 1:
            price = 2.50
        elif d % 2 == 1 and h % 2 == 0:
            price = 1.25
        else:
            price = 1
        bill += price
    total += bill
    print(f"Day: {d} - {bill:.2f} leva")
    bill = 0

print(f"Total: {total:.2f} leva")
