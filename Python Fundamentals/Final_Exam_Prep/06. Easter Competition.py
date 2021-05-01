easter_bread = int(input())
backer_score = 0
backer_one_notes = 0
backer_one = str
for i in range(1, easter_bread+1):
    backer = input()
    while True:
        note = input()
        if note == 'Stop':
            break
        backer_score += int(note)
    print(f"{backer} has {backer_score} points.")
    if backer_score > backer_one_notes:
        backer_one = backer
        backer_one_notes = backer_score
        print(f"{backer_one} is the new number 1!")
    backer_note = 0

print(f"{backer_one} won competition with {backer_one_notes} points!")