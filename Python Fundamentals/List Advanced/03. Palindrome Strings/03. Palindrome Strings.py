"""
Write a program that receives on the first line words separated by a space and a searched palindrome on the second.
Print all the palindromes on the first line. Print all the occurrences of the searched palindrome in the format:
"Found palindrome {count} times"
Input
wow father mom wow shirt stats
wow
Output
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times
Input
hey how you doin? lol
mom
Output
['lol']
Found palindrome 0 times
"""

sentence = input().split()
searched_palindrome = input()
palindrome_string = [i for i in sentence if i[::-1] == i]

#for i in sentence:
   # revert_string = i[::-1]
   # if i == revert_string:
        #palindrome_string.append(revert_string)

print(palindrome_string)
print(f"Found palindrome {palindrome_string.count(searched_palindrome)} times")
