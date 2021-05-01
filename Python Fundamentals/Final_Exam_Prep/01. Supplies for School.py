pens = int(input())*5.80
markers = int(input())*7.20
liquid = float(input())*1.20


total = pens+markers+liquid
discount = total*float(input())/100
total = total - discount

print(f"{total:.3f}")