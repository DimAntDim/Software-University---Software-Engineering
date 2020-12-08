"""
Write a program that converts British pounds to US dollars formatted to the 3th decimal point.
1 British Pound = 1.31 Dollars
Examples
Input
Output
80
104.800
39
51.090
"""
pounds = float(input())
dolars = pounds*1.31
print(f"{dolars:.3f}")
