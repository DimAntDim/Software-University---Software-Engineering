effect = input().split(', ')
effects = [int(el) for el in effect]
power = input().split(', ')
powers = [int(el) for el in power]
Palm = 0
Willow = 0
Crossette = 0
while len(effects) != 0 and len(powers) != 0:
    firework = int(effects[0])
    explosive = int(powers[-1])
    if firework <= 0:
        effects.pop(0)
    elif explosive <= 0:
        powers.pop()
    elif Palm >= 3 and Willow >= 3 and Crossette >= 3:
        break
    elif (firework + explosive) % 3 == 0 and (firework + explosive) % 5 != 0:
        Palm += 1
        effects.pop(0)
        powers.pop()
    elif (firework + explosive) % 5 == 0 and (firework + explosive) % 3 != 0:
        Willow += 1
        effects.pop(0)
        powers.pop()
    elif (firework + explosive) % 5 == 0 and (firework + explosive) % 3 == 0:
        Crossette += 1
        effects.pop(0)
        powers.pop()
    else:
        temp_value = effects[0]
        temp_value -= 1
        effects.pop(0)
        effects.append(temp_value)
        firework = int(effects[0])
        explosive = int(powers[-1])
        if firework <= 0:
            effects.pop(0)
        elif explosive <= 0:
            powers.pop()
        elif Palm == 3 and Willow == 3 and Crossette == 3:
            break
        elif (firework + explosive) % 3 == 0 and (firework + explosive) % 5 != 0:
            Palm += 1
            effects.pop(0)
            powers.pop()
        elif (firework + explosive) % 5 == 0 and (firework + explosive) % 3 != 0:
            Willow += 1
            effects.pop(0)
            powers.pop()
        elif (firework + explosive) % 5 == 0 and (firework + explosive) % 3 == 0:
            Crossette += 1
            effects.pop(0)
            powers.pop()
if Palm >= 3 and Willow >= 3 and Crossette >= 3:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can’t make the perfect firework show.")
if len(effects) > 0:
    print(f'Firework Effects left: {str(effects)[1:-1]}')
if len(powers) > 0:
    print(f'Explosive Power left: {str(powers)[1:-1]}')
print(f'Palm Fireworks: {Palm}')
print(f'Willow Fireworks: {Willow}')
print(f'Crossette Fireworks: {Crossette}')
