info = {}

def print_out():
    sorted_info = dict(sorted(info.items(), key=lambda x: x[0]))
    for company_name in sorted_info:
        print(company_name)
        for id in sorted_info[company_name]:
            print(f"-- {id}")

while True:
    data = input().split(' -> ')
    if data[0] == 'End':
        print_out()
        break
    company = data[0]
    id = data[1]
    if company not in info:
        info[company] = []
        if id not in info[company]:
            info[company].append(id)
    else:
        if id not in info[company]:
            info[company].append(id)
