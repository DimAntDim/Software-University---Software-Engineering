import re
dates = input()

pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<mount>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
matches = re.finditer(pattern, dates) # прави обект в паметта

for day in matches:
    d = day.groupdict() # правим променлива която да групира резултатите в речник
    print(f"Day: {d['day']}, Month: {d['mount']}, Year: {d['year']}")