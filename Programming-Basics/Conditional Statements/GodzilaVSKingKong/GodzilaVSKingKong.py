"""Снимките за дългоочаквания филм &quot;Годзила срещу Конг&quot; започват. Сценаристът Адам Уингард ви моли да
напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
Известно е, че:
 Декорът за филма е на стойност 10% от бюджета.
 При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.
Вход
От конзолата се четат 3 реда:
Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
Изход
На конзолата трябва да се отпечатат два реда:
 Ако парите за декора и дрехите са повече от бюджета:
o &quot;Not enough money!&quot;
o &quot;Wingard needs {парите недостигащи за филма} leva more.&quot;
 Ако парите за декора и дрехите са по малко или равни на бюджета:
o &quot;Action!&quot;
o &quot;Wingard starts filming with {останалите пари} leva left.&quot;
Резултатът трябва да е форматиран до втория знак след десетичната запетая."""

budget = float(input(""))
actors = int(input(""))
dress_price = float(input(""))

if actors > 150:
    price_dress_all_actors = actors * (dress_price - dress_price*0.1)
else:
    price_dress_all_actors = actors * dress_price

total_price = (budget * 0.1) + price_dress_all_actors

if total_price > budget:
    print("Not enough money! ")
    print(f"Wingard needs %.2f" % (total_price - budget) + " leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with %.2f" % (budget - total_price) + " leva left.")
