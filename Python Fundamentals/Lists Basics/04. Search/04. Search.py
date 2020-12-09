"""
You will receive a number total_electrons and a word. On the next total_electrons lines you will be given some strings. You have to add them
in a list and print them. After that you have to filter out only the strings that
include the given word and print that list too.
"""

n = int(input())
list = []
new_list = []
key = input()
for n in range(n):
    word = input()
    list.append(word)
print(list)

for i in list:
    if key in i:
        new_list.append(i)

print(new_list)

