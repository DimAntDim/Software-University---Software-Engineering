numbers = list(map(int, input().split('@')))
jump_position = int
command = input()
house_index = 0
while command != 'Love!':
    jump = int(command.split()[1])
    if house_index + jump > len(numbers)-1:
        house_index = 0
        if numbers[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            numbers[house_index] -= 2
            if numbers[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")
    else:
        house_index += jump
        if numbers[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            numbers[house_index] -= 2
            if numbers[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

    command = input()


print(f"Cupid's last position was {house_index}.")
if sum(numbers) == 0:
    print("Mission was successful.")
else:
    while 0 in numbers:
        numbers.remove(0)
    print(f"Cupid has failed {len(numbers)} places.")