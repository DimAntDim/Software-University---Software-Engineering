name = input()

l = []

check = 0
grade = 0

while True:

    score = float(input())
    l.append(score)
    avg = sum(l) / len(l)

    if score <= 4:
        check += 1
    if check == 2:
        print(f"\n{name} has been excluded at {grade} grade")
        break
    grade += 1
    if grade == 12:
        print(f"\n{name} graduated. Average grade: %.2f" % avg)
        break
