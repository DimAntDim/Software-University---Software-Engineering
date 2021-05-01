from collections import deque


def best_list_pureness(*args):
    max_result = 0
    count_rotation = int
    number_of_rotation = int(args[1]+1)
    i = 0
    data = deque(args[0])
    while True:
        if i == number_of_rotation:
            break
        sum_deque = 0
        for n in range(len(data)):
            sum_deque += data[n]*n
        if sum_deque > max_result:
            max_result = sum_deque
            count_rotation = i
        data.rotate()
        i += 1
    return f"Best pureness {max_result} after {count_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)



