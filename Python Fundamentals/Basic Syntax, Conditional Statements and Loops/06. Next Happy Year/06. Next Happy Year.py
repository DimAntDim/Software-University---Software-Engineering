"""
You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct digits,
(e.g) 2018. Write a program that receives an integer number and finds the next happy year.
Input   Output
8989    9012
1001    1023
"""

year = int(input())
happyYear=year+1
a=str(happyYear)
i = 0
isMatch=False
while i < len(a):
    j = i + 1
    while j<len(a):
        if a[i] == a[j]:
            happyYear+=1
            a=str(happyYear)
            i = 0
            isMatch=True
            break
        j+=1
    if isMatch:
        isMatch=False
        continue
    else:
        i+=1
print(a)



