"""
You have a water tank with capacity of 255 liters. On the next total_electrons lines, you will receive liters of water,
which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!"
 and continue reading the next line. On the last line, print the liters in the tank.
Input
The input will be on two lines:
On the first line, you will receive total_electrons – the number of lines, which will follow
On the next total_electrons lines – you receive quantities of water, which you have to pour in the tank
Output
Every time you do not have enough capacity in the tank to pour the given liters, print:
Insufficient capacity!
On the last line, print only the liters in the tank.
Constraints
total_electrons will be in the interval [1…20]
liters will be in the interval [1…1000]
Input
5
20
100
100
100
20
Output
Insufficient capacity!
240

Input
1
1000
Output
Insufficient capacity!
0

"""
tank_capacity = 255
n = int(input())
tank_fill = 0
for i in range(n):
    quantities = int(input())
    if quantities <= tank_capacity:
        tank_capacity -= quantities
    else:
        print("Insufficient capacity!")
print(255-tank_capacity)
