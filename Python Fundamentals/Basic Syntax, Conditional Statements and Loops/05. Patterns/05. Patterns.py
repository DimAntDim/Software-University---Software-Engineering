input = int(input())

for i in range(1, input+1):
    print("*"*i, end="\n")
for r in range(input-1, 0, -1):
    print("*"*r, end="\n")

