resources = {}
counter = 0
resource = str
while True:
    data = input()
    if data == 'stop':
        for i in resources:
            print(f"{i} -> {resources.get(i)}")
        break
    if counter % 2 == 0:
        resource = data
        if resource not in resources:
            resources[resource] = 0
    elif counter % 2 != 0:
        quantity = int(data)
        resources[resource] += quantity
    counter += 1




