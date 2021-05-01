elements = input().split()
win_flag = False
moves = 0

while True:
    command = input().split()
    if command[0] == 'end':
        break
    searching_element = int(command[0])
    matching_element = int(command[1])
    moves += 1
    if matching_element < 0 or matching_element > len(elements) \
            or searching_element < 0 or searching_element > len(elements) \
            or searching_element == matching_element:
        print("Invalid input! Adding additional elements to the board")
        insert_index = len(elements) // 2
        elements.insert(insert_index, f'-{moves}a')
        elements.insert(insert_index, f'-{moves}a')
    else:
        el_1 = elements[searching_element]
        el_2 = elements[matching_element]
        if el_1 == el_2:
            elements.remove(el_1)
            elements.remove(el_2)
            print(f"Congrats! You have found matching elements - {el_1}!")
        else:
            print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        win_flag = True
        break

if not win_flag:
    print("Sorry you lose :(")
    print(" ".join(elements))


