n = int(input())
min = 0
max = 0
l = list()
for i in range(n):
    num = int(input())
    l.append(num)
l.sort()

print(f"Max number: {l[-1]}")
print(f"Min number: {l[0]}")
