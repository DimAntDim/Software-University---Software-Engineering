skills = input()

command_line = input()


while command_line != 'For Azeroth':
    data = command_line.split()
    if data[0] == 'GladiatorStance':
        word = skills.upper()
        skills = word
        print(skills)
    elif data[0] == 'DefensiveStance':
        word = skills.lower()
        skills = word
        print(skills)
    elif data[0] == 'Dispel':
        index = int(data[1])
        letter = data[2]
        if index  < len(skills):
            skil = ''
            for s in range(len(skills)):
                if s != index:
                    skil += skills[s]
                else:
                    skil += letter
            skills = skil
            print('Success!')
        else:
            print('Dispel too weak.')
    elif data[0] == 'Target' and data[1] == 'Change':
        substring = data[2]
        second_substring = data[3]
        skill = skills.replace(substring, second_substring)
        skills = skill
        print(skills)
    elif data[0] == 'Target' and data[1] == 'Remove':
        substring = data[2]
        skill = skills.replace(substring, '')
        skills = skill
        print(skills)
    else:
        print("Command doesn't exist!")
    command_line = input()
