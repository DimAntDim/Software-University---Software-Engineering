"""
Given a number, print the largest number that can be formed from the digits of the given number.
Examples
Input
Output
213
321
7389
9873
"""
number = input()
list = []
for i in number:
    list.append(i)

list.sort(reverse=True)
list_print = "".join(list)
print(list_print)

