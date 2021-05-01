import os


def create_file(file_name):
    try:
        f = open(f"{file_name}", 'x')
    except FileExistsError:
        print(f'File with name {file_name} exist')


def add_content_to_file(file_name, content):
    try:
        with open(f"{file_name}", 'a') as f:
            f.writelines(content + '\n')
    except FileNotFoundError:
        print('File not found')


def replace_content_in_file(file_name, old_string, new_string):
    try:
        with open(file_name, 'r+') as f:
            txt = ''.join(f.readlines())
            replaced_txt = txt.replace(old_string, new_string)
            f.seek(0)
            f.write(replaced_txt)
    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


while True:
    data = input().split('-')
    command = data[0]
    if command == 'Create':
        file_ = data[1]
        create_file(file_)
    elif command == 'Add':
        file_ = data[1]
        text = data[2]
        add_content_to_file(file_, text)
    elif command == 'Replace':
        file_ = data[1]
        string = data[2]
        replace_string = data[3]
        replace_content_in_file(file_, string, replace_string)
    elif command == 'Delete':
        file = data[1]
        delete_file(file)
    else:
        exit()
