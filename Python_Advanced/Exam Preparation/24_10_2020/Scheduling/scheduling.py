cycles_count = 0
tasks = list(map(int, input().split(', ')))
target_index = int(input())

tasks_dict = {}
for i in range(len(tasks)):
    tasks_dict[i] = tasks[i]

for index, value in sorted(tasks_dict.items(), key=lambda x: x[1]):
    if index == target_index:
        cycles_count += int(value)
        break
    else:
        cycles_count += int(value)

print(cycles_count)
