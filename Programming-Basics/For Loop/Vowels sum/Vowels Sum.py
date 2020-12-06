w = input()

a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0

for c in w:
    if c == 'a':
        sum += a
    elif c == 'e':
        sum += e
    elif c == 'i':
        sum += i
    elif c == 'o':
        sum += o
    elif c == 'u':
        sum += u

print(sum)