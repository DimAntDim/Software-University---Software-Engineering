from collections import deque

total_time = 0

customers = deque(list(map(int, input().split(', '))))
taxi_drivers = deque(list(map(int, input().split(', '))))


while True:
    if customers and taxi_drivers:
        customer = customers[0]
        taxi = taxi_drivers[-1]

        if taxi >= customer:
            total_time += customers[0]
            customers.popleft()
            taxi_drivers.pop()
        else:
            taxi_drivers.pop()

    if not customers:
        print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
        break
    elif not taxi_drivers:
        print(f"Not all customers were driven to their destinations\n"
              f"Customers left: {', '.join(map(lambda x: str(x), [num for num in customers]))}")
        break
