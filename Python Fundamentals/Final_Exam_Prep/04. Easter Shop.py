eggs = int(input())
store_eggs = eggs
quantity = 0
sell_eggs = 0
while True:
    buy = input()
    if buy == 'Buy':
        quantity = int(input())
        if quantity > store_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {store_eggs}.")
            break
        store_eggs -= quantity
        sell_eggs += quantity

    elif buy == 'Fill':
        quantity = int(input())
        store_eggs += quantity

    else:
        print("Store is closed!")
        print(f"{sell_eggs} eggs sold.")
        break

