"""
Симона и Светлин ще ходят на почивка в Африка и искат да отидат на сафари.
Понеже за делничните дни вече имат планове, решават, че ще отидат събота или неделя.
 Напишете програма, която изчислява колко ще им струва ходенето на сафари и дали бюджетът им ще им стигне да отидат, като имате предвид следното:
Цената на един литър гориво е 2.10 лв.
Цената за екскурзовод е 100лв.
В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%
Вход
От конзолата се четат 3 реда:
Бюджет – реално число в интервала [0.00… 10000.00]
Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
Ден от седмицата – текст с възможности "Saturday" и "Sunday"
"""
budget = float(input())
fuel = float(input())*2.10
day = input()
tutor = 100
if day == 'Saturday':
    discount = 0.10
elif day == "Sunday":
    discount = 0.20
total = fuel + tutor
total = total - total*discount
if total <= budget:
    print(f"Safari time! Money left: %.2f lv. " %(budget-total))
else:
    print(f"Not enough money! Money needed: %.2f lv." % (total-budget))

