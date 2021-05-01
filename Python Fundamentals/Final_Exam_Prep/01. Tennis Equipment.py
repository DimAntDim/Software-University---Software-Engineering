import math
tenis =float(input())
quantity = int(input())
shoes = int(input())

price_tenis = tenis * quantity
shoes_price = 1/6*tenis
shoes = shoes*shoes_price

total = price_tenis+shoes
other_ithems = total*0.20
total += other_ithems
print(f"Price to be paid by Djokovic {math.floor(1/8*total)}"
)
print(f"Price to be paid by sponsors {math.ceil(7/8*total)}")
