hight = int(input())
jump = 0
number_jumps = 0
jump_counter = 0
start_hight = hight - 30
while True:
    while True:
        jump = int(input())
        number_jumps += 1
        if jump > start_hight:
            start_hight += 5
            number_jumps = 0
            if start_hight > hight:
                break
        elif number_jumps > 2:
            break
        jump_counter += 1

    if start_hight > hight:
        break
    if number_jumps > 2:
        break
if start_hight > hight:
    print(f"Tihomir succeeded, he jumped over {start_hight-5}cm after {jump_counter+1} jumps.")
else:
    print(f"Tihomir failed at {start_hight}cm after {jump_counter+1} jumps.")