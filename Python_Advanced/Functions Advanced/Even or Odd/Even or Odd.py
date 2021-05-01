def even_odd(*args):
    numbers = args[:-1]
    command = args[-1]
    if command == 'even':
        return list(filter(lambda x: x % 2 == 0, numbers))
    return list(filter(lambda x: x % 2 != 0, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))