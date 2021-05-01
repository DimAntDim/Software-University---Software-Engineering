import string


def read_text_file():
    try:
        with open("text.txt", 'r') as f:
            f = f.readlines()
    except FileNotFoundError:
        print('File not found!')
    return f


def create_file():
    try:
        f = open(f"new_file.txt", 'x')
    except FileExistsError:
        print('File already exist!')


def edit_new_file():
    copy_from_file = read_text_file()
    try:
        with open('new_file.txt', 'a') as new_file:
            for i in range(len(copy_from_file)):
                letter_counter = 0
                punctuation_counter = 0
                row = ''.join(copy_from_file[i])
                row = row.replace('\n', '')
                for letter in row:
                    if letter.isalpha():
                        letter_counter += 1
                    elif letter in string.punctuation:
                        punctuation_counter += 1
                new_file.write(f"Line {i+1}: {row} ({letter_counter}) ({punctuation_counter})\n")
    except FileNotFoundError:
        print("File not found!")


create_file()
edit_new_file()
