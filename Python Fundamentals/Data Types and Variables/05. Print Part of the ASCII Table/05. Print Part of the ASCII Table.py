"""
Find online more information about ASCII (American Standard Code for Information Interchange) and
write a program that prints part of the ASCII table of characters on the console.
On the first line of input you will receive the char position_counter you should start with and
on the second line - the position_counter of the last character you should print.
"""
first = int(input())
second = int(input())
string = ''
for i in range(first, second+1):
    l = chr(i)
    string += f" {l}"

print(string)