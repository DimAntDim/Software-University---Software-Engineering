command = input()
products = {}
while command != 'buy':
    data = command.split()
    name = data[0]
    price = round(float(data[1]),2)
    quantity = int(data[2])
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][1] += quantity
    if products[name][0] != price:
        products[name][0] = price
    command = input()

for i in products:
    total_price = products[i][0]*products[i][1]
    print(f"{i} -> {total_price:.2f}")


