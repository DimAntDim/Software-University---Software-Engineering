"""
Read four integer numbers. Add first to the second, divide (integer)
the sum by the third number and multiply the result by the fourth number. Print the result.
Examples
Input
10
20
3
3
Output
30
Input
15
14
2
3
Output
42
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(int((a+b)/c)*d)
