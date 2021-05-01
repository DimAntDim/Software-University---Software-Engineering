show = input()
season = int(input())
series = int(input())
time = float(input())
series += series*0.20

print(f"Total time needed to watch the {show} series is {round(season * series * time + season*10)} minutes.")