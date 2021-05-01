from collections import deque

q = deque()
names = input().split()
for name in names:
    q.append(name)

n = int(input())

counter = 0
while len(q) > 1:
    counter += 1
    if counter == n:
        print(f"Removed {q.popleft()}")
        counter = 0
    else:
        move = q.popleft()
        q.append(move)

print(f"Last is {q.popleft()}")
