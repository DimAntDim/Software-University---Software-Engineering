unacceptable_note = int(input())
counter_bad_notes = 0
counter_all_notes = 0
martin_notes = 0
all_notes = 0

while True:
    name = input()
    if name == 'Enough':
        avg = all_notes/counter_all_notes
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {counter_all_notes}")
        print(f"Last problem: {name_to_print}")
        break
    note = int(input())
    all_notes += note
    if note <= 4:
        counter_bad_notes += 1
    else:
        martin_notes += note
    if counter_bad_notes == unacceptable_note:
        print(f"You need a break, {unacceptable_note} poor grades.")
        break
    counter_all_notes += 1
    name_to_print = name
