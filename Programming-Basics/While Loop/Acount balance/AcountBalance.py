increase = input()
total = 0
while increase != 'NoMoreMoney':
    if float(increase) < 0 :
        print("Invalid operation!")
        break
    else:
        print(f"Increase: %.2f" % float(increase))
        total += float(increase)
    increase = input()
print(f"Total: %.2f" % total)