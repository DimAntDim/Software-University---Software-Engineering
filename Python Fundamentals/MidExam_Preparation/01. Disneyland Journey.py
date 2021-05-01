journey_cost = float(input())
months = int(input())
savings = 0

for i in range(1, months+1):
    if i % 2 != 0 and i > 1:
        spend = savings * 0.16
        savings -= spend
    if i % 4 == 0:
        bonus = savings * 0.25
        savings += bonus
    money = journey_cost * 0.25
    savings += money

if savings >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {savings-journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost-savings:.2f}lv. more.")


