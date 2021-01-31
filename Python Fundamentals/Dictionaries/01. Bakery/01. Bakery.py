data = input().split()
bakery = {}

for d in range(0, len(data), 2):
    key = data[d]
    value = data[d+1]
    bakery[key] = int(value)
print(bakery)