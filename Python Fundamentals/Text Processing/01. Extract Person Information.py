import re
n = int(input())
name = r"@([A-Za-z]+)\|"
age = r"#(\d+)\*"
for line in range(n):
    text = input()
    match_name = re.findall(name, text)
    match_age = re.findall(age, text)
    print(f"{match_name[0]} is {match_age[0]} years old.")




