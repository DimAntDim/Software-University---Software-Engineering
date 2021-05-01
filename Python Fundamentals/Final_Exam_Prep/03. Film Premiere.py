movie = input()
packet = input()

tickets = int(input())
price = 0

if movie == 'John Wick':
    if packet == 'Drink':
        price = 12
    elif packet == 'Popcorn':
        price = 15
    else:
        price = 19
elif movie == 'Star Wars':
    if packet == 'Drink':
        price = 18
    elif packet == 'Popcorn':
        price = 25
    else:
        price = 30
    if tickets >= 4:
        price -= price*0.3
elif movie == 'Jumanji':
    if packet == 'Drink':
        price = 9
    elif packet == 'Popcorn':
        price = 11
    else:
        price = 14
    if tickets == 2:
        price -= price*0.15

total = tickets*price

print(f"Your bill is {total:.2f} leva.")
