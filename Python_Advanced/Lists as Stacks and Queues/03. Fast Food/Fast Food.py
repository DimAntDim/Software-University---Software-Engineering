from collections import deque

q = deque()

food = int(input())

orders = list(map(lambda x: int(x), input().split()))
sorting_orders = sorted(orders)
biggest_order = sorting_orders[-1]
print(biggest_order)

for order in orders:
    q.append(order)

while q:
    order = q[0]
    if food-order < 0:
        break
    else:
        food -= order
        q.popleft()
rest = []


if len(q) > 0:
    while q:
        rest.append(q.popleft())
    rest = map(lambda x: str(x), rest)
    print(f"Orders left: {' '.join(rest)}")
else:
    print("Orders complete")

