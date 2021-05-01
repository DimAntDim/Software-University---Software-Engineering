win = 0
lose = 0
day_win = 0
day_lose = 0
money_win_day = 0
money_win_total = 0
bonus = 0
tournament_days = int(input())
for day in range(1, tournament_days+1):
    while True:
        sport = input()
        if sport == 'Finish':
            if win > lose:
                day_win += 1
                bonus = money_win_day*0.1
                money_win_day += bonus
                money_win_total = money_win_total + money_win_day
            else:
                day_lose += 1
                money_win_total = money_win_total + money_win_day
            win = 0
            lose = 0
            bonus = 0
            money_win_day = 0
            break
        result = input()
        if result == 'win':
            win += 1
            money_win_day += 20
        else:
            lose += 1
if day_win > day_lose:
    money_win_total = money_win_total + money_win_total*0.20
    print(f"You won the tournament! Total raised money: {money_win_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_win_total:.2f}")