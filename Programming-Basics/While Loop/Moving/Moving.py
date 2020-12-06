w = int(input())
l = int(input())
h = int(input())

sumbox = 0
volume = w*h*l
while True:
    box = input()
    if box == "Done":
        break
    sumbox += int(box)

    if sumbox > volume:
        break
if sumbox > volume:
    print(f"No more free space! You need {sumbox-volume} Cubic meters more.")
else:
    print(f"{volume-sumbox} Cubic meters left.")
