judge = {}
individual_standings = {}
while True:
    data = input()
    if data == 'no more time':
        break
    data = data.split(' -> ')
    user = data[0]
    contest = data[1]
    points = int(data[2])
    if contest not in judge:
        judge[contest] = {}
    if user not in judge[contest]:
        judge[contest][user] = points
    else:
        if points > judge[contest][user]:
            judge[contest][user] = points


for contests, stats in judge.items():
    print(f"{contests}: {len(stats)} participants")
    sort = dict(sorted(stats.items(), key=lambda x: (-x[1], x[0])))
    counter = 1
    for name, point in sort.items():
        print(f"{counter}. {name} <::> {point}")
        counter += 1
    for k,v in stats.items():
        if k not in individual_standings:
            individual_standings[k] = 0
        individual_standings[k] += v


print("Individual standings:")
position = 1
for username, totalPoints in sorted(individual_standings.items(), key=lambda x: (-x[1], x[0])):
    print(f"{position}. {username} -> {totalPoints}")
    position += 1


