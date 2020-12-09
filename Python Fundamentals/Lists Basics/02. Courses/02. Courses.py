"""
You will receive a single number total_electrons.
On the next total_electrons lines you will receive names of courses. You have to create a list of them and print it
"""
n = int(input())
list = []
for i in range(n):
    names = input()
    list.append(names)

print(list)