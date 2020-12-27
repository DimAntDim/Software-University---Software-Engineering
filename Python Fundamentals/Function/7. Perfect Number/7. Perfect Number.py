number = int(input())


def perfect_num(n):
    sum = 0
    for i in range(1, n-1):
        if n % i == 0:
            sum += i
    if sum == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect")


perfect_num(number)