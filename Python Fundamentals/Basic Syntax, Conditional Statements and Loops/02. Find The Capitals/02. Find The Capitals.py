"""
Write a program that takes a single string and prints a list of all the indices of all the capital letters.
Examples
Input
Output
pYtHoN
[1, 3, 5]
CApiTAls
[0, 1, 4, 5]
"""

string = input()
list = []
counter = 0
for s in string:
    if s.isupper() == True:
        count_char = counter
        list.append(count_char)
    counter += 1
print(list)

