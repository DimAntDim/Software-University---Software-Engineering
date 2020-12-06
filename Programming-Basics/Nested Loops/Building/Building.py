floors = int(input())
rooms = int(input())
evenfloor = 0
oddfloor = 0
for l in range(floors-1, floors):
    for r in range(0, rooms, 1):
        print(f"L{floors}{r} ", end="")
    floors -=1
for f in range(floors, 0, -1):
    print("\r")
    for r in range(0, rooms, 1):
        if f % 2 == 0 :
            evenfloor = f
            print(f"О{f}{r} ", end="")
        else:
            oddfloor = f
            print(f"A{f}{r} ", end="")