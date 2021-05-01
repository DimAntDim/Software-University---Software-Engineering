tax = 0
discount = 0
total = 0
internet = 0
contract = input()
contact_type = input()
mobile_internet = input()

mounts = int(input())

if contract == 'one':
    if contact_type == 'Small':
        tax = 9.98
    elif contact_type == 'Middle':
        tax = 18.99
    elif contact_type == 'Large':
        tax = 25.98
    elif contact_type == 'ExtraLarge':
        tax = 35.99
elif contract == 'two':
    if contact_type == 'Small':
        tax = 8.58
    elif contact_type == 'Meddle':
        tax = 17.09
    elif contact_type == 'Large':
        tax = 23.59
    elif contact_type == 'ExtraLarge':
        tax = 31.79

bill = tax * mounts

if mobile_internet == 'yes':
    if tax <= 10:
        internet = 5.50*mounts
    elif tax <= 30:
        internet = 4.35*mounts
    elif tax > 30:
        internet = 3.85*mounts
else:
    internet = 0
if contract == 'two':
    total = bill + internet
    total = total - total*0.0375
elif contract == 'one':
    total = bill + internet
else:
    total = bill + internet

print(f"{total:.2f} lv.")