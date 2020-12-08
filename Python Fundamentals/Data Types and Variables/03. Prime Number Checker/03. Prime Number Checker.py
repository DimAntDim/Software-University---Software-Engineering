n = int(input())

if n > 1:
    # check for factors
    for i in range(2, n):
        if (n % i) == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
