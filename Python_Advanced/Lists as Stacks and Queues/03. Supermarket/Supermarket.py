from collections import deque

end_program = 'End'
print_queue = 'Paid'
q = deque()

while True:
    data = input()
    if data == end_program:
        print(f"{len(q)} people remaining.")
        break
    elif data == print_queue:
        while q:
            print(q.popleft())
    else:
        q.append(data)

