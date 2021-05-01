def input_to_list(count):
    data = []
    for _ in range(count):
        data.append(input())
    return data


def avg(g):
    return sum(g) / len(g)


students_number = int(input())

data_list = input_to_list(students_number)

students_grades = {}

for student in data_list:
    name, grade = student.split(' ')
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for st, grades in students_grades.items():
    average = avg(grades)
    st_grades = ' '.join(map(lambda gr: f"{gr:.2f}", grades))
    print(f"{st} -> {st_grades} (avg: {average:.2f})")
