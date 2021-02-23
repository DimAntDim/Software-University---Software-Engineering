data = input().split()
request = input().split()
stock = {}

for d in range(0, len(data), 2):
    key = data[d]
    value = data[d+1]
    stock[key] = int(value)

for r in request:
    if r in stock:
        print(f"We have {stock[r]} of {r} left")
    else:
        print(f"Sorry, we don't have {r}")