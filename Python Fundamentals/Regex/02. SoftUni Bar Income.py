import re

data = input()
pattern = r"%(?P<name>[A-Z][a-z]*)%.*?<(?P<product>\w.*?)>.*?\|(?P<count>\d+?)\|.*?(?P<price>\d+\.?\d+)\$"
customers = []
while not data == "end of shift":
    matches = re.finditer(pattern, data)
    customer = {}
    for match in matches:
        customer = match.groupdict()
    if customer:
        customers.append(customer)
    data = input()
total_price = 0
for shift in customers:
    total = int(shift['count']) * float(shift['price'])
    total_price += total
    print(f"{shift['name']}: {shift['product']} - {total:.2f}")
print(f"Total income: {total_price:.2f}")
