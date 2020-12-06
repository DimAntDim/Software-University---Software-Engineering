
holliday_money = float(input())
saving_money = float(input())
spending_counter = 0
day_counter = 1
while True:
    command = input()
    money = float(input())
    if command == 'save':
        saving_money = saving_money + money
    else:
        saving_money = saving_money - money
        spending_counter += 1
        if saving_money < 0:
            saving_money = 0
    if saving_money >= holliday_money:
        print(f"You saved the money for {day_counter} days.")
        break
    if spending_counter == 5:
        print("You can't save the money.")
        print(f"{day_counter}")
        break
    day_counter += 1
