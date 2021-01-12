"""
Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers
Input
3, 2, 1, 5, 8
Output
[1, 4]
Input
2, 4, 6, 9, 10
Output
[0, 1, 2, 4]
"""

numbers = list(map(lambda x: int(x), input().split(', ')))

even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
