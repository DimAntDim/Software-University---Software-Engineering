class Party:
    def __init__(self):
        self.people_going = []


party = Party()
while True:
    command = input()
    if command == 'End':
        print(f"Going: {', '.join(party.people_going)}\nTotal: {len(party.people_going)}")
        break
    party.people_going.append(command)
