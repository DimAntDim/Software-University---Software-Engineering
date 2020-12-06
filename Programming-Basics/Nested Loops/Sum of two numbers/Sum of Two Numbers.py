start = int(input())
end = int(input())
magnum = int(input())
combination = 0
sum = 0

flag = False

count = []
for i in range(start, end+1):
    for i2 in range(start, end+1):
        sum = i + i2
        combination += 1
        if sum == magnum:
            count.append(combination)
            count.append(i)
            count.append(i2)
            flag = True
            start = end

if flag:
    print(f"Combination N:{count[0]} ({count[1]} + {count[2]} = {magnum})")
else:
    print(f"{combination} combinations - neither equals {magnum}")