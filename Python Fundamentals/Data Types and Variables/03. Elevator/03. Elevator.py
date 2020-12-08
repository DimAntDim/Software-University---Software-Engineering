"""
Calculate how many courses will be needed to elevate total_electrons persons by using an elevator with capacity of p persons.
The input holds two lines: the number of people total_electrons and the capacity p of the elevator.
"""
import math
n = int(input())
p = int(input())

c = n/p
print(math.ceil(c))
