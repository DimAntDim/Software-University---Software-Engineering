"""
Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма, която спрямо времето от
денонощието и градусите да препоръча на Виктор какви дрехи да облече.
Вашият приятел има различни планове за всеки етап от деня,
които изискват и различен външен вид - може да ги видите от таблицата.
От конзолата се четат точно два реда:
Градусите - цяло число;
Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
Време от денонощието / градуси


Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."
"""

temperature = int(input())

time = input()

if 10 <= temperature <= 18:
    if time == "Morning":
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")

if 18 < temperature <= 24:
    if time == "Morning":
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")

if temperature > 24:
    if time == "Morning":
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")