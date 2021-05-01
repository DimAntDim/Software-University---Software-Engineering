from collections import deque

deque1_robots = deque()
deque2_products = deque()

robots = {}
job_log = []


data = input().split(';')

start_time = input().split(':')

h = int(start_time[0])*3600
m = int(start_time[1])*60
s = int(start_time[2])
time = h + m + s + 1
time_s = 0
while True:
    stock = input()
    if stock == 'End':
        break
    deque2_products.append(stock)

for element in data:
    tokens = element.split('-')
    name = tokens[0]
    processing_time = int(tokens[1])
    robots[name] = {'processing_time': processing_time, 'working_time': time + time_s}
    time_s += 1
    deque1_robots.append(name)


while deque2_products:
    robot_name = deque1_robots[0]
    product = deque2_products.popleft()
    if robots[robot_name]['working_time'] == time:
        robots[robot_name]['working_time'] += robots[deque1_robots[0]]['processing_time']
        job_log.append([robot_name, product, time])
        time += 1
        deque1_robots.rotate(-1)
    else:
        deque2_products.append(product)
        deque1_robots.rotate(-1)
        time += 1

for i in job_log:
    print(f"{i[0]} - {i[1]} [{convert(i[2])}]")



