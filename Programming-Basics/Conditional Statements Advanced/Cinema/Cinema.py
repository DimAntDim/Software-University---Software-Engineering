"""
1. Кино
В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
Има три вида прожекции с билети на различни цени:
Premiere – премиерна прожекция, на цена 12.00 лева;
Normal – стандартна прожекция, на цена 7.50 лева;
Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
Резултатът да се отпечата във формат 2 знака след десетичната точка.
"""

ticket = input("")

premiere = 12.00
normal = 7.50
discount = 5.00

r = int(input("Row"))
c = int(input("Colon"))
all_seats = r*c


if ticket == 'Premiere':
    net_incom = premiere * all_seats
    print("Net incom: %.2f" %net_incom)
elif ticket == 'Normal':
    net_incom = normal * all_seats
    print("Net incom: %.2f" %net_incom)
elif ticket == 'Discount':
    net_incom = discount * all_seats
    print("Net incom: %.2f" %net_incom)