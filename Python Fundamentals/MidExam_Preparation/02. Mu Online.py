initial_health = 100
total_bitcoins = 0
rooms = input().split('|')
index = 0
for r in rooms:
    index += 1
    command, number = r.split()
    if command == 'potion':
        health = int(number)
        if initial_health + health >= 100:
            print(f"You healed for {100 - initial_health} hp.")
            initial_health = 100
        else:
            initial_health += health
            print(f"You healed for {health} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == 'chest':
        bitcoins = int(number)
        total_bitcoins += bitcoins
        print(f"You found {bitcoins} bitcoins.")

    else:
        monster = command
        monster_attack = int(number)
        initial_health -= monster_attack
        if  initial_health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {index}")
            break
if initial_health > 0:
    print(f"You\'ve made it!")
    print(f"Bitcoins: {total_bitcoins}")
    print(f"Health: {initial_health}")