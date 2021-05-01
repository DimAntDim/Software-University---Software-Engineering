one_eggs = int(input())
second_eggs = int(input())

while True:
    winner = input()
    if winner == 'End of battle':
        print(f"Player one has {one_eggs} eggs left.")
        print(f"Player two has {second_eggs} eggs left.")
        break
    if winner == 'one':
        second_eggs -= 1
    elif winner == 'two':
        one_eggs -= 1
    if one_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_eggs} eggs left.")
        break
    elif second_eggs == 0:
        print(f"Player two is out of eggs. Player one has {one_eggs} eggs left.")
        break