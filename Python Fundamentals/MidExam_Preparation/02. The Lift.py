people_waiting = int(input())
wagons = list(map(lambda x: int(x), input().split()))
free_seats = len(wagons)*4 -sum(wagons)
is_waiting = True
for w in range(len(wagons)):
    while wagons[w] < 4:
        wagons[w] += 1
        people_waiting -= 1
        free_seats -= 1
        if people_waiting == 0:
            is_waiting = False
            break
    if not is_waiting:
        break

if is_waiting and free_seats <= 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif not is_waiting and free_seats > 0:
    print("The lift has empty spots!")

wagons_print = list(map(lambda x: str(x), wagons))
print(' '.join(wagons_print))
