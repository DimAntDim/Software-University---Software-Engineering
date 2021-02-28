n = int(input())

dragons = {}

for _ in range(n):
    data = input().split()
    type = data[0]
    name = data[1]
    damage = (data[2])
    health = (data[3])
    armor = (data[4])
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    if type not in dragons and type.title():
        dragons[type] = {}
    if name not in dragons and name.title():
        dragons[type][name] = {}
    dragons[type][name] = {"damage": int(damage), "health": int(health), "armor": int(armor)}


for types, other in (dragons.items()):
    avg_damage = 0
    avg_health = 0
    avg_armor = 0
    number_of_dragons = 0
    for name, stats in dragons[types].items():
        number_of_dragons += 1
        avg_damage += stats['damage']
        avg_health += stats['health']
        avg_armor += stats['armor']
    print(f"{types}::({(avg_damage / number_of_dragons):.2f}/{(avg_health / number_of_dragons):.2f}/{(avg_armor / number_of_dragons):.2f})")
    for names, data in sorted(other.items(), key= lambda x: x[0]):
        print(f"-{names} -> damage: {data['damage']}, health: {data['health']}, armor: {data['armor']}")
