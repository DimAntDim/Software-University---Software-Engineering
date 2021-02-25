legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
win_flag = False

while True:
    data = input().split(' ')
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i+1].lower()
        if material in key_materials.keys():
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                win_flag = True
                key_materials[material] -= 250
                print(f"{legendary_items[material]} obtained!")
                break
        else:
            junk_materials[material] = 0
            junk_materials[material] += quantity
    if win_flag:
        break

for k,v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k}: {v}")

for k,v in sorted(junk_materials.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")

