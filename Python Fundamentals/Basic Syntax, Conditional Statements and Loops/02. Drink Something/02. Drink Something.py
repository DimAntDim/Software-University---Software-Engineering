"""
Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
Make a program that receives an age, and returns what they drink.
Rules:
Kids under 14 years old.
Teens under 18 years old.
Young adults under 21 years old.
Adults above 21.
Note: All the values except the last one are inclusive!
"""
input = int(input())

if input <= 14:
    print("drink toddy")
elif 14 < input <= 18:
    print("drink coke")
elif 18 < input <= 21:
    print("drink beer")
else:
    print("drink whisky")