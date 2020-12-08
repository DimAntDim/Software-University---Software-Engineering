"""
You will be given an integer that will be distance in meters.
Write a program that converts meters to kilometers formatted to the second decimal point.
Examples
Input
1852
Output
1.85
Input
798
Output
0.80
"""
meters = int(input())
km = meters/1000
print(f"{km:.2f}")
