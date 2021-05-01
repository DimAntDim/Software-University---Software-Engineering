numbers = list(map(lambda x: int(x), input().split(', ')))
print(f"Positive: {', '.join(map(lambda x: str(x), [num for num in numbers if num >= 0]))}\n"
      f"Negative: {', '.join(map(lambda x: str(x), [num for num in numbers if num < 0]))}\n"
      f"Even: {', '.join(map(lambda x: str(x), [num for num in numbers if num % 2 == 0]))}\n"
      f"Odd: {', '.join(map(lambda x: str(x), [num for num in numbers if num % 2 != 0]))}\n")

