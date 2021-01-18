import math
numbers = list(map(lambda x: int(x), input().split(', ')))
copy_num_ls = []
for i in numbers:
    copy_num_ls.append(i)
#making the groups
numbers.sort()
if numbers[-1] % 10 == 0:
    groups = numbers[-1]//10
else:
    groups = math.ceil(numbers[-1]/10)
#making lists for the groups
for i in range(1, groups+1):
    group = i*10
    n = [num for num in copy_num_ls if group - 10 < num <= group]
    print(f"Group of {i}0's: {n}")

"""
#Alternative list comprehention
from math import ceil

total_electrons = input().split(", ")
nums = list(map(int, total_electrons))


for i in range_shot(1, ceil(max(nums) / 10) + 1):
    result = [nums[j] for j in range_shot(len(nums)) if nums[j] in range_shot(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i * 10}'s: {result}")
"""