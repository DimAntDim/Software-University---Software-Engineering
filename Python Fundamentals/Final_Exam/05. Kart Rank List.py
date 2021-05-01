import sys
record = sys.maxsize

gold_counter = 0
silver_counter = 0
bronze_counter = 0

winner_time_min = 0
winner_time_sec = 0
winner_name = 0

while True:
    driver_name = input()
    if driver_name == 'Finish':
        break
    minutes = int(input())
    sec = int(input())
    driver_time = minutes * 60 + sec

    if driver_time < 55:
        gold_counter += 1
    elif 55 < driver_time <= 85:
        silver_counter += 1
    elif 85 < driver_time <= 120:
        bronze_counter += 1

    if driver_time < record:
        winner_name = driver_name
        winner_time_min = minutes
        winner_time_sec = sec
        record = driver_time

print(f"With {winner_time_min} minutes and {winner_time_sec} seconds {winner_name} is the winner of the day!")
print(f"Today's prizes are {gold_counter} Gold {silver_counter} Silver and {bronze_counter} Bronze cards!")
