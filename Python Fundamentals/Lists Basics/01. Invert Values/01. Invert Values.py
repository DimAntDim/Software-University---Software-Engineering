"""
Write a program that receives a single string containing numbers separated by a single space.
Print a list containing the opposite of each number.
"""
txt = input()

x = txt.split()

new_list = []
for i in x:
    i = int(i) * -1
    new_list.append(i)

print(new_list)
