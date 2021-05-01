clients = int(input())
counter_items = 0
bill = 0
total = 0
for client in range(1, clients+1):
    while True:
        item = input()

        if item == 'basket':
            bill += 1.50

        elif item == 'wreath':
            bill += 3.80

        elif item == 'chocolate bunny':
            bill += 7
        counter_items += 1
        if item == 'Finish':
            counter_items -= 1
            if counter_items % 2 == 0:
                bill = bill - bill * 0.20
            break


    print(f"You purchased {counter_items} items for {bill:.2f} leva.")
    total = total + bill
    bill = 0
    counter_items = 0

print(f"Average bill per client is: {total/clients:.2f} leva.")

