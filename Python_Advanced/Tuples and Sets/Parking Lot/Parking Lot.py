def input_lines(count):
    garage = []
    for _ in range(count):
        garage.append(input())
    return garage


def print_out(cars):
    if cars:
        for c in cars:
            print(c)
    else:
        print("Parking Lot is Empty")


lines = input_lines(int(input()))
parking = set()
for car in lines:
    command, car = car.split(', ')
    if command == 'IN':
        parking.add(car)
    else:
        parking.remove(car)

print_out(parking)
