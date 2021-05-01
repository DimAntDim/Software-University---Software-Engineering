pen = int(input())*4.75
fol= int(input())*1.80
block = int(input())*6.50
note = int(input())*2.50

total = pen+fol+block+note
total -= total*0.05
print(f"Your total is {total:.2f}lv")