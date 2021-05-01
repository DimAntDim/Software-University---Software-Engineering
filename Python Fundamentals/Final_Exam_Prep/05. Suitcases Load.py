load_space = float(input())

case_counter = 0
volume_case = 0
while True:
    volume = input()
    if volume == 'End':
        print(f"Congratulations! All suitcases are loaded!")
        break
    volume_case = float(volume)

    if case_counter % 2 == 0 and case_counter != 0:
        volume_case += volume_case*0.1

    if load_space < volume_case:
        print('No more space!')
        break

    load_space -= volume_case
    case_counter += 1

print(f"Statistic: {case_counter} suitcases loaded.")
