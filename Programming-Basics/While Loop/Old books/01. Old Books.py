book = input()
counter = 0

while True:
    search = input()

    if search == book:
        print(f"You checked {counter} books and found it.")

        break
    elif search == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter += 1