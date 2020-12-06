standard = 0
kid = 0
student = 0
movielist = []
total_tickets = 0
total = 0
total_tickets_list = []
seats = 0
seat = 0
while True:
    movie = input()
    if movie == 'Finish':
        break
    movielist.append(movie)
    seats = int(input())

    while True:
        ticket = input()

        if ticket == 'standard':
            standard += 1
            total_tickets += 1
            seat += 1
        elif ticket == 'kid':
            kid += 1
            total_tickets += 1
            seat += 1
        elif ticket == 'student':
            student += 1
            total_tickets += 1
            seat += 1
        if seat == seats:
            total = '100.00'
            total_tickets_list.append(total)
            seat = 0
            total_tickets = 0
            break
        if ticket == 'End':
            total = round((total_tickets / seats) * 100, 2)
            total_tickets_list.append(total)
            seat = 0
            total_tickets = 0
            break

join = "\n".join(f"{x} - {float(y):.2f}% full." for x, y in zip(movielist, total_tickets_list))
print(join)

totaltickets = standard + kid + student

print(f"Total tickets: {totaltickets}")
print("{:.2f}".format((student / totaltickets) * 100) + "% student tickets.")
print("{:.2f}".format((standard / totaltickets) * 100) + "% standard tickets.")
print("{:.2f}".format((kid / totaltickets) * 100) + "% kids tickets.")
