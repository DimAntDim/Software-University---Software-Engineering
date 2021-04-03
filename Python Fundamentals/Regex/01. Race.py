import re

names = input().split(', ')
race_stat = {}
for i in names:
    race_stat[i] = 0
pattern_name = r"[A-Za-z]+"
pattern_time = r"\d"
while True:
    data = input()
    if data == 'end of race':
        break
    name_match = re.findall(pattern_name, data)
    time_match = re.findall(pattern_time, data)
    driver_name = ''.join(name_match)
    time_match = map(int, time_match)
    if driver_name in race_stat:
        race_stat[driver_name] += sum(time_match)
finalist = []
for k,v in sorted(race_stat.items(), key=lambda x: -x[1]):
    finalist.append(k)
print(f"1st place: {finalist[0]}\n2nd place: {finalist[1]}\n3rd place: {finalist[2]}")
