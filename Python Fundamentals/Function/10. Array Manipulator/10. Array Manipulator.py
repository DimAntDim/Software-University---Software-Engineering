def exchange(num, s):
    if len(num) > s:
        first_part = num[:s + 1]
        second_part = num[s + 1:]
        exchange_ls = second_part + first_part
        return exchange_ls
    else:
        print("Invalid position_counter")
        return num


def max_min_odd(num):
    if command[0] == 'max':
        max_odd = []
        counter_max_odd = 0
        for n in num:
            if n % 2 != 0:
                max_odd.append(n)
        if len(max_odd) == 0:
            return 'No matches'
        else:
            max_odd.sort(reverse=True)
            n_max = max_odd[0]
            for i in range(len(num)):
                if num[i] == n_max:
                    return counter_max_odd
                counter_max_odd += 1
    elif command[0] == 'min':
        min_odd = []
        counter_min_odd = 0
        for n in num:
            if n % 2 != 0:
                min_odd.append(n)
        if len(min_odd) == 0:
            return 'No matches'
        else:
            min_odd.sort(reverse=True)
            n_min = min_odd[-1]
            for i in range(len(num)):
                if num[i] == n_min:
                    return counter_min_odd
                counter_min_odd += 1


def max_min_even(num):
    if command[0] == 'max':
        max_even = []
        counter_max_even = 0
        for n in num:
            if n % 2 == 0:
                max_even.append(n)
        if len(max_even) == 0:
            return 'No matches'
        else:
            max_even.sort()
            n_max = max_even[-1]
            for i in range(len(num)):
                if num[i] == n_max:
                    return counter_max_even
                counter_max_even += 1
    elif command[0] == 'min':
        min_even = []
        counter_min_even = 0
        for n in num:
            if n % 2 == 0:
                min_even.append(n)
        if len(min_even) == 0:
            return 'No matches'
        else:
            min_even.sort()
            n_min = min_even[0]
            for i in range(len(num)):
                if num[i] == n_min:
                    return counter_min_even
                counter_min_even += 1


def first_odd_even(num):
    odd = []
    even = []
    s = int(command[1])
    if s > len(num):
        return 'Invalid count'
    else:
        for i in num:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        if command[2] == 'odd':
            return odd[:s]
        elif command[2] == 'even':
            return even[:s]


def last_odd_even(num):
    odd = []
    even = []
    s = int(command[1]) * -1
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if command[2] == 'odd':
        return odd[s:]
    elif command[2] == 'even':
        return even[s:]


numbers = input().split()
num_ls = list(map(int, numbers))
result_exchange = str
command = input().split()

while command[0] != 'end':
    if command[0] == 'exchange':
        sep = int(command[1])
        result_exchange = exchange(num_ls, sep)
    elif command[0] == 'max' or command[0] == 'min':
        if command[1] == 'odd':
            result = max_min_odd(num_ls)
            print(result)
        elif command[1] == 'even':
            result = max_min_even(num_ls)
            print(result)
    elif command[0] == 'first':
        result = first_odd_even(num_ls)
        print(result)
    elif command[0] == 'last':
        result = last_odd_even(num_ls)
        print(result)

    command = input().split()

print(result_exchange)
