number = input().split(', ')
ls_result = []


def palindrome(num):
    rev = num[::-1]
    if rev == num:
        result = 'True'
    else:
        result = 'False'
    return ls_result.append(result)


for element in range(len(number)):
    palindrome(number[element])

for index in ls_result:
    print(index)
