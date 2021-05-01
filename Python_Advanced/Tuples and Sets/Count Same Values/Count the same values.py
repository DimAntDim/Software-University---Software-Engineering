numbers = tuple(map(float, input().split()))

nums_and_repetitions = {}

for num in numbers:
    if num not in nums_and_repetitions:
        nums_and_repetitions[num] = 0
    nums_and_repetitions[num] += 1

for k, v in nums_and_repetitions.items():
    print(f"{k} - {v} times")
