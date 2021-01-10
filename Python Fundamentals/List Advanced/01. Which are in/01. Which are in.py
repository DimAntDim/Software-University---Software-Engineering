"""
Given two lists of strings print a new list of the strings that contains words from the first list
which are substrings of any of the strings in the second list (only unique values)
Input
arp, live, strong
lively, alive, harp, sharp, armstrong
Output
['arp', 'live', 'strong']
Input
tarp mice bull
lively alive harp sharp armstrong
Output
[]

"""

sub_srt = input().split(', ')
words = input().split(', ')

la_un = []

for sub in sub_srt:
    for word in words:
        if sub in word and sub not in la_un:
            la_un.append(sub)
print(la_un)
