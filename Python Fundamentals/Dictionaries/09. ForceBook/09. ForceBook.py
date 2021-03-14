from collections import defaultdict

force_book_dict = defaultdict(list)

while True:
    commands = input()
    if commands == "Lumpawaroo":
        break

    if "|" in commands:
        side, username = commands.split(" | ")

        if username not in force_book_dict[side]:
            force_book_dict[side].append(username)

    if "->" in commands:
        username, side = commands.split(" -> ")

        for key, value in force_book_dict.items():
            if username in value:
                force_book_dict[key].remove(username)

        force_book_dict[side].append(username)
        print(f"{username} joins the {side} side!")

sorded_items = dict(sorted(force_book_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for key, values in sorded_items.items():
    if len(values) != 0:
        print(f"Side: {key}, Members: {len(values)}")

        for value in sorted(values):
            print(f"! {value}")