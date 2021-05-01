from collections import deque

number_of_pumps = int(input())
stops = deque()
truck_fuel = 0
fuel_station = []
for _ in range(number_of_pumps):
    data = input()
    stops.append(data)
    fuel_station.append(data)
flag = False
while not flag:
    for station in stops:
        fuel = int(station.split()[0])
        truck_fuel += fuel
        distance = int(station.split()[1])
        if truck_fuel - distance >= 0:
            truck_fuel -= distance
            flag = True
        elif truck_fuel - distance < 0:
            stops.rotate()
            flag = False
            truck_fuel = 0
            break
    if flag:
        break

result = stops.popleft()
pump_index = fuel_station.index(result)
print(pump_index)




