import math
movie = input()
time = int(input())
breaking = int(input())

time_for_luch = 1/8*breaking
time_for_rest = 1/4*breaking

rest_time = breaking - (time_for_luch+time_for_rest)

if time > rest_time:
    print(f"You don't have enough time to watch {movie}, you need {math.ceil(time-rest_time)} more minutes.")
else:
    print(f"You have enough time to watch {movie} and left with {math.ceil(rest_time-time)} minutes free time.")