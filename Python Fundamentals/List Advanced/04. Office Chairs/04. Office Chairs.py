rooms = int(input())
free_chairs = []
chairs_needed = []
for r in range(1, rooms+1):
    room = input().split()

    chairs = room[0]
    occupy = int(room[1])
    total_chairs = chairs.count('X')

    if total_chairs > occupy:
        free_chairs.append(total_chairs - occupy)
        chairs_needed.append(0)
    else:
        chairs_needed.append(occupy-total_chairs)
        free_chairs.append(0)

if sum(chairs_needed) == 0:
    print(f"Game On, {sum(free_chairs)} free chairs left")
else:
    for c in range(len(chairs_needed)):
        if chairs_needed[c] > 0:
            print(f"{chairs_needed[c]} more chairs needed in room {c+1}")
