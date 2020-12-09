"""
Write a program that receives two numbers (factor and count) and creates a list with length
of the given count and contains only elements that are multiples of the given factor.
"""

factor = int(input())
count = int(input())
list = []
i = 0
for r in range(count):
    i += factor
    list.append(i)

print(list)