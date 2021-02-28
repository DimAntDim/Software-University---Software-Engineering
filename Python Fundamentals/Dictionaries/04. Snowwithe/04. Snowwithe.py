import collections

dwarfs = {}
dwarf_hat_color_count = collections.defaultdict(int)

while True:
    data = input()
    if data == "Once upon a time":
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    key = (dwarf_name, dwarf_hat_color)

    if key in dwarfs:
        if dwarfs[key] < dwarf_physics:
            dwarfs[key] = dwarf_physics
    else:
        dwarfs[key] = dwarf_physics
        dwarf_hat_color_count[dwarf_hat_color] += 1

for key, value in sorted(dwarfs.items(), key=lambda item: (-item[1], -dwarf_hat_color_count[item[0][1]])):
    name, hat_color = key
    physics = value
    print(f"({hat_color}) {name} <-> {physics}")
