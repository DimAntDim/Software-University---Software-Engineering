n = int(input())

students = {}
students_avg = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

for student in students:
    avg_grade = sum(students[student])/len(students[student])
    if avg_grade >= 4.50:
        students_avg[student] = avg_grade

sort_student = dict(sorted(students_avg.items(), key=lambda x: x[1], reverse=True))
for s in sort_student:
    print(f"{s} -> {sort_student[s]:.2f}")

