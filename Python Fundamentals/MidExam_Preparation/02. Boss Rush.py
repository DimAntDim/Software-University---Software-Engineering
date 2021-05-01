n_inputs = int(input())

def split_check(command):
    if ':' in command and command.count(':') == 1:
        return True
    return False


def name_validity(name):
    if name.startswith('|') and name.endswith('|'):
        boss_name = name.replace('|', '')
        if boss_name.isupper() and len(boss_name) > 3:
            return True
        return False


def title_check(title):
    if title.startswith('#') and title.endswith('#'):
        title_name = title.replace('#', '')
        title_ls = title_name.split()
        if len(title_ls) == 2:
            for t in title_name:
                if t.isdigit():
                    return False
            return True


def space_check(title):
    counter = 0
    for t in title:
        if t.isspace():
            counter += 1
    if counter == 1:
        return True
    return False


for i in range(n_inputs):
    command = input()
    if split_check(command):
        data = command.split(':')
        name = data[0]
        title = data[1]
        name_print = name.replace('|', '')
        title_print = title.replace('#', '')
        if name_validity(name):
            if title_check(title):
                if space_check(title):
                    print(f"{name_print}, The {title_print}")
                    print(f">> Strength: {len(name_print)}")
                    print(f">> Armour: {len(title_print)}")
                else:
                    print('Access denied!')
            else:
                print('Access denied!')
        else:
            print('Access denied!')
    else:
        print('Access denied!')
