from collections import deque

quantity = int(input())
q = deque()
while True:
    name = input()
    if name == 'Start':
        while True:
            data = input()
            command = data.split()
            if command[0] == 'refill':
                litters = command[1]
                quantity += int(litters)
            elif command[0] == 'End':
                print(f"{quantity} liters left")
                break
            else:
                if int(command[0]) <= quantity:
                    print(f"{q.popleft()} got water")
                    quantity -= int(command[0])
                else:
                    print(f"{q.popleft()} must wait")
        break
    else:
        q.append(name)
