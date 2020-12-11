product = input()
quantity = int(input())


def price(item, q):
    if item == 'coffee':
        total_price = 1.50*q
    elif item == 'water':
        total_price = 1.00*q
    elif item == 'coke':
        total_price = 1.40*q
    else:
        total_price = 2.00*q
    return total_price


print(f"{price(product, quantity):.2f}")
