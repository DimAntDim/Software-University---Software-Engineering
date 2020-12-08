divisor = int(input())
bound = int(input())

lst = []

for num in range(divisor, bound + 1):
    if num % divisor == 0 and bound >= num > 0:
        lst.append(num)
print(max(lst))
