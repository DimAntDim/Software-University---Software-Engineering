def sum_odd_or_even(command):
    numbers = input().split()
    if command == 'Even':
        return sum(filter(lambda x: x % 2 == 0, map(int, numbers)))*len(numbers)
    return sum(filter(lambda x: x % 2 != 0, map(int, numbers)))*len(numbers)


print(sum_odd_or_even(input()))
