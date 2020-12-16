password = input()


def length_check(key):
    if 6 <= len(key) <= 10:
        return True
    else:
        return False


def letters_and_digits(key):
    mark = 0
    for c in key:
        if 33 <= ord(c) <= 47 or 58 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123 <= ord(c) <= 126:
            mark += 1
            break
    if mark > 0:
        return False
    else:
        return True


def digit_counter_check(key):
    digit_counter = 0
    for c in key:
        if 48 <= ord(c) <= 57:
            digit_counter += 1
    if digit_counter >= 2:
        return True
    else:
        return False


if not length_check(password):
    print("Password must be between 6 and 10 characters")
if not letters_and_digits(password):
    print("Password must consist only of letters and digits")
if not digit_counter_check(password):
    print("Password must have at least 2 digits")
if length_check(password) and letters_and_digits(password) and digit_counter_check(password):
    print("Password is valid")
