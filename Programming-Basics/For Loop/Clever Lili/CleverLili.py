years = int(input())
wash_m = float(input())
toy_price = int(input())
toys = 0
savings = 0
addon = 10
money = 0
for i in range(1, years+1):
    if i % 2 == 1:
        toys += 1
    else:
        money = money + addon -1
        addon = addon+10

savings = money + toys * toy_price
rest = savings - wash_m
if wash_m <= savings:
    print(f"Yes! {rest:.2f}")
else:
    rest = rest * -1
    print(f"No! {rest:.2f}")