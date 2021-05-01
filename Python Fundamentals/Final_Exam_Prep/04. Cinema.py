cinema_seats = int(input())
ocupy_seats = 0
counter = 0
discount = 0
income = 0
while True:
    users = input()
    if cinema_seats == 0 and users == 'Movie time!':
        print(f"There are {cinema_seats} seats left in the cinema.")
        break
    if users == 'Movie time!':
        print(f"There are {cinema_seats} seats left in the cinema.")
        break

    users = int(users)
    if users > cinema_seats:
        print("The cinema is full.")
        break
    if users % 3 == 0:
        discount = 5
    income += users * 5 - discount
    counter += users
    cinema_seats -= users
    if cinema_seats == 0 and users == 'Movie time!':
        print(f"The cinema is full")
        break
    
    discount = 0

print(f"Cinema income - {income} lv.")
