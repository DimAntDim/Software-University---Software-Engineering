"""
Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма,
която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:
Май и октомври
Юни и септември
Юли и август
Студио – 50 лв./нощувка
Студио – 75.20 лв./нощувка
Студио – 76 лв./нощувка
Апартамент – 65 лв./нощувка
Апартамент – 68.70 лв./нощувка
Апартамент – 77 лв./нощувка
Предлагат се и следните отстъпки:
За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
Вход
Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
На първия ред е месецът – May, June, July, August, September или October;
На втория ред е броят на нощувките – цяло число.
Изход
Да се отпечатат на конзолата 2 реда:
На първия ред: "Apartment: {цена за целият престой} lv."
На втория ред: "Studio: {цена за целият престой} lv."
Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
"""

mount = input("")
days = int(input(""))

if mount == 'May' or mount == 'October':
    studio_price = 50
    apartment_price = 65
    if days > 14:
        discount = 50 * 0.3
        discount_apartment = apartment_price * 0.1
        studio_price = days * (studio_price - discount)
        apartment_price = days * (apartment_price - discount_apartment)
    elif days > 7:
        discount = studio_price*0.05
        studio_price = days * (studio_price - discount)
        apartment_price = days * apartment_price
    else:
        studio_price = days * studio_price
        apartment_price = days * apartment_price

if mount == 'June' or mount == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        discount = studio_price * 0.2
        discount_apartment = apartment_price * 0.1
        studio_price = days * (studio_price - discount)
        apartment_price = days * (apartment_price - discount_apartment)
    else:
        studio_price = days * studio_price
        apartment_price = days * apartment_price

if mount == 'July' or mount == 'August':
    studio_price = 76
    apartment_price = 77
    if days > 14:
        discount_apartment = apartment_price * 0.1
        studio_price = days * studio_price
        apartment_price = days * (apartment_price - discount_apartment)
    else:
        studio_price = days * studio_price
        apartment_price = days * apartment_price

print(f"Apartment: %.2f lv." % apartment_price)
print("Studio: %.2f lv." % studio_price)