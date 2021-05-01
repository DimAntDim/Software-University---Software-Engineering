parts_price = 0
while True:
    parts = input()
    if parts == 'special':
        discount = 0.1
        break
    if parts == 'regular':
        discount = 0
        break
    if float(parts) > 0:
        parts_price += float(parts)
    else:
        print("Invalid price_pattern!")

taxes = parts_price*0.2
total_sum = (parts_price + taxes)
total_sum -= total_sum*discount
if total_sum == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n\
    Price without taxes: {parts_price:.2f}$\nTaxes: {taxes:.2f}$\n-----------\n\
    Total price_pattern: {total_sum:.2f}$")

