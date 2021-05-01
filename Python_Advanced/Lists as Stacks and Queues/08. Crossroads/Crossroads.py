from collections import deque

traffic = deque()

green_light = int(input())
free_windows = int(input())

copy = traffic
data = input()

car_log = 0
car_on_wait = 0
while data != 'END':
    time = green_light
    if data == 'green':
        while traffic:
            # While there is a traffic take the next car from the deque
            car_model = traffic[0]
            car = deque(traffic.popleft())
            # While there is a green light(time) the cars are passing
            while time and car:
                if car:
                    car.popleft()
                    time -= 1
            # If the while cycle finish without interrupt, the else statement will run
            else:
                # If there is a car in the crossroad,
                # start countdown of the extra time(which is the rest of the time add the extra time)
                extra_time = free_windows + time
                if car:
                    while extra_time and car:
                        car.popleft()

                        extra_time -= 1
                        if not extra_time and car:
                            print(f"A crash happened!\n{car_model} was hit at {car[0]}.")
                            exit()
                    else:
                        car_log += 1
                        break
                else:
                    car_log += 1
    else:
        traffic.append(data)
        car_on_wait += 1

    data = input()

print(F"Everyone is safe.\n{car_log} total cars passed the crossroads.")
