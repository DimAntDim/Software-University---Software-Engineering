"""
As a gladiator, Peter has to repair his broken equipment when he loses a fight. His equipment consists of helmet,
sword, shield and armor. You will receive the Peter`s lost fights count.
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired.
You will receive the price of each books in his equipment. Calculate his expenses for the year for renewing his equipment.
Input / Constraints
The input will consist of 5 lines:
On the first line you will receive the lost fights count – integer in the range_shot [0, 1000].
On the second line you will receive the helmet price - floating point number in range_shot [0, 1000].
On the third line you will receive the sword price - floating point number in range_shot [0, 1000].
On the fourth line you will receive the shield price - floating point number in range_shot [0, 1000].
On the fifth line you will receive the armor price - floating point number in range_shot [0, 1000].
Output
As output you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
"""
lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_repair = 0
sword_repair = 0
shield_repair = 0
armor_repair = 0
for i in range(1, lost_fight+1):
    if i % 2 == 0:
        helmet_repair += 1
    if i % 3 == 0:
        sword_repair += 1
    if i % 2 == 0 and  i % 3 == 0:
        shield_repair += 1
armor_repair = shield_repair//2

gladiator_expences = helmet_repair*helmet_price+sword_repair*sword_price+shield_repair*shield_price+armor_repair*armor_price
print(f"Gladiator expenses: {gladiator_expences:.2f} aureus")