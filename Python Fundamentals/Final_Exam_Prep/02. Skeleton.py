minutes = int(input())*60
seconds = int(input())
gool = minutes+seconds

lenght = float(input())
sec_per_100m = int(input())


minus_time = lenght/120
minus_time = minus_time*2.5

time = (lenght/100)*sec_per_100m - minus_time


if time <= gool:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(gool-time):.3f} second slower.")
