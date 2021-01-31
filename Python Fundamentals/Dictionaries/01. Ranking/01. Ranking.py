contest = {}
users_points = {}
while True:
    data = input().split(':')
    if data[0] == 'end of contests':
        break
    contest_name = data[0]
    contest_pass = data[1]
    key = contest_name, contest_pass
    contest[key] = {}

while True:
    data = input().split('=>')
    if data[0] == 'end of submissions':
        break
    class_name = data[0]
    password = data[1]
    user = data[2]
    points = int(data[3])
    k = (class_name, password)
    v = (user, int(points))
    if k in contest.keys():
        contest[k][user] = points

        if user not in users_points:
            users_points[user] = {}
        if class_name not in users_points[user]:
            users_points[user][class_name] = points
        else:
            if points > users_points[user][class_name]:
                users_points[user][class_name] = points

best_score = 0
best_user = str
for user_name, scores in users_points.items():
    points = sum(scores.values())
    if points > best_score:
        best_score = points
        best_user = user_name

print(f"Best candidate is {best_user} with total {best_score} points.\nRanking:")
for k, v in sorted(users_points.items(), key=lambda item: item[0]):
    print(k)
    sort_results = dict(sorted(v.items(), key=lambda x: -x[1]))
    for k,v in sort_results.items():
        print(f"#  {k} -> {v}")
