s = list(map(lambda x: int(x), input().split()))
racks = 1
rack_capacity = int(input())
capacity = 0
while s:
    if capacity + s[-1] == rack_capacity:
        racks += 1
        s.pop()
        capacity = 0
    elif capacity + s[-1] > rack_capacity:
        racks += 1
        capacity = 0
    else:
        capacity += s.pop()

print(racks)
