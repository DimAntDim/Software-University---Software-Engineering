"""
As a young adventurer, you travel with your party around the world, seeking for gold and glory. But you need
to split the profit among your companions.
You will receive a party size. After that you receive the days of the adventure.
Every day, you are earning 50 coins, but you also spent 2 coins per companion for food.
Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have a motivational
party the same day, you spent additional 2 coins per companion.
Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
You have to calculate how much coins gets each companion at the end of the adventure.
Input / Constraints
The input will consist of exactly 2 lines:
party size – integer in range [1…100]
days – integer in range [1…100]
Output
Print the following message: "{companions_count} companions received {coins} coins each."
You cannot split a coin, so take the integral part (round down the coins to integer number).
Input
3
5
Output
3 companions received 90 coins each.
Input
15
30
Output
19 companions received 102 coins each.
"""

import math
party_size = int(input())
days = int(input())

benefit = 0

for d in range(1, days+1):
    if d % 10 == 0:
        party_size -= 2
    if d % 15 == 0:
        party_size += 5
    benefit += 50 - party_size*2
    if d % 3 == 0:
        benefit -= party_size*3
    if d % 5 == 0:
        benefit += party_size*20
    if d % 5 == 0 and d % 3 == 0:
        benefit -= party_size*2


print(f"{party_size} companions received {math.floor(benefit/party_size)} coins each.")