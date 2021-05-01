def concatenate(*args):
    string = [s for s in args]
    return ''.join(string)


print(concatenate("Soft", "Uni", "Is", "Great", "!"))