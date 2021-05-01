try:
    with open("numbers.txt", 'r') as file:
        a = [int(el[:-1]) for el in file.readlines()]
        print(sum(a))
except FileNotFoundError:
    print('File not found')
