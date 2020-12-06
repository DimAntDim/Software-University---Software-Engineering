"""
Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
В зависимост от сезона:
Цената за наем на кораба през пролетта е  3000 лв.;
Цената за наем на кораба през лятото и есента е  4200 лв.;
Цената за наем на кораба през зимата е  2600 лв.
В зависимост от броя на групата има различна отстъпка:
Ако групата е до 6 човека включително  –  отстъпка от 10%;
Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
Ако групата е от 12 нагоре  –  отстъпка от 25%.
Рибарите ползват допълнително 5% отстъпка, ако са четен брой,
освен ако не е есен - тогава нямат допълнителна отстъпка,
която се начислява след като се приспадне отстъпката по горните критерии.
Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
Вход
От конзолата се четат три реда:
Бюджет на групата – цяло число;
Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
Брой рибари – цяло число.
Изход
На конзолата да се отпечата следното:
Ако бюджетът е достатъчен:
"Yes! You have {останалите пари} leva left."
Ако бюджетът НЕ Е достатъчен:
"Not enough money! You need {сумата, която не достига} leva."
Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
"""
budget = int(input(""))
season = input("")
fishers = int(input(""))

if fishers <= 6:
    discount = 0.10
elif 7 <= fishers <= 11:
    discount = 0.15
elif fishers >= 12:
    discount = 0.25

if season == 'Spring':
    rent = 3000
elif season == 'Summer':
    rent = 4200
elif season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

price = rent - rent * discount

if fishers % 2 == 0 and season != 'Autumn':
    f_discount = 0.05
    price = price - price*f_discount
    if budget >= price:
        rest = budget - price
        print(f"Yes! You have %.2f leva left." % rest)
    if budget < price:
        need = price - budget
        print("Not enough money! You need %.2f leva." % need)
else:
    if budget >= price:
        rest = budget - price
        print(f"Yes! You have %.2f leva left." % rest)
    if budget < price:
        need = price - budget
        print("Not enough money! You need %.2f leva." % need)