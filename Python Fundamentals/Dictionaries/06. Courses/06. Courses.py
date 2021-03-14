courses = {}

def print_out(courses):
    sorted_dict = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
    for course in sorted_dict:
        sorted_dict[course].sort()
        print(f"{course}: {len(courses[course])}")
        for user in courses[course]:
            print(f"-- {user}")



while True:
    data = input()
    if data == 'end':
        print_out(courses)
        break
    course_name, student_name = data.split(' : ')

    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)

