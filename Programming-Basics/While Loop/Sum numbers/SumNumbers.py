number = int(input())
check = True
s = 0
while check == True:
    n = int(input())
    s = s + n
    if s >= number:
        check = False
print(s)