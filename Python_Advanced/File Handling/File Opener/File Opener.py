try:
    with open("text.txt", 'r') as file:
        if file:
            print('File found')
except FileNotFoundError:
    print('File not found')
