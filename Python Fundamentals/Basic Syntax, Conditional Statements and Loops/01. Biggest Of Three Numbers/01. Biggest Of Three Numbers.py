first_num = int(input())
second_num = int(input())
tird_num = int(input())

if first_num > second_num and first_num > tird_num:
    print(first_num)
elif second_num > first_num and second_num > tird_num:
    print(second_num)
else:
    print(tird_num)