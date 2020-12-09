cells = input().casefold().split('#')
water = int(input())

total_fire = 0
effort = 0
fire_cells = []
cold_cells = []
for cell in cells:
    data = cell.split(' = ')
    cell_type = data[0]
    cell_value = int(data[1])

    if cell_type == 'high' and 81 <= cell_value <= 125:
        fire_cells.append(cell_value)
    elif cell_type == 'medium' and 51 <= cell_value <= 80:
        fire_cells.append(cell_value)
    elif cell_type == 'low' and 1 <= cell_value <= 50:
        fire_cells.append(cell_value)
    else:
        continue

for fire_cell in fire_cells:
    if water >= fire_cell:
        water -= fire_cell
        total_fire += fire_cell
        effort += fire_cell * 0.25
        cold_cells.append(fire_cell)
    else:
        continue
print('Cells:')
for cold_cell in cold_cells:
    print(f'- {cold_cell}')
print(f'Effort: {round(effort, 2):.2f}\nTotal Fire: {total_fire}')