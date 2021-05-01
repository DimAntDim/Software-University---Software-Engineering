eggs_size = input()
eggs_color = input()
n = int(input())
price = 0
for _ in range(n):
    if eggs_size == 'Large':
        if eggs_color == 'Red':
            price = 16
        elif eggs_color == 'Green':
            price = 12
        else:
            price = 9
    if eggs_size == 'Medium':
        if eggs_color == 'Red':
            price = 13
        elif eggs_color == 'Green':
            price = 9
        else:
            price = 7
    if eggs_size == 'Small':
        if eggs_color == 'Red':
            price = 9
        elif eggs_color == 'Green':
            price = 8
        else:
            price = 5

total = price*n
total -= total*0.35
print(f"{total:.2f} leva.")
