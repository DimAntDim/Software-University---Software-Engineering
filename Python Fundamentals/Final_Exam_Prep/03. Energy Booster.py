fruit = input()
set = input()
type = int(input())
price = 0
if fruit == 'Watermelon' and set == 'small':
    price = 56*2
elif fruit == 'Watermelon' and set == 'big':
    price = 28.70*5
elif fruit == 'Mango' and set == 'small':
    price = 36.66*2
elif fruit == 'Mango' and set == 'big':
    price = 19.60*5
elif fruit == 'Pineapple' and set == 'small':
    price = 42.10*2
elif fruit == 'Pineapple' and set == 'big':
    price = 24.80*5
elif fruit == 'Raspberry' and set == 'small':
    price = 20*2
elif fruit == 'Raspberry' and set == 'big':
    price = 15.20*5

total = type*price

if 400 <= total <= 1000:
    total = total - total*0.15
elif total > 1000:
    total = total - total/2

print(f"{total:.2f} lv.")