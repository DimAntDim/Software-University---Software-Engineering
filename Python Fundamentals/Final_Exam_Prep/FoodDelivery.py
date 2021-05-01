chicken_menu = int(input())*10.35
fish_menu = int(input())*12.40
vegetarian_menu = int(input())*8.15

total = chicken_menu + fish_menu + vegetarian_menu

desert = total*0.2

total += 2.5 + desert

print(f"Total: {total:.2f}")