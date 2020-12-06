while True:
    save_money = 0
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while budget > save_money:
        save = float(input())
        save_money += save
    print(f"Going to {destination}!")