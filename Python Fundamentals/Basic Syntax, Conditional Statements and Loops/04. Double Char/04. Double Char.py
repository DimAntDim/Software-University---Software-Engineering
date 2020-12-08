"""
Given a string, you have to print a string in which each character (case-sensitive) is repeated.
"""
word = input()

for w in word:
    print(w*2, end="")
