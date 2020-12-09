"""
As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events.
Each event is separated with '|' (vertical bar): "event1|event2|event3…"
Each event contains event name or books and a number, separated by dash("{event/ingredient}-{number}")
If the event is "rest": you gain energy, the number in the second part.
But your energy cannot exceed your initial energy (100).
Print: "You gained {0} energy.".
After that, print your current energy: "Current energy: {0}.".
If the event is "order": You've earned some coins, the number in the second part.
Each time you get an order, your energy decreases with 30 points.
If you have energy to complete the order, print: "You earned {0} coins.".
If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".
In any other case you are having an ingredient, you have to buy.
The second part of the event, contains the coins you have to spent and remove from your coins.
If you are not bankrupt (coins <= 0) you've bought the ingredient successfully,
and you should print ("You bought {ingredient}.")
If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
If you managed to handle all events through the day, print on the next three lines:
"Day completed!", "Coins: {coins}", "Energy: {energy}".
"""

energy = 100
coins = 100

ingredient = ''
events = input().split('|')
flag = True
for e in range(len(events)):
    item = events[e].split('-')
    event = item[0]
    number = int(item[1])
    if event == 'rest':
        gained_energy = number
        if energy + gained_energy > 100:
            gained_energy = 0
            energy = 100
        else:
            energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy - 30 < 0:
            energy += 50
            print(f"You had to rest!")
        else:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
    else:
        if coins - number <= 0:
            ingredient = event
            flag = False
            break
        else:
            coins -= number
            print(f"You bought {event}.")

if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {ingredient}.")
