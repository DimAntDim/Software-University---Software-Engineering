users = int(input())
back = 0
chest = 0
legs = 0
abdominals = 0
protein_shake = 0
protein_bar = 0

for u in range(users):
    workout = input()
    if workout == 'Back':
        back += 1
    elif workout == 'Protein shake':
            protein_shake += 1
    elif workout == 'Protein bar':
            protein_bar += 1
    elif workout == 'Chest':
        chest += 1
    elif workout == 'Legs':
        legs += 1
    elif workout == 'Abs':
        abdominals += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abdominals} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
work_mens = back+chest+legs+abdominals
protein = protein_bar+protein_shake
print(f"{work_mens/users*100:.2f}% - work out")
print(f"{protein/users*100:.2f}% - protein")