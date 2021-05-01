from collections import deque

bomb_effect_deque = deque(list(map(int, input().split(', '))))
bomb_casing_deque = deque(list(map(int, input().split(', '))))

bombs = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bombs_created = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

bomb_pouch_flag = False
bombs_created_flag = False

while bomb_casing_deque or bomb_effect_deque:

    first_element_of_bomb_effect = bomb_effect_deque[0]
    last_element_of_bomb_casing = bomb_casing_deque[-1]
    sum_of_materials = first_element_of_bomb_effect + last_element_of_bomb_casing
    if sum_of_materials in bombs:
        bomb_name = bombs.get(sum_of_materials)
        bombs_created[bomb_name] += 1
        bombs_created_flag = True
        bomb_effect_deque.popleft()
        bomb_casing_deque.pop()
    else:
        bomb_casing_deque[-1] -= 5

    if bombs_created['Datura Bombs'] >= 3 and \
            bombs_created['Cherry Bombs'] >= 3 and \
            bombs_created['Smoke Decoy Bombs'] >= 3:
        bomb_pouch_flag = True
        break

if bomb_pouch_flag:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect_deque:
    bomb_effects = list(map(str, bomb_effect_deque))
    print(f"Bomb Effects: {', '.join(bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casing_deque:
    bomb_casing = list(map(str, bomb_casing_deque))
    print(f"Bomb Casings: {', '.join(bomb_casing)}")
else:
    print("Bomb Casings: empty")

if bombs_created_flag:
    for bomb, quantity in sorted(bombs_created.items(), key=lambda x: x[0]):
        print(f"{bomb}: {quantity}")

