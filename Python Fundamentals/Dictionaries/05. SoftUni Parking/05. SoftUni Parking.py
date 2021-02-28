users = {}

n = int(input())

for i in range(n):
    data = input().split()
    command = data[0]
    if command == 'register':
        user_name = data[1]
        plate_number = data[2]
        if user_name not in users:
            users[user_name] = plate_number
            print(f"{user_name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[user_name]}")
    elif command == 'unregister':
        user_name = data[1]
        if user_name not in users:
            print(f"ERROR: user {user_name} not found")
        else:
            users.pop(user_name)
            print(f"{user_name} unregistered successfully")

for i in users:
    print(f"{i} => {users[i]}")
