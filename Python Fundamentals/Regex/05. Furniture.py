import re

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"

text = input()

total = 0
items = []
while text != 'Purchase':
    match = re.finditer(pattern, text)
    for i in match:
        item = i[1]
        items.append(item)
        price = float(i[2])
        quantity = int(i[4])
        total += price * quantity
    text = input()

print('Bought furniture:')
for it in items:
    print(it)
print(f"Total money spend: {total:.2f}")
