input_price = float(input())
laps = input()
fen_cart = input()
cart_type = input()
price = 0
if cart_type == 'Child':
    if laps == 'five':
        price = 7
    else:
        price = 11
elif cart_type == 'Junior':
    if laps == 'five':
        price = 9
    else:
        price = 16
elif cart_type == 'Adult':
    if laps == 'five':
        price = 12
    else:
        price = 21
else:
    if laps == 'five':
        price = 18
    else:
        price = 32

if fen_cart == 'yes':
    price -= price*0.2

if input_price >= price:
    print(f"You bought {cart_type} ticket for {laps} laps. Your change is {input_price-price:.2f}lv.")
else:
    print(f"You don't have enough money! You need {price-input_price:.2f}lv more.")



