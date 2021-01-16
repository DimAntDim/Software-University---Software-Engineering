total_electrons = int(input())

electron_distribution = []
i = 1
while total_electrons > 0:
    layer_electrons = 2 * i ** 2
    if sum(electron_distribution) + layer_electrons <= total_electrons:
        electron_distribution.append(layer_electrons)
    else:
        electron_distribution.append(total_electrons)
        break
    total_electrons -= layer_electrons
    i += 1

print(electron_distribution)