time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

total_time_min = total_time // 60

total_time_sec = total_time % 60


if total_time_sec < 10:
    print(f"{total_time_min}:0{total_time_sec}")
else:
    print(f"{total_time_min}:{total_time_sec}")