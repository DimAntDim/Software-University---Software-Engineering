targets = list(map(lambda x: int(x), input().split()))
shoot_counter = 0
while True:
    command = input()
    if command == 'End' or len(targets) == 0:
        break

    target_index = int(command)
    if target_index < 0 or target_index > len(targets)-1:
        pass
    else:
        shoot_counter += 1
        current_target_value = targets[target_index]
        targets[target_index] = -1
        for i in range(len(targets)):
            if i == target_index or targets[i] == -1:
                pass
            elif targets[i] > current_target_value:
                targets[i] -= current_target_value
            elif targets[i] <= current_target_value:
                targets[i] += current_target_value

str_targets = list(map(lambda x: str(x), targets))
print(f"Shot targets: {shoot_counter} -> {' '.join(str_targets)}")