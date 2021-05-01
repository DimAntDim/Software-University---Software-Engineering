bit = int(input())
uan = float(input())
comision = float(input())/100
bit = bit*1168 / 1.95

uan = (uan*0.15)*1.76
uan = uan/1.95
total = bit+uan
comisin = total*comision
print(f"{total-comisin:.2f}")