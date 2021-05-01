student = 0
standard = 0
kid = 0
counter = 0
while True:
    movie = input()
    if movie == 'Finish':
        break
    free_seats = int(input())
    for f in range(free_seats):
        ticket = input()
        if ticket == 'End':
            break
        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        else:
            kid += 1
        counter += 1
    print(f"{movie} - {counter/free_seats*100:.2f}% full.")
    counter = 0
total_tickets = standard+student+kid
print(f"Total tickets: {total_tickets}")
print(f"{student/total_tickets*100:.2f}% student tickets.")
print(f"{standard/total_tickets*100:.2f}% standard tickets.")
print(f"{kid/total_tickets*100:.2f}% kids tickets.")