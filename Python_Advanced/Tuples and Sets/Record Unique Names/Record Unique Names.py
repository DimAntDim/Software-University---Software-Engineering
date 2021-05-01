def lines_input(count):
    names = []
    for _ in range(count):
        names.append(input())
    return names


def print_unique_names(names):
    unique = set(names)
    for name in unique:
        print(name)


print_unique_names(lines_input(int(input())))
