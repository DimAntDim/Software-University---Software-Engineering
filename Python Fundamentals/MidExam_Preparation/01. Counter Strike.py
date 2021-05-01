energy = int(input())
won_battle = 0
while True:
    command = input()
    if command == 'End of battle':
        print(f"Won battles: {won_battle}. Energy left: {energy}")
        break
    energy_to_kill = int(command)
    if energy - energy_to_kill >= 0:
        energy -= energy_to_kill
        won_battle += 1
    else:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {energy} energy")
        break
    if won_battle % 3 == 0:
        energy += won_battle
