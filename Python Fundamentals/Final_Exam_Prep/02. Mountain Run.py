import math
gol = float(input())

distance = float(input())

clim_time = float(input())

slow = math.floor(distance/50)
slow = slow * 30
georgi_run = distance*clim_time+slow

if georgi_run < gol:
    print(f"Yes! The new record is {georgi_run:.2f} seconds.")
else:
    print(f"No! He was {abs(gol-georgi_run):.2f} seconds slower.")