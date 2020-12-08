num = int(input())

for n in range(1, num + 1):

    sum_digits = 0

    digits = n

    while digits > 0:

        sum_digits += digits % 10

        digits = int(digits / 10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{n} --> True")
    else:
        print(f"{n} --> False")










