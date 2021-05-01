row = int(input())
position = int(input())
row_counter_odd = 0
row_counter_even = 0
position_counter = 0
for r in range(1, row+1):
    if r % 2 != 0:
        row_counter_odd += 1
    else:
        row_counter_even += 1
for p in range(1, position+1):
    if p % 3 != 0:
        position_counter += 1

strawberry = position*3.5*row_counter_odd
blueberry = position_counter*5.00*row_counter_even
total = strawberry + blueberry
total *= 0.8
print(f"Total: {total:.2f} lv.")
