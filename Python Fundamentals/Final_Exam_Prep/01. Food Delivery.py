chicken = int(input())*10.35
fish = int(input())*12.40
veg = int(input())*8.15

total = chicken+fish+veg
desert = total*0.20
total += desert + 2.50

print(f"Total: {total:.2f}")