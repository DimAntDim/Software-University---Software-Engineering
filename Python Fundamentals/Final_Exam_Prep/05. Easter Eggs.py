red = 0
orange = 0
blue = 0
green = 0

eggs = int(input())

for e in range(eggs):
    egg_color = input()
    if egg_color == 'red':
        red += 1
    elif egg_color == 'orange':
        orange += 1
    elif egg_color == 'blue':
        blue += 1
    else:
        green += 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
if red > orange and red > blue and red > green:
    max = red
    name = 'red'
elif orange > red and orange > blue and orange > green:
    max = orange
    name = 'orange'
elif blue > green and blue > red and blue > orange :
    max = blue
    name = 'blue'
elif green > blue and green > red and green > orange:
    max = green
    name = 'green'
else:
    max = orange
    name = 'orange'
print(f"Max eggs: {max} -> {name}")
