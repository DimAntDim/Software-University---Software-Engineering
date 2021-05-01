chat = input()
command_line = input().split(':|:')
command = command_line[0]
message = str
while command != "Reveal":
    flag_error = False
    if command == 'InsertSpace':
        index = int(command_line[1])
        message = chat[0:index] + ' ' + chat[index:]

    elif command == 'Reverse':
        substring = command_line[1]
        if substring in chat:
            changed_substring = substring[::-1]
            changed_substring = ''.join(changed_substring)
            message = chat.strip(substring)
            message += changed_substring
        else:
            flag_error = True
    else:
        substring = command_line[1]
        replacement = command_line[2]
        message = chat.replace(substring, replacement)

    chat = message
    if not flag_error:
        print(chat)
    else:
        print('error')
    command_line = input().split(':|:')
    command = command_line[0]

print(f"You have a new text message: {chat}")