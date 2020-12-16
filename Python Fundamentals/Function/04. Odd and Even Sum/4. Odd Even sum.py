ls_odd = []
ls_even = []
ls_num = []


def odd_even(num):
    for c in num:
        ls_num.append(int(c))
    for i in ls_num:
        if int(i) % 2 == 0:
            ls_even.append(int(i))
        else:
            ls_odd.append(int(i))


number = input()
odd_even(number)

print(f"Odd sum = {sum(ls_odd)}, Even sum = {sum(ls_even)}")