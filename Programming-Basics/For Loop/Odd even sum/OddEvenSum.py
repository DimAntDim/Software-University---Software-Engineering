sumeven =0
sumodd =0
summ = 0
n = int(input())
for i in range(n):
    num = int(input(""))
    if i % 2 == 0:
        sumeven += num
    else:
        sumodd += num

if sumodd == sumeven:
    summ = sumodd
    print(f"Yes\nSum = {summ}")
elif sumodd != sumeven:
    summ = sumodd - sumeven
    if summ < 0:
        print(f"No\n Diff = {summ * -1}")
    else:
        print(f"No\n Diff = {summ}")
