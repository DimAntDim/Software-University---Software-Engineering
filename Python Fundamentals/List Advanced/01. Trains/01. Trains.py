"""
You will receive how many wagons the train has. Create a list with that length with all zeros.
Until you receive the data "End", you get some of the following commands:
add {people} -> adds the people in the last wagon
insert {position_counter} {people} -> adds the people at the given wagon
leave {position_counter} {people} -> removes the people from the wagon
After you receive the "End" data print the train
Input
3
add 20
insert 0 15
leave 0 5
End
Output
[10, 0, 20]

Input
5
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End
Output
[16, 32, 100, 0, 105]
"""

wagons_length = int(input())
wagons = [0 for i in range(wagons_length)]

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'add':
        last_wagon = int(wagons[-1]) + int(command[1])
        wagons.append(last_wagon)
        wagons.remove(wagons[-2])
    elif command[0] == 'insert':
        wagon_selected = wagons[int(command[1])]
        wagon_selected += int(command[2])
        wagons.insert(int(command[1]), wagon_selected)
        wagons.remove(wagons[int(command[1])+1])
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        person_left = int(wagons[index]) - int(people)
        if person_left < 0:
            person_left = 0
        wagons.insert(index, person_left)
        wagons.remove(wagons[index+1])
    print(wagons)
