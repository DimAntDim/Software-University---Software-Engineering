def dictionary_data(item):
    for _ in item:
        items[_] = {}
    return items


items = {}

dictionary_data(input().split(', '))

for i in range(int(input())):
    data = input().split(' - ')
    category = data[0]
    item_name = data[1]
    properties = data[2].split(';')
    quantity = properties[0].split(':')[1]
    quality = properties[1].split(':')[1]
    items[category][item_name] = {'quantity': int(quantity), 'quality': int(quality)}

count_of_items = 0
average_quality = 0
for k, v in items.items():
    for food, props in v.items():
        count_of_items += props['quantity']
        average_quality += props['quality']


print(f"Count of items: {count_of_items}")
print(f"Average quality: {average_quality/len(items):.2f}")
for k, v in items.items():
    print(f"{k} -> {', '.join(v.keys())}")
