group = int(input())

musala = 0
monblan = 0
kiliman = 0
k2 = 0
everest = 0

for _ in range(group):
    people = int(input())
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kiliman += people
    elif 26 <= people <= 40:
        k2 += people
    else:
        everest += people
all_peolpe = musala + monblan + kiliman + k2 + everest

print(f"{musala/all_peolpe*100:.2f}%")
print(f"{monblan/all_peolpe*100:.2f}%")
print(f"{kiliman/all_peolpe*100:.2f}%")
print(f"{k2/all_peolpe*100:.2f}%")
print(f"{everest/all_peolpe*100:.2f}%")
