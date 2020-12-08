



quantity = int(input())
days = int(input())

#-------------------------------------Spirit----------------------------
christmas_spirit = 0
for c in range(1, days+1):
    if c % 2 == 0:
        christmas_spirit += 5
    if c % 3 == 0:
        christmas_spirit += 13
    if c % 5 == 0:
        christmas_spirit += 17
    if c % 3 == 0 and c % 5 == 0:
        christmas_spirit += 30
    if c % 10 == 0:
        christmas_spirit -= 20

if days % 10 == 0:
    christmas_spirit -= 30
#-------------------------------------Spirit------------------------------

#----------------------------------------Price----------------------------
total_cost = 0

for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += quantity * 2
    if i % 3 == 0:
        total_cost += quantity * 5 + quantity * 3
    if i % 5 == 0:
        total_cost += quantity * 15
    if i % 10 == 0:
        total_cost += 23

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")



"""
You will receive allowed quantity for one type of decoration and days left until Christmas day to decorate the house.
There are 4 types of decorations and each piece costs a price
Ornament Set – 2$ a piece
Tree Skirt – 5$ a piece
Tree Garlands – 3$ a piece
Tree Lights – 15$ a piece
Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought 
Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
Every tenth day you lose 20 spirit, because your cat ruins all tree decorations and you have to rebuild the tree and 
buy one piece of tree skirt, garlands and lights. That is why you are forced to increase the allowed quantity with 2 
at the beginning of every eleventh day.
Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you lose 
additional 30 spirit.
At the end you must print the total cost and the gained spirit.
Input / Constraints
The input will consist of exactly 2 lines:
quantity – integer in range_shot [1…100]
days – integer in range_shot [1…100]
Output
At the end print the total cost and the total gained spirit in the following format:
"Total cost: {budget}"
"Total spirit: {totalSpirit}"
Examples
Input
1
7
Output
Total cost: 37
Total spirit: 58
Input
3
20
Output
Total cost: 558
Total spirit: 156
"""
